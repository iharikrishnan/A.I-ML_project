import speech_recognition as sr
from translate import Translator
from gtts import gTTS
import os

#step 1 :  input audio and convert to text format
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1) # clear background noise
    print("waiting for your message...")
    recordedaudio=recognizer.listen(source) #record audio
    print('Done recording..!')
try:
    print('Printing the message..')
    texts=recognizer.recognize_google(recordedaudio,language='en-US') #convert the recordedaudio to text format

    print('Your message:{}'.format(texts))

except Exception as ex:
    print(ex)

#step 2 : Transilate the text to another language

language = input("enter the language:") #input the language to translate
translator= Translator(to_lang=language)
translation = translator.translate(texts) #translate the text to given language
print (translation)

#step 3 : convert the transilated text to audio
transilated_audio = gTTS( text=translation, lang=language)  #converting the transilated text to audio

transilated_audio.save("voice.mp3") #save the audio
os.system("voice.mp3")