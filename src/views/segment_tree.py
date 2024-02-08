from src.controllers.avl_segment_tree import AVLSegmentTree


def solve_segment_tree(queries: list) -> list:
    tree = AVLSegmentTree()
    s = 0

    def f(x):
        return (x + s) % 1_000_000_001

    result = []

    for i, args in enumerate(queries):
        option = args[0]
        if option == "?":
            key = f(int(args[1]))
            result.append((i + 1, "Found" if tree.contains(key) else "Not found"))
        elif option == "+":
            key = f(int(args[1]))
            tree.insert(key)
        elif option == "s":
            left, right = f(int(args[1])), f(int(args[2]))
            s = tree.sum_between(left, right)
            result.append((i + 1, s))
        elif option == "-":
            key = f(int(args[1]))
            tree.delete(key)

    return result


def task_segment_tree():
    n = int(input())
    queries = [input().split() for _ in range(n)]

    for _, ans in solve_segment_tree(queries):
        print(ans)
