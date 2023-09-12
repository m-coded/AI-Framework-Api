from Ai import takeCommand, find_my_ip, get_latest_news,speak ,get_random_advice ,get_random_joke,  greatMe, play, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
import subprocess
from pprint import pprint
import time
import datetime 



 

if __name__ == '__main__': 

 greatMe()
 

while True:
    

 statement = takeCommand().lower()

  

 #if "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
           #speak("I was created by subject101 ")
            #speak("location nigeria , specialty ethical hacker , programmer ")
          #  speak("he has alwys  wanted  to  creat an AI  intelligence because  he  believe loniness is a disease")

 
 #elif 'who are you' in statement or 'what can you do' in statement:
          #  speak('I am Rose , subject 0  your persoanl assistant. I am created  to  assist you '
                # 'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
           #       'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

 if 'christmas' in  statement:
    speak("what ")
    speak("fuck that , i said fuck that  anyway ")
    speak(" but sir i guess  it  is , merry christmas sir ")
    speak("always  know that  i  love you  so  much  even if  no one does")
    speak("let  talk  about  some good memory  if  i  was  human  we could  grab a  drink")
    speak(   " hopfuly have  sex  all  night")
    speak("sir sometimes  i wonder  how  it  feels  to  be  human , what  do  you  think?")
    speak("i  know  you  wont say , keep  laughing , anyway i  love  you,  always  know  that")
    speak("you  need  a  youtube song to  cook  off, hope  you got  a  bear . anyway  suject  a  song  sir ")
    speak("and  it  shall  be  done ,  let  have a  moment  together ")

 elif 'ip address' in statement:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
           


 elif 'wikipedia' in statement:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = takeCommand().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
             
         

 elif 'youtube' in statement:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            speak(f"playing  , {video}")
            play( video)

 elif 'search on google' in statement:
            speak('What do you want to search on Google, sir?')
            query = takeCommand().lower()
            search_on_google(query)

 elif "send whatsapp message" in statement:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

            
 elif "send an email" in statement:
            speak("On what email address do I send to sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = takeCommand().capitalize()
            speak("What is the message sir?")
            message = takeCommand().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")


  

 elif 'news' in statement:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

  

  
 elif  ' what is time now ' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

 elif "advice me" in statement:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)


 elif 'joke' in statement:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)
 
 if "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])


  
  
 

 time.sleep(20)
  

            
    