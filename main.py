import ethereum_sequence as eth
import utils
import pysynth
import pysynth_e as pse
import pysynth_b as psb
import pysynth_s as pss
import pysynth_p as psp
import pysynth_c as psc

def eth_music():
    durations = utils.create_duration_series()
    eth_sequence = eth.generate_eth_sequence()
    note_sequence = utils.hex_to_notes(eth_sequence)

    note_durations = [[note, 4] for note in note_sequence]
    utils.generate_final_music(note_durations, durations)
    print(note_durations)

    pysynth.make_wav(note_durations, fn="ethereum.wav")

    
def generate_wav_from_notes():
    note_list = [['f#', 2],
 ['d', 2],
 ['f#', 16],
 ['a', 8],
 ['d', 2],
 ['e', 4],
 ['b', 4],
 ['g', 2],
 ['b', 8],
 ['f#', 4],
 ['c', 2],
 ['f#', 16],
 ['d', 16],
 ['f#', 8],
 ['e', 16],
 ['g#', 2],
 ['e', 2],
 ['e', 16],
 ['a#', 4],
 ['e', 2],
 ['b', 8],
 ['g#', 4],
 ['c', 4],
 ['c', 4],
 ['d', 2],
 ['d', 4],
 ['d', 16],
 ['g#', 2],
 ['g#', 4],
 ['c#', 16],
 ['e', 2],
 ['c', 16],
 ['c#', 2],
 ['g#', 2],
 ['f', 2],
 ['d#', 2],
 ['f', 2],
 ['d#', 2],
 ['f', 16],
 ['d', 2],
 ['e', 8],
 ['a#', 16],
 ['f#', 2],
 ['e', 2],
 ['a#', 8],
 ['f', 8],
 ['c', 4],
 ['d#', 8],
 ['g#', 2],
 ['d#', 8],
 ['e', 2],
 ['b', 8],
 ['g', 16],
 ['d#', 8],
 ['f', 8],
 ['c', 4],
 ['a', 4]]
    
    pysynth.make_wav(note_list, fn="trends.wav")
    pse.make_wav(note_list, fn="trends-e.wav")
    psb.make_wav(note_list, fn="trends-b.wav")
    pss.make_wav(note_list, fn="trends-s.wav")
    psp.make_wav(note_list, fn="trends-p.wav")
    psc.make_wav(note_list, fn="trends-c.wav")

generate_wav_from_notes()
# eth_music()