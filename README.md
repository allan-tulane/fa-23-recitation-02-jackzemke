# CMPS 2200  Recitation 02

**Name (Team Member 1):** Jack Zemke (solo)  

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
  - $aW(n/b) + 1$   __--->__ $\sum_{i=0}^{\log _{2} n} an+2^i$ __--->__ $2^i \log _{2} (2n)$ __--->__ $2n+an\log _{2} n \in O( \log{n})$
  - $aW(n/b) + \log n$   __--->__ $\sum_{i=0}^{\log _{2} n}( an+2^i \log n)$ __--->__ $\sum_{i=0}^{\log _{2} n}an+ \sum_{i=0}^{\log _{2} n}2^i \log n$  __--->__ $an\log _{2} n+2n\log{n}$ __--->__ $\log{n}(an+2n) \in O(n\log{n})$
   - $aW(n/b) + n$   __--->__ $\sum_{i=0}^{\log _{2} n} n(a+2^i)$  __--->__ $n({a\log _{2} n}+a+2n-1) \in O(n^2)$



- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 
   - if $c < \log_b a$, that means that $n^c$ will grow slower than $\log_b a$. Thus the work will be dominated by $W(n)$, as $n \to \infty$, $W(n)$ will grow much larger than $n^c$. In plain english, this means that the individual work of each node will be less and less costly relative to the number of subproblems defined. According to the master theorem, the runtime will be $\in O(n^{\log_b a})$
   - if $c > \log_b a$, $n^c$ will grow faster than $\log_b a$. Thus the work will be dominated by $n^c$, as $n \to \infty$, $n^c$ will grow much larger than $W(n)$. In plain english, this means that the individual work of each node will be more and more costly relative to the number of subproblems defined. According to the master theorem, the runtime will be $\in O(n^c)$
   - if $c = \log_b a$, $W(n)$ will grow equally as fast as $n^c$. In this case, the work will be balanced bwtween the individual work of each node and the number of subproblems defined. According to the master theorem, the runtime will be $\in O(n^d\log n)$

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 
  - The span of an algorithm is dependent on tree depth. Tree depth can be found by taking $\log_b n$, and does not depend on the additional work of each leaf. Seeing as each recurrence in problem 4 is only differentiated by the additional work of each leaf, the span of all three of the recurrences is:  $\log_b n\in O(\log n)$

