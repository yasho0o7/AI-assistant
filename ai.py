import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb
import os
import requests
import json

engine = pyttsx3.init()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def time():
	Time = datetime.datetime.now().strftime("%I:%M:%S")
	speak("Right now it's")
	speak(Time)

def date():
	day = int(datetime.datetime.now().day)
	month = int(datetime.datetime.now().month)
	year = int(datetime.datetime.now().year)
	speak("Today's date is")
	speak(day)
	speak(month)
	speak(year)

def greets():
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour < 12:
		speak("Good Morning Neo!")
	elif hour >= 12 and hour < 17:
		speak("Good Afternoon Neo!")
	else:
		speak("Good Evening Neo!")	
	speak("You have one unread message.")
	speak("It's from Trinity.") 	
	speak("She says follow the white rabbit.")
	speak("The message expired. Erasing the cache memory now. So tell me Neo, what can I help you with?")	

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing...")	
		query = r.recognize_google(audio, language = 'en-in')
		print(query)
	except Exception as e:
		print(e)	
		speak("Can you repeat that?")
		return "None"
	return query	

def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.startttls()
	server.login('abc@mail.com','qwerty')
	server.sendmail('abc@mail.com',to,content)
	server.close()

if __name__ == '__main__':
	greets()

	while True:

		query = takeCommand().lower()
		if 'time' in query:
			time()

		elif 'date' in query:
			date()

		elif 'wikipedia' in query:
			speak("Searching it for you Neo")
			query = query.replace("wikipedia","")
			result = wikipedia.summary(query, sentences = 3)
			speak(result)

		elif 'send email' in query:
			try:
				speak("What should the content of email be Neo?")
				content = takeCommand()
				to = takeCommand()
				sendEmail(to,content)
				speak("Email has been sent Neo")
			except Exception as e:
				speak("Sorry Neo! Something went wrong. Let's try again")

		elif 'search' in query:
			speak("What should I search Neo?")
			chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
			search = takeCommand().lower()
			wb.get(chromepath).open_new_tab(search+'.com')

		elif 'play songs' in query:
			song_dir =  'D:/Music'
			songs = os.listdir(song_dir)
			os.startfile(os.path.join(song_dir,songs[0]))

		elif 'open notes' in query:
			fn = open('data.txt','r')

		elif 'go offline' in query:
			speak("Going offline Neo. Remember, they are watching you.")
			quit()	