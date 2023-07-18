from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Word"}

if __name__== "main":    
    uvicorn.run("main:app", host="0.0.0.0", reload= True, port=8000)  