"""
- Since one should just comput and print the mean of each column, I expect just to be numbers there
- I also expect the first line to be a headline
"""

import sys

def main():
    if (len(sys.argv) != 2):
        print("USAGE: parse_csv_number /path/to/csv", file=sys.stderr)
        return
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()
    headers = lines[0].split(",")
    vals = [l.split(",") for l in lines[1:]]

    res = dict()
    for i in range(len(headers)):
        all_vals = [float(v[i]) for v in vals]
        res[headers[i]] = sum(all_vals) / len(all_vals)

    for k,v in res.items():
        print(k.strip(), v)


if __name__ == "__main__":
    main()
