# 行ごとにリスト化
def main():
    with open("2024/day2/input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        num_list = list(map(int, line.strip().split()))

# 列ごとにリスト化
def main():
    a, b = zip(*[map(int, line.strip().split()) for line in open("2024/day1/input.txt")])

if __name__ == "__main__":
    main()