SWARAS_OFFSET_MAP = {
    "s":0, "R1":1, "R2":2, "R3":3, "G1":2, "G2":3, "G3":4, "M1":5, "M2":6, 
    "P":7, "D1":8, "D2":9, "D3":10, "N1":9, "N2":10, "N3": 11, "S": 12,
}

class raga(object):
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes
        self.sequence = [SWARAS_OFFSET_MAP[elem] for elem in self.notes]
        self.sequence_diff = [self.sequence[i + 1] - self.sequence[i] for i in range(len(self.sequence)-1)] 

    def __repr__(self):
        return self.name

    def check_gb(self, raga_other):
        u, v = self.sequence_diff, raga_other.sequence_diff
        n, i, j = len(u), 0, 0
        if n != len(v):
            return False
        while i < n and j < n:
            k = 1
            while k <= n and u[(i + k) % n] == v[(j + k) % n]:
                k += 1
            if k > n:
                return True
            if u[(i + k) % n] > v[(j + k) % n]:
                i += k
            else:
                j += k
        return False