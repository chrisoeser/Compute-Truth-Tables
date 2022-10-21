Compute-Truth-Tables
===

This program inputs two arbitrary Boolean expressions, generates each truth table and then compare them to check for equivalences

It prints out their truth tables.

|  A  |  B  | AND |
|:---:|:---:|:---:|
|  0  |  0  |  0  |
|  0  |  1  |  0  |
|  1  |  0  |  0  |
|  1  |  1  |  1  |

|  A  |  B  | OR |
|:---:|:---:|:---:|
|  0  |  0  |  0  |
|  0  |  1  |  1  |
|  1  |  0  |  1  |
|  1  |  1  |  1  |

The two input lines must contain two letter variables and one these boolean operators, AND, OR, NOT. The input can also include parenthesis.

e.g. `a AND NOT b` `a OR b` `NOT(a AND b)`
