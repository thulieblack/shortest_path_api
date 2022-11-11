from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse

description = """
### Avengers Assemble API aims at finding the shortest path between two Avenger Hero's or Villain's 
"""

app = FastAPI(
    title= "Avengers Assemble",
    version= "1.0",
    description= description

)

@app.get("/")
async def root():
    return {"mesage": "The shortest path between two Avengers"}

word_dict = ["ironman", "captain america", "hulk","thor", "black panther","dr strange", "falcon", "thanos", "spiderman",
             "antman", "wasp"]


@app.get("/shortest-path/")
async def shortest_path(start_word: str, end_word: str):
    if start_word == end_word:
        return 0

    if end_word not in word_dict:
        return JSONResponse("Please try another Avenger!")

    if start_word not in word_dict:
        return JSONResponse("Please try another Avenger!")

    # assume total length of the string as min distance
    short_dist = len(word_dict) + 1

    # traverse through the entire dict
    for index in range(len(word_dict)):

        if word_dict[index] == start_word:
            for search in range(len(word_dict)):

                if word_dict[search] == end_word:

                    # the distance between the words is the first word index - the curr word index
                    curr_wrd = abs(index - search) - 1;

                    # comparing current distance with previous distance
                    if curr_wrd < short_dist:
                        short_dist = curr_wrd

    return short_dist
