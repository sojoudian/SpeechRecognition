import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hey there!! Say something !!!")
    audio = r.listen(source)
try:
    print(" Maziar Think you said: \n" + r.recognize_google(audio))

except:
    pass