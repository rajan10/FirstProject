import httpx

from config.settings import EXTERNAL_API_URL
from state.chat_state import ChatState

# ChatState represents the information carried through your chatbot workflow.
# """def
#  │
#  ▼
# api_node
#  │
#  ├── input: state
#  │
#  └── output: dict """

def api_node(state: ChatState) -> dict:
    print("Executing API Node")

    try:
        # """ response is the package delivered by the Internet courier 📦.
        #     response
        #     ├── status_code = 200
        #     ├── headers = ...
        #     └── body = JSON data
        # """
        response = httpx.get(       
            EXTERNAL_API_URL,
            timeout=10.0   # for production code, you don't want your application waiting forever for a remote service
        )

        response.raise_for_status()  #  if HTTP response indicates an error then find out 400, 401,500 etc error

        data = response.json() 
                #     """
                #     { json format
                # "id": 1,
                # "title": "delectus aut autem",
                # "completed": false
                #     }
                #     """

        context = f"""
        External service record ID: {data.get('id')} 
        """.strip()

            #data.get("id")  #If id doesn't exist no error but if you use data['id'] => if no id then it throws KeyError!
        # """
        # Service message: {data.get('title')}
        # Completed: {data.get('completed')}
        # """
    except httpx.HTTPError as error:
        context = (
            "The external API is currently unavailable. "
            f"Error type: {type(error).__name__}"  #  gives the erronr name eg HTTPStatusError
        )

    return {"context": context}
