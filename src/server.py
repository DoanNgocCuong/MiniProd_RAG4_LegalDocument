from flask import Flask, request, jsonify  # Import Flask
from rag_pipeline.back import LLMHandler, VectorDatabase, QuestionAnsweringChain
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
import sys
import logging
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import sys
import logging

# Set console output encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Set up detailed logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "allow_headers": ["Content-Type"],
        "expose_headers": ["Content-Type"],
        "methods": ["GET", "POST", "OPTIONS"]
    }
})

# Parameters
load_dotenv()
gemini_key = os.getenv('gemini_key')
qdrant_key = os.getenv('qdrant_key')
rerank = True
rewrite = True
num_docs = 5

# Global variables
vector_db = None
llm_handler = None
qa_chain = None

def initialize_components():
    global vector_db, llm_handler, qa_chain
    if vector_db is None:
        vector_db = VectorDatabase(
            model_name="hiieu/halong_embedding",
            collection_name='cmc_final_db',
            api=qdrant_key
        )
    if llm_handler is None:
        llm_handler = LLMHandler(model_name="gemini-1.5-flash", gemini_key=gemini_key)
    if qa_chain is None:
        qa_chain = QuestionAnsweringChain(
            llm_handler=llm_handler,
            vector_db=vector_db,
            num_docs=num_docs,
            apply_rerank=rerank,
            apply_rewrite=rewrite,
            date_impact=0.001
        )

# Initialize once when starting
initialize_components()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Use global qa_chain
    response, extracted_links = qa_chain.run(question)
    return jsonify({
        "response": response,
        "links": extracted_links
    })

if __name__ == '__main__':
    logger.info("🚀 Starting Flask application...")
    app.run(host='0.0.0.0', port=3000, debug=True)