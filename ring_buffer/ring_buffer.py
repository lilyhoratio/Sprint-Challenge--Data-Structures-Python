from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):

        # If storage is not at capacity, add to tail and update current
        if self.current < self.capacity:
            self.current += 1
        # If at capacity, add to tail and remove from head
        else:
            self.storage.remove_from_head()
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        current_element = self.storage.head
        while current_element:
            list_buffer_contents.append(current_element.value)
            current_element = current_element.next

        return list_buffer_contents

# testing_ring_buffer = RingBuffer(3)
# testing_ring_buffer.append(6)
# testing_ring_buffer.append(7)
# testing_ring_buffer.append(10)
# testing_ring_buffer.append(15)
# testing_ring_buffer.append(14)
# testing_ring_buffer.append(24)
# print(testing_ring_buffer.__dict__)
# # print(testing_ring_buffer.storage.head.__dict__)
# print(testing_ring_buffer.get())

# ----------------Stretch Goal-------------------



class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
