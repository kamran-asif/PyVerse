"""
Probability of Two Boxes Having the Same Number of Distinct Balls
Given 2n balls of k different colors, find the probability that when the balls are randomly divided into two boxes with n balls each, both boxes have the same number of distinct colors.
"""

from math import factorial  # import factorial function from math module
from typing import List     # for type hinting the input as a list of integers

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2  # total number of balls in one box (half of total balls)

        # helper function to compute the multinomial coefficient:
        # total! / (x1! * x2! * ... * xk!) where xi are counts of each color
        def multinomial(nums):
            result = factorial(sum(nums))  # numerator = factorial of total number of balls
            for num in nums:
                result //= factorial(num)  # divide by factorial of each count
            return result  # return the computed multinomial coefficient

        # recursive DFS function to try all possible distributions of balls
        def dfs(i, box1, box2):
            if i == len(balls):  # base case: all colors have been considered
                if sum(box1) == sum(box2) == n:  # if both boxes have exactly n balls
                    # calculate number of ways to arrange the current distribution
                    prob = multinomial(box1) * multinomial(box2)

                    # count number of distinct colors in both boxes
                    distinct1 = sum(1 for x in box1 if x > 0)
                    distinct2 = sum(1 for x in box2 if x > 0)

                    # if both boxes have same number of distinct colors,
                    # return this as a valid arrangement
                    return (prob, prob if distinct1 == distinct2 else 0)
                # If not a valid total count of balls, ignore this case
                return (0, 0)

            total_prob, valid_prob = 0, 0  # Initialize probability counters

            # try all possible ways to split balls[i] between box1 and box2
            for x in range(balls[i] + 1):
                y = balls[i] - x  # Remaining balls go to the second box

                # only proceed if we don't exceed the limit in either box
                if sum(box1) + x <= n and sum(box2) + y <= n:
                    # Add current color split to both boxes
                    new_box1 = box1 + [x]
                    new_box2 = box2 + [y]

                    # recurse to the next color
                    t, v = dfs(i + 1, new_box1, new_box2)

                    # accumulate total and valid probabilities
                    total_prob += t
                    valid_prob += v

            # return accumulated probabilities for this path
            return (total_prob, valid_prob)

        # start DFS from the first color with empty boxes
        total_prob, valid_prob = dfs(0, [], [])

        # return the ratio of valid to total arrangements (i.e., the probability)
        return valid_prob / total_prob if total_prob > 0 else 0
