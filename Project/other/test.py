from signal_processor import EEG

try:
    eeg = EEG()
    while True:
        print(eeg.get_data())
except Exception as e:
    print(e)

