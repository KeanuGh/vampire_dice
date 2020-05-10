import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


def odds(n_dice: int, n_iter: int, diff: int, die_size: int = 10, plot: bool = False) -> None:
    """
    Calculates and displays probabilities of successes for n_dice
    if you roll:
     1: -1 success
     die_size (default 10): 2 success
     >=diff: 1 success
    :param plot: if True displays bar plot of possible outcomes and their probabilities
    :param n_dice: number of dice to roll
    :param n_iter: number of iterations
    :param diff: roll difficulty
    :param die_size: how many sides does your dice have
    :return: None
    """
    successes = []
    for i in range(n_iter):
        success = 0
        # For each dice, roll and calculate success
        for die in range(n_dice):
            roll = np.random.randint(die_size) + 1  # because dice go 1 to n not 0 to n-1
            if roll == 1:
                success += -1
            elif roll == die_size:
                success += 2
            elif roll >= diff:
                success += 1

        successes.append(success)

    counts = Counter(successes)
    counts_proba = {k: 100 * v / n_iter for k, v in counts.items()}
    for score, proba in sorted(counts_proba.items()):
        print(f'{score}: {proba}')

    if plot:
        plt.bar(counts_proba.keys(), counts_proba.values(), color='r', edgecolor='k')
        plt.xticks(list(counts_proba.keys()))
        plt.xlabel("Success")
        plt.ylabel("%")
        plt.annotate(f"diff = {diff}\nmean = {np.mean(successes):.2f}\nstd = {np.std(successes):.2f}",
                     xy=[.75, .75], xycoords='figure fraction')
        plt.show()


if __name__ == '__main__':
    for diff in range(1,10):
        odds(n_dice=3,
             n_iter=1000000,
             diff=diff,
             plot=True
             )
