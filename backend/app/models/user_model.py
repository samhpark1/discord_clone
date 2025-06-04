from app.tables import User
from app.db import db_manager

class UserModel:
    #Create
    @staticmethod
    def create_user(username, email, avatar, password_hash, created_at):
        session = db_manager.get_sql_session()
        try:
            new_user = User(
                username=username,
                email=email,
                avatar=avatar,
                password_hash=password_hash,
                created_at=created_at
            )

            session.add(new_user)
            session.commit()  # manual commit
            session.refresh(new_user)
            return new_user.username
        except Exception as e:
            session.rollback()
            raise e  # Let Flask handle this in the route
        finally:
            session.close()



