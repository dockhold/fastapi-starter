from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "It's live. This FastAPI app is running on Dockhold.",
        "docs": "https://dockhold.eu/docs/recipes/deploy-a-python-fastapi-app",
    }


@app.get("/health")
def health():
    return {"status": "ok"}
