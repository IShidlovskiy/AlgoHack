from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = value
        self.left = left
        self.right = right

    value: int
    left: Optional['Node']
    right: Optional['Node']


def sorted_tree(tree: Node) -> list:
    sorted_list = []
    if tree.left:
        sorted_list.extend(sorted_tree(tree.left))
    if tree.value:
        sorted_list.append(tree.value)
    if tree.right:
        sorted_list.extend(sorted_tree(tree.right))
    return sorted_list


node_3 = Node(value=3)
node_6 = Node(value=6)
node_9 = Node(value=9)
node_11 = Node(value=11)


node_5 = Node(value=5, left=node_3, right=node_6)
node_10 = Node(value=10, left=node_9, right=node_11)
node_8 = Node(value=8, left=node_5, right=node_10)


assert sorted_tree(node_8) == [3, 5, 6, 8, 9, 10, 11]