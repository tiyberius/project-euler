## Problem 22 - Names Scores

#### Why choose this problem?

I chose this problem because it seemed like a good starting point. As I was reading the problem
description, I was breaking the problem down and envisioning the solution. I also thought the
problem provided a good opportunity to demonstrate how I like to implement separation of duties
when I write my code.

#### Process

I started by reading the problem description and writing functions definitions that I would need
along with the arguments I thought would be necessary. I then added doctests to the functions, then
wrote the function code. After I had all the functions I needed, then I wrote the solve_challenge()
function and found the correct answer the second time I ran the code. I got the wrong answer
the first time I ran it because I forgot to sort the names before passing them to
`calculate_name_scores()`. Initially I was going to fix it by sorting the names _inside_ the
`calculate_names_scores()` function, but thought that the code would lose some flexibility.
The `calculate_names_scores()` function should be able to calculate names scores for inversely
sorted names, if the problem were to ever change.

In summary it was a very easy problem, but a good way to get all the common project files set up
(like tox.ini, setup.py, requirements.txt, etc).

#### References used

Stack Overflow and Code Review Stack Exchange
http://codereview.stackexchange.com/questions/73832/project-euler-22-names-scores

#### Time spent

About 2 hours