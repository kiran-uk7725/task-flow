from app import create_app

app = create_app()
print(app.config['DEBUG'])
print(app.config['TESTING'])