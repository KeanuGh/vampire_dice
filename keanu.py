import numpy as np
from collections import Counter


def odds(n_dice: int, n_iter: int, diff: int, die_size: int = 10) -> None:
    """
    Calculates and displays probabilities of successes for n_dice
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
            elif dice_n >= diff:
                success += 1

        successes.append(success)

    counts = Counter(successes)
    counts_proba = {k: v / n_iter for k, v in counts.items()}
    for key, value in sorted(counts_proba.items()):
        print(f'{key}: {value}')


if __name__ == '__main__':
    for n in range(1):
        odds(n_dice=18,
             n_iter=1000000,
             diff=7)
        print('\n')
