# めぐる式二分探索
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
