import re
import itertools


def compare_truth_tables(expression1, expression2):
    # Define the variables in the expressions
    variables = sorted(set(re.findall(r'\b[A-Za-z]\b', expression1 + expression2)))

    # Determine the width of the longest variable
    width = max(len(v) for v in variables)

    # Print the header row
    print('+' + '+'.join(['-' * (width + 2) for v in variables]) + '+---------+---------+')
    print('| ' + ' | '.join(v.center(width) for v in variables) + ' | Result1 | Result2 |')
    print('+' + '+'.join(['-' * (width + 2) for v in variables]) + '+---------+---------+')

    # Generate all possible combinations of values for the variables
    for values in itertools.product([True, False], repeat=len(variables)):
        # Create a dictionary mapping variables to values
        assignment = dict(zip(variables, values))

        # Evaluate the expressions under this assignment of values
        result1 = eval(expression1, assignment)
        result2 = eval(expression2, assignment)

        # Print the values of the variables and the results of the expressions
        if result1 != result2:
            print('| ' + ' | '.join(str(int(v)).rjust(width) for v in values) + ' |  ' + str(result1).ljust(7) + '|  ' + str(result2).ljust(7) + '| *')
        else:
            print('| ' + ' | '.join(str(int(v)).rjust(width) for v in values) + ' |  ' + str(result1).ljust(7) + '|  ' + str(result2).ljust(7) + '|')

    # Print the footer row
    print('+' + '+'.join(['-' * (width + 2) for v in variables]) + '+---------+---------+')


expression1 = "(A and B) or (C and D)"
expression2 = "(A and B) or (C and not D)"

compare_truth_tables(expression1, expression2)
