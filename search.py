# Import necessary modules from langchain
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
import os

# Initialize the OpenAI model
api_key=os.environ.get('OPENAI_API_KEY')
llm=OpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=api_key)

# Create a SQLDatabase object that connects to the SQLite database
sqlite_db_path='/Users/claire/Documents/db_search/demo.db'
db=SQLDatabase.from_uri(f'sqlite:///{sqlite_db_path}')
#pip install mysql-connector-python
#db=SQLDatabase.from_uri('mysql://user:password@localhost:3306/db_name')
##substitute your own database name, user, and password

# Create a SQLDatabaseChain object that connects the OpenAI model to the SQLDatabase
db_chain=SQLDatabaseChain(llm=llm,database=db,verbose=True)

while True:
    question=input("Ask a question: ")
    if question=="quit":
        break
    db_chain.run(question)  
