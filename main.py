from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

# Path to the quotes.json file
quotes_file_path = Path("quotes.json")

# Check if the file exists and if it can be opened
def read_quotes():
    if quotes_file_path.exists():
        with open(quotes_file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"error": "quotes.json file not found!"}

@app.get("/quotes")
def get_quotes():
    quotes = read_quotes()
    return quotes

"""from fastapi import FastAPI
import json
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/quotes")
async def read_quotes():
    with open('quotes.json', 'r') as file:
        # Load JSON as a list (ensure the order is preserved)
        quotes = [json.loads(line) for line in file]
    
    # Return the quotes in the same order they were loaded
    return JSONResponse(content=quotes)
"""