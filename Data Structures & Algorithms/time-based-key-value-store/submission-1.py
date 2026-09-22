class TimeMap:

    def __init__(self):
        self.m = defaultdict(dict)
        self.timestamp_prev = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value
        last_timestamp = self.timestamp_prev[key][-1] if len(self.timestamp_prev[key]) > 0 else -1
        self.timestamp_prev[key].extend([last_timestamp] * (timestamp - len(self.timestamp_prev[key])))
        self.timestamp_prev[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.m:
            if timestamp in self.m[key]:
                return self.m[key][timestamp]
            else:
                size = len(self.timestamp_prev[key])
                right = min(timestamp, size - 1)
                last_timestamp = self.timestamp_prev[key][right] if size > 0 else 0
                if last_timestamp >= 0:
                    return self.m[key][last_timestamp]
                else:
                    return ""
        else:
            return ""
        
