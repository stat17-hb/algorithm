#%%
import heapq

heap = []

a = [5,2,9,6,3,2,1,5]
for i in a:
    heapq.heappush(heap, i)
    
lst = []
while len(heap)!=0:
    lst.append(heapq.heappop(heap))
lst
