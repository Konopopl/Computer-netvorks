import sqlalchemy
from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
#engine = create_engine("sqlite:///:memory:")
#engine = create_engine("mysql://log:pass@localhost/foo")
engine = create_engine("postgresql://postgres:postgres@localhost:5432")
metadata = MetaData()
metadata.drop_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
insp = inspect(engine)
print(insp.get_table_names())
file = open("088d7db8b2b6401e8d7db8b2b6b01e85_all.sql", "r")
escaped_sql = sqlalchemy.text(file.read().replace("\":", "\": ").replace("(order ","(\"order\" ").replace("(from ","(\"from\" ").replace("(to ", "(\"to\" "))
session.execute(escaped_sql)
session.commit()

#sql_file = open('file.sql','r')

# Create an empty command string
#sql_command = ''

# Iterate over all lines in the sql file
#i = 0
#for line in file:
#    # Ignore commented lines
#    if not line.startswith('--') and line.strip('\n'):
#        # Append line to the command string
#        sql_command += line.strip('\n')

        # If the command string ends with ';', it is a full statement
#        if sql_command.endswith(';'):

#                session.execute(text(sql_command.replace("\":", "\": ").replace("(order ","(\"order\" ").replace("(from ","(\"from\" ").replace("(to ", "(\"to\" ")))
#                session.commit()
#                if i % 100 == 0:
#                  print(i)
#                i += 1

#                sql_command = ''