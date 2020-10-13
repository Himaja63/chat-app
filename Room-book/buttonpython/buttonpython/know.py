import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\\divya\\divya.json"


def create_knowledge_base(project_id, display_name):
    """Creates a Knowledge base.

    Args:
        project_id: The GCP project linked with the agent.
        display_name: The display name of the Knowledge base."""
        
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.KnowledgeBasesClient()
    project_path = client.project_path(project_id)

    knowledge_base = dialogflow.types.KnowledgeBase(
        display_name=display_name)

    response = client.create_knowledge_base(project_path, knowledge_base)

    print('Knowledge Base created:\n')
    print('Display Name: {}\n'.format(response.display_name))
    print('Knowledge ID: {}\n'.format(response.name))


create_knowledge_base("test-chatbot2-rhylal", "test1")

