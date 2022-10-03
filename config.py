# config.py

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    #DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

customhost = "employee.camaffquqobs.us-east-1.rds.amazonaws.com"
customuser = "aws_user"
custompass = "Bait3273"
customdb = "employee"
custombucket = "yeejangjue-employee"
customregion = "us-east-1"