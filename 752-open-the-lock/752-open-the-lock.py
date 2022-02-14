class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        
        q = deque()
        q.append(["0000", 0]) #lock,number of turns
        visit = set(deadends)  #hash set
        while q:
            lock, number_of_turns = q.popleft()
            if lock == target:
                return number_of_turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, number_of_turns + 1])
        return -1