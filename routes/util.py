import requests
from routes.environment import Environment

URL = "https://tray.io/graphql"


def get_response(url, query, headers):
    response = requests.post(url=url, json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Query failed to run with a {response.status_code}.")


def get_response_with_variables(url, query, variables, headers):
    response = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Query failed to run with a {response.status_code}.")


def create_user_token():
    """ Create User Token with user ID """
    env = Environment()

    query = """
    mutation ($userId: ID!) {
        authorize(input: {
            userId: $userId
        }) {
            accessToken
        }
    }
    """
    variables = {"userId": env.user_id}
    headers = {'Authorization': 'Bearer %s' % env.master_token}

    response = requests.post(url=URL, json={'query': query, 'variables': variables}, headers=headers)

    if response.status_code == 200:
        res_json = response.json()
        return res_json["data"]["authorize"]["accessToken"]
    else:
        raise Exception(f"Query failed to run with a {response.status_code}.")
