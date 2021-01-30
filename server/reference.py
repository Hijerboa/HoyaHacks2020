from objects import Mention
from database_connection import create_session

#create database session
database_session = create_session()

#create initial object
new_Mention = Mention()

#add shit here
new_Mention.id = 1234

#add object to database session
database_session.add(new_Mention)
#commit session
database_session.commit()