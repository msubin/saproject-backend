from routes.environment import Environment
from routes.util import get_response_with_variables


def init(app, url):
    env = Environment()

    @app.route('/api/get-instances')
    def get_solution_instances():
        """ Get Solution InstanceList with a user token """
        query = """
                query ($ownerId: String!){
                    viewer {
                        solutionInstances(criteria: { owner: $ownerId}) {
                            edges {
                                node {
                                    id
                                    name
                                    enabled
                                    owner
                                    created
                                    solutionVersionFlags {
                                        hasNewerVersion
                                        requiresUserInputToUpdateVersion
                                        requiresSystemInputToUpdateVersion
                                    }
                                    workflows {
                                        edges {
                                            node {
                                                triggerUrl
                                                id
                                                sourceWorkflowId
                                            }
                                        }
                                    }
                                    authValues {
                                        externalId
                                        authId
                                    }
                                    configValues {
                                        externalId
                                        value
                                    }
                                }
                                cursor
                            }
                            pageInfo {
                                startCursor
                                endCursor
                                hasNextPage
                                hasPreviousPage
                            }
                        }
                    }
                }
                """
        variables = {
            "ownerId": env.user_id
        }

        headers = {'Authorization': 'Bearer %s' % env.master_token}

        return get_response_with_variables(url, query, variables, headers)
