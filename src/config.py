from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')
    DAYS_EXP=config('DAYS_EXP')
    DOMINIO=config('DOMINIO')

class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False

config= {
    'development': DevelopmentConfig,
    'production' : ProductionConfig
}