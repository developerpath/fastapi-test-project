from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "welcome": "Hello! Thanks for taking the time to do this challenge. I hope you have a great day!"
    }
