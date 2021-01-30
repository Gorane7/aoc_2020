import random
import math
import numpy as np
from functools import reduce

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    # data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    valid = 0
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional = ["cid"]
    current = fields[:]
    disqualified = False
    validations = {
        "byr": lambda x: x.isnumeric() and len(x) == 4 and 1920 <= int(x) <= 2002,
        "iyr": lambda x: x.isnumeric() and len(x) == 4 and 2010 <= int(x) <= 2020,
        "eyr": lambda x: x.isnumeric() and len(x) == 4 and 2020 <= int(x) <= 2030,
        "hgt": lambda x: "cm" in x and x.strip("cm").isnumeric() and 150 <= int(x.strip("cm")) <= 193 or "in" in x and x.strip("in").isnumeric() and 59 <= int(x.strip("in")) <= 76,
        "hcl": lambda x: len(x) == 7 and x[0] == "#" and reduce(lambda a, b: a and b, [x[y] in "0123456789abcdef" for y in range(1, 7)]),
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: len(x) == 9 and x.isnumeric()
    }
    for line in data:
        if len(line) == 0:
            current = fields[:]
            disqualified = False
            continue
        for pair in line.split(" "):
            key = pair.split(":")[0]
            value = pair.split(":")[1]
            if key in current:
                if key in validations.keys() and not validations[key](value):
                    disqualified = True
                current.remove(key)
                if len(current) == 0 and not disqualified:
                    valid += 1
    print(valid)
