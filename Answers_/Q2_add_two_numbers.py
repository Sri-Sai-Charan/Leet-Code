


class Node:
	def __init__(self, data=0,next=None):
		self.data = data # Assign data
		self.next = next # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = None


    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

    def lengthOfList(self):
        len = 0
        temp = self.head
        while (temp):
            len+1
            temp = temp.next
        return len
     


def addTwoNumbers(l1,l2):
    len_1 = l1.lengthOfList()
    len_2 = l2.lengthOfList()
    result = []
    current_node_1 = l1.head
    current_node_2 = l2.head
    carry = 0
    while current_node_1 and current_node_2:
            sum = current_node_1.data + current_node_2.data
            if sum < 10:
                result.append(sum+carry)
                carry=0
            else:
                sum -=10
                result.append(sum+carry)
                carry = 1
            current_node_1 = current_node_1.next
            current_node_2 = current_node_2.next
    return result

def main():
    l1 = LinkedList()
    l1.head = Node(2)
    l12 = Node(4)
    l13 = Node(3)
    l1.head.next = l12
    l12.next = l13

    l2 = LinkedList()
    l2.head = Node(5)
    l22 = Node(6)
    l23 = Node(4)
    l2.head.next = l22
    l22.next = l23
    result = addTwoNumbers(l1,l2)
    print (result)
if __name__ == '__main__':
    main()