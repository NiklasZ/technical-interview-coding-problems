# https://www.hackerrank.com/challenges/climbing-the-leaderboard?isFullScreen=true

import bisect
from typing import List


# Ranking is always descending, player_scores always ascending
def climbing_leaderboard(existing_scores: List[int], player_scores: List[int]):
    unique_existing_scores = []
    existing_scores_set = set()

    # Filter duplicates
    for s in existing_scores:
        if s not in existing_scores_set:
            existing_scores_set.add(s)
            unique_existing_scores.append(s)

    # reverse to ascending as that is what bisect supports
    unique_existing_scores = list(reversed(unique_existing_scores))

    # Write your code here
    player_ranks = []
    for score in player_scores:
        idx = bisect.bisect_left(unique_existing_scores, score)
        if idx == len(unique_existing_scores) or unique_existing_scores[idx] != score:
            unique_existing_scores.insert(idx, score)
        player_ranks.append(len(unique_existing_scores) - idx)
    return player_ranks


ranking_scores = [100, 100, 50, 40, 40, 20, 10]
player_scores = [5, 25, 50, 120]
out = climbing_leaderboard(ranking_scores, player_scores)
print(out)