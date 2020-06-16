import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("8acc3c8-00c7-1aec-b41b-7d916bc7a5f4")

def basilica_api_client():
    connection = basilica.Connection(API_KEY)
    print(type(connection)) #> <class 'basilica.Connection'>
    return connection

if __name__ == "__main__":

    print("---------")
    connection = basilica_api_client()

    print("---------")
    sentence = "Hello again"
    sent_embeddings = connection.embed_sentence(sentence)
    print(list(sent_embeddings))

    print("---------")
    sentences = ["Hello world!", "How are you?"]
    print(sentences)
    # it is more efficient to make a single request for all sentences...
    embeddings = connection.embed_sentences(sentences)
    print("EMBEDDINGS...")
    print(type(embeddings))
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]