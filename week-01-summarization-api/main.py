from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize the application
app = FastAPI(
    title="AI Summarizer",
    description="A production-ready NLP API",
    version="1.0.0"
)

# Define the input schema: What the API accepts
class SummaryRequest(BaseModel):
    text: str
    max_length: int = 130  # Default max length for the summary
    min_length: int = 30   # Default min length for the summary

# Define the output schema: What the API returns
class SummaryResponse(BaseModel):
    summary: str
    word_count_original: int
