import ethereum_sequence as eth
import utils
import pysynth

def eth_music():
    durations = utils.create_duration_series()
    eth_sequence = eth.generate_eth_sequence()
    note_sequence = utils.hex_to_notes(eth_sequence)

    note_durations = [[note, 4] for note in note_sequence]
    utils.generate_final_music(note_durations, durations)
    print(note_durations)

    pysynth.make_wav(note_durations, fn="ethereum.wav")

    

eth_music()