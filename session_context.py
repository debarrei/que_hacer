from models import db
from contextlib import contextmanager
from sqlalchemy.exc import IntegrityError

@contextmanager
def transactional_session():
    session = db.session
    try:
        yield session
        session.commit()
    except IntegrityError:
        session.rollback()
        raise
    finally:
        session.close()