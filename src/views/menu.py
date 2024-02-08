import art

from src.views.is_bst import task_is_bst, task_is_general_bst
from src.views.rope import task_rope
from src.views.segment_tree import task_segment_tree
from src.views.traversal import task_traversal

tasks = [
    ("Traversal", task_traversal),
    ("BST property check", task_is_bst),
    ("General BST property check", task_is_general_bst),
    ("Segment tree", task_segment_tree),
    ("Rope", task_rope),
]


def menu():
    print(art.text2art("Search Trees"))
    print("Select task:")

    for i, option in enumerate(tasks):
        print(f"#{i + 1}. {option[0]}")

    option_number = int(input())

    if 1 <= option_number <= len(tasks):
        tasks[option_number - 1][1]()
    else:
        print("Unknown option")
