""" Server file """
#environmental variables
import os
from dotenv import load_dotenv
from app import app

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
