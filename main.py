#! /bin/python

from functools import reduce
from operator import or_

def number_of_options(votes):
    return len(reduce(or_, [set(v) for v in votes]))


def score(votes):
    nb_options = number_of_options(votes)
    vote_values = map(lambda vote: {k: nb_options-(v) for v, k in enumerate(vote)}, votes)

    sum_votes = reduce(lambda v, w: {k: v[k]+ w[k] for k in v.keys()}, vote_values)

    return sum_votes


def borda(votes):
    sum_votes = score(votes)
    return max(sum_votes, key=sum_votes.get)


def main():
    tests()


def tests():
    votes = [
        ['a', 'b', 'c', 'd'],  # a = 4*2 + 3*2 = 14
        ['b', 'a', 'c', 'd'],  # b = 4*1 + 3*1 + 2*1 + 1*1 = 10
        ['c', 'a', 'b', 'd'],  # c = 4*1 + 3*1 + 2*2 = 11
        ['a', 'c', 'd', 'b'],  # d = 2*1 + 1*3 = 5
    ]

    print(number_of_options(votes) == 4)
    print(number_of_options(votes + ['c', 'a', 'b', 'd', 'e']) == 5)
    print(score(votes) == {'a': 14, 'b': 10, 'c': 11, 'd': 5})
    print(borda(votes) == 'a')


if __name__ == "__main__":
    main()
