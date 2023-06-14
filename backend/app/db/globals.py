import os
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASS = os.environ.get("MYSQL_PASS")

DATABASE_URL= f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@mysqldb:3306/{DB_NAME}"