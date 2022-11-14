from fastapi import FastAPI, Query
from typing import Optional
from fastapi.responses import JSONResponse

description = """
This API takes two words and a dictionary of words as input and return the shortest possible path between the two words.🚀🚀

- Both the start and end words are lowercase strings of varying lengths.
- The start and end words can be different lengths.
- Only one letter can be changed, added, or deleted at a time.
- Each intermediate word must exist in the dictionary of words.
"""

app = FastAPI(
    title= "Shortest Path API - OpenAPI 3.0",
    description= description,
    license_info= {"name" : "Apache 2.0",
              "url" : "http://www.apache.org/licenses/LICENSE-2.0.html",
              "version" : "1.0.0"

  }


)

@app.get("/shortest-path",summary= "Returns the shortest possible path between two words"
    , description= "This API returns the shortest possible path between two words contained inside a dictionary of words.")
async def shortest_path(word_dict: str = Query(example= "apple pear banana orange grapes"),
                        start_word: str = Query(example="apple"),
                        end_word: str= Query(example="orange")):

    if start_word == end_word:
        return JSONResponse("Try Another Value")

    if end_word not in word_dict:
        return JSONResponse("Invalid Parameter!")

    if start_word not in word_dict:
        return JSONResponse("Invalid Parameter!")
    
    # get individual words in a list
    word_dict = word_dict.split(" ")

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
