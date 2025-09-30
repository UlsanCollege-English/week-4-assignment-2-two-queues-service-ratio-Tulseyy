from collections import deque

class Gate:
    def __init__(self):
        self._pattern = ["fastpass", "regular", "regular", "regular"]
        self._idx = 0
        self._fast = deque()
        self._reg = deque()

    def arrive(self, line, person_id):
        if line == "fastpass":
            self._fast.append(person_id)
        elif line == "regular":
            self._reg.append(person_id)
        else:
            raise ValueError("Line must be 'fastpass' or 'regular'")

    def serve(self):
        if not self._fast and not self._reg:
            raise IndexError("No people to serve")

        attempts = 0
        while attempts < len(self._pattern):
            line_type = self._pattern[self._idx]

            if line_type == "fastpass" and self._fast:
                person = self._fast.popleft()
                self._idx = (self._idx + 1) % len(self._pattern)
                return person
            elif line_type == "regular" and self._reg:
                person = self._reg.popleft()
                self._idx = (self._idx + 1) % len(self._pattern)
                return person

            self._idx = (self._idx + 1) % len(self._pattern)
            attempts += 1

        raise IndexError("No people to serve")

    def peek_next_line(self):
        attempts = 0
        idx = self._idx
        while attempts < len(self._pattern):
            line_type = self._pattern[idx]
            if line_type == "fastpass" and self._fast:
                return "fastpass"
            if line_type == "regular" and self._reg:
                return "regular"
            idx = (idx + 1) % len(self._pattern)
            attempts += 1
        return None
