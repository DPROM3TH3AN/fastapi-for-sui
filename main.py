"""
main.py - SuiAutoforge Project

This module serves as the entry point for the SuiAutoforge API. It imports the FastAPI
application from API.py and starts the server using uvicorn.
"""

import uvicorn
from api import app

if __name__ == "__main__":
    # Start the FastAPI server on host 0.0.0.0 and port 8000.
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)