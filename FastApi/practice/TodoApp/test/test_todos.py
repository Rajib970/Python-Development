from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from ..database import Base, SesionLocal

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread" : False},
    poolclass = StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = SesionLocal()
    try:
        yeild db 
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db        
            