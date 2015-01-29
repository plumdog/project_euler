#!/usr/bin/env python3

import sys
import copy
import time


SUB = 3
UPTO = 9
RANGE = list(range(1, UPTO + 1))
SUBRANGE = list(range(1, SUB + 1))


class Section(object):
    def items(self):
        raise NotImplementedError

    def values(self):
        return list(v for _, v in self.items())

    def valid(self):
        """Returns false if this section contains an inconsistency. Otherwise,
        returns true.

        """

        numbers = list(filter(None, self.values()))
        return len(set(numbers)) == len(list(numbers))

    def complete(self):
        """Returns true if this section has all of the required numbers.

        """

        numbers = list(self.values())
        return set(numbers) == set(RANGE)


class Square(Section):
    def __init__(self, square=None):
        self._square = [[None]*SUB for _ in SUBRANGE]

        if square is not None:
            for i, rowlet in zip(SUBRANGE, square):
                for j, number in zip(SUBRANGE, rowlet):
                    self[(i, j)] = number

    def __getitem__(self, pos):
        x, y = pos
        return self._square[x - 1][y - 1]

    def __setitem__(self, pos, value):
        x, y = pos
        self._square[x - 1][y - 1] = value

    def items(self):
        for i in SUBRANGE:
            for j in SUBRANGE:
                yield ((i, j), self[(i, j)])

    def __repr__(self):
        return str(self._square)


class Line(Section):
    def __init__(self, line=None):
        self._line = [None] * UPTO
        if line is not None:
            if len(line) != UPTO:
                raise ValueError(
                    'Line is incorrect length, len={}'.format(len(line)))
            for i, num in zip(RANGE, line):
                self[i] = num

    def __getitem__(self, key):
        return self._line[key - 1]

    def __setitem__(self, key, value):
        self._line[key - 1] = value

    def __repr__(self):
        l = []
        for i in self.values():
            if i is not None:
                l.append(str(i))
            else:
                l.append('_')
        return ''.join(l)

    def items(self):
        for i in range(UPTO):
            yield (i + 1, self._line[i])


class Sudoku(object):
    def __init__(self, grid_as_lines):
        """Input should be a list of strings, where each string is digits 0-9
        where a 0 indicates a space, and a number indicates a starting
        number.

        """

        self.grid = Line()
        for rownum, row in zip(RANGE, grid_as_lines):
            gridrow = Line()
            for pos, char in zip(RANGE, row):
                num = int(char)
                if num in RANGE:
                    gridrow[pos] = num
                elif num == 0:
                    pass
                else:
                    raise ValueError('Invalid character in input: {}'.format(num))

            self.grid[rownum] = gridrow

    def __repr__(self):
        return '\n'.join(str(row) for row in self.grid.values())

    def row(self, rownum):
        return self.grid[rownum]

    def col(self, colnum):
        return Line([self.grid[rownum][colnum] for rownum in RANGE])

    def square(self, xnum, ynum):
        sq = []
        for x in SUBRANGE:
            sq_line = []
            for y in SUBRANGE:
                sq_line.append(self.grid[(xnum - 1) * SUB + x][(ynum - 1) * SUB + y])
            sq.append(sq_line)
        return Square(sq)

    def square_items(self, xnum, ynum):
        for x in SUBRANGE:
            for y in SUBRANGE:
                yield (((xnum - 1) * SUB + x, (ynum - 1) * SUB + y),
                       self.grid[(xnum - 1) * SUB + x][(ynum - 1) * SUB + y])

    def square_for_pos(self, x, y):
        def _sqnum(num):
            return (num - 1) // SUB + 1
        return (_sqnum(x), _sqnum(y))

    def rows(self):
        for rownum in RANGE:
            yield self.row(rownum)

    def cols(self):
        for colnum in RANGE:
            yield self.col(colnum)

    def squares(self):
        for x in SUBRANGE:
            for y in SUBRANGE:
                yield self.square(x, y)

    def items(self):
        for i in RANGE:
            for j in RANGE:
                yield ((i, j), self.grid[i][j])

    def _check_method(self, method_name, describe=False):
        all_rows = all(getattr(r, method_name)() for r in self.rows())
        if not all_rows:
            if describe:
                print('row error')
            return False
        all_cols = all(getattr(c, method_name)() for c in self.cols())
        if not all_cols:
            if describe:
                print('col error')
            return False
        all_sqs = all(getattr(sq, method_name)() for sq in self.squares())
        if not all_sqs:
            if describe:
                print('sq error')
            return False
        return True

    def valid(self, describe=False):
        return self._check_method('valid', describe)

    def complete(self, describe=False):
        return self._check_method('complete', describe)



