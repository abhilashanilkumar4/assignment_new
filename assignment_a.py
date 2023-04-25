class AB:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_in_groups(head, k):
    if head is None or k == 1:
        return head

    ABC = AB(0)
    ABC.next = head
    prev = ABC

    while prev.next:
        curr = prev.next
        tail = curr
        count = 1

        while count < k and tail.next:
            tail = tail.next
            count += 1

        if count < k:
            break

        next = tail.next
        prev.next = tail
        while curr != next:
            t = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = t

        prev = tail

    return ABC.next

n1 = AB(1)
n2 = AB(2)
n3 = AB(3)
n4 = AB(4)
n5 = AB(5)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

new_head = reverse_in_groups(n1, 3)
curr = new_head
while curr:
    print(curr.data, end=" ")
    curr = curr.next