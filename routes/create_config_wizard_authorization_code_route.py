import json
import requests
from routes.environment import Environment
from flask import request


def init(app, url):
    env = Environment()

    @app.route('/api/create-config', methods=['POST'])
    def create_config_wizard():
        """ Create Config Wizard Authorization Code """
        temp = request.data.decode("UTF-8")
        data = json.loads(temp)
        instance_id = data["instanceId"]

        query = """
        mutation ($userId: ID!) {
            generateAuthorizationCode( input: {
                userId: $userId
            }) {
                authorizationCode
            }
        }
        """
        variables = {"userId": env.user_id}
        headers = {'Authorization': 'Bearer %s' % env.master_token}

        response = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)

        if response.status_code == 200:
            data = response.json()
            config_code = data["data"]["generateAuthorizationCode"]["authorizationCode"]
            config_url = f"https://embedded.tray.io/external/solutions/{env.user_id}/configure/{instance_id}?code={config_code}"
            print(config_url)
            return config_url
        else:
            raise Exception(f"Query failed to run with a {response.status_code}.")
