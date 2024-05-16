import sqlite3

DATABASE_PATH = 'user_db.db'  # Replace with your actual database path

class db:
  def connectdb():
      conn = sqlite3.connect(DATABASE_PATH)
      return conn
