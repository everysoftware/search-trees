from src.controllers.rope.operations.adaptated import rope_split, rope_merge
from src.models.nodes import RopeNode


def rope_build_helper(s: str, left: int, right: int) -> RopeNode:
    if left < right:
        m = (left + right) // 2
        left_part = rope_build_helper(s, left, m)
        right_part = rope_build_helper(s, m + 1, right)

        return rope_merge(left_part, right_part)
    else:
        return RopeNode(left, s[left])


def rope_build(s: str) -> RopeNode:
    """Построение Rope из строки."""
    return rope_build_helper(s, 0, len(s) - 1)


"""
Перемещение подстроки s[i:j + 1] на позицию k оставшейся строки.

Функция аналогична следующей:

def move_substring(self, i, j, k):
    without_sub = self.s[:i] + self.s[j + 1:]
    before = without_sub[:k]
    sub = self.s[i:j + 1]
    after = without_sub[k:]
    self.s = before + sub + after
    return self.s
        
Но работает за O(log n), где n - размер строки.

"""


def rope_move_substr(node: RopeNode | None, i: int, j: int, k: int) -> RopeNode | None:
    """Перемещение подстроки s[i:j + 1] на позицию k оставшейся строки"""
    if node is None:
        return None

    # Разделяем строку на две части: до i-го символа и начиная с i-го символа
    left, temp = rope_split(node, i)

    # Разделяем temp на две части: до j-го символа включительно и после j-го символа
    # Поскольку temp начинается с i-го символа, то делаем j - i.
    # После этого добавляем 1, чтобы включить j-ый символ в срез.
    sub, right = rope_split(temp, j - i + 1)

    # Объединяем левую и правую части строки без подстроки
    without_sub = rope_merge(left, right)

    # Разделяем without_sub на две части: до k-го символа включительно (k начинается с 1) и после k-го символа
    before, after = rope_split(without_sub, k)

    # Объединяем sub и after
    sub_and_after = rope_merge(sub, after)

    # Объединяем before и new_right
    return rope_merge(before, sub_and_after)


def rope_to_string(root: RopeNode | None) -> str:
    """Получить строку из Rope."""
    st = []
    result = ""
    node = root

    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            result += node.value
            node = node.right

    return result
