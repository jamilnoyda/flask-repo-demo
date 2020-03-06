from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
from flask import render_template, flash, redirect, url_for


from routes import *

from flask import render_template
from flask import request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy import (
    Boolean,
    CHAR,
    CheckConstraint,
    Column,
    DECIMAL,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    Table,
    Text,
)
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


db = SQLAlchemy()
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)


class AccountsUser(db.Model):
    __tablename__ = "accounts_user"

    id = Column(Integer, primary_key=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime)
    is_superuser = Column(Boolean, nullable=False)
    email = Column(String(40), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_staff = Column(Boolean, nullable=False)
    date_joined = Column(DateTime, nullable=False)
    bio = Column(Text)


class AuthGroup(db.Model):
    __tablename__ = "auth_group"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)


t_sqlite_sequence = Table(
    "sqlite_sequence", metadata, Column("name", NullType), Column("seq", NullType)
)


class AccountsProfile(db.Model):
    __tablename__ = "accounts_profile"

    id = Column(Integer, primary_key=True)
    birth_date = Column(Date)
    gender = Column(String(1), nullable=False)
    phone_number = Column(String(17), nullable=False)
    user_id = Column(ForeignKey("accounts_user.id"), nullable=False)
    full_name = Column(String(17), nullable=False)

    user = relationship("AccountsUser")


class AccountsUserGroup(db.Model):
    __tablename__ = "accounts_user_groups"
    __table_args__ = (
        Index(
            "accounts_user_groups_user_id_group_id_59c0b32f_uniq",
            "user_id",
            "group_id",
            unique=True,
        ),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("accounts_user.id"), nullable=False, index=True)
    group_id = Column(ForeignKey("auth_group.id"), nullable=False, index=True)

    group = relationship("AuthGroup")
    user = relationship("AccountsUser")


class AuthPermission(db.Model):
    __tablename__ = "auth_permission"
    __table_args__ = (
        Index(
            "auth_permission_content_type_id_codename_01ab375a_uniq",
            "content_type_id",
            "codename",
            unique=True,
        ),
    )

    id = Column(Integer, primary_key=True)
    content_type_id = Column(
        ForeignKey("flask_content_type.id"), nullable=False, index=True
    )
    codename = Column(String(100), nullable=False)
    name = Column(String(255), nullable=False)

    content_type = relationship("FlaskContentType")


class FlaskContentType(db.Model):
    __tablename__ = "flask_content_type"
    __table_args__ = (
        Index(
            "flask_content_type_app_label_model_76bd3d3b_uniq",
            "app_label",
            "model",
            unique=True,
        ),
    )

    id = Column(Integer, primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class AccountsUserUserPermission(db.Model):
    __tablename__ = "accounts_user_user_permissions"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("accounts_user.id"), nullable=False, index=True)
    permission_id = Column(ForeignKey("auth_permission.id"), nullable=False, index=True)

    permission = relationship("AuthPermission")
    user = relationship("AccountsUser")


class AuthGroupPermission(db.Model):
    __tablename__ = "auth_group_permissions"

    id = Column(Integer, primary_key=True)
    group_id = Column(ForeignKey("auth_group.id"), nullable=False, index=True)
    permission_id = Column(ForeignKey("auth_permission.id"), nullable=False, index=True)

    group = relationship("AuthGroup")
    permission = relationship("AuthPermission")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = UserForm()
    print("request", request)
    # if form.validate_on_submit():

    #     return redirect(url_for('index'))
    user = AccountsUser()
    db.session.add(user)
    db.session.commit()

    return render_template("login.html", title="Sign In", form=form)


@app.route("/users/list/", methods=["GET", "POST"])
def users_list():
    # users = AccountsUser.query.all()
    users = db.session.query(AccountsUser).all()
    return render_template("users_list.html", title="user list", users=users)


@app.route("/")
def hello_world():
    return render_template(
        "index.html",
        title="Sign In",
        # form=form
    )

