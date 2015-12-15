from collections import namedtuple

import time

from names_scores.names_scores import solve_problem as solve_names_problem
from xor_decryption.xor_decryption import solve_problem as solve_xor_problem
from laser_reflections.laser_reflections import solve_problem as solve_laser_problem

Problem = namedtuple('Problem', ['number', 'description', 'solution_function'])


def solve_all_problems():
    problems = [Problem(22, 'Names Scores', solve_names_problem),
                Problem(59, 'XOR Decryption', solve_xor_problem),
                Problem(144, 'Laser Beams', solve_laser_problem)]

    for problem in problems:
        print 'Problem {number} - {description}'.format(number=problem.number,
                                                        description=problem.description)
        start = time.clock()
        answer = problem.solution_function()
        end = time.clock()
        print '  Answer: {answer}'.format(answer=answer)
        print '  Time: {time} seconds'.format(time=round(end - start, 3))
        print ''


if __name__ == '__main__':
    solve_all_problems()
