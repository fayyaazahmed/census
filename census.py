import sys, argparse, csv
from itertools import combinations

def read_csv(file_name):
    
    populations = []
    
    with open(file_name, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            for item in row:
                try:
                    number = int(item)
                    populations.append(number)
                except ValueError:
                    pass  # Skip non-integer values
                except IOError:
                    # catches erroneous file names
                    sys.stdout.write("Could not read file \'" + file_name + "\'\n")
                    sys.exit()

    return populations


def find_subset(nums, target):
    for r in range(1, len(nums) + 1):
        for subset in combinations(nums, r):
            if sum(subset) == target:
                return list(subset)
    
    # No subset found. sad :(
    return []


def main():
    """
    Parses command-line arguments and runs the program to read in a csv file of populations uses combinations to 
    create sum sets and then checks the sum of each. The first valid subset is returned.
    
    Command-line arguments:
    -h, --help: show this help message and exit
    input_file: required positional argument; specifies the CSV file of populations to read (Format: count (integer))
    target:     required value to sum to.

    Returns:    String output
    """
    # basic CLI interface for better accessiblity
    parser = argparse.ArgumentParser(
        description="Census - Finds the subset of populations that sum to the target",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("input_file", help="CSV file of populations (Format: count (integer)")
    parser.add_argument("target", help="Target value to sum to.")
    args = parser.parse_args()
    config = vars(args)

    populations = read_csv(config['input_file'])
    target = int(config['target'])
    subset = find_subset(populations, target)

    # returns and exits for empty set
    if len(populations) < 1:
        sys.stdout.write("No values were found in \'" + config['input_file'] + "\'\n")
        sys.exit()

    if subset:
        print('Target:\t\t' + str(target))
        print('Subset:\t\t' + str(subset))
    else:
        print("No subset found with a total population of ", target)


if __name__ == "__main__":
    main()