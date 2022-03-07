import json
from flask import request
from routes.util import get_response_with_variables, create_user_token


def init(app, url):
    @app.route('/create-solution-instance', methods=['POST'])
    def create_solution_instance():
        """ Create Solution Instance """
        temp = request.data.decode("UTF-8")
        data = json.loads(temp)

        solution_id = data["solutionId"]
        customer_name = data["customerName"]
        initial = data["saInitial"]
        solution_title = data["solutionTitle"]
        instance_name = f"{customer_name} - {solution_title} - {initial}"

        query = """
        mutation ($solutionId: ID!, $instanceName: String!){
            createSolutionInstance(input: {
                solutionId: $solutionId
                instanceName: $instanceName
            }) {
                solutionInstance {
                    id
                    name
                    enabled
                    authValues{
                        authId
                        externalId
                    }
                }
            }
        }
        """
        variables = {
            "solutionId": solution_id,
            "instanceName": instance_name
        }

        headers = {'Authorization': 'Bearer %s' % create_user_token()}

        return get_response_with_variables(url, query, variables, headers)
