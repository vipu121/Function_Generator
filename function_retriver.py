from fastapi import  HTTPException
from function_registry import function_bank
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv("API_KEY")




class Retriever:
    def __init__(self):
        # self.model=SentenceTransformer(model, device="cpu")
        self.embedding_model=None
        self.documents=None
        self.vector_store=None
        self.chat_history=[]

    def create_embeddings(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",model_kwargs={"device": "cpu"})
        self.documents=[
            Document(page_content=func["description"],metadata={"name":name})
            for name, func in function_bank.items()
        ]
        self.vector_store = FAISS.from_documents(self.documents, self.embedding_model)
        

    def retrieve(self,user_query):
        docs=self.vector_store.similarity_search(user_query, k=1)
        if docs:
            return docs[0].metadata["name"]
        return None
    
    def execute(self,user_query):
        function=self.retrieve(user_query)
        
        if function and function in function_bank:
            result=function_bank[function]["function"]()
            if result:
                return {"Executed": function, "Result": result}
            return {"Executed": function, "Result": "Program Launched"}
        raise HTTPException(status_code=404, detail="Function not found.")
    

    def update_chat_history(self,user_query,model_response):
        self.chat_history.append({"user": user_query, "model": model_response})
        if (len(self.chat_history)>7):
            self.chat_history.pop(0)

    def retrieve_contextual_response(self,code_to_improve):
        context = "\n".join([f"User: {entry['user']}\nModel: {entry['model']}" for entry in self.chat_history])
        prompt = f"Context:\n{context}\n\nNew Query: {code_to_improve}\nProvide an improved response based on past interactions."
        return prompt


    def Invocation(self,user_query):
        function_name=self.retrieve(user_query)

        if not function_name:
            raise HTTPException(status_code=404, detail="No matching function found.")
        
        code_to_improve = f"""{function_bank[function_name]["code"]}"""
        prompt = "Ensure proper imports, error handling, and modularity."

# Initialize the client
        client = Groq(api_key=API_KEY)
        code_to_improve=self.retrieve_contextual_response(code_to_improve)
        # Create a chat completion request
        completion = client.chat.completions.create(
            model="llama-3.3-70b-specdec",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": code_to_improve}
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                response += chunk.choices[0].delta.content
                # print(chunk.choices[0].delta.content, end="")  # Print as it streams
        response_lines = response.strip().split("\n")

        self.update_chat_history(user_query, response)
        return {"function": function_name, "code": response_lines}
        # return response


        
