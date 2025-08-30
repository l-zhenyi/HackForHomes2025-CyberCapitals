from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin 
 
@login.user_loader 
def load_user(id): 
    return User.query.get(int(id)) 

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Core user fields
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    family_name = db.Column(db.String(64))
    given_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False) #CHANGE

    # Account type: 1 = Tenant, 2 = Landlord
    acc_type = db.Column(db.Integer, nullable=False)

    # Tenant verification fields (nullable if landlord)
    phone_verified = db.Column(db.Boolean, default=False)
    bank_acc_verified = db.Column(db.Boolean, default=False)
    gov_id_verified = db.Column(db.Boolean, default=False)
    emp_study_proof_verified = db.Column(db.Boolean, default=False)
    guarantor_verified = db.Column(db.Boolean, default=False)

    @property
    def star_rating(self):
        """
        Calculate tenant star rating from verification fields.
        Landlords get None by default.
        """
        if self.acc_type != 1:  # Not a tenant
            return None

        checks = [
            self.phone_verified,
            self.bank_acc_verified,
            self.gov_id_verified,
            self.emp_study_proof_verified,
            self.guarantor_verified
        ]
        return sum(1 for check in checks if check)  # count how many are True
    
    def set_password(self, password): 
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username} ({'Tenant' if self.acc_type == 1 else 'Landlord'})>"
