from aframe import Aframe, xyz
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from textblob import TextBlob

app = FastAPI()

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"


@app.get('/')
def hello_world():
    a = Aframe()
    a.set_scene(background="color: #ECECEC")
    a.box(position=xyz(-1, 0.5, -3), rotation=xyz(0, 45, 0), 
          color="#4CC3D9", shadow=True)
    a.sphere(position=xyz(0, 1.25, -5), radius=1.25, 
             color="#EF2D5E", shadow=True)
    a.cylinder(position=xyz(1, 0.75, -3), radius=0.5, 
               height=1.5, color="#FFC65D", shadow=True)
    a.plane(position=xyz(0, 0.1, -4), rotation=xyz(-90, 0, 0), 
            width=4, height=4, color="#7BC8A4")
    a.gltf_model(src="https://raw.githubusercontent.com/nina180/SGD285/main/shiba/scene.gltf", position=xyz(0, 4.2, -4), scale=xyz(2, 2, 2))

    sample_text = "Today I am happy!"
    sentiment_result = analyze_sentiment(sample_text)
    a.text(value=f"Sentiment: {sentiment_result}", position=xyz(5, 5, -6), color="red")

    return HTMLResponse(a.generate())

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
