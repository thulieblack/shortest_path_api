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

3. ### Running the Shortest Path API
Now that we are able to run our FastAPI instance, the final step is to insert the code for our Shortest Path API found [here](https://github.com/thulieblack/shortest_path_api/blob/main/main.py) to your already created `main.py` file.

4. ### Final Results

 Below is an example image of the Shortest Path API result:
 ![image](https://user-images.githubusercontent.com/66913810/201628283-d642a06f-b7dd-4dd6-8029-5b406c62a8f8.png)


