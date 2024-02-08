from src.controllers.rope import Rope


def solve_rope(s: str, queries: list[list[int]]) -> str:
    r = Rope(s)
    for i, j, k in queries:
        r.move_substr(i, j, k)
    return r.to_string()


def task_rope():
    s = input()
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    print(solve_rope(s, queries))
