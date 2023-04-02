import pyttsx3
import PySimpleGUI as sg

engine = pyttsx3.init()

layout = [
    [sg.Text("Enter the text to speak:")],
    [sg.InputText(key="text")],
    [sg.Text("Select a voice:")],
    [sg.Radio("Male", "voice", default=True, key="male"),
     sg.Radio("Female", "voice", key="female")],
    [sg.Button("Speak"), sg.Button("Quit")]
]
window = sg.Window("Text-to-Speech App", layout)
while True:
    event, values = window.read()
    if event == "Quit" or event == sg.WIN_CLOSED:
        break
    elif event == "Speak":
        
        if values["male"]:
            voices = engine.getProperty("voices")
            engine.setProperty("voice", voices[0].id)
        elif values["female"]:
            voices = engine.getProperty("voices")
            engine.setProperty("voice", voices[1].id)
            
        engine.say(values["text"])
        engine.runAndWait()


window.close()
