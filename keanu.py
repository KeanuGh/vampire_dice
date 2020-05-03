import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


def odds(n_dice: int, n_iter: int, diff: int, die_size: int = 10, plot: bool = None) -> None:
    """
    Calculates and displays probabilities of successes for n_dice
    :param plot:
    :param n_dice: number of dice to roll
    :param n_iter: number of iterations
    :param diff: roll difficulty
    :param die_size: how many sides does your dice have
    :return: None
    """
    successes = []
    for i in range(n_iter):
        success = 0

        for d in range(n_dice):
            dice_n = np.random.randint(die_size)
            if dice_n == 0:
                success += -1
            elif dice_n == die_size - 1:
                success += 2
            elif dice_n >= diff - 1:
                success += 1

        successes.append(success)

    counts = Counter(successes)
    counts_proba = {k: 100 * v / n_iter for k, v in counts.items()}
    for key, value in sorted(counts_proba.items()):
        print(f'{key}: {value}')

    if plot:
        bins = list(counts_proba.keys())
        plt.bar(counts_proba.keys(), counts_proba.values(), color='r', edgecolor='k')
        plt.xticks(bins)
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