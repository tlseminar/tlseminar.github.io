% Final Exam - Solutions

# Logical Formulas and Inference Rules

1. For each candidate inference rule below,  indicate if it is _sound_ or
_unsound_ (circle the correct answer).  For the rules that are unsound,
provide a counter-example to show it is unsound.  You do not need to
provide any justification for the rules that are sound.

	a. $\infer{Q}{P}$

	(3) **Unsound.** Counter-example: $P = \text{\bf{True}}, Q = \text{\bf{False}}$.

	b. $\infer{P}{(P \wedge Q) \vee (P \wedge \overline{Q})}$

	(2) **Sound.** If $P$ is $\text{\bf{False}}$, there is no way to make the
  antecedent true since each clause is a conjunction that includes
  $P$.

	c. $\infer{P}{(P \wedge Q) \wedge (P \wedge \overline{Q})}$
    
    (2) **Sound.** If $P$ is $\text{\bf{False}}$, there is no way to make the
  antecedent true since each clause is a conjunction that includes
  $P$.

    d. $\infer{P}{(P \implies Q) \wedge Q}$
    
    (3) **Unsound.** Counter-example: $P = \text{\bf False}, Q = \text{\bf True}$.

\clearpage

# Well Ordering

2. For each set and operator below, answer if the set is
_well-ordered_ or not. Support your answer with a brief, but clear and
convincing, argument.

  a. the even natural numbers; $<$.

  (2) **Well-Ordered**.  The even natural numbers is a subset of
  $\mathbb{N}$, which we know is well-ordered by $<$, and every subset
  of a well-ordered set is well-ordered.

  b. the non-negative real numbers; $<$.

  (3) **Not Well-Ordered.** The subset $\mathbb{S} - \{ 0 \}$ has no least
  element, so the set is not well-ordered.  We could prove this by
  contradiction.  Assume (to get a contradiction) that there is a
  minimum element $m$.  Since $m$ is a non-negative real number, it is
  some sequence of digits, $m_1m_2m_3\ldots$.  The number
  $0m_1m_2m_3\ldots$ is a real number less than $m$.  Hence, we have a
  contradiction and the set is not well-ordered.  (Not necessary to
  prove this for full credit, but +2 bonus for a proof.)

  c. the empty set; $<$.
  
  (2) **Well-Ordered.**  All subsets of the empty set have a least element, since there are no subsets of the empty set.

   d. $\text{pow}(\mathbb{N})$; $\text{compare}(S, T) := |S| < |T|$

   (3) **Not Well-Ordered.**  Here's an example of a subset of $\text{pow}(\mathbb{N})$ that is not well-ordered by the comparator: $\{ s_1 = \{ 0 \}, s_2 = \{ 1 \} \}$.  Since the comparison is based on the sizes, there is no least element: neither $| s_1 | < | s_2 |$ or $| s_2 | < | s_1 |$.

\clearpage

# Sets and Relations

3. Indicate for each statement if it is valid (always true) or
invalid.  For invalid statements, provide a counter-example supporting
your answer.

   a. For any sets $A$ and $B$, $|A \cup B|\, \le \,| A | \, + \, | B |$.

   (2) **Valid.**  $|A \cup B| = |A| + |B| - |A \cap B| \le |A| + |B|$. 

   b. For any sets $A$ and $B$, $(\forall a \in A \ldotp a \in B)
\implies A \subseteq B$.

   (2) **Valid.** Follows directly from the definition of $\subseteq$.

   c. For any sets $A$ and $B$, there exists a total ([$\ge 1$
arrow out]), injective ([$\le 1$ arrow in]) relation $R$ between $A$
and $A - B$.

   (3) **Invalid.** Counter-example: $A = B$.  Then, $A-B = \emptyset$,
so there is no way to have arrows out of $A$ in $R$.

   d. For any sets $A$ and $B$, $B \in \text{pow}(A) \implies |B| \, < |A|$.

   (3) **Invalid.**  $A \in \text{pow}(A)$.

\clearpage

# Induction

4. Prove by induction that every finite non-empty subset of the real
numbers contains a _least_ element, where an element $x \in S$ is
defined as the least element if $\forall z \in S - \{ x \} \ldotp x <
z$.  (Note: you should not just assume all finite sets are well
ordered for this question.)

(This question was on Exam 2, Exam 1, and Problem Set 5, with minor
modifications, and you were notified in the Exam 2 solutions that you would see it again on the final. So, everyone should have gotten a good proof for this!)

Our induction predicate is:
$$
P(n) ::= \text{all sets of real numbers of size}\ n\ \text{have a {\em least} element}.
$$
We what to show this holds for all non-empty sets, $n \in \mathbb{N}^{+}$.

_Base case_: $n = 1$. Consider a set of real numbers with size one:
$\{ x \}$.  It has only a single element, $x$, so that element will be
the minimum.
	
