import itertools
import re


def truth_table(expression):
    # Define the variables in the expression
    variables = sorted(set(re.findall(r'\b[A-Za-z]\b', expression)))

    # Determine the width of the longest variable
    width = max(len(v) for v in variables)

    # Print the header row
    print('+' + '+'.join(['-' * (width + 2) for v in variables]) + '+--------+')
    print('| ' + ' | '.join(v.center(width) for v in variables) + ' | Result |')
    print('+' + '+'.join(['-' * (width + 2) for v in variables]) + '+--------+')

    # Generate all possible combinations of values for the variables
    for values in itertools.product([True, False], repeat=len(variables)):
        # Create a dictionary mapping variables to values
        assignment = dict(zip(variables, values))

        # Evaluate the expression under this assignment of values
        result = eval(expression, assignment)

        # Print the values of the variables and the result of the expression
        print('| ' + ' | '.join(str(int(v)).rjust(width) for v in values) + ' | ' + str(result).ljust(7) + '|')

    # Print the footer row
    print('+' + '+'.join(['-' * (width + 2) for v in variables]) + '+--------+')


truth_table("(A and B) or (C and D)")
