#!/usr/bin/env python3

import os
import glob
import subprocess
import itertools
import time
import sys


ANSWERS_FILE = 'answers.txt'


def check_all(root_dir, reference_answers):
    problems = sorted_problems(root_dir)
    calculated_answers = (run_problem(problem) for problem in problems)

    zipped = itertools.zip_longest(
        reference_answers, calculated_answers, fillvalue=False)

    incorrect = 0

    for problem_index, (ref_ans, cal_ans_and_time) in enumerate(zipped):
        result = _check_problem_answer(
            problem_index, ref_ans, cal_ans_and_time)
        if not result:
            incorrect += 1
    if incorrect > 0:
        print('{} problems checked, {} incorrect'.format(
            len(problems), incorrect))
        exit(1)
    else:
        print('{} problems checked, all correct'.format(
            len(problems)))


def _check_problem_answer(problem_index, reference_answer,
                          run_problem_result, print_answer=False):
    if run_problem_result is False:
        print('No attempt made for Problem {}'.format(problem_index + 1))
        return False
    else:
        cal_ans, time_taken = run_problem_result
        if (reference_answer == cal_ans):
            if print_answer:
                print('Problem {} correct: {} ({:.2f}s)'.format(
                    problem_index + 1, cal_ans, time_taken))
            else:
                print('Problem {} correct ({:.2f}s)'.format(
                    problem_index + 1, time_taken))

            return True
        else:
            print('Problem {} incorrect (ref: {} vs cal: {})'.format(
                problem_index + 1, reference_answer, cal_ans))
            return False


def check_one(root_dir, reference_answers, problem_number):
    problem_dir = 'problem%02d' % (problem_number,)
    try:
        ref_answer = list(reference_answers)[problem_number - 1]
    except IndexError:
        ref_answer = None

    run_problem_result = run_problem(os.path.join(root_dir, problem_dir))
    if not _check_problem_answer(problem_number - 1, ref_answer,
                                 run_problem_result, print_answer=True):
        exit(1)


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
        return None, None

    sta = time.time()

    try:
        out = subprocess.check_output(
            main_script,
            cwd=problem,
            stderr=subprocess.STDOUT).strip().decode('utf-8')
    except subprocess.CalledProcessError as e:
        print('Error running main script. Output:')
        print(e.output.decode('utf-8'))
        return None, None
    dt = (time.time() - sta)

    try:
        out_int = int(out)
    except ValueError:
        print('No integer output found for {} ({} found instead)'.format(
            problem, out))
        return None, dt

    return out_int, dt


if __name__ == '__main__':
    # if an argument is given, just check that problem

    try:
        problem_number = sys.argv[1]
    except IndexError:
        problem_number = None

    if problem_number:
        try:
            problem_number = int(problem_number)
        except ValueError:
            print('Invalid problem number')
            exit(2)

    current_file = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(current_file, '..'))
    answers_path = os.path.join(root_dir, ANSWERS_FILE)

    with open(answers_path) as f:
        reference_answers = (int(l.strip()) for l in f.readlines())

    if not problem_number:
        check_all(root_dir, reference_answers)
    else:
        check_one(root_dir, reference_answers, problem_number)
