from argparse import ArgumentParser
from random import choices
from pandas import read_csv
import matplotlib.pyplot as plt
import csv


def calculateWeights(numbers, middle):
    smalls = tuple((number for number in numbers if number <= middle))
    biggs = tuple((number for number in numbers if number > middle))
    small_chance = 50/len(smalls)
    big_chance = 50/len(biggs)
    weights = []
    for number in numbers:
        if number in smalls:
            weights.append(small_chance)
        else:
            weights.append(big_chance)
    return weights


def createRandoms(size, min_num, max_num, middle, randoms_file_path):
    numbers = tuple(range(min_num, max_num))

    weights = calculateWeights(numbers, middle)
    data = tuple(choices(population=numbers, weights=weights, k=size))
    dataset = tuple(set(data))
    datarep = tuple((data.count(d) for d in dataset))
    with open(randoms_file_path, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["number", "repeat"])
        writer.writerows([[number, datarep[index]]
                         for index, number in enumerate(dataset)])


def plotRandoms(randoms_file_path="randoms.csv", step=10):
    data = read_csv(randoms_file_path)
    if step != 0:
        numbers = tuple(data.number)[::step]
        repeats = tuple(data.repeat)[::step]
    else:
        numbers = tuple(data.number)
        repeats = tuple(data.repeat)
    plt.plot(numbers, repeats, 'go--')
    plt.show()


def main():
    parser = ArgumentParser()
    parser.add_argument("-s", "--size", required=True,
                        help="Size of randoms.")
    parser.add_argument("-min", "--min", required=True,
                        help="Minimum number of rabdoms")
    parser.add_argument("-max", "--max", required=True,
                        help="Maximum number of rabdoms")
    parser.add_argument("-m", "--middle", required=True,
                        help="Middle of randoms")
    parser.add_argument("-step", "--plot-step", required=False,
                        help="Steps of plot.")
    parser.add_argument("-rfp", "--randoms-file-path", required=False,
                        help="Randoms csv file path. path from current directory.")
    args = parser.parse_args()

    print(f"Randoms size: {args.size}\tRandoms middle number: {args.middle}\nRandoms minimum number: {args.min}\tRandoms maximum number: {args.max}")

    if args.randoms_file_path:
        randoms_file_path = args.randoms_file_path
    else:
        randoms_file_path = str(__file__)[:-11] + "randoms.csv"

    createRandoms(int(args.size), int(args.min),
                  int(args.max), int(args.middle), randoms_file_path)

    print(f"Randoms were saved at {randoms_file_path}")

    plotRandoms(randoms_file_path, int(args.plot_step))


if __name__ == "__main__":
    main()
