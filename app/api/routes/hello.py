from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException, Response, status


app = FastAPI()
auth = APIRouter()

@app.auth.get('/')
async def main():
    return "hello"