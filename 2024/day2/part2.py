# 引数のリストがsafeかどうか
def is_safe(num_list):
    diff_list = [num_list[i + 1] - num_list[i] for i in range(len(num_list) - 1)]
    is_increasing = all(n > 0 for n in diff_list)
    is_decreasing = all(n < 0 for n in diff_list)
    is_safe = all(abs(n) in {1, 2, 3} for n in diff_list)
    if (is_increasing or is_decreasing) and is_safe:
        return True
    else:
        return False
    
def main():
    ans = 0
    with open("2024/day2/input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        num_list = list(map(int, line.strip().split()))

        # 操作なしでもsafeか
        if is_safe(num_list):
            ans += 1

        # 操作ありでsafeか判断
        else:
            for i in range(len(num_list)):
                new_nums = num_list[:i] + num_list[i+1:]
                if is_safe(new_nums):
                    ans += 1
                    break
                
    print(ans)

if __name__ == "__main__":
    main()