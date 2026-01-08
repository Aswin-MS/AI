import speech_recognition as sr
def speech2text():
    st=sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('Speak now!')
            audio=st.listen(source)
        try:
            text=st.recognize_google(audio)
            print(f"You said '{text}'")
            break
        except:
            print("Didn't hear,please repeat" )
speech2text()


