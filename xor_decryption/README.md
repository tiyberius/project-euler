## Problem 59 - XOR Decryption

#### Why choose this problem?

Encryption is hot right now! In the wave of the recent Paris attacks, it has reignited the debate
about encrypted communications. The government wants crypto backdoors. The security community
is pushing back and thinks crypto backdoors are a horrible idea. There was a fire fight!!!

The reason I chose this challenge is because I have seen many of these crypto challenges in Capture
the Flag competitions like CSAW CTF (https://csaw.engineering.nyu.edu/ctf/) and never worked on
any because there was always someone on my team that was better at crypto. So when I saw this in
the list of problems on Project Euler, I thought now is my chance! No better way
to learn about something than to have to write a piece of code, so here we are.

#### Process

Since I had already seen similar problems in CTF competitions, I already had an idea of how to
solve it but wanted to see what solutions existed. I landed on a few, each having their strengths
and weaknesses. I picked the strengths from each solution and took the liberty of renaming some
variables and restructuring the code a bit more for readability and testability.

There were two primary ways of solving this one and I took the simpler approach because simpler is
(almost) always better. I could have implemented Frequency Analysis code but in the end, I thought
it was overkill. By researching exisitng solutions, I now just how frequency analsysis works so
that's cool.

Again here I mostly used TDD to write the code, writing the doctests first, then the body of the
function. Overall it was a fairly easy challenge and much easier than I anticipated.

#### References used

Solution heavily influenced by http://blog.dreamshire.com/project-euler-59-solution/

Idea to use CSV Reader from http://www.toddsifleet.com/projects/euler

#### Time spent

About 3 hours