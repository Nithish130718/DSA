# -*- coding: utf-8 -*-
"""
This module provides a function that finds the odd distinct pairs of a list. This exercise
comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 8th April 2023

Revised on: 9th April 2023

Original Author: Nithish Kumar S
"""


import random


def odd_product(data):
    """
    Parameters: 'data' which is a list of integers.

    This function checks and given the possible distinct pairs with odd product, created from the elements that are
    present in a list (passed as an argument).

    Raises Exception: if len(data) is less than 1.

    Returns: a list of distinct pairs with odd product, if len(data) > 1.

    """

    temp = data.copy()
    odd_no = []
    pairs = []

    print("The list is:", temp)

    if len(data) < 1:
        raise Exception(
            f"List has {len(data)} elements and cannot have any distinct pairs as asked."
        )

    else:
        for i in data:
            if i % 2 != 0:
                odd_no.append(i)

        for i in range(len(odd_no)):
            for j in range(i + 1, len(odd_no)):

                pairs.append((odd_no[i], odd_no[j]))

        print("The pairs with odd product are:", pairs)

        distinct_pairs = list(set(pairs))

        return distinct_pairs


# getting input for the no. of terms and range to  create random list for each trial of execution.
# using __name__ so that the input test cases are not imported.

if __name__ == "__main__":
    n = int(input("Enter the number of terms in the sequence:"))
    start = int(input("Enter the start range:"))
    end = int(input("Enter the end range:"))

    data = []

    for i in range(n):
        number = random.randint(start, end)
        data.append(number)

    print("The distinct pairs in the list with odd product are:", odd_product(data))
