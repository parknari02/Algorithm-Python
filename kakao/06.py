def solution(n, m, x, y, r, c, k):
    dist = abs(x-r) + abs(y-c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    dirs = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

    ans = []
    cur_x, cur_y = x, y

    for step in range(k):
        remain = k - step - 1
        moved = False

        for ch, dx, dy in dirs:
            nx, ny = cur_x + dx, cur_y + dy
            if not ( 1 <= nx <= n and 1 <= ny <= m):
                continue
            need = abs(nx-r) + abs(ny-c)
            if need <= remain:
                ans.append(ch)
                cur_x, cur_y = nx, ny
                moved = True
                break
        if not moved:
            return "impossible"
    return "".join(ans)