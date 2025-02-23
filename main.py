from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to our FastAPI Service!",
        "status": "Running",
        "name": "Omi Kumari",
        "Location": "Dehradun"
    }

@app.get("/{data}")
def read_data(data: str):
    return {"hii": data, "Location": "Dehradun"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
