Project Euler solutions
=======================

This project contains Python code to solve a few of the problems from
[Project Euler](https://projecteuler.net/about). It was designed with readability, performance,
and extensibility in mind. Your input is welcome!

If you would like to contribute to this repository or you just want to run this code on your
machine:

    $ git clone https://github.com/tiyberius/project-euler.git
    $ cd project-euler
    $ mkvirtualenv project-euler
    $ pip install -r requirements.txt  # only necessary if you plan on running the tests/hacking
    $ python solve_problems.py  # wouldn't it be nice if real life worked this way

If you're developing, you can use 

    $ tox

to run all unit and integration tests.

To solve all the problems in this repo, run `solve_problems.py` and you should get output like

    Problem 22 - Names Scores
      Answer: 871198282
      Time: 0.027 seconds

    Problem 59 - XOR Decryption
      Answer: 107359
      Time: 1.221 seconds

    Problem 144 - Laser Beams
      Answer: 354
      Time: 0.003 seconds
