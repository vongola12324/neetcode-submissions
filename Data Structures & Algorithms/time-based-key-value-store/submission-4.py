from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.m[key]
        idx = bisect_right(arr, timestamp, key=lambda x: x[0]) - 1
        return arr[idx][1] if idx >= 0 else ""
        
