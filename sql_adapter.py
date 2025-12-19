import pyodbc
import os
import logging

class SQLAdapter:
  def __init__(self):
    conn_str = (
      f"ODBC_DRIVER = {{ ODBC Driver 17 }};"
      f"DATABASE_SERVER = {{ str(os.getenv("server")) }};"
      f"DATABASE_NAME = {{ str(os.getenv("database")) }};"
      f"DATABASE_USER = {{ str(os.getenv("uid")) }};"
      f"DATABASE_PWD = {{ str(os.getenv("pwd")) }};"
    )

def query(self, sql: str, params: tuple = ()) :
  cursor = self.conn.cursor()
  logger.debug(f" info {sql} {params} ")
  cursor.execute(sql, params)
  columns = [col[0] for col in cursor.description]
  results = [dict(zip(columns, row)) for row in cursor.fetchall()]
  cursor.close()
  return results
  
