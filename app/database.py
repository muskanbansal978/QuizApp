from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#The Url structure is 'postgresql://username:password@db:5432/DatabaseName'. 
#Here, db is the hostname, matching the service name defined in your Compose file.

URL_DATABASE = 'postgresql://postgres:root@db:5432/QuizApp'

''' Creates a database engine that connects to the specified database URL
This engine manages connections and handles communication with the database '''

engine = create_engine(URL_DATABASE)


''' Creates a new session for database interactions
autocommit=False: Prevents automatic commit transactions
autoflush=False: Prevents automatic flush of changes to the DB
bind=engine: Associates sessions with the specified database engine '''

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

''' Creates a base class for all ORM models to inherit from
This base class provides the metadata and mappings for model classes '''

Base = declarative_base()

