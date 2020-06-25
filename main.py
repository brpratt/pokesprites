from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/sprites/{id}")
async def get_sprite(id: int):
    return FileResponse(f"images/{id}.png")
