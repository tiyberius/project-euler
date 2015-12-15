## Problem 144 - Investigating multiple reflections of a FRICKIN laser beam

#### Why choose this problem?

I chose this problem because I had already chosen two relatively straightforward problems and I
wanted to tackle one that was a little more difficult. I saw the problem and didn't immediately
know how to solve it, so I knew I would have to shake off the rust from my math brain to get it
done. I also didn't know if TDD would work for this type of problem, so I was curious to see how
that would pan out.

#### Process

I started by deliberately NOT searching for solutions because I wanted to struggle with it so that
I could understand the problem before going straight to a solution. After about an hour of reading
up on calculating angles of reflection and points of intersection, I felt like I had put
enough math back into my brain to comprehend any of the solutions that I might find. The search
for existing solutions turned up
http://www.mathblog.dk/project-euler-144-investigating-multiple-reflections-of-a-laser-beam/
which heavily influenced my solution, even though I was writing in Python and the solution was in
C#. The C# solution consists of very few lines of code, which is generally a good thing but hardly
what I would deem production ready. My reasoning follows:

+ The code is monolithic. Although the excercise is very narrow in scope, production code is very
rarely this way and there is useful functionality that could be broken out and reused elsewhere.
+ The code uses comments to describe itself. I try to use comments as a last resort to explain my
code. Comments and code can change independently, and so as the code changes, the comments may not
match the code. Good code should explain itself using function names and variable names.

Using TDD I only had to fix one bug before I reached the correct solution. The tests for this
code are useful, but only to a certain extent. It occurred to me as I was writing the tests that if
you wanted to choose a different ellipse to bounce the laser around, you would have to change quite
a few of the tests.

All in all, it was a fun challenge to solve and if I'm not mistaken, so far I am the only one to
post a solution in Python. I don't write a lot of "math" code, so it was a good change of pace.

#### Time spent

About 7 hours