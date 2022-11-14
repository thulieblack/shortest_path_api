# Shortest Path API

## Problem Statement
- Design and implement an API that takes two words and a dictionary of words as input. Your API should return the shortest possible path between the two words.
- Both the start and end words are lowercase strings of varying lengths.
- The start and end words can be different lengths.
- Only one letter can be changed, added, or deleted at a time.
- Each intermediate word must exist in the dictionary of words.
---
## Solution Approach
- ln order to solve the problem statement, l opted for a code-first approach since its a learning project.
- After creating a solution function, it was time to choose an API to integrate with the code.
- l choose to go with the FastAPI framework and GET method because of its simplicity.
- Lastly, it was time to change and tweak the meta data and improve the swagger UI design.
---
## Languages and Frameworks used
- Python 🐍
- FastAPI ⚡

## Getting Started
This project can be run on any enviroment. In my case I ran it on Pycharm and Gitpod. 

In the section below, we are going to create a simple "Hello World" example which will help us get acquinted and familiar with FastAPI. The code is easy to follow and can be run locally without any additional dependencies.

1. ### Dependency Installation
To run our API we need to install the latest FastAPI library and `uvicorn` for running a live server on your browser.

``` bash
pip install fastapi
pip install uvicorn
```

2. ### Creating a FastAPI instance
The next step after installation is to create a `main.py` file. Afterwards we can create our FastAPI instance:

``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

And from the terminal you can run the following script:

``` bash
uvicorn my_file:app
```
You'll get an output that contains the following URL which will redirect you to your browser:

```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

On your browser you'll see a JSON response: 

``` json
{"message": "Hello World"}
```

To conclude our FastAPI instance, you'll need to run the following URL:

``` bash
http://127.0.0.1:8000/docs
```
The above URL will open up an interactive API documentation provided by Swagger UI.

Alternatively, you also check the API documentation provided by ReDoc:
``` bash
http://127.0.0.1:8000/redoc
```
3. ### Creating the Shortest Path API function
Now that we are able to run our FastAPI instance, the next step is to create a simple function that will find the shortest possible path between two words. Our function needs to take two words and a dictionary of words as input.

Below is a simple function that finds the shortest distance between two avenger characters:

``` python
start_wrd = "ironman"

end_wrd = "falcon"

word_dict = ["ironman", "captain america", "hulk","thor", "black panther","dr strange", "falcon", "thanos", "spiderman",
             "antman", "wasp"]

def distance(word_dict, start_wrd, end_wrd):
    if start_wrd == end_wrd:
        return 0

    # assume total length of the string as min distance
    min_dist = len(word_dict) + 1

    # traverse through the entire dict
    for index in range(len(word_dict)):

        if word_dict[index] == start_wrd:
            for search in range(len(word_dict)):

                if word_dict[search] == end_wrd:

                    # the distance between the words is the first word index - the curr word index
                    curr_wrd = abs(index - search) - 1;

                    # comparing current distance with previous distance
                    if curr_wrd < min_dist:
                        min_dist = curr_wrd

    return min_dist

print(distance(word_dict, start_wrd, end_wrd))
```
Output:

```python
5
```

4. ### Running the Shortest Path API

The final step is to insert the code for our Shortest Path API found [here](https://github.com/thulieblack/shortest_path_api/blob/main/main.py) to your already created `main.py` file. Things to note when running our API:
- When creating a dictionary of words, there shouldn't be any parenthesis, commas, or special characters. The dictionary words can be seperated by a space.
- The start word and end word can be different lenghts and must be contained inside the word dictionary. If not, the execution will return an error message.

5. ### Final Results

 Below is an example image of a successful Shortest Path API execution result:
 ![image](https://user-images.githubusercontent.com/66913810/201628283-d642a06f-b7dd-4dd6-8029-5b406c62a8f8.png)

6. ### Testing 
To test our FastAPI application, simply open and run this [file](https://github.com/thulieblack/shortest_path_api/blob/main/app/tests.py) under the `app folder`

7. ### Next Steps
- You can try building your API using the Design First approach instead of the Code First implementation
- Add security features and measures to your API application
