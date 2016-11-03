# 1
  - Age: Integer (although for databases it would be better to store the date of birth using a date format)
  - Salary: Float
  - ZIP Code: Integer
  - City: String

# 2
  The Median is robust against outliers. The Mean and Standard Deviation are not.

  Sample Data Set:

  ` D = {10, 10, 20, 30, 4000} `

  The Mean is: `(10 + 10 + ...) / 5 = 814`.
  It's heavily influenced by the outlier `4000`.

  The Median is: `20` (The element in the middle of the sorted set `D`).
  It's not really influenced by the outlier `4000` and thus the Median is robust.

  The Standard Deviation is: `sqrt( ( (10 - 814)^2 + (10 - 814)^2 + ... ) / (5-1) ) = 1781,04`.
  It's influenced by the outlier `4000` because it uses the Mean.

# 3
### a
- Mean of X: `71,45`
- Median of X: `71,5`
- Mode of X: `74` (occurs 3 times)

### b
Variance of X: `( (69 - 71,45)^2 + (74 - 71,45^2) + ...) / (n-1) = 14,576`

<div class="page-break" />

### c
![](scatterPlot3c.png)

### d
Pearson's correlation coefficient `Corr(X, Y) = 0,84471`

This means that there is a pretty strong correlation between the two variables and that the relationship between them can be pretty well described by a linear equation `y = f(x) = m*x + b`. (If the correlation was `+1`, the relationship could be perfectly described by a linear equation.) Furthermore, we know that with increasing X values, Y values will also increase because the value of the correlation is positive. The interpretation fits the impression that the scatter plot gave us about the data: that there seems to be a relationship between X and Y.

Further interpretation is not really possible since the only semantics given about X and Y is that they are "random variables". It can only be said that their values don't seem to be that random after all.

A test with `A = (1, 2, ..., 100)`, `B = (2, 4, ..., 200)` (so that the B value is always exactly twice as big as the corresponding A value) yields a near "total positive" correlation of `0,99`. When scatter-plotted, one can draw a straight line with `y = f(x) = 2*x` to exactly connect all dots. This confirms our interpretation.

<div class="page-break" />

# 4

Show that `P(X) = P(X|Y) <=> P(X, Y) = P(X)P(Y)`

### Part 1
`P(X) = P(X|Y)`

- with the *Multiplication Axiom* `P(X, Y) = P(X|Y)P(Y)`

=> `P(X) = P(X, Y) / P(Y)`

=> `P(X, Y) = P(X)P(Y)`

### Part 2

`P(X, Y) = P(X)P(Y)`

- if the probability of X **AND** Y is the same as the probability of X **times** the probability of Y, then X, Y are *independent* from each other
- thus, the probability of X is the same as the probability of X under the condition that the event Y already occurred because the Y doesn't influence the likelihood of the X (since they're independent from each other)

=> `P(X) = P(X|Y)`
