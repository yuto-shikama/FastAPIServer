import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sql.setting import Base,ENGINE

class User(Base):
    __tablename__ = 'oauth2_users'
    id = Column('id', String(20), primary_key = True)
    password = Column('password', String(200))
    name = Column('name', String(200))
    email = Column('email', String(100))
    authority_flg = Column('authority', Integer)
    lock_flg = Column('lock_flg', Integer)
    del_flg = Column('del_flg', Integer)
    created_at = Column('created_at',DateTime, nullable=True)
    updated_at = Column('updated_at_at',DateTime, nullable=True)

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)