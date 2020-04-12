# 对链表进行排序，快排和归并排序

class LinkNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def list_to_linklist(num_list):
    head = None
    if num_list:
        head = LinkNode(num_list[0])
    
    p = head

    for x in num_list[1:]:
        p.next = LinkNode(x)
        p = p.next
    
    return head

# 归并排序
def merge_sort(head):

    if head is None or head.next is None:
        return head

    quick_p = head
    slow_p = head

    # 快慢指针找到链表中点
    while quick_p.next and quick_p.next.next:
        slow_p = slow_p.next
        quick_p = quick_p.next.next

    quick_p = slow_p.next
    slow_p.next = None    
    
    left = merge_sort(head)
    right = merge_sort(quick_p)


    return merge(left, right)

def merge(left, right):

    if left is None:
        return right
    if right is None:
        return left
    
    p = LinkNode(0)
    r = p

    while left and right:
        if left.val < right.val:
            p.next = left
            left = left.next
        else:
            p.next = right
            right = right.next
        p = p.next
    
    if left:
        p.next = left
    if right:
        p.next = right

    return r.next

# 迭代归并排序
def merge_sort_by_iter(head: LinkNode) -> LinkNode:

    dummyHead = LinkNode(0)
    dummyHead.next = head
    p = head
    len_ = 0
    while p:
        len_ += 1
        p = p.next
    
    step = 1
    while step < len_:
        cur = dummyHead.next
        tail = dummyHead

        while cur:
            left = cur
            # left->@, right->@, cur->@->@... 
            right = cut(left, step)
            cur = cut(right, step)

            tail.next = merge(left, right)
            while tail.next:
                tail = tail.next
            
        step *= 2
    
    return dummyHead.next
            

def cut(head, step):
    
    p = head

    while p and step-1:
        p = p.next
        step -= 1
    
    if p is None:
        return None
    
    nex = p.next
    p.next = None
    return nex
    


if __name__ == "__main__":
    b = list_to_linklist([1,3,5,2,4,6,0])
    # d = merge_sort(b)
    d = merge_sort_by_iter(b)
    while d:
        print(d.val)
        d = d.next
    pass
