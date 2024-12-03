import re

def main():
    with open("2024/day3/input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    nums_pair_list = []
    for line in lines:
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        nums_pair_list += re.findall(pattern, line)

    ans = 0
    for num_pair in nums_pair_list:
        m, n = map(int, num_pair)
        ans += m * n

    print(ans)

if __name__ == "__main__":
    main()