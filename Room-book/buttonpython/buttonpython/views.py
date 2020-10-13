from django.shortcuts import render
import requests
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\\divya\\divya.json"
import dialogflow_v2beta1 as dialogflow
from google.api_core.exceptions import InvalidArgument
def button(request):
    return render(request,'home.html')

def create_document(project_id, knowledge_base_id, display_name, mime_type,
                    knowledge_type, content_uri):
    """Creates a Document.

    Args:
        project_id: The GCP project linked with the agent.
        knowledge_base_id: Id of the Knowledge base.
        display_name: The display name of the Document.
        mime_type: The mime_type of the Document. e.g. text/csv, text/html,
            text/plain, text/pdf etc.
        knowledge_type: The Knowledge type of the Document. e.g. FAQ,
            EXTRACTIVE_QA.
        content_uri: Uri of the document, e.g. gs://path/mydoc.csv,
            http://mypage.com/faq.html."""
    
    client = dialogflow.DocumentsClient()
    knowledge_base_path = client.knowledge_base_path(project_id,
                                                     knowledge_base_id)

    document = dialogflow.types.Document(
        display_name=display_name, mime_type=mime_type,
        content_uri=content_uri)

    document.knowledge_types.append(
        dialogflow.types.Document.KnowledgeType.Value(knowledge_type))

    response = client.create_document(knowledge_base_path, document)
    print('Waiting for results...')
    document = response.result(timeout=120)
    print('Created Document:')
    print(' - Display Name: {}'.format(document.display_name))
    print(' - Knowledge ID: {}'.format(document.name))
    print(' - MIME Type: {}'.format(document.mime_type))
    print(' - Knowledge Types:')
    # for knowledge_type in document.knowledge_types:
    #     print('    - {}'.format(KNOWLEDGE_TYPES[knowledge_type]))
    print(' - Source: {}\n'.format(document.content_uri))
   
    document = {}
    response = client.update_document(document)
    def callback(operation_future):
        # Handle result.
        result = operation_future.result()

    response.add_done_callback(callback)
    # Handle metadata.
    metadata = response.metadata()

def output(request):
    try:
        project_id = "test-chatbot2-rhylal"
        knowledge_base_id = "MzI4ODc3NzgxNzE0MzExNTc3Ng"
        display_name = "C_programming"
        mime_type = "text/html"
        knowledge_type = "FAQ"
        content_uri = "https://www.geeksforgeeks.org/commonly-asked-c-programming-interview-questions-set-1/"

                    # create_document("python-ppximk", "NjIwODc5OTIyNTUzOTQ2MTEyMA", "Balance",
                    #      "text/html", "FAQ", "https://www.balancedancestudios.com/faq/")
        create_document(project_id, knowledge_base_id, display_name, mime_type,
                                knowledge_type, content_uri)

        data = "executed"
    
    except:
        if InvalidArgument:
            data = "Executed"
        else:
            data = "this FAQ document is already existing"
    

      

    return render(request, 'home.html', {"data":data})








