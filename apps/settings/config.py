class DefaultConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.59.129:3306/toutiao'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    REDIS_IP = '192.168.59.129' #redis 的地址
    REDIS_PORT = 6379  #redis端口

    JWT_SECRET = 'test'

config_dict = {
    'dev': DefaultConfig
}

