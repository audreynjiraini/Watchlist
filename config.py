import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    
    # SECRET_KEY = os.environ.get('\xec\xa0K\xf1\xce<b\xacP\xfc\x84xQ"\xde\x9e\x0f\xd5G\xab\xf9\xfc7s')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}