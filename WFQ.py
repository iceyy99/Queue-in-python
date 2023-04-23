from queue import Queue
import heapq

# define three queues
queue_p = Queue()
queue_s = Queue()
queue_e = Queue()

# read data from .txt file and append items to the queues
with open("priorityqueue.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("P"):
            queue_p.put(line)
        elif line.startswith("S"):
            queue_s.put(line)
        elif line.startswith("E"):
            queue_e.put(line)

# define the weights for each queue
weights = {"P": 3, "S": 2, "E": 1}

# define a priority queue
pq = []

# push items from each queue to the priority queue according to weight
if not queue_p.empty():
    heapq.heappush(pq, (1/weights["P"], queue_p.get()))
if not queue_s.empty():
    heapq.heappush(pq, (1/weights["S"], queue_s.get()))
if not queue_e.empty():
    heapq.heappush(pq, (1/weights["E"], queue_e.get()))

# dequeue items from the priority queue in prioritized order
while pq:
    item = heapq.heappop(pq)[1]
    print(item)
    if item.startswith("P"):
        if not queue_p.empty():
            heapq.heappush(pq, (1/weights["P"], queue_p.get()))
    elif item.startswith("S"):
        if not queue_s.empty():
            heapq.heappush(pq, (1/weights["S"], queue_s.get()))
    elif item.startswith("E"):
        if not queue_e.empty():
            heapq.heappush(pq, (1/weights["E"], queue_e.get()))
