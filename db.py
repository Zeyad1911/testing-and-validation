import sqlite3

DATABASE_PATH = 'user_db.db' 

class db:
  def connectdb():
      conn = sqlite3.connect(DATABASE_PATH)
      return conn
