# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=self.ll_2_num(l1)
        num2=self.ll_2_num(l2)
        print(num1)
        print(num2)
        return self.num_2_ll(int(num1)+int(num2))

    def ll_2_num(self,l):
        nums=[]
        while l is not None:
            nums.append(str(l.val))
            l=l.next
        nums.reverse()
        # list转数组
        return ''.join(nums)

    def num_2_ll(self,n):
        nums=list(str(n))
        nums.reverse()
        print(nums)
        root=None
        lastnode=root
        for i in range(0,len(nums)):
            if i==0:
                root=ListNode(int(nums[i]))
                lastnode=root
            else:
                temp=ListNode(int(nums[i]))
                lastnode.next=temp
                lastnode=temp

        return root

class Solution2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        root=temp=ListNode(0)
        while l1 or l2 or carry:
            v1=0
            v2=0
            if l1:
                v1=l1.val
                l1=l1.next

            if l2:
                v2=l2.val
                l2=l2.next

            carry,next_val=divmod(carry+v1+v2,10)
            temp.next=ListNode(next_val)
            temp=temp.next

        return root.next





if __name__ == '__main__':

    root1=ListNode(0)
    root1.next=ListNode(2)

    root2=ListNode(0)
    root2.next=ListNode(8)

    so=Solution2()
    result=so.addTwoNumbers(root1,root2)
    nums=[]
    while result is not None:
        nums.append(result.val)
        result=result.next

    nums.reverse()
    print(nums)