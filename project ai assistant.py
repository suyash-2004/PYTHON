import speech_recognition as sr
import os
import wikipedia
import pyttsx3
import random
from datetime import datetime
import time
import smtplib
import webbrowser as wb
import pywhatkit as pykt


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[4 ].id)
rate = engine.getProperty("rate")
engine.setProperty("rate", 140)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    time = int(datetime.now().hour)
    if time >=0 and time <=12 :
        speak("hey! Good Morning! how may i help you")
    elif time >12 and time<=18:
        speak("hey! Good Afternoon!,how may i help you")
    elif time >18 and time <24:
        speak("Good Evening Sir!,how may i help you")

def command_inpt():
    rec = sr.Recognizer()
    
    def input2():
        with sr.Microphone() as source :
            print("listening.....")
            rec.pause_threshold = 1
            audio = rec.listen(source)
        try :
            print("recognising.....")
            global query
            query = rec.recognize_google(audio,language="en-IN")
            print("user said :-",query)
            
            return query
        except Exception:
            speak("say that again please!")
            return input2()
    return input2()

def gettym():
    curtym = datetime.now()
    tym_now = curtym.strftime("%H:%M")
    
    ln = len(tym_now)
    tym = ""
    for i in range(ln):
        if i != 2:
            tym = tym + tym_now[i]
    global h
    h = tym[0:2]
    global m
    m = tym[2:4]
    
def tym_to_wrds(h,m):
    tymdict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine"}

    
    if h > 12:
        h = h - 12
    if m == 0:
        print("It's "+tymdict[h]+" o'clock")
        speak("It's "+tymdict[h]+" o'clock")
        
    elif m == 30:
        print("It's half past "+tymdict[h])
        speak("It's half past "+tymdict[h])
    elif m == 1:
        print("It's one minutes past "+tymdict[h])
        speak("It's one minutes past "+tymdict[h])
    elif m >1and m < 30:
        print("It's "+tymdict[m]+" minutes past "+tymdict[h])
        speak("It's "+tymdict[m]+" minutes past "+tymdict[h])
    else:
        h += 1
        m = 60 -m
        print("It's "+tymdict[m]+" minutes to "+tymdict[h])
        speak("It's "+tymdict[m]+" minutes to "+tymdict[h])

def timer(duratn):
    if "hours" in query or "hour" in query:
        tym_sec = duratn*60
        for i in range(tym_sec):
            time.sleep(1)
            if i == tym_sec//2:
                print("Time Left : "+str(tym_sec/60))
                speak("Time Left : "+str(tym_sec/60))
            elif i == 0:
                print("Time Up!")
                speak("Time Up!")
            else:
                continue
    elif "seconds" in query:        
        for i in range(duratn,0,-1):
            time.sleep(1)
            print(i)
            if i == duratn // 2: 
                print("Time Left : " + str(i) + " Seconds")
                speak("Time Left : " + str(i) + "seconds")
            elif i == 0:
                print("Time Up!")
                speak("Time Up!")
            else:
                continue
            
            
    
