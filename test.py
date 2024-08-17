from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://user:password@localhost:5432/mydatabase'

engine = create_engine(DATABASE_URI, pool_pre_ping=True, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Demais configurações de reforço para a segurança podem ser inseridas no código