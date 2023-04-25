class A:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete(head):
    if head is None:
        return None

    AB = A(0)
    AB.next = head

    curr = head
    running_sum = 0
    d = {0: AB}

    while curr:
        running_sum += curr.data

        if running_sum in d:
            prev = d[running_sum]
            to_delete = prev.next
            sum = running_sum

            while to_delete != curr:
                sum += to_delete.data
                del d[sum]
                to_delete = to_delete.next

            prev.next = curr.next
        else:
            d[running_sum] = curr

        curr = curr.next

    return AB.next

n1 = A(1)
n2 = A(2)
n3 = A(-7)
n4 = A(5)
n5 = A(-6)
n6 = A(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6


new_head = delete(n1)

curr = new_head
while curr:
    print(curr.data, end=" ")
    curr = curr.next

