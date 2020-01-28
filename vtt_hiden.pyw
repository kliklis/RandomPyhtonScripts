import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import datetime
import sounddevice as sd
import soundfile as sf
import random
import bs4
import requests
import re

def record(duration):
    sr = 44100
    myrecording = sd.rec(int(duration * sr), samplerate=sr, channels=2)
    sd.wait()  
    #sd.play(myrecording, sr)

    now_date, now_time = str(datetime.datetime.now()).split(' ')
    now_date = str(now_date).strip()
    now_time = now_time[:now_time.find('.')-3]
    now_time = str(now_time.replace(':','-')).strip()
    print(now_time)

    sf.write("rec_"+now_date+"_"+now_time+".wav", myrecording, sr)


def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!\n")
        #r.adjust_for_ambient_noise(source)
        #audio = r.listen(source,2)

        try:
            audio = r.listen(source,30)
        except sr.WaitTimeoutError:
            audio = None
            
    recognized_audio = None

    if(audio!=None):
        # recognize speech using Sphinx
        try:
            recognized_audio = r.recognize_google(audio)
            print("Sphinx thinks you said \n" + recognized_audio)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
            #say("I can't understand you.")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        return recognized_audio

def say(text):
    #en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    #engine.setProperty('voice', en_voice_id)
    
    engine.setProperty('volume', 0.9)
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()

NAME = None


engine = pyttsx3.init()
say("Hi boss! What can I do for you?")

while(True):
    recognized_audio = listen()
    if(recognized_audio != None):
        if( "play" in recognized_audio and "music" in recognized_audio):
            webbrowser.open('https://www.youtube.com/watch?v=GDZtGY7EgyQ')
        elif("what" in recognized_audio and "your" in recognized_audio and "name" in recognized_audio):
            if(NAME == None):
                say("I don't have a name")
                say("What do you want to be my name?")
                new_name = listen()
                say("I thing I like "+new_name)
                NAME = new_name
            else:
                say("My name is "+NAME)
            
            
        elif("what" in recognized_audio or "what's" in recognized_audio and "is" in recognized_audio):
            search_key = recognized_audio.replace("what is",'').strip().replace(" ","_")
            print(search_key)
            #webbrowser.open('https://en.wikipedia.org/wiki/'+search_key)
            
            response = requests.get("https://en.wikipedia.org/wiki/"+search_key)
            if response is not None:
                html = bs4.BeautifulSoup(response.text, 'html.parser')
                title = html.select("#firstHeading")[0].text
                paragraphs = html.select("p")
                # just grab the text up to contents as stated in question
                intro_text = '\n'.join([ para.text for para in paragraphs[0:5]])
                intro_text = re.sub("\[\d*\]", "",intro_text)
                final_text = re.sub("\(.*\)", "",intro_text).strip()
                


                if(final_text == search_key[0].upper()+search_key[1:]+" may refer to:"):
                    urls = []
                    new_url = ''
                    for url in html.findAll('a'):
                        urls.append(url.get('href'))
                        #print(url)
                        
                        if("https://en.wikipedia.org/wiki/" in str(url.get('href'))):
                            new_url = url.get('href')
                            break
                    #print("-->  "+new_url)
                    response = requests.get("https://en.wikipedia.org"+urls[17])
                    print("https://en.wikipedia.org"+urls[17])
                    if response is not None:
                        html = bs4.BeautifulSoup(response.text, 'html.parser')
                        title = html.select("#firstHeading")[0].text
                        paragraphs = html.select("p")
                        # just grab the text up to contents as stated in question
                        intro_text = '\n'.join([ para.text for para in paragraphs[0:5]])
                        intro_text = re.sub("\[\d*\]", "",intro_text)
                        final_text = re.sub("\(.*\)", "",intro_text).strip()

                print(final_text)
                say(final_text.split("\n\n")[0])

                                    

            
            
        elif("take" in recognized_audio and ("notes" in recognized_audio or "notes" in recognized_audio)):
            now = str(datetime.datetime.now().hour)
            #"+str(now)+"
            file = open("notes_.txt","w+")
            
            say("What do you want me to note?")
            recognized_audio = listen()
            if(recognized_audio != None):
                file.write(recognized_audio)

            while(True):
                say("Do you want me to continue?")
                recognized_audio = listen()
                if(recognized_audio != None):
                    if("yes" in recognized_audio or "continue" in recognized_audio):
                        recognized_audio = listen()
                        if(recognized_audio != None):
                            file.write(recognized_audio)
                    else:
                        break
            file.close()
        elif(recognized_audio.split()[0] == "say"):
            say(' '.join(recognized_audio.split()[1:]))
        elif("record" in recognized_audio):
            say("Ok! I will record for 10 seconds.")
            record(10)
            
        elif("exit" in recognized_audio or "stop" in recognized_audio or "nothing" in recognized_audio):
            say("Ok boss, see you later!")
            break
        else:
            r = random.randrange(10)
            if(r<5):
                say("Sorry, I don't know what"+recognized_audio+" means.")
            elif(r>=5):
                say("I have no idea what "+recognized_audio+" means.")

        #if(recognized_audio != ):
        r = random.randrange(10)
        if(r<5):
            say("What else can I do for you?")
        elif(r>=5):
            say("What can I do to help you?")

    
            
'''
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Microsoft Azure Speech
AZURE_SPEECH_KEY = "INSERT AZURE SPEECH API KEY HERE"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY))
except sr.UnknownValueError:
    print("Microsoft Azure Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Azure Speech service; {0}".format(e))

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))
'''
