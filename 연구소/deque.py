# deque
from collections import deque

# list.append()와 deque.append() 비교
lst = ["a", "b", "c"]
lst.append("d")
lst

deq = deque(["a", "b", "c"])
deq.append("d")
deq

deq.appendleft("e")
deq

deq.pop()

len(deq)

