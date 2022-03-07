from flask import request
import json
from routes.util import create_user_token, get_response_with_variables


def init(app, url):
    @app.route('/set-instance-enable', methods=['POST'])
    def set_instance_enable():
        """ Enable the Solution Instance """
        temp = request.data.decode("UTF-8")
        data = json.loads(temp)
        instance_id = data["instanceId"]
        instance_name = data["instanceName"]

        query = """
        mutation($solutionInstanceId: ID!, $instanceName: String!, $enabled: Boolean!) {
            updateSolutionInstance(input: {
                solutionInstanceId: $solutionInstanceId,
                instanceName: $instanceName,
                enabled: $enabled
            }) {
                solutionInstance {
                    id
                    name
                    enabled
                    created
                }
            }
        }
        """
        variables = {
            "solutionInstanceId": instance_id,
            "instanceName": instance_name,
            "enabled": True
        }
        headers = {'Authorization': 'Bearer %s' % create_user_token()}
        return get_response_with_variables(url, query, variables, headers)
