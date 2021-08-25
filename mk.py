import sys
import random

from raga import Raga
from utils import *


raga_names = open("raga_names.txt", "r").read().splitlines()

raga_notes = []
for m in ["M1", "M2"]:
    for (r,g) in [("R1", "G1"), ("R1", "G2"), ("R1", "G3"), ("R2", "G2"), ("R2", "G3"), ("R3", "G3")]:
        for (d,n) in [("D1","N1"), ("D1", "N2"), ("D1", "N3"), ("D2", "N2"), ("D2", "N3"), ("D3", "N3")]:
            raga_notes.append(["s", r, g, m, "P", d, n, "S"])

raga_list = []

for name, notes in zip(raga_names, raga_notes):
    raga_list.append(Raga(name, notes))

random.shuffle(raga_list)
i = -1

base_note = sys.argv[1]
duration = float(sys.argv[2])

for i, raga in enumerate(raga_list):
    print(i+1)
    play_scale(raga, base_note=base_note, duration=duration)
    key_in = None

    while(not key_in == "n"):
        key_in = input("Press n to play new raga, r to replay current raga, and c for correct answer")
        if key_in == "c":
            print(raga.name)
        elif key_in== "r":
            play_scale(raga, base_note=base_note, duration=duration)
