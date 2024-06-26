from typing import TypeVar          # For use in type hinting

# Type Declarations
T = TypeVar('T')        # generic type
SLL = TypeVar('SLL')    # forward declared
Node = TypeVar('Node')  # forward declare `Node` type


class SLLNode:
    """
    Node implementation
    Do not modify.
    """

    __slots__ = ['val', 'next']

    def __init__(self, value: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param value: value held by node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.val = value
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method to casts nodes to strings
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: bool
        """
        return self is other if other is not None else False


class SinglyLinkedList:
    """
    Implementation of an SLL
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        :return: None
        DO NOT MODIFY THIS FUNCTION
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        DO NOT MODIFY THIS FUNCTION
        """
        return self.to_string()

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        DO NOT MODIFY THIS FUNCTION
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

# ============ Modify below ============ #
    def push(self, value: T) -> None:
        """
        Pushes an SLLNode to the end of the list
        :param value: value to push to the list
        :return: None
        """
        new_node = SLLNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        pass

    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of the linked list
        """
        answer = ""
        current = self.head
        if current is None:
            return "None"

        while current is not None:
            # cur = str(current.val)
            answer += '{}'.format(current.val)
            if current.next is not None:
                answer += ' --> '
            current = current.next
        return answer

        pass

    def length(self) -> int:
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

        pass

    def sum_list(self) -> T:
        """
        Sums the values in the list
        :return: sum of values in list
        """
        current = self.head

        if current is None:
            return None
        sum = current.val
        while current.next is not None:
            current = current.next
            sum += current.val
        return sum

        pass

    def remove(self, value: T) -> bool:
        """
        Removes the first node containing `value` from the SLL
        :param value: value to remove
        :return: True if a node was removed, False otherwise
        """
        current = self.head



        if current is None:
            return False
        if current.val == value:
            if current == self.tail:
                self.tail = None
            self.head = current.next
            return True

        while current.next is not None and current.next.val != value:
            current = current.next
        if current.next is None:
            return False
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next
        return True

    pass

    def remove_all(self, value: T) -> bool:
        """
        Removes all instances of a node containing `value` from the SLL
        :param value: value to remove
        :return: True if a node was removed, False otherwise
        """
        current = self.head
        previous = None


        removed = False
        if current is None:
            return False
        while current is not None:
            if current.val is value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                removed = True
                if current is self.tail:
                    self.tail = previous

            else:
                previous = current
            current = current.next

        if self.head is None:
            self.tail = None

        return removed

        pass

    def search(self, value: T) -> bool:
        """
        Searches the SLL for a node containing `value`
        :param value: value to search for
        :return: `True` if found, else `False`
        """
        current = self.head
        if current is None:
            return False

        while current is not None:
            if current.val == value:
                return True
            current = current.next
        return False
        pass

    def count(self, value: T) -> int:
        """
        Returns the number of occurrences of `value` in this list
        :param value: value to count
        :return: number of time the value occurred
        """

        count = 0

        current = self.head
        while current is not None:
            if current.val is value:
                count+=1
            current = current.next
        return count


def show_encrypted(data: SLL) -> None:
    """
    Reverses the SLL
    :param data: an SLL
    :return: None
    """
    current = data.head
    prev = None
    data.tail = data.head


    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    data.head = prev

    pass
