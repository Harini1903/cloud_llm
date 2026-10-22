from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def landing_page():
    return { "message" : "hi" } 
@app.get("/health")
def health_page():
    return { "message" : "hello"}

