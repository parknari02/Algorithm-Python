def solution(commands):
    # 50x50 평탄화: (r, c) -> idx = (r-1)*50 + (c-1)
    def idx(r, c):
        return (r - 1) * 50 + (c - 1)

    # 유니온-파인드 기본구조
    N = 50 * 50
    parent = list(range(N))     # parent[i] = i 자신이 대표
    value = [""] * N            # 대표에만 값 저장 (빈 문자열 == EMPTY)
    
    # 경로 압축 find
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    # union: 규칙에 맞게 값 결정
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        # 문제 규칙: 두 셀 모두 값이 있으면 (r1,c1)쪽 값을 따른다
        # 여기서는 union 호출 순서를 (r1,c1) -> (r2,c2)로 부르도록 해
        # ra를 대표로 삼는다. (필요시 랭크 써도 되지만 규모가 작아 단순히 고정)
        va, vb = value[ra], value[rb]
        parent[rb] = ra
        # 값 병합 규칙:
        # - 둘 다 값 있음 -> ra의 값 유지
        # - 한쪽만 값 있음 -> 그 값으로
        # - 둘 다 없음 -> 빈 값
        if va and vb:
            value[ra] = va
        elif va:
            value[ra] = va
        elif vb:
            value[ra] = vb
        else:
            value[ra] = ""
        value[rb] = ""  # 하위 대표 값은 비워둔다 (대표만 값 보관)

    # 특정 대표의 모든 멤버 수집 (UNMERGE용)
    def members_of(root):
        root = find(root)
        return [i for i in range(N) if find(i) == root]

    def to_rc(i):
        r = i // 50 + 1
        c = i % 50 + 1
        return r, c

    answer = []
    for line in commands:
        parts = line.split()
        cmd = parts[0]

        if cmd == "UPDATE":
            if len(parts) == 4:
                # UPDATE r c value
                r, c = int(parts[1]), int(parts[2])
                v = parts[3]
                root = find(idx(r, c))
                value[root] = v
            else:
                # UPDATE value1 value2
                v1, v2 = parts[1], parts[2]
                # 모든 대표를 훑으며 v1→v2 치환
                seen = set()
                for i in range(N):
                    r0 = find(i)
                    if r0 in seen:
                        continue
                    seen.add(r0)
                    if value[r0] == v1:
                        value[r0] = v2

        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:5])
            a, b = idx(r1, c1), idx(r2, c2)
            if find(a) != find(b):
                # (r1,c1) 값 우선 규칙을 지키려면 a를 먼저, b를 나중에 union
                union(a, b)

        elif cmd == "UNMERGE":
            r, c = int(parts[1]), int(parts[2])
            x = idx(r, c)
            root = find(x)
            # 현재 대표 값 보관
            keep_val = value[root]
            # 해당 대표의 모든 멤버를 찾고 초기화
            mems = members_of(root)
            for m in mems:
                parent[m] = m
                value[m] = ""
            # (r,c)에만 값을 복원
            value[x] = keep_val

        elif cmd == "PRINT":
            r, c = int(parts[1]), int(parts[2])
            v = value[find(idx(r, c))]
            answer.append(v if v else "EMPTY")

    return answer