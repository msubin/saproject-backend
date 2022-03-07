from routes import get_solutions_route, get_filtered_solutions_route, \
    get_solution_instances_route, create_config_wizard_authorization_code_route, \
    create_solution_instance_route, set_instance_enable_route, \
    set_instance_disable_route, delete_solution_instance_route

# CONSTANT
URL = "https://tray.io/graphql"


def initialize(app):
    """
    Initialize all route.

    :param app: Flask application
    """
    get_solutions_route.init(app, URL)
    get_filtered_solutions_route.init(app, URL)
    get_solution_instances_route.init(app, URL)
    create_config_wizard_authorization_code_route.init(app, URL)
    create_solution_instance_route.init(app, URL)
    set_instance_enable_route.init(app, URL)
    set_instance_disable_route.init(app, URL)
    delete_solution_instance_route.init(app, URL)
