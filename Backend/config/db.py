from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
=======
SQLALCHEMY_DATABASES_URL= "mysql+pymysql://root:1234@localhost:3307/test"
engine = create_engine(SQLALCHEMY_DATABASES_URL)
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base= declarative_base()
>>>>>>> 18a0686ba9476220cf5ad14205bf2efe0c4c7c3c
