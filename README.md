# OpenAI Streaming API 

## Running the Project

1. Clone the repository.
2. Install Python (Python 3.8+ is recommended).
3. run cmd: <directory_python_path>\python.exe -m venv env, ex: C:\Users\ADMIN\.pyenv\pyenv-win\versions\3.10.0\python.exe -m venv env
4. run cmd: .\env\Scripts\activate
5. Install necessary libraries. This project uses FastAPI, uvicorn, LangChain, among others. You can install them with pip: `pip install fastapi uvicorn langchain openai chromadb tiktoken unstructured unstructured[pdf]`.
6. Create constants.py and Add your OpenAI API key to the `constants.py` file. The template like constants.example.py
7. Start the FastAPI server by running `uvicorn main:app` in the terminal.
8. Access the application by opening your web browser and navigating to `localhost:8000`.
