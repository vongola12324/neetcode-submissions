class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import heapq

        heap = []
        for idx in range(len(position)):
            heapq.heappush(heap, (-position[idx], speed[idx]))

        fleets = 0
        max_time = 0
        
        while len(heap) > 0:
            p, s = heapq.heappop(heap)
            t = (target - -p) / s
            if t > max_time:
                fleets += 1
                max_time = t
        return fleets


"""
1->4->7->10
4->6->8->10
"""

"""
0->1->2->3
1->3->5->7
4->6->8->10
7->8->9->10
"""