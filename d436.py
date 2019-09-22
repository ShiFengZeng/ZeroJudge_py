def backtracking(s, n, ln):
    if n == ln:
        print("".join(sol))
        return

    last_char = ''
    for i in range(ln):
        if not is_used[i] and s[i] != last_char:
            last_char = s[i]
            is_used[i] = True

            sol[n] = s[i]
            backtracking(s, n + 1, ln)

            is_used[i] = False


while True:
    try:
        n = int(input())
        for _ in range(n):
            s = input()
            s = sorted(s)
            ln = len(s)
            is_used = [False] * 10
            sol = [''] * 10
            backtracking(s, 0, ln)
            print()
    except EOFError:
        backtracking(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 0, 9)
        print()
        break
