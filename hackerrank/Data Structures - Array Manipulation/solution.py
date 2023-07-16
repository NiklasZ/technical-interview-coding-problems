# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true
from typing import List, Tuple
import bisect
from collections import defaultdict


def split_up_intervals(relevant_intervals: List[Tuple[int, int, int]],
                       start: int,
                       end: int,
                       value: int) -> List[Tuple[int, int, int]]:
    new_intervals = []
    for r_start, r_end, r_value in relevant_intervals:
        # 1. The query interval is contained within the current interval
        if start >= r_start and end <= r_end:
            new_intervals += [(r_start, start - 1, r_value),
                              (start, end, r_value + value),
                              (end + 1, r_end, r_value)]
        # 2. The current interval is contained within the query interval
        elif start <= r_start and end >= r_end:
            new_intervals += [(r_start, r_end, r_value + value)]

        # 3. The query interval intersects from the left into the current interval
        elif start < r_start <= end:
            new_intervals += [(r_start, end, r_value + value),
                              (end + 1, r_end, r_value)]
        # 4. The query interval affects the right of the current interval
        elif start <= r_end < end:
            new_intervals += [(r_start, start - 1, r_value),
                              (start, r_end, r_value + value)]
        else:
            raise Exception('Badness! Should not happen')

    # Filter out edge cases where an interval is empty
    filtered_intervals = [i for i in new_intervals if i[0] <= i[1]]
    return filtered_intervals


def array_manipulation(num_values: int, queries: List[Tuple[int, int, int]]):
    # An interval is given by a (start, end, value) tuple
    starting_interval = (0, num_values - 1, 0)
    intervals = [starting_interval]

    # Move to 0-indexing because that's why python uses
    proper_queries = [(s - 1, e - 1, v) for s, e, v in queries]

    for step, (start, end, value) in enumerate(proper_queries):
        # left-most interval
        start_idx = bisect.bisect_left(intervals, start, key=lambda x: x[1])
        # right-most interval
        end_idx = bisect.bisect_right(intervals, end, key=lambda x: x[0])

        relevant_intervals = intervals[start_idx:end_idx]
        lower_remaining_interval = intervals[:start_idx]
        upper_remaining_interval = intervals[end_idx:]
        new_intervals = split_up_intervals(relevant_intervals, start, end, value)
        intervals = lower_remaining_interval + new_intervals + upper_remaining_interval

        # print(intervals)
    return max([v for _, _, v in intervals])


# ChatGPT's implementation that makes me look bad
def array_manipulation_fast(num_values: int, queries: List[Tuple[int, int, int]]) -> int:
    changes = defaultdict(int)
    for start, end, value in queries:
        changes[start - 1] += value  # Subtract 1 because Python uses 0-indexing
        if end < num_values:
            changes[end] -= value
    max_value = 0
    current_value = 0
    for i in sorted(changes):
        current_value += changes[i]
        max_value = max(max_value, current_value)
    return max_value


num_values = 10
queries = [(1, 5, 3),
           (4, 8, 7),
           (6, 9, 1)]

# print(array_manipulation(num_values, queries))


big_queries = [[29, 40, 787],
               [9, 26, 219],
               [21, 31, 214],
               [8, 22, 719],
               [15, 23, 102],
               [11, 24, 83],
               [14, 22, 321],
               [5, 22, 300],
               [11, 30, 832],
               [5, 25, 29],
               [16, 24, 577],
               [3, 10, 905],
               [15, 22, 335],
               [29, 35, 254],
               [9, 20, 20],
               [33, 34, 351],
               [30, 38, 564],
               [11, 31, 969],
               [3, 32, 11],
               [29, 35, 267],
               [4, 24, 531],
               [1, 38, 892],
               [12, 18, 825],
               [25, 32, 99],
               [3, 39, 107],
               [12, 37, 131],
               [3, 26, 640],
               [8, 39, 483],
               [8, 11, 194],
               [12, 37, 502]]

big_num_values = 40

# print(array_manipulation(big_num_values, big_queries))
print(array_manipulation_fast(num_values, queries))
