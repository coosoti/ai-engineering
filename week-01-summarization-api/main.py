from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import time

# Initialize the application
app = FastAPI(
    title="AI Summarizer",
    description="A production-ready NLP API",
    version="1.0.0"
)

# Load a distilled (smaller, faster) version of the BART model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Define the input schema: What the API accepts


class SummaryRequest(BaseModel):
    text: str
    max_length: int = 130  # Default max length for the summary
    min_length: int = 30   # Default min length for the summary

# Define the output schema: What the API returns


class SummaryResponse(BaseModel):
    summary: str
    word_count_original: int
    word_count_summary: int
    elapsed_seconds: float


@app.post("/summarize", response_model=SummaryResponse)
async def summarize_text(request: SummaryRequest):
    # clean the input
    raw_text = request.text.strip()

    # basic validation: checking if raw_text is empty
    if not raw_text:
        raise HTTPException(
            status_code=400, detail="The 'text' field cannot be empty.")

    # Context window check: Maximum Array/Buffer Size = this is 1024 tokens
    words = raw_text.split()
    word_count = len(words)

    MAX_INPUT_WORDS = 800  # Safe threshold beliw the 1024 token limit

    if word_count > MAX_INPUT_WORDS:
        words = words[:MAX_INPUT_WORDS]
        raw_text = " ".join(words)
        word_count = MAX_INPUT_WORDS
        if word_count < request.min_length:
            raise HTTPException(
                status_code=400,
                detail="Text is too short to summarize."
            )

    # AI Inference
    try:

        start_time = time.time()
        # Pass the clean, validated text to the model
        result = summarizer(
            raw_text,
            max_length=request.max_length,
            min_length=request.min_length,
            do_sample=False  # Deterministic output
        )
        elapsed_time = round(time.time() - start_time, 2)
        summary_text = result[0]['summary_text']
        summary_words = len(summary_text.split())

        # Return the response
        return SummaryResponse(
            summary=summary_text,
            word_count_original=word_count,
            word_count_summary=summary_words,
            elapsed_seconds=elapsed_time
        )

    except Exception as e:
        # Catch any unexpected ML math errors
        raise HTTPException(status_code=500, detail=f"Model failure: {str(e)}")

# Health check route for SRE monitoring later


@app.get("/health")
async def health():
    return {"status": "up", "model": "distilbart-cnn-12-6"}
