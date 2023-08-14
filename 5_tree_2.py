from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = value
        self.left = left
        self.right = right

    value: int
    left: Optional['Node']
    right: Optional['Node']


def visited_tree(tree: Node) -> list:
    visited = []
    tree_queue = [tree]

    while tree_queue:
        current_node = tree_queue.pop(0)
        visited.append(current_node.value)

        if current_node.left:
            tree_queue.append(current_node.left)
        if current_node.right:
            tree_queue.append(current_node.right)
    return visited


node_3 = Node(value=3)
node_6 = Node(value=6)
node_9 = Node(value=9)
node_11 = Node(value=11)


node_5 = Node(value=5, left=node_3, right=node_6)
node_10 = Node(value=10, left=node_9, right=node_11)
node_8 = Node(value=8, left=node_5, right=node_10)

assert visited_tree(node_8) == [8, 5, 10, 3, 6, 9, 11]
