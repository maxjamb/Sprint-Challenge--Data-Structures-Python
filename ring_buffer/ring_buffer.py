from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # while there space is available, add to tail, and update current
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
    # if theres no more space
        else:
            # update current value
            self.current.value = item
        # if we're currently at the tail
            if self.current is self.storage.tail:
                # go back to head
                self.current = self.storage.head
            else:
                # else, go to the next
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        var = self.storage.head
        # TODO: Your code here
        while var:
            list_buffer_contents.append(var.value)
            var = var.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
