from function_retriver import Retriever
from fastapi import FastAPI
from pydantic import BaseModel
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

R=Retriever()
R.create_embeddings()

app = FastAPI()


class QueryRequest(BaseModel):
    query: str

@app.post("/execute")
async def execute_function(request: QueryRequest):
    """API endpoint to execute a function with logging and monitoring."""
    start_time = time.time()
    try:
        response = R.execute(request.query)
        logger.info(f"Function executed successfully: {request.query}")
    except Exception as e:
        logger.error(f"Error executing function: {str(e)}")
        response = {"error": str(e)}
    
    execution_time = round(time.time() - start_time, 4)
    logger.info(f"Execution Time: {execution_time} seconds")

    return {
        "query": request.query,
        "response": response,
        "execution_time": execution_time
    }

@app.post("/improve_code")
async def improve_code(request: QueryRequest):
    """API endpoint to retrieve and enhance function code with logging."""
    start_time = time.time()
    try:
        response = R.Invocation(request.query)
        logger.info(f"Code improvement successful for: {request.query}")
    except Exception as e:
        logger.error(f"Error improving code: {str(e)}")
        response = {"error": str(e)}
    
    execution_time = round(time.time() - start_time, 4)
    logger.info(f"Execution Time: {execution_time} seconds")

    return {
        "query": request.query,
        "improved_code": response,
        "execution_time": execution_time
    }

user_defined_functions = {}

@app.post("/add_function")
async def add_function(request: QueryRequest):
    """API endpoint to allow users to define custom functions."""
    try:
        exec(request.query, globals(), user_defined_functions)
        logger.info(f"User-defined function added successfully.")
        return {"message": "Function added successfully"}
    except Exception as e:
        logger.error(f"Error adding function: {str(e)}")
        return {"error": str(e)}

@app.post("/run_function")
async def run_function(request: QueryRequest):
    """API endpoint to execute a user-defined function."""
    try:
        function_name = request.query.strip()
        if function_name in user_defined_functions:
            result = user_defined_functions[function_name]()
            logger.info(f"User-defined function '{function_name}' executed successfully.")
            return {"function": function_name, "result": result}
        else:
            return {"error": "Function not found"}
    except Exception as e:
        logger.error(f"Error executing function: {str(e)}")
        return {"error": str(e)}


