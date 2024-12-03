import re

def main():
    enabled = True  # 直後mulの実行可否
    pattern_do = r"do\(\)"
    pattern_dont = r"don't\(\)"
    pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"
    ans = 0

    with open("2024/day3/input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # mul, do, don'tを全て抽出し、先頭から一致した文字列を見ていく
    for line in lines:
        for match in re.finditer(f"{pattern_mul}|{pattern_do}|{pattern_dont}", line):
            if match.group(0).startswith("mul"):
                if enabled:
                    x, y = map(int, match.groups())
                    ans += x * y
            elif match.group(0).startswith("don't"):
                enabled = False
            elif match.group(0).startswith("do"):
                enabled = True

    print(ans)

if __name__ == "__main__":
    main()