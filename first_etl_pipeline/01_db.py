import clickhouse_connect
from sqlalchemy import create_engine

DB_USER = "admin"
DB_PASSWORD = "Admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "shop_db"

postgres_connection_string = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
postgres_engine = create_engine(postgres_connection_string)

CH_HOST = "localhost"
CH_PORT = 8123
CH_USER = "admin"
CH_PASSWORD = "Admin123"
CH_DATABASE = "dwh"


def get_clickhouse_client():
  return clickhouse_connect.get_client(
      host=CH_HOST,
      port=CH_PORT,
      username=CH_USER,
      password=CH_PASSWORD,
      database=CH_DATABASE,
  )