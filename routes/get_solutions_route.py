from routes.environment import Environment
from routes.util import get_response


def init(app, url):
    env = Environment()

    @app.route('/')
    def get_solutions():
        """ Get Solutions from Tray.io """
        query = """
        { 
            viewer { 
                solutions { 
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
        headers = {'Authorization': 'Bearer %s' % env.master_token}

        return get_response(url, query, headers)
