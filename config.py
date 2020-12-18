import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = 'database-west.database.windows.net'
    SQL_DATABASE = 'database-west'
    SQL_USER_NAME = 'csadmin'
    SQL_PASSWORD = 'hueUDA(2020)'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = 'cshelloworldstorage'
    BLOB_STORAGE_KEY = 'rKjteVETUBiCYd6pLJpNQxzAE3FVTFU06mMplCMri4U2RIyPI4uYRTrWW4/jx7vrRJjW05KWmQTtp4slmaELtQ=='
    BLOB_CONTAINER = 'images'
