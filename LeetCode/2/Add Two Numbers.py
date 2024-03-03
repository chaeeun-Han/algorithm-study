class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        # l1의 값을 문자열로 구성
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next

        # l2의 값을 문자열로 구성
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        # 문자열을 정수로 변환하여 더하고, 다시 문자열로 변환
        result = str(int(num1) + int(num2))

        # result 문자열을 역수 노드로 만들어 연결 리스트 구성
        dummy = ListNode(0)
        current = dummy
        for digit in result[::-1]:  # 문자열을 역순으로 순회
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
