from app.db.fake_db import db

# A real project would use a DB session maker here.
def get_db():
    return db
