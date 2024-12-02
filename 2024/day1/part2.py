def main():
    a, b = zip(*[map(int, line.strip().split()) for line in open("2024/day1/input.txt")])
    ans = 0
    
    for num in a:
        cnt = b.count(num)
        ans += num * cnt
    print(ans)

if __name__ == "__main__":
    main()