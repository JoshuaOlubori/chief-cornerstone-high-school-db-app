from . import login_manager, db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    # @staticmethod
    # def reset_password(self, new_password):
    #     self.password = generate_password_hash(new_password)
    #     db.session.commit()
    
    # @staticmethod
    # def reset_password(self,new_password):
    #     user.password = new_password
    #     db.session.add(user)
    #     return True
    
#

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))