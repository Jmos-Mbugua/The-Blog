import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:7363@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos' 

    
    
class ProductionConfig(Config):
    
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProductionConfig,
    # 'default': DevelopmentConfig
}