class Solver(object):
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solve(self):
        raise NotImplementedError()


class BruteForceSolver(Solver):

    class InvalidSudokuError(Exception):
        pass

    def solve(self):
        if self.sudoku.complete():
            return self.sudoku
        elif not self.sudoku.valid():
            raise BruteForceSolver.InvalidSudokuError()
        else:
            x, y = self.first_empty_square()

            for num in self.numbers_to_try(x, y):
                new_sudoku = copy.deepcopy(self.sudoku)
                new_sudoku.grid[x][y] = num

                try:
                    return self.brute_force(new_sudoku)
                except BruteForceSolver.InvalidSudokuError:
                    pass

        raise BruteForceSolver.InvalidSudokuError()

    def numbers_to_try(self, x, y):
        return RANGE

    def first_empty_square(self):
        for i in RANGE:
            for j in RANGE:
                if self.sudoku.grid[i][j] is None:
                    return (i, j)
        raise Exception('No empty squares')

    def brute_force(self, sudoku=None):
        if not sudoku:
            sudoku = self.sudoku
        return self.__class__(sudoku).solve()


class InferenceSolver(Solver):
    def __init__(self, sudoku):
        super().__init__(sudoku)
        self.options = Line()
        for i in RANGE:
            option_col = Line()
            for j in RANGE:
                option_col[j] = set(RANGE)
            self.options[i] = option_col

    def _print_options(self):
        to_print = {}
        for i, row in self.options.items():
            for j, value in row.items():
                if value is True:
                    to_print[(i, j)] = '[[' + str(self.sudoku.grid[i][j]).center(UPTO-2) + ']]'
                else:
                    to_print_values = []
                    for num in RANGE:
                        if num in value:
                            to_print_values.append(str(num))
                        else:
                            to_print_values.append(' ')
                    to_print[(i, j)] = '{%s}' % ''.join(to_print_values)
        for i in RANGE:
            for j in RANGE:
                print(to_print[(i, j)], end='')
                if j == UPTO:
                    print('\n', end='')
                elif j % SUB == 0:
                    print('|', end='')
                
            if (i < UPTO) and (i % SUB == 0):
                print('-'*((UPTO+2)*UPTO+(SUB-1)))
                

    def update_options(self):
        for (i, j), value in self.sudoku.items():
            if value is not None:
                self.options[i][j] = True
                for colnum in RANGE:
                    self.remove_option(i, colnum, value)
                for rownum in RANGE:
                    self.remove_option(rownum, j, value)
                sqx, sqy = self.sudoku.square_for_pos(i, j)
                for (x, y), _ in self.sudoku.square_items(sqx, sqy):
                    self.remove_option(x, y, value)

    def update_values(self):
        change_made = False

        # check each square and see if it has just one option
        for i in RANGE:
            for j in RANGE:
                opts = self.options[i][j]
                if opts is True:
                    pass
                elif len(opts) == 1:
                    value = list(opts)[0]
                    change_made = True
                    self.set_value(i, j, value)
                    if not self.sudoku.valid(describe=True):
                        print('########### not valid #############')
                        print(self.sudoku)
                        raise Exception

        # check each row and see if a number can only appear once
        for rownum in RANGE:
            for num in RANGE:
                
                col_options = set()
                found = False
                for colnum in RANGE:
                    val = self.sudoku.grid[rownum][colnum]
                    if val is not None:
                        if val == num:
                            found = True
                            break
                    else:
                        opts = self.options[rownum][colnum]
                        if (opts is not True) and (num in opts):
                            col_options.add(colnum)
                if not found and (len(col_options) == 1):
                    value = list(col_options)[0]
                    change_made = True
                    self.set_value(rownum, value, num)

        # check each col and see if a number can only appear once
        for colnum in RANGE:
            for num in RANGE:
                row_options = set()
                found = False
                for rownum in RANGE:
                    val = self.sudoku.grid[rownum][colnum]
                    if val is not None:
                        if val == num:
                            found = True
                            break
                    else:
                        opts = self.options[rownum][colnum]
                        if (opts is not True) and (num in opts):
                            row_options.add(rownum)
                if not found and (len(row_options) == 1):
                    value = list(row_options)[0]
                    change_made = True
                    self.set_value(value, colnum, num)

        # check each square and see if a number can only appear once
        for sqx in SUBRANGE:
            for sqy in SUBRANGE:
                for num in RANGE:
                    sq_options = set()
                    found = False
                    for sq_pos, value in self.sudoku.square_items(sqx, sqy):
                        if value == num:
                            found = True
                            break
                        else:
                            sq_options.add(sq_pos)
                    if not found and (len(sq_options) == 1):
                        valuex, valuey = list(sq_options)[0]
                        change_made = True
                        self.set_value(valuex, valuey, num)

        return change_made

    def set_value(self, x, y, value):
        current_value = self.sudoku.grid[x][y]
        if (current_value is not None):
            if current_value != value:
                raise Exception('Value already set at ({}, {}) to {}, attempting to set to {}'.format(
                    x, y, self.sudoku.grid[x][y], value))
            else:
                # already set to the correct thing, nothing to do
                return
        if value not in self.options[x][y]:
            raise Exception('Invalid value {} set at ({}, {}), valid options={}'.format(
                value, x, y, self.options[x][y]))

        self.options[x][y] = True
        self.sudoku.grid[x][y] = value

    def remove_option(self, x, y, value):
        try:
            self.options[x][y].remove(value)
        except KeyError:
            # not in the set
            return
        except AttributeError:
            # not a set anyway
            return

        if len(self.options[x][y]) == 0:
            raise Exception('Last option, {}, removed from ({}, {})'.format(
                value, x, y))

    def solve(self):
        self.update_options()

        changes = 0

        while self.update_values():
            changes += 1
            self.update_options()
        return self.brute_force()

    def brute_force(self, instance=None):
        if not instance:
            instance = self
        return BruteForceSolver(instance.sudoku).solve()


