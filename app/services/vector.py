import os
import string
import unicodedata

from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

from app import constants

ALLOWED_EXTENSIONS = {'pdf', 'txt'}  # Các phần mở rộng được phép

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  
def create_vector():
    os.environ["OPENAI_API_KEY"] = constants.APIKEY
    
    app_dir = os.getcwd() + "\\app"
    
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # assets_path = os.path.join(current_dir, '..', 'assets')
    # persist_path = os.path.join(current_dir, '..', 'persist')
    
    assets_path = app_dir + "\\assets"
    persist_path = app_dir + "\\persist"
    
    loader = DirectoryLoader(assets_path)
    
    VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":persist_path}).from_loaders([loader])

def secure_filename(filename: str) -> str:
    valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
    filename = unicodedata.normalize("NFKD", filename).encode("ASCII", "ignore").decode()
    return "".join(c for c in filename if c in valid_chars)