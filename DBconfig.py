import mysql.connector
from sqlalchemy import MetaData, Table, String, Column, Text

metadata = MetaData()

members_info = Table('members_info', metadata,
        Column('user_id', Integer(), primary_key=True, unique=True, autoincrement=True),

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = '',
    database = 'first_ecwa_db'
)
