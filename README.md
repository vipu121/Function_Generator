# LLM-RAG Automation API with Groq  

A **Python-based API service** that dynamically retrieves and executes automation functions using **LLM + RAG (Retrieval-Augmented Generation)**. The system processes user prompts, maps them to predefined automation functions, and dynamically generates executable Python code for function invocation using the **Groq API**.  

## Key Features  
- **LLM + RAG with Groq API**: Uses Groq's AI models for accurate function retrieval and code generation.  
- **Dynamic Code Execution**: Converts user prompts into executable Python scripts.  
- **Predefined Function Mapping**: Matches user requests with existing automation workflows.  
- **FastAPI Integration**: Provides a scalable API for task execution.  

## How It Works  
1. **User Input**: A prompt describing the automation task is received.  
2. **RAG-Based Retrieval**: Searches for relevant predefined functions using embeddings.  
3. **Groq API Generation**: Uses Groq to generate Python code for function execution.  
4. **Execution & Response**: The system runs the generated code and returns results.  

## Use Cases  
- **Automated Data Processing**  
- **Dynamic Script Generation**  
- **Task Scheduling & Execution**  
- **API-Based Automation**  

This project leverages **Groq API, LLM-driven reasoning, and RAG** to automate workflows efficiently and intelligently.
 


## Features
- Uses FAISS for efficient document retrieval.
- Integrates HuggingFace embeddings.
- Enhances LLM responses with contextual retrieval.
- Built with FastAPI for easy deployment.

## Installation
Clone the repository and install dependencies:
```sh
git clone https://github.com/vipu121/LLM-RAG.git
cd LLM-RAG
pip install -r requirements.txt
