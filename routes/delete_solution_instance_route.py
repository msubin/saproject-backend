from flask import request
import json
from routes.util import create_user_token, get_response_with_variables


def init(app, url):

    @app.route('/delete-solution-instance', methods=['POST'])
    def delete_solution_instance():
        """ Delete Solution Instance """
        temp = request.data.decode("UTF-8")
        data = json.loads(temp)
        instance_id = data["instanceId"]

        query = """
        mutation ($solutionId: ID!){
            removeSolutionInstance(input: {
                solutionInstanceId: $solutionId
            }) {
                clientMutationId
            }
        }
        """
        variables = {
            "solutionId": instance_id,
        }

        headers = {'Authorization': 'Bearer %s' % create_user_token()}
        return get_response_with_variables(url, query, variables, headers)
