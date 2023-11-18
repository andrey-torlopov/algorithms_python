from types import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # если один из списков еще имеет элементы
    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next  # возвращаем следующий узел после фиктивного, так как он будет первым в результирующем списке
