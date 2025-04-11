import pyttsx3 # <- Strictly for Development

class Voice:

    @staticmethod
    def speak(text):
        engine = pyttsx3.init()

        engine.setProperty('voice', engine.getProperty('voices')[1].id) # Set voice to female
        engine.setProperty('rate', 250) # Set rate for Speech
        
        engine.say(text) #Speak
        engine.runAndWait() # Wait but keep active