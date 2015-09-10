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
    calculated_answer_sets = (run_problem_set(problem) for problem in problems)

    zipped = itertools.zip_longest(
        reference_answers, calculated_answer_sets, fillvalue=False)

    incorrect = 0

    for problem_index, (ref_ans, result_set) in enumerate(zipped):
        results = []
        if result_set:
            for sub_dir_name, cal_ans_and_time in result_set:
                result = _check_problem_answer(
                    sub_dir_name, problem_index, ref_ans, cal_ans_and_time)
                results.append(result)
            if not all(results):
                incorrect += 1
        else:
            print('{} not attempted'.format(problem_index + 1))
    if incorrect > 0:
        print('{} problems checked, {} incorrect'.format(
            len(problems), incorrect))
        exit(1)
    else:
        print('{} problems checked, all correct'.format(
            len(problems)))


def _check_problem_answer(sub_dir_name, problem_index, reference_answer,
                          run_problem_result, print_answer=False):
    cal_ans, time_taken = run_problem_result
    if (reference_answer == cal_ans):
        if print_answer:
            print('Problem {} ({}) correct: {} ({:.2f}s)'.format(
                problem_index + 1, sub_dir_name, cal_ans, time_taken))
        else:
            print('Problem {} ({}) correct ({:.2f}s)'.format(
                problem_index + 1, sub_dir_name, time_taken))

        return True
    else:
        print('Problem {} ({}) incorrect (ref: {} vs cal: {})'.format(
            problem_index + 1, sub_dir_name, reference_answer, cal_ans))
        return False


def check_one(root_dir, reference_answers, problem_number):
    problem_dir = 'problem%03d' % (problem_number,)
    try:
        ref_answer = list(reference_answers)[problem_number - 1]
    except IndexError:
        ref_answer = None

    run_problem_results = run_problem_set(os.path.join(root_dir, problem_dir))
    for dir_name, run_problem_result in run_problem_results:
        if not _check_problem_answer(dir_name, problem_number - 1, ref_answer,
                                     run_problem_result, print_answer=True):
            exit(1)


def sorted_problems(root_dir):
    def key_fn(problem_dir):
        return int(os.path.basename(problem_dir)[7:])
    problems = glob.iglob(os.path.join(root_dir, 'problem[0-9]*'))
    return sorted(problems, key=key_fn)


def run_problem_set(problem):
    results = []
    for dir_ in sorted(os.listdir(problem)):
        path = os.path.join(problem, dir_)
        if os.path.isdir(path):
            dir_name = os.path.basename(path)
            results.append((dir_name, run_problem(path)))
    return results
            


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
