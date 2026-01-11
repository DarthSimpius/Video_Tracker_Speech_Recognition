import speech_recognition as speech
import sys
from difflib import SequenceMatcher
import os

sound = speech.Recognizer()
script_dir = os.path.dirname(os.path.realpath(__file__))

print(0)

with speech.Microphone() as audio:
    print("Adjusting Energy Level")
    sound.adjust_for_ambient_noise(audio)
    sound.pause_threshold = 2

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
#     print("Say Something!")
#     said = sound.listen(audio)

# try:
#     print(sound.recognize_google(said, language = 'en-IN', show_all = True))
# except LookupError:
#     print("Could not understand. Please repeat")
# except speech.UnknownValueError:
#     print("Could not understand. Please repeat")


Video_Name = sys.argv[1] + ".txt"
File_Path = script_dir + "\\Video_Transcriptions\\" + Video_Name
#File_Path = R"Video_Tracker_Speech_Recognition\Video_Transcriptions\01-1- 7L Departure North.txt"
#File_Path = R"C:\Users\taran\Github Project\Video_Tracker_Speech_Recognition\Video_Transcriptions\01-1- 7L Departure North.txt"
with open(File_Path, 'r') as f:
    Dialogue_Lines = f.readlines()
    f.close()
    print(Dialogue_Lines)

Finished_Dialogue = False
Dialogue_Index = 0
while not Finished_Dialogue:
    if (Dialogue_Index != len(Dialogue_Lines)):
        with speech.Microphone() as audio:
            print("Say Something!")
            said = sound.listen(audio)

        try:
            Spoken = sound.recognize_google(said)
            print(Spoken)
            if similar(Spoken,Dialogue_Lines[Dialogue_Index]) > 0.6:
                Dialogue_Index += 1
                print("Check Passed")
            else:
                print("Check not passed")
        except LookupError:
            print("Could not understand. Please repeat")
        except speech.UnknownValueError:
            print("Could not understand. Please repeat")
    else:
        Finished_Dialogue = True

print(1)

