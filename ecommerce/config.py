import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'mac')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'P0stgr3s')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'fast_api_eco')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'fast_api_eco_test')
