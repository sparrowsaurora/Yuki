import datetime
import pytz
import voice_input, speech_output

def print_wa_time():
    tz = pytz.timezone('Australia/Perth')
    now = datetime.datetime.now(tz)
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    hours = now.strftime("%H")
    minutes = now.strftime("%M")
    sec = now.strftime("%S")
    if int(hours) > 12:
        hours = int(hours) - 12
        time = str(hours) + ":" + str(minutes) + "pm"

    else:
        time = str(hours) + ":" + str(minutes) +  "am"
    speech_output.speak("The current time is " + time)
print_wa_time()

def seconds():
    tz = pytz.timezone('Australia/Perth')
    now = datetime.datetime.now(tz)
    print(now.strftime('%Y-%m-%d %H:%M:%S'))

def stopwatch():
    tz = pytz.timezone('Australia/Perth')
    now = datetime.datetime.now(tz)
    print(now.strftime('%Y-%m-%d %H:%M:%S'))