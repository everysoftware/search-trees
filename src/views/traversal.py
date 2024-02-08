from src.controllers.bst import BST


def solve_traversal(_n: int, a: list[list[int]]) -> list[list[int]]:
    tree = BST().from_array(a)
    return [
        tree.dfs(style="inorder"),
        tree.dfs(style="preorder"),
        tree.dfs(style="postorder"),
    ]


def task_traversal():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    for traversal in solve_traversal(n, a):
        print(*traversal)
