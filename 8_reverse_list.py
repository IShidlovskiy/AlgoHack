from typing import Optional


class ListEl:
    def __init__(self, value: int, next: Optional['ListEl'] = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + " -> " + str(self.next)

    value: int
    next: Optional['ListEl']


def reverse_list(data: ListEl) -> ListEl:
    prev = None
    current = data

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


el_4 = ListEl(value=4, next=None)
el_3 = ListEl(value=3, next=el_4)
el_2 = ListEl(value=2, next=el_3)
el_1 = ListEl(value=1, next=el_2)

print(el_1)
reversed_head = reverse_list(el_1)
print(reversed_head)
