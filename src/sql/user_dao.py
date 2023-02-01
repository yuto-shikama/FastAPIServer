from sql.setting import session
import datetime

# Userモデルの取得
from sql.user_model import User

def selectAll():
    return session.query(User).all()

def selectId(id: str):
    return session.query(User).filter(User.id == id).all()

def insertUser(id: str, password: str, name: str, email: str, authority_flg: int, lock_flg: int, del_flg: int):
    user = User()
    user.id = id
    user.password = password
    user.name = name
    user.email = email
    user.authority_flg = authority_flg
    user.lock_flg = lock_flg
    user.del_flg = del_flg

    ut = datetime.datetime.now()
    user.created_at = ut
    user.updated_at = ut

    session.add(user)
    session.commit()

def updatePassword(password: str):
    user = session.query(User).filter(User.id == id).all()
    user.password = password
    session.commit()

def deleteUser(id: str):
    session.query(User).filter(User.id == id).delete()
    session.commit()
