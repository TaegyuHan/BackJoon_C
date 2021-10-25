import sys
# sys.stdin = open("./1924.txt")
month, day = map(int, sys.stdin.readline().split())
month_day = { "1": 31,   "12": 31, "2": 28,
              "3": 31,   "4": 30,
              "5": 31,   "6": 30,
              "7": 31,   "9": 30,
              "8": 31,   "11": 30,
              "10": 31 }

week_table = {
    0: "SUN",
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT"
}

day_sum = 0
for mon in range(month - 1, 0, -1):
    day_sum += month_day[str(mon)]
day_sum += day
week = day_sum%7

print(week_table[week])