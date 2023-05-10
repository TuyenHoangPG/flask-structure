import os
from pathlib import Path
from dotenv import load_dotenv
from src.app import create_app

load_dotenv()

app = create_app(os.getenv("FLASK_ENV", "dev"))

if __name__ == "__main__":
    app.run()
