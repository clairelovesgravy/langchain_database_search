# README.md

## Query database using natural language powered by Langchain 
(An Interface to OpenAI GPT-3.5-turbo & SQL Databases)

### Introduction
This project provides a way to use OpenAI's GPT-3.5-turbo language model in combination with SQL databases, enabling the powerful and intuitive language processing of OpenAI to interact with databases directly. This is achieved using the `langchain` module which includes classes like `OpenAI`, `SQLDatabase`, and `SQLDatabaseChain`.

### Prerequisites
Before starting with this project, ensure you have the following:
1. Python 3.6 or newer
2. OpenAI's Python package
3. MySQL Connector Python (Optional if using a MySQL database)
4. SQLite database or MySQL database

Install necessary packages using pip:
```
pip install openai
pip install langchain
pip install mysql-connector-python
```

### Setting Up
1. **Initialize OpenAI model**: Initialize the OpenAI model using the `OpenAI` class from `langchain` module. It requires an API key that can be retrieved from your OpenAI account.

2. **Connect to Database**: Create an instance of the `SQLDatabase` object that connects to the SQLite database or MySQL database using the `from_uri` method.

3. **Create SQLDatabaseChain object**: Create an instance of the `SQLDatabaseChain` object that connects the OpenAI model to the `SQLDatabase`.

### Usage

After setup, run a while loop to take in user input. If the user types "quit", the loop will break. Otherwise, it will run the input question through the `SQLDatabaseChain` object which will interact with the database using the OpenAI model. Here's the code:

```python
while True:
    question=input("Ask a question: ")
    if question=="quit":
        break
    db_chain.run(question)
```
The OpenAI model will interpret the question and return a relevant SQL query, which will then be executed on the connected SQL database. This functionality is encapsulated in the `SQLDatabaseChain.run()` method.

### Conclusion
This project is a powerful tool that leverages the abilities of OpenAI's language models to interact with databases in an intuitive, conversational manner. It can be very useful for performing complex database operations without needing to write complicated SQL queries.

### Note
This project is in a development phase. We encourage users to report any issues and contribute to the development by submitting pull requests.

For more information, please visit the project homepage.

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### Acknowledgments
* Thanks to OpenAI for providing the GPT-3.5-turbo model.
* Thanks to users who contribute to the project's improvement.
