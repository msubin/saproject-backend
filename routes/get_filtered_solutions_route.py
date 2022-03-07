import requests
from routes.environment import Environment


def init(app, url):
    env = Environment()

    @app.route('/get-solutions/ecosystem')
    def get_filtered_solutions():
        """ Get Solutions filtered by tags """
        query = """
        ($tags: [String!]) { 
            viewer { 
                solutions(criteria: {tags: $tags}) { 
                    edges { 
                        node {
                            id
                            title
                            description
                            tags
                            customFields {
                                key
                                value
                            }
                            configSlots {
                                externalId
                                title
                                defaultValue
                            }
                        }
                        cursor
                    }
                    pageInfo {
                        hasNextPage
                        endCursor
                        hasPreviousPage
                        startCursor
                        }
                    }
                }
            }
        """
        variables = {'tags': 'ecosystem'}

        headers = {'Authorization': 'Bearer %s' % env.master_token}
        response = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Query failed to run with a {response.status_code}.")