wish()
query = str(command_inpt()).lower()
while True:
      if "hi" in query or "hello" in query:
            hi_output = ["Hi!","Hey There!","Hello","Hi there! How are you?"]
            choice = random.choices(hi_output)
            speak(choice)
            break
            if choice == "Hi there! How are you?":
                answr = command_inpt()    
                positive_reply = ["i am good","i am fine","i am great","good","fine","great"]
                if answr in positive_reply:
                    print("good to hear that")
                    speak("good to hear that")
                else :
                    print("Sorry To Hear That!")
                    speak("Sorry To Hear That!")
      elif 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 3,auto_suggest = True)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            break
     
      elif "youtube" in query:
          print("Searching Youtube!")   
          speak("searching youtube")
          subjectlst = query.split(" ") 
          print(subjectlst)
          subject = ""
          for i in subjectlst:
              if i == "search" :
                  continue
              elif i == "youtube":
                  continue
              elif i == "for":
                  continue
              else:
                  subject += str(i)
                  subject += " "
          
          link = "https://www.youtube.com/results?search_query="+subject
          wb.open(link,new = 2,autoraise = True)
          break
      elif "timer" in query:
          subjectlst = query.split(" ") 
          subjectstr = str(subjectlst)
          digit = ""
          
          for i in subjectstr:
              if i.isdigit():
                  digit += i
              else:
                  continue
          digit = int(digit)
          if "seconds" in query:
              print("Setting Timer For " + str(digit) +" seconds")
              speak("Setting Timer For " + str(digit) +" seconds")
          elif "hour" in query or "hours" in query:
              if digit == 1:
                  print("Setting Timer For " + str(digit) +" hour")
                  speak("Setting Timer For " + str(digit) +" hour")
              else:
                  print("Setting Timer For " + str(digit) +" hours")
                  speak("Setting Timer For " + str(digit) +" hours")
          timer(digit)
          break
          
      elif "time" in query:
          gettym()
          tym_to_wrds(int(h),int(m))
          break
      
      elif "class" in query:
          if "english" in query:
              if "zoom" in query:
                  lnk = "https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09" # replace link with the actual english class zoom link
                  wb.open(lnk,new = 2)
                  break
              elif "google meet" in query or "meet" in query:
                  lnk = "https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179" # replace link with the actual english class meet link
                  wb.open(lnk,new = 2)
                  break
          elif "maths" in query:
              if "zoom" in query:
                  lnk = "https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09" # replace link with the actual maths class zoom link
                  wb.open(lnk,new = 2)
                  break
              elif "google meet" in query or "meet" in query:
                  lnk = "https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179" # replace link with the actual maths class meet link
                  wb.open(lnk,new = 2)
                  break   
          elif "chemistry" in query:
              if "zoom" in query:
                  lnk = "https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09" # replace link with the actual chemistry class zoom link
                  wb.open(lnk,new = 2)
                  break
              elif "google meet" in query or "meet" in query:
                  lnk = "https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179" # replace link with the actual chemistry class meet link
                  wb.open(lnk,new = 2)
                  break
          elif "physics" in query:
              if "zoom" in query:
                  lnk = "https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09" # replace link with the actual physics class zoom link
                  wb.open(lnk,new = 2)
                  break
              elif "google meet" in query or "meet" in query:
                  lnk = "https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179" # replace link with the actual physics class meet link
                  wb.open(lnk,new = 2)
                  break 
          elif "cs" in query or "computer science" in query:
              if "zoom" in query:
                  lnk = "https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09" # replace link with the actual computer science class zoom link
                  wb.open(lnk,new = 2)
                  break
              elif "google meet" in query or "meet" in query:
                  lnk = "https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179" # replace link with the actual computer science class meet link
                  wb.open(lnk,new = 2)
                  break
      
      elif  "what" in query or "how" in query or "tell me about" in query:
          if "tell me about" in query:
              subjectlst = query.split(" ") 
              print(subjectlst)
              subject = ""
              for i in subjectlst:
                  if i == "tell" :
                      continue
                  elif i == "me":
                      continue
                  elif i == "about":
                      continue
                  else:
                      subject += str(i)
                      subject += " "
              speak("searching for " + subject + " ......")
              time.sleep(1)
              pykt.search(subject)
              break
          else:
              speak("searching for " + query + " ......")
              time.sleep(1)
              pykt.search(query)
              print("hello")
              break
         
      elif "bye" in query or "exit" in query or "quit" in query:
          print("Bye!, Have A Good Day")
          speak("Bye!, Have A Good Day")
          break
      elif "play music" in query or "play songs" in query:
          path=r"C:\Users\suyas\Desktop\songsforproject"
          songlst=os.listdir(path)
          song=random.choice(songlst)
          speak("playing " + song)
          print("playing " + song)
          os.startfile("C:\\Users\\suyas\\Desktop\\songsforproject\\" + song)
          break
          
      else:
          pykt.search(query)
          break