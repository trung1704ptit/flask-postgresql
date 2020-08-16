import os

from src.app import create_app

if __name__ == '__main__':
    env_name=os.getenv('FLASK_ENV')
    app = create_app('Development')

    # run app
    app.run()