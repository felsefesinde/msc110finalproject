import ethereum_sequence as eth
import utils
import pysynth

def eth_music():
    eth_sequence = eth.generate_eth_sequence()
    note_sequence = utils.hex_to_notes(eth_sequence)

    note_durations = [(note, 4) for note in note_sequence]
    pysynth.make_wav(note_durations, fn="ethereum.wav")

    #print(eth_sequence)
    #print(note_durations)

