CSCI-561	- Fall	2016	- Foundations	of	Artificial	Intelligence

Homework	1-3

I have uploaded all the assignments that I did in CSCI-561 in Fall 2016 semester in this repository.

All the .py files take "input.txt" as input and write output to "output.txt". The format of each input and output file is mentioned in the project description .pdf files.

Project Description: Each .py file has a corresponding project description .pdf file which contains the problem statement.

*****For INFERENCE USING RESOLUTION project*****
The operator with its operand(s) are enclosed in parenthesis.

The sample input and output files given in project description are incorrect, the correct sample input file and output file are given below:

Sample input.txt:

6

F(Bob)

H(John)

~H(Alice)

~H(John)

G(Bob)

G(Tom)

14

(A(x) => H(x))

(D(x,y) => (~H(y)))

((B(x,y) ^ C(x,y)) => A(x))

B(John,Alice)

B(John,Bob)

((D(x,y) ^ Q(y)) => C(x,y))

D(John,Alice)

Q(Bob)

D(John,Bob)

(F(x) => G(x))

(G(x) => H(x))

(H(x) => F(x))

(R(x) => H(x))

R(Tom)


output.txt for the above input.txt:

FALSE

TRUE

TRUE

FALSE

FALSE

TRUE
