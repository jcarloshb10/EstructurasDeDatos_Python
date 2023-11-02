from adt.stack_queue.queue import Queue
from adt.stack_queue.nodes import PriorityNode


class PriorityQueue(Queue):
    def enqueue(self, new_data: object, priority: int = 1):
        if type(priority) == int and priority >= 1:
            new_node = PriorityNode(new_data, priority)
            if self.is_empty():
                self._front = self.tail = new_node
                return True
            elif type(new_data) == type(self.front()):
                self.__enqueue(new_data, priority)
                return True
        return False

    def __enqueue(self, new_data: object, priority: int):
        current_node = self._front
        cnt = 0
        while current_node:
            if priority < current_node.priority:
                break
            else:
                current_node = current_node.next
                cnt += 1

        new_node = PriorityNode(new_data, priority)
        if cnt == 0:
            new_node.next = self._front
            self._front = new_node
        elif 0 < cnt < len(self):
            current_node = self._front
            for i in range(cnt - 1):
                current_node = current_node.next
            current_node.next, new_node.next = new_node, current_node.next
        elif cnt == len(self):
            self.tail.next = new_node
            self.tail = new_node
