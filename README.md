# Project Yuki

## Hi, I'm [Sparrow](https://sparrowsaurora.github.io/Terminal-Portfolio/)

### **`Programmer // enterpreneur // content creator`**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/https://www.linkedin.com/in/ryan-kelley-8762a8285/)
[![Twitch](https://img.shields.io/badge/Twitch-%239146FF.svg?logo=Twitch&logoColor=white)](https://twitch.tv/https://www.twitch.tv/sparrows_aurora)
[![X](https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white)](https://x.com/https://x.com/RyanKelleyBiz)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/https://www.instagram.com/sparrows_aurora)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://youtube.com/@https://www.youtube.com/@sparrows_aurora)

I'm an indie software developer and content creator with interests in AI, machine learning, front end development and building functional projects. I'm currently studying a cert IV in programming and I'm passionate about building new things and creating innovative projects

Currently I'm building Yuki an AI voice assistant with real-world capabilities to organize tasks and enhance productivity.

I am actively learning advanced C++ and C# to build impactful projects in different ways.

Contact me at: [sparrows.au@gmail.com](mailto:sparrows_aurora)

## About Yuki

Yuki was designed to be a voice-based Ai assistant with dynamic Speech and a human-ish voice.  
modules can be added by the user but it has main functionality as an assistant.  
it was created to manage daily tasks, automate workflows, and assist with coding as well as to keep the user company

## Yuki's display model

Yuki's display model was made to be interactive, inspired by [Vedal987](https://github.com/Vedal987)'s Neuro-sama, however the character is different

## File Paths

    Yuki/
    │
    ├── main.py                       # Main script to initialize the assistant
    │
    ├── display/                      # Main script for the display model
    │   ├── display.md                # Description of the 'display' directory
    │
    │
    ├── input_control/                # Controls inputs
    │   ├── input_control.md          # Description of the 'input_contol' directory
    │   ├── command_normalisation.py  # determination and normalisation of commands
    │   ├── emotional_analysis.py     # determination of emotion and tone
    |   └── speech_to_text.py         # speech to tech via openAI whisper
    │
    │
    ├── voice_output/                 # Controls the voice output
    │   ├── voice_output.md           # Description of the 'voice_output' directory
    │
    │
    ├── modules/                      # Controls Modules
    │   ├── modules.md                # Description of the 'modules' directory
    │   ├── voice_notes_dir/          # directory that holds voice note files
    |   │   └── voice_notes.py        # module for voice notes
    │   ├── voice_input.py            # Module for capturing voice input
    │   ├── speech_output.py          # Module for voice responses
    │   ├── emailer.py                # Module for sending emails
    │   ├── task_automation.py        # Module for task automation
    │   ├── note_taker.py             # Module for taking notes
    │   ├── voice_record.py           # Module for recording voice
    │   ├── wikipedia_search.py       # Module for Wikipedia searches
    │   ├── browser_automation.py     # Module for opening tabs
    │   ├── time_and_date.py          # Module for stating time and date
    │   ├── file_reader.py            # Module for reading files out loud
    │   ├── code_writer.py            # Module for generating code files from voice
    │
    ├── personality/                  # Controls the "personality of Yuki
    │   ├── personality.md            # Description of the 'personality' directory
    │
    ├── README.md                     # Its a read me file, what do you expect?
    └── requirements.txt              # Dependencies

## Flowchart

                                        Input
                                          |
                                     Clean Input
                                          │
                                YES---If Command?----NO
                                 |                   |
                             Normalize          Emote Analysis
                                 |                   |
                              Modules           Personality
                                 |                   |
                          Find Module Data   Check For Relevant
                                 |             data in Memory
                -----------------|                   |
                |                └── Gen Response ----
    Complete module if not info            |
                                Retrieve Emotional Ref Data
                                           |
                                Give Data To Model Controller
                                           | 
                                (TTS) + action control for model
                            
## MVP Features

- Conversational AI
- Voice Input + Output
- Full Wake

### Inspired by [Vedal987](https://github.com/Vedal987)'s [Neuro-sama](https://www.youtube.com/@Neurosama)

---

**([^ Back To Top ^](#project-yuki))**
