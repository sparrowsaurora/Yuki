import wikipediaapi, voice_input, speech_output

def get_wikipedia_summary(query):
    user_agent = "Project-Yui/1.0 (https://github.com/Sparrow/Project-Yui; contact-sparrows.au@gmail.com)"
    wiki_wiki = wikipediaapi.Wikipedia(user_agent)  # Correct the user_agent parameter
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary
    else:
        return "No information found on Wikipedia."

def define_query():
    query = voice_input.capture_voice()
    if query:
        summary = get_wikipedia_summary(query)
        speech_output.speak(summary)
        print("Wikipedia Summary: " + summary)


define_query()