_Inductive step_: $\forall m \in \mathbb{N}^+ \ldotp P(m) \implies P(m + 1)$.  Assume all sets of real numbers of size $m$ have a least element. Every set of size $m + 1$, $S'$, is the result of adding a new element, $q$, to a set of size $m$: $S' = S \cup \{ q \}$, $q \notin S$.   By the inductive hypothesis, we know $S$ (size $m$) has a least element, $w$.  There are two possibilities for the new element: (1) $q < m$. Then, $\text{minimum}(S') = q$.  or (2) $q > m$. Then, $\text{minimum}(S') = m$.  In both cases, the minimum of $S'$ is well defined.

By induction, we have proven $P(n)$ holds for all $n \in \mathbb{N}^{+}$.


\clearpage

# State Machines

5.  Consider the state machine, $M_1 = (S, G, q_0)$ below:

\begin{equation*}
\begin{split}
S &= \{ (a, b) \, | \, a, b \in \mathbb{N} \} \\
G &= \{ (a, b) \rightarrow (a', b') \, | \, a, a', b, b' \in \mathbb{N} \wedge a + b = a' + b' \} \\
q_0 &= (0, 0) \\
\end{split}
\end{equation*}

a. Describe the reachable states for $M_1$.

(4) There is only one reachable state: $(0, 0)$.  Since the
transitions rule requires $a' + b' = a + b$, if $a + b = 0$ (as it
does for state $q_0 = (0, 0)$), there are no other natural numbers
that some to 0.

(If you misread the $\mathbb{N}$ as $\mathbb{Z}$, which is a more
sensible state machine, then the reachable states are the states $(a,
-a)$ for all $a \in \mathbb{Z}$.)

For each of the following predicates, answer whether or not it is a
_preserved invariant_ for $M_1$ as defined above, and provide a brief
justification supporting your answer.

b. $P(q = (a, b)) := a > b$

(3) **Not Preserved**.  There is a transition from $(3, 2) \rightarrow (1,
  4)$, but the property is satisfied by $(3, 2)$ but not by $(1, 4)$.

c. $P(q = (a, b)) := a + b\ \text{is odd}$

(3) **Preserved**.  The transitition rule ensures $a' + b' = a + b$, so if $a + b$ is odd, so is $a' + b'$.

\clearpage

# Cardinality

6. For each set defined below, answer is the set if _countable_ or
_uncountable_ and support your answer with a convincing and concise
proof.  (Recall that $\mathbb{N}$ is the set of natural numbers,
$\mathbb{R}$ is the set of real numbers.)

a. set of all subsets of students in cs2102

(2) **Countable.** The number of students in cs2102 is finite, so the size
  of its powerset of also finite.  All finite sets are countable.

b. $\{ (a, b) | a, b \in \mathbb{N} \}$

(3) **Countable.** This set is the same as $\mathbb{N} \times \mathbb{N}$,
  which we already proved is countable.  Alternately, you should show
  a bijection between $\mathbb{N}$ and the set: 

	$$ 0 \leftrightarrow (0, 0), 1 \leftrightarrow (0, 1), 2 \leftrightarrow (1, 0), 3 \leftrightarrow (1, 1), 4 \leftrightarrow (1, 2), \ldots $$
   dove-tailing through the pairs similarly to the proof that the
rationals are countable.

c. $\{ (a, b) | a \in \mathbb{N}, b \in \mathbb{R} \}$

(2) **Uncountable.** Since $\mathbb{R}$ is uncountable, any sequence
that includes an element from $\mathbb{R}$ must also be uncountable.

d. the set of all Turing Machines that accept no strings

(3) **Countable.** This is a subset of the set of all Turing Machines,
which we know is countable.  Any subset of a countable set must be
countable.

\clearpage

# Proofs

Consider the Take-Away game: start with $n$ sticks; at each turn, a
player must remove 1 or 2 sticks. The player who takes the last stick
wins.  

7. Prove that Player 1 has a winning strategy for a two-player
game of Take-Away where Player 1 moves first if the initial number of
sticks is $n$ is not divisible by 3.

We prove using strong induction.  The predicate is:
$$
P(n) ::= \text{Player 1 has a winning strategy for a Take-Away game starting with}\ n\ \text{sticks, if}\ n\ \text{ is not divisible by 3}.$$

We want to show $P(n)$ holds for all positive natural numbers.

_Base cases_: $P(1)$ and $P(2)$.  Player 1 can win by removing 1 (for $n = 1$) stick or 2 (for $n = 2$) sticks on her first move.

_Inductive case_: $\forall m \in \mathbb{N}, m > 2 \ldotp \forall k \le m . P(k) \implies P(m + 1)$.

We have three cases to consider: 

(1) $m = 3n$.  To show $P(3n + 1)$, Player 1 can remove 2 sticks,
leaving $3n - 1 = 3(n - 1) + 2$ sticks.  Since this is not divisible
by three, by the strong induction hypothesis, we know $P(3(n-1) + 2)$
is true, so this is a winning strategy, showing $P(m + 1)$ for this case.

