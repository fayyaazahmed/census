# Cenus
Finds the subset of populations that sum to the target value. Uses combinations to create 
subarrays of the populations that are then summed and checked against the target value.

The first valid subset is returned.


## Requirements
- `Python 2.7`

## Usage
```
python census.py [-h] <input_file> <target>
```

## Arguments
### Required Arguments
`input_file`: Specifies the path to the CSV file to be processed.

`target`: Specifies the target value for the subset problem.
### Optional Arguments
`-h`, `--help`: Shows help message and exit.

## Input Format
The input file must be in CSV format (.csv) and contain the following field(s):

`populations`: Integer value of the population (integer).

## Output Format
```
Target:     <target>
Subset:     [populations[0], populations[1], populations[n]]
```
For output to .txt file use piping:
```
python census.py input_files/sample.csv > result_sample.txt
```


## Example Usage
The following command processes sample.csv and outputs the subset of populations to the command line:

```
python census.py input_files/sample.csv 101000000
```

## Limitations
- Only returns first valid subset