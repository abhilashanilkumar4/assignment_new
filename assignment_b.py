class A:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_alternate(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    p1 = head1
    p2 = head2
    prev = None
    C = None

    while p1 is not None and p2 is not None:
        C = p2.next
        p2.next = p1.next
        p1.next = p2
        prev = p2
        p1 = p2.next
        if p1 is None:
            break
        p2 = C

    if p1 is None:
        prev.next = p2

    return head1

list1 = A(1)
list1.next = A(3)
list1.next.next = A(5)
list1.next.next.next = A(7)
list1.next.next.next.next = A(9)

list2 = A(2)
list2.next = A(4)
list2.next.next = A(6)
list2.next.next.next = A(8)

merged = merge_alternate(list1, list2)

while merged is not None:
    print(merged.data, end=" -> ")
    merged = merged.next
print("None")
