def init(app):
    @app.route('/')
    def index():
        return 'Hello World'
