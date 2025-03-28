# LLM-RAG Automation API  

A **Python-based API service** that dynamically retrieves and executes automation functions using **LLM + RAG (Retrieval-Augmented Generation)**. The system processes user prompts, maps them to predefined automation functions, and generates executable Python code for function invocation.  

## Key Features  
- **LLM + RAG Integration**: Enhances response generation by retrieving relevant automation functions.  
- **Dynamic Code Generation**: Translates user prompts into executable Python code.  
- **Function Mapping**: Matches prompts with predefined automation workflows.  
- **API-Driven Architecture**: Built with FastAPI for seamless integration and execution.  

## How It Works  
1. **User Input**: The system receives a prompt describing an automation task.  
2. **RAG Retrieval**: Searches for relevant predefined functions using an embedding-based retrieval system.  
3. **Code Generation**: LLM generates a Python script to execute the identified function.  
4. **Execution & Response**: The system runs the generated code and returns results to the user.  

## Use Cases  
- **Automated Data Processing**  
- **Task Scheduling and Execution**  
- **Custom Script Generation**  
- **API-Triggered Automation**  

This API service enables efficient task automation by leveraging **LLM-driven reasoning and retrieval-based augmentation** to ensure accurate function execution. 🚀  


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
