def solution(users, emoticons):
    n_users = len(users)
    m = len(emoticons)
    rates = [10, 20, 30, 40]

    best_sub = -1
    best_rev = -1

    assign = [0] * m

    def evaluate():
        nonlocal best_sub, best_rev
        sub_cnt = 0
        revenue = 0

        discounted = [int(price * (100 -r) / 100) for price, r in zip(emoticons, assign)]

        for min_rate, threshold in users:
            spend = 0
            for r, price_d in zip(assign, discounted):
                if r >= min_rate:
                    spend += price_d
            if spend >= threshold:
                sub_cnt += 1
            else:
                revenue += spend
        if sub_cnt > best_sub or (sub_cnt == best_sub and revenue > best_rev):
            best_sub, best_rev = sub_cnt, revenue
    
    def dfs(idx):
        if idx == m:
            evaluate()
            return
        for r in rates:
            assign[idx] = r
            dfs(idx+1)
    dfs(0)
    return [ best_sub, best_rev]