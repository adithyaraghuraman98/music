NOTE_OFFSET_DICT = {
    "C": -9, 
    "C#": -8,
    "D": -7,
    "D#": -6,
    "E": -5,
    "F": -4,
    "F#": -3,
    "G": -2,
    "G#": -1,
    "A": 0,
    "A#": 1,
    "B": 2
}

import numpy as np
import simpleaudio as sa

def sound(x,z):
    frequency = x # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = z

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, int(seconds * fs), False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()

def get_gb(raga_list):
    done = []
    out_map = {}
    for i in range(len(raga_list)-1):
        if(raga_list[i] in done):
            continue
        done.append(raga_list[i])
        out_map[raga_list[i]] = []
        for j in range(i+1, len(raga_list)):
            raga_1 = raga_list[i]
            raga_2 = raga_list[j]

            if(raga_1.check_gb(raga_2)):
                out_map[raga_1].append(raga_2)
                done.append(raga_2)
    return out_map



def play_scale(raga, base_note="C", duration=2):
    pitch_sequence = raga.sequence
    base_offset = NOTE_OFFSET_DICT[base_note]
    pitch_sequence = [elem + base_offset for elem in pitch_sequence]
    pitch_sequence = pitch_sequence + pitch_sequence[::-1]
    
    for pitch in pitch_sequence:
        freq = (2**(pitch/12))*440
        sound(freq, duration)
