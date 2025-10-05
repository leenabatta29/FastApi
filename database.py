from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:admin%40123@localhost:5432/Leena"
#engine is used to establish a connection to the database specified by the db_url.
engine = create_engine(db_url)
#autocommit=False ensures that changes are not automatically committed to the database after each operation, allowing for explicit transaction control.
#autoFlush=False prevents the session from automatically flushing changes to the database before certain operations, giving more control over when changes are sent to the database.
#bind=engine links the session to the previously created engine, allowing it to communicate with the database.
session = sessionmaker(autocommit = False, autoflush=False, bind=engine)