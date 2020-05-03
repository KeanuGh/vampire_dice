import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


def odds(n_dice: int, n_iter: int, diff: int, die_size: int = 10):
    """
    Calculates and displays probabilities of successes for n_dice
    if you roll:
     1: -1 success
     10 (max): 2 success
     >=diff: 1 success
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
    mean = np.mean(successes)
    std = np.std(successes)

    counts = Counter(successes)
    counts_proba = {k: 100 * v / n_iter for k, v in counts.items()}

    return counts_proba.keys(), counts_proba.values(), mean, std


def main():
    # range of dice and difference (inclusive)
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
            axs[i, j].set_xticks(list(x))
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
