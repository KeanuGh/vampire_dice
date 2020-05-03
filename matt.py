# only importing ordered dictionary, there are probably other libraries with useful tools for this
from collections import OrderedDict


def odds(num, diff):
    # input is the number of dice rolled and the difficulty of the roll (must be between 2 and 9)
    # make ordered dictionary of all possible number of successes and set their count to 0
    tally = OrderedDict()
    for x in range(3 * num + 1):
        tally[str(x - num)] = 0

    # print(tally)

    # generate an integer with digits equal to number of dice rolled
    # has additional 1 digit in front to keep 0 digit information
    count = 10 ** num

    # iterate through all the possible combinations (this needs to be improved)
    # could only calculate a subset and multiply by the number of permutations
    for m in range(count):
        # reset count on number of successes for this roll
        n_success = 0
        # turn the count to a string so can look at individual digits, maybe there is a better method than this
        c = str(count)

        # run through each digit, representing the roll of each die
        for l in range(num):
            # check how many successes or faiures each dice generates based on difficulty
            if int(c[l + 1]) == 1:
                n_success -= 1
                # print('That's a botch')
            elif int(c[l + 1]) == 0:
                n_success += 2
                # print('Critical success!')
            elif int(c[l + 1]) >= diff:
                n_success += 1
                # print('Success!')
                # print(c[l+1])

        # print(succ)
        # print(count)

        # add to tally of number of rolls that generate a certain number of successes
        tally[str(n_success)] += 1

        # increase the count by 1 to give a new dice roll
        count += 1

    # change tally into percentages
    for y in range(3 * num + 1):
        tally[str(y - num)] = float(tally[str(y - num)]) / 10 ** (num - 2)

    # print out results, want to add a graph readout later, show the bell curve
    print('Percentage chance of each possible number of successes:')
    for key, value in tally.items():
        print(key, value)
    # print(tally)


odds(3, 7)
# odds(8,7)
