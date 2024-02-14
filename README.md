# Implementing the RAG Pattern in PromptFlow

This codebase provides an example implementation of a RAG (Retrieval-Augmented-Generation) flow using:

- Azure AI Search
- Azure OpenAI models
- PromptFlow

## Prerequisites

In order to complete this workshop, you will need to the following:

- Python 3.11 or higher (recommended using an Anaconda environment)
- Visual Studio Code
  - Python and Jupyter extensions
  - PromptFlow extension (<https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow>)
- Access to an Azure AI Search deployment
- Access to an Azure OpenAI deployment
  - You will need a `gpt-4` or `gpt-3.5-turbo` model deployed (so far, only tested with GPT-4 for results)
  - A `text-embedding-ada-002` model deployed

## Setup

#### Create a Python Virtual Environment

It's a good practice to use virtual environments to isolate your project dependencies and avoid conflicts with system-wide packages.

1. **Create a new virtual environment:**

    Navigate to your project directory in the terminal and run the following command to create a new virtual environment. Replace `env` with the name you want to give to your virtual environment.

    ```bash
    python3 -m venv env
    ```

2. **Activate the virtual environment:**

    - On Windows, run:

        ```cmd
        .\env\Scripts\activate
        ```

    - On Unix or MacOS, run:

        ```bash
        source env/bin/activate
        ```

    After running this command, your terminal prompt should change to show the name of the activated environment.

3. **Install packages:**

    You can now install packages into the isolated environment. For example:

    ```bash
    pip install -r requirements.txt
    ```

4. **Deactivate the virtual environment:**

    When you're done working, you can deactivate the virtual environment to return to your normal shell. Simply run:

    ```bash
    deactivate
    ```

5. **Requirements file:**

    If you want to keep track of your project's dependencies, you can use `pip freeze` to generate a `requirements.txt` file:

    ```bash
    pip freeze > requirements.txt
    ```

    This file can be committed into version control and shared with others.

#### Setup your environment to run this codebase, you will need

1. Open the folder in Visual Studio Code and go to Terminal. In your python environment, enter `pip install -r requirements.txt`. This will install all dependencies listed in requirements.txt. (You can skip this if it was already done when setting up the envirioment)
2. Copy the `.env.template` file into a `.env` file, and fill out the required fields. From Terminal type `copy .env.template .env`
3. Copy the data you wish to index into a new `data` folder
4. Open the PromptFlow extension on the left side of VS Code

    - Expand the "Connections" section (may be at the bottom)
    - Add an `Azure OpenAI` and `Cognitive Search` connection to your respective services.

## Create the Index

Before we create the index, let's go over why we need it.

We are using a RAG pattern to get the desired outputs from the LLM.

RAG (Retrieval-Augmented Generation) is a method used in Natural Language Processing (NLP) that combines the benefits of both retrieval-based and generative models.

Here's a brief overview of how it works:

1. **Retrieval Step**: Given an input (like a question), the model retrieves a set of documents from a corpus that are relevant to the input. This is done using a retrieval-based model, which is trained to select relevant documents based on the input.

2. **Generation Step**: The model then generates a response (like an answer to the question) based on both the input and the retrieved documents. This is done using a generative model, which is trained to generate responses based on both the input and the documents.

The key advantage of RAG is that it can leverage the vast amount of information in the document corpus to generate more informed and accurate responses. It's particularly useful for tasks like question answering, where the answer may not be in the training data but can be inferred from the documents in the corpus.

In this lab, we use Azure AI Search to store the vector representation on the documents. Azure AI Search is a Vector database which are crucial in RAG because they enable efficient storage and retrieval of embeddings.

In the context of RAG, embeddings are high-dimensional vector representations of objects (text documents, images, etc). We will generate these embeddings using the text-embedding-ada-002 model to capture the semantic meaning of the documents.

When a question comes in, the RAG model generates an embedding for the question and uses a Azure AI Search to find the embeddings of documents that are closest to the question embedding. This is known as nearest neighbor search.

Vector databases are designed to handle high-dimensional data and can perform nearest neighbor search much more efficiently than traditional databases. This makes them ideal for use in RAG models, where the speed and accuracy of the retrieval step is critical to the performance of the model.

To create the search index, we can run the provided `building_index.ipynb` jupyter notebook. Make sure you copied the data to be index to the data folder.

## Executing the Flow

#### Why Prompt Flow

Prompt Flow is a feature of Azure Machine Learning that simplifies the design, evaluation, and deployment of large language model-based applications.

It allows users to easily track, reproduce, visualize, and improve prompts and flows across a variety of tools and resources, making it quicker to be production-ready.

It also provides a managed end-to-end platform to streamline the entire large language model lifecycle and model management with native MLOps capabilities.

You can develop and run flows locally or in the Cloud.

#### Running the flow

- Open the `flow.dag.yaml` file. If you have the PromptFlow extension installed in VS Code, you can press `Ctrl+k, v` to switch to the visualizer (or click the small "Visual Editor" link at the top of the file).

- For the `DetermineIntent`, `RetrieveDocuments`, and `DetermineReply` nodes, be sure to select the connections you configured during setup.

- Finally, at the top of the flow, click the `enable_chat` checkbox, and select the `Chat Input` and `Chat History` radio buttons for `query` and `chat_history` respectively. Also select `reply` as the `Chat Output` in the Outputs.

- Now, you should be ready to add inputs to the chat at the top, and run the flow! You should be prompted to choose between standard mode and interactive mode. I prefer interactive mode in text for testing it out.

## Additional Scenarios

Now that we have our basic RAG pattern working there are some additional features / enhancement we could implement.

- [Monitoring and Evaluation]( https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/concept-model-monitoring-generative-ai-evaluation-metrics?view=azureml-api-2)

- [Deploy a flow for real-time inference](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-deploy?tabs=azure-studio)

- [Responisible AI](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext)
