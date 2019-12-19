class DefaultConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/toutiao'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    REDIS_IP = '192.168.59.129' #redis 的地址
    REDIS_PORT = 6379  #redis端口

    JWT_SECRET = 'test'

config_dict = {
    'dev': DefaultConfig
}

