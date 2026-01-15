def hasCycle(self, head: Optional[ListNode]) -> bool:
    '''
    Docstring for hasCycle

    :param self: Description
    :param head: Description
    :type head: Optional[ListNode]
    :return: Description
    :rtype: bool

    Floyd's Tortoise and Hare
    # Floyd's cycle finding algorithm or Hare-Tortoise algorithm is a pointer algorithm that uses only two pointers, moving through the sequence at different speeds. This algorithm is used to find a loop in a linked list. It uses two pointers one moving twice as fast as the other one. The faster one is called the fast pointer and the other one is called the slow pointer.While traversing the linked list one of these things will occur-
    # The Fast pointer may reach the end (NULL) which shows that there is no loop in the linked list.
    # The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.

    '''
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

    # Time and space complexity - O(n), O(1)

    # another solution using hashset (non optimal)
    # seen = set()
    # cur = head

    # while cur:
    #     if cur in seen:
    #         return True
    #     seen.add(cur)
    #     cur = cur.next

    # return False

    # Time and space complexity - O(n), O(n)
