from src.controllers.bst import BST
from src.controllers.bst.operations import is_bst, is_general_bst


def task_is_bst():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    tree = BST().from_array(a)

    print("CORRECT" if is_bst(tree) else "INCORRECT")


def task_is_general_bst():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    tree = BST().from_array(a)

    print("CORRECT" if is_general_bst(tree) else "INCORRECT")
