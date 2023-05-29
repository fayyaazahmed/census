# Cenus
Finds the subset of populations that sum to the target value.


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

`populations`: Score of the student (integer).

## Output Format
The program outputs the top student(s) in the following format to STDOUT (see result_example.txt):
```
Target: <target>
Populations: [populations[0], populations[1], populations[n]]
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

- 