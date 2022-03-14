from routes.environment import Environment
from routes.util import get_response_with_variables


def init(app, url):
    env = Environment()

    @app.route('/api/get-solutions')
    def get_solutions():
        """ Get Solutions tagged 'ecosystem' from Tray.io """
        query = """
                query ($tags: [String!]) { 
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

        return get_response_with_variables(url, query, variables, headers)
