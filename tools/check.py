#!/usr/bin/env python3

import os
import glob
import subprocess
import itertools


ANSWERS_FILE = 'answers.txt'

def main():
    current_file = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(current_file, '..'))
    answers_path = os.path.join(root_dir, ANSWERS_FILE)

    with open(answers_path) as f:
        reference_answers = (int(l.strip()) for l in f.readlines())

    problems = sorted_problems(root_dir)
    calculated_answers = (run_problem(problem) for problem in problems)

    zipped = itertools.zip_longest(reference_answers, calculated_answers, fillvalue=False)

    for problem_index, (ref_ans, cal_ans) in enumerate(zipped):
        if cal_ans == False:
            print('No attempt made for Problem {}'.format(problem_index + 1))
        else:
            if (ref_ans == cal_ans):
                print('Problem {} correct'.format(problem_index + 1))
            else:
                print('Problem {} incorrect (ref: {} vs cal: {})'.format(problem_index + 1, ref_ans, cal_ans))


def sorted_problems(root_dir):
    def key_fn(problem_dir):
        return int(os.path.basename(problem_dir)[7:])
    problems = glob.iglob(os.path.join(root_dir, 'problem[0-9]*'))
    return sorted(problems, key=key_fn)


def run_problem(problem):
    """Attempt to run a problem and return the integer for the
    result. Return message if something goes wrong.
    """

    try:
        p = os.path.join(problem, 'main.*')
        main_script = glob.glob(p)[0]
    except IndexError:
        print('No main found for {}'.format(problem))
        return None

    out = subprocess.check_output(main_script).strip()
    try:
        out_int = int(out)
    except ValueError:
        print('No integer output found for {} ({} found instead)'.format(problem, out))
        return None
        
    return out_int


if __name__ == '__main__':
    main()