class BruteForceOnInferenceSolver(BruteForceSolver):
    def __init__(self, sudoku, options):
        super().__init__(sudoku)
        self.options = options

    def numbers_to_try(self, x, y):
        return self.options[x][y]

    def brute_force(self, sudoku=None):
        if not sudoku:
            sudoku = self.sudoku
        return self.__class__(sudoku, self.options).solve()


class InferenceBruteForceOnInference(InferenceSolver):
    def brute_force(self, instance=None):
        if not instance:
            instance = self
        return BruteForceOnInferenceSolver(instance.sudoku, instance.options).solve()


def solve(grid_as_lines):
    s = Sudoku(grid_as_lines)
    solver = InferenceBruteForceOnInference(s)
    #solver = BruteForceSolver(s)
    return solver.solve()


def millis():
    return int(time.time() * 1000)


def main():
    fname = sys.argv[1]
    try:
        number = int(sys.argv[2])
    except (IndexError, ValueError):
        number = None
    
    with open(fname) as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]

    total = 0

    for i, l in enumerate(lines):
        if l.startswith('Grid'):
            if (number is None) or (number and (l == ('Grid %02d' % number))):
                grid_as_lines = lines[i+1:UPTO+i+1]
                #print(l)
                a = millis()
                solution = solve(grid_as_lines).grid
                #print('solved in:', '{}ms'.format(millis() - a))

                digits = [solution[1][i] for i in (1,2,3)]
                digits_number = int(''.join(str(i) for i in digits))

                total += digits_number
    #print('###################')
    print(total)


if __name__ == '__main__':
    main()
