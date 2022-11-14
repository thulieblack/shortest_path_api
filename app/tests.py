from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
    
client = TestClient(app)

def test_shortest_path():
    response = client.get("/shortest-path")
    assert response.status_code == 200
    assert response.json() == {"start_word": "apple"}
