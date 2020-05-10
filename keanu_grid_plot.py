import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def odds(n_dice: int, n_iter: int, diff: int, die_size: int = 10):
    """
    Calculates and displays probabilities of successes for n_dice.
    if you roll:
     1: -1 success
     10 (max): 2 success
     >=diff: 1 success
    :param n_dice: number of dice to roll
    :param n_iter: number of iterations
    :param diff: roll difficulty
    :param die_size: how many sides does your dice have
    :return: lists of sucess counts and their probabilities, mean, standard deviation
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

    mean = np.mean(successes)
    std = np.std(successes)

    counts = Counter(successes)
    counts_proba = {k: 100 * v / n_iter for k, v in counts.items()}

    return list(counts_proba.keys()), list(counts_proba.values()), mean, std


def main():
    # range of dice and difficulty (inclusive)
    n_dice_range = (3, 6)
    n_diff_range = (4, 8)

    # create plot of plots objects
    fig, axs = plt.subplots(n_dice_range[1] - n_dice_range[0] + 1,
                            n_diff_range[1] - n_diff_range[0] + 1,
                            sharex='col', sharey='row')
    for i, n_dice in enumerate(range(n_dice_range[0], n_dice_range[1] + 1)):
        for j, diff in enumerate(range(n_diff_range[0], n_diff_range[1] + 1)):
            x, y, m, s = odds(n_dice=n_dice,
                              n_iter=100000,
                              diff=diff,
                              )
            axs[i, j].bar(x, y, color='r', edgecolor='k')
            axs[i, j].set_xlabel("Success")
            axs[i, j].set_ylabel("%")
            axs[i, j].set_xticks(x)
            axs[i, j].text(.75, .75,
                           f"n_dice = {n_dice}\ndiff = {diff}\n"
                           f"mean = {m:.2f}\nstd = {s:.2f}",
                           transform=axs[i, j].transAxes, fontsize=6)

    for ax in fig.get_axes():
        ax.label_outer()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    plt.tight_layout()
    plt.savefig('nice_grid.png')
    plt.show()


if __name__ == '__main__':
    main()
