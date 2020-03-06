from wtforms.ext.sqlalchemy.orm import model_form
from flask_wtf import Form


from models import AccountsUser

UserForm = model_form(AccountsUser,)


# class UserForm(ModelForm):
#     class Meta:
#         model = AccountsUser
#         # exclude = ['']
