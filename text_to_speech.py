def speak(str):
    from win32com.client import Dispatch
    say=Dispatch("SAPI.SpVoice")
    say.Speak(str)


if __name__ == "__main__":
    f=open("for_voice.txt","r")
    content=f.read()
    speak(content)
    f.close()