import json
from typing import List
from llm import History, llm_chat


# Function to read JSON file
def json_read_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


# Function to generate a transcript based on a list of transcripts and a new topic
def generate_transcript(transcripts: List, topic: str):
    history = History()
    history.system("You are a transcript analyzer, to come up with future transcripts that follow a similar pattern:")
    history.system("""Foreword: First of all the band I'm working for as a social media strategist and content will deal with selling green light energy (service not active yet). as of now the page deals with telling through reels with fresh and young tov, all those possible problems, life in general that we all have to face alone/ with family/ as a couple or with roommates. in the reels we explain how to save money, how to make greener and eco decisions and how to solve messes that you don't know how to do e.g. how do I wash clothes? What do I put in the dishwasher? What are the symbols I find on clothes to wash them?""")
    history.system("""Objectives: To create a community of people who are not only on the ig page to learn but also to have their say, give input on how they make a living and manage household chores. Our reels want to not only explain but also for them to be a source of debate among users and inspiration to each other.

The rewards we will use both in stories and for reels/posts etc. 
They are: self (content that provides useful information that can enrich users' personal experience. ), relatability(content that makes us think “omg he's talking about me.”) and social (content that creates appreciation for users by users themselves). 
""")

    for transcript in transcripts:
        history.system("Transcript: " + transcript)
    history.system("What type of tone and personality is represented in the transcripts?")
    answer = llm_chat(history)
    history.assistant(answer)

    history.system("Generate a new transcript in line with the tone and personality previously described for topic: " + topic)
    answer = llm_chat(history)
    history.assistant(answer)

    return answer


# Function to generate a transcript based on a list of transcripts and a new topic
def generate_topic(transcripts: List):
    history = History()
    history.system("You are a transcript analyzer, to come up with future transcripts that follow a similar pattern:")
    history.system("""Foreword: First of all the band I'm working for as a social media strategist and content will deal with selling green light energy (service not active yet). as of now the page deals with telling through reels with fresh and young tov, all those possible problems, life in general that we all have to face alone/ with family/ as a couple or with roommates. in the reels we explain how to save money, how to make greener and eco decisions and how to solve messes that you don't know how to do e.g. how do I wash clothes? What do I put in the dishwasher? What are the symbols I find on clothes to wash them?""")
    history.system("""Objectives: To create a community of people who are not only on the ig page to learn but also to have their say, give input on how they make a living and manage household chores. Our reels want to not only explain but also for them to be a source of debate among users and inspiration to each other.

The rewards we will use both in stories and for reels/posts etc. 
They are: self (content that provides useful information that can enrich users' personal experience. ), relatability(content that makes us think “omg he's talking about me.”) and social (content that creates appreciation for users by users themselves). 
""")

    for transcript in transcripts:
        history.system("Transcript: " + transcript)
    history.system("What type of tone and personality is represented in the transcripts?")
    personality = llm_chat(history)
    history.assistant(personality)

    history.system("Generate a topic for future videos, suggest the title of the topic:")
    topic = llm_chat(history, temperature=1.0)
    history.assistant(topic)

    history.system("Generate a new transcript in line with the tone and personality previously "
                   "described for the suggested topic: ")
    transcript = llm_chat(history)
    history.assistant(transcript)

    return topic, transcript
