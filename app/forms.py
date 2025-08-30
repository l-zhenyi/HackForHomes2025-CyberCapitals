from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Optional
from app.models import User,Document


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    remember_me = BooleanField("Remember Me")


class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=6, message="Password must be at least 6 characters long")
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(),
        EqualTo("password", message="Passwords must match.")
    ])
    submit = SubmitField("Register")

    def validate_email(self, email):
        try:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('This email is already registered. Please use a different email address.')
        except Exception as e:
            print(f"Error in validate_email: {str(e)}")
            # Re-raise a simplified error to avoid exposing internal details
            raise ValidationError('Error checking email. Please try again.')

class UserProfileForm(FlaskForm):
    # User Info
    first_name = StringField("First Name", validators=[Optional()])
    last_name = StringField("Last Name", validators=[Optional()])
    email = StringField("Email", render_kw={"readonly": True})

    # Optional section
    mobile_number = StringField('Mobile Number', validators=[DataRequired(), Length(min=8, max=15)])
    insurance_type = StringField("Insurance Type", validators=[Optional()])
    dob = DateField("Date of Birth", format='%Y-%m-%d', validators=[Optional()])
    address = StringField("Address", validators=[Optional()])
    gender = SelectField("Gender", choices=[("Female", "Female"), ("Male", "Male"), ("Other", "Other")], validators=[Optional()])
    password = PasswordField("New Password", validators=[Optional()])
    confirm_password = PasswordField("Confirm Password", validators=[Optional(), EqualTo("password")])

    # Verification fields (Check Boxes)
    phone_verified = BooleanField("Phone Verification")
    bank_acc_verified = BooleanField("Bank Account Verification")
    gov_id_verified = BooleanField("Government ID Verification")
    emp_study_proof_verified = BooleanField("Employment/Study Proof Verification")
    guarantor_verified = BooleanField("Guarantor Verification")

    # Submit button
    submit = SubmitField("Save Changes")

    @property
    def star_rating(self):
        """
        Calculate the star rating based on the verification fields.
        Each True checkbox increases the rating by 1.
        """
        verified_fields = [
            self.phone_verified.data,
            self.bank_acc_verified.data,
            self.gov_id_verified.data,
            self.emp_study_proof_verified.data,
            self.guarantor_verified.data
        ]
        return sum(1 for field in verified_fields if field)

class DocumentForm(FlaskForm):
    upload_document = FileField(
        'Choose File',
        validators=[
            FileRequired(message="A file is required."),
            FileAllowed(['pdf', 'doc', 'docx', 'txt', 'jpg', 'png','zip'],
                        message="Only PDF, DOC/DOCX, TXT, JPG or PNG allowed.")
        ]
    )
    document_name = StringField("Document Name", validators=[DataRequired()])
    upload_date = DateField("Upload Date", validators=[DataRequired()])
    document_type = StringField("Document Type", validators=[DataRequired()])
    document_notes = TextAreaField('Notes', validators=[Optional()])
    practitioner_name = StringField("Practitioner Name", validators=[DataRequired()])
    expiration_date = DateField("Expiration Date", validators=[Optional()])
    practitioner_type = StringField("Practitioner Type", validators=[DataRequired()])

class RequestPasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password',
                                     validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')