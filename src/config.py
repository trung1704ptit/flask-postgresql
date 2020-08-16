import os

class Development(object):
    """
    Development eviroment configuration
    """
    DEBUG=True
    TESTING=False
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABSE_URI=os.getenv('DATABSE_URL')

class Production(object):
    """
    Production eviroment configuration
    """
    DEBUG=False
    TESTING=False
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABSE_URI=os.getenv('DATABSE_URL')


app_config = {
    'Development': Development,
    'Production': Production
}