(2) $m = 3n + 1$.  To shows $P(3n + 2)$, Player 1 can remove 1 stick,
leaving $3n + 1$ sticks.  Since this is not divisible by 3, by the strong induction hypothesis, we know $P(3n + 1)$ is true, so this is a winning strategy.

(3) $m = 3n + 2$. To show $P(3n + 3)$, we observe that $3n + 3$ is
divisible by 3.  Hence, $P(3(n+1))$ holds, since the predicate only
says there needs to be a winning strategy then $n$ is divisible by 3.

The three cases show $P(m + 1)$ holds in all cases, proving $P(n)$
holds for all $n \in \mathbb{N}^{+}$.

\clearpage

# Program Correctness

Consider the Python program below, that returns `True` if and only if
none of the elements of the input list are below 5.  You may assume
`p` is a non-empty list of natural numbers.

\begin{verbatim}
   def all_good(p):
      i = 0
      good = True
      while i < len(p):
         if p[i] < 5:
            good = False
         i = i + 1
      return good
\end{verbatim}

8. Complete the definition of the state machine, $M_g = (S, G, q_0)$,
below that models `all_good`.

\begin{equation*}\Large
\begin{split}
S &= \{ (i, g) \, | \, i \in \mathbb{N}, g \in \{ \text{\bf True}, \text{\bf False} \} \} \\
G &= \{ (i, g) \rightarrow (i', g') \; | \\
  & \qquad i, i' \in \mathbb{N}, g, g' \in \{ \text{\bf True}, \text{\bf False} \} \\
  & \qquad \wedge \underline{i < \text{len(p)}} \\
  & \qquad \wedge i' = \underline{i + 1}\\
  & \qquad \wedge g' = \begin{cases}
 \underline{\text{\bf False}} \;\, \text{if p[i]} < 5 \\
 \underline{g} \;\, \text{otherwise} \\
\end{cases} \\
& \qquad \} \\
q_0 &= \underline{(0, \text{\bf{True}})}
\end{split}
\end{equation*}

\clearpage

9. Prove that for any input that is a finite list of natural numbers,
the state machine $M_g$ always terminates, and the final state is a
state where the value of $g$ is $\text{\bf True}$ if and only if the
input list contains no elements with value below 5.

First, we prove termination.  All the transitions must satisfy $i <
\text{len(p)}$, so there are no transitions from any state where $i
\ge \text{len(p)}$.  Since $\text{len(p)}$ is finite, the initial state
has $i = 0$, and all transitions include $i' = i + 1$ which increases
$i$ by 1, the machine must eventually reach a state where $i =
\text{len(p)}$.  Since that state has no outgoing edges, the machine
terminates.

To prove correctness, we use the invariant principle.  The preserved
invariant is:

$$
P(q = (i, g)) := 
$$




\clearpage

# Recursive Data Types

Define a $\text{\em BalancedTree}$ as:

- **Base case:** $\text{\bf null} \in \text{\em BalancedTree}$.

- **Constructor case:** if $t_1, t_2 \in \text{\em BalancedTree}$ and
    $\text{count}(t_1) = \text{count}(t_2)$ then $\text{node}(t_1,
    t_2) \in \text{\em BalancedTree}$.

where $\text{count}$ is defined for all $\text{\em BalancedTree}$ objects as:

\begin{equation*}
\text{count}(t) := \begin{cases} 
0 \qquad\qquad & t = \text{\bf null} \\
1 + \text{count}(t_1) + \text{count}(t_2) & t = \text{node}(t_1, t_2) \\
\end{cases}
\end{equation*}

The $\text{left}$ and $\text{right}$ operations are defined by:
\begin{equation*}
\begin{split}
\text{left}(\text{node}(t_1, t_2)) := t_1 \\  
\text{right}(\text{node}(t_1, t_2)) := t_2
\end{split}
\end{equation*}

10. Explain why $\text{left}$ is not a _total function_ for $\text{\em
BalancedTree}$ objects domain.

\answerbox{0.5in}

11. Prove that for all non-null $\text{\em BalancedTree}$ objects, $t$, $\text{count}(\text{left}(t)) = \text{count}(\text{right}(t))$.


\clearpage

# Turing Machines

12. Prove that there exists a Turing Machine that (1) accepts an
infinite number of inputs and (2) does not terminate on an infinite
number of inputs.

\clearpage

# Countable Sets are Well-Ordered

13. Prove that all countable sets are well-ordered.


\answerbox{7.5in}

\cdbox{End of Exam Questions (last page is optional).}

\clearpage

# Optional Guidance

This question is optional, and it will not count against you if you
decline to answer it.  

What grade do you believe you deserve in cs2102?  \bigfillin

Explain why:

\answerbox{3in}

Anything else you want me to know?

\answerbox{3in}

\begin{flushright}\Huge
Score: \fillin
\end{flushright}

