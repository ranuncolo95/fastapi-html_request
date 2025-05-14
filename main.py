from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from textblob import TextBlob



app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )


@app.get("/saluto", response_class=HTMLResponse)
def saluto(request: Request, nome_persona: str, cognome_persona: str):
    return templates.TemplateResponse(
        request=request, name="saluto.html", 
        context={
            "nome": nome_persona,
            "cognome" : cognome_persona
            })


@app.get("/sentimento", response_class=HTMLResponse)
def sentimento_home(request: Request):
    return templates.TemplateResponse(
        request=request, name="sentimento.html")


@app.get("/risposta", response_class=HTMLResponse)
def sentimento(request: Request, testo: str):
    blob = TextBlob(testo)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        risposta = "Il sentiment è positivo"
    elif sentiment < 0:
        risposta = "Il sentiment è negativo"
    else:
        risposta =  "Il sentiment è neutrale"
    
    return templates.TemplateResponse(
        request=request, name="risposta.html", context={"risposta" : risposta})