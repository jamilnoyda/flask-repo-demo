# coding: utf-8
from sqlalchemy import Boolean, CHAR, CheckConstraint, Column, DECIMAL, Date, DateTime, ForeignKey, Index, Integer, String, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AccountsUser(Base):
    __tablename__ = 'accounts_user'

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


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)



t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class AccountsProfile(Base):
    __tablename__ = 'accounts_profile'

    id = Column(Integer, primary_key=True)
    birth_date = Column(Date)
    gender = Column(String(1), nullable=False)
    phone_number = Column(String(17), nullable=False)
    user_id = Column(ForeignKey('accounts_user.id'), nullable=False)
    full_name = Column(String(17), nullable=False)

    user = relationship('AccountsUser')


class AccountsUserGroup(Base):
    __tablename__ = 'accounts_user_groups'
    __table_args__ = (
        Index('accounts_user_groups_user_id_group_id_59c0b32f_uniq', 'user_id', 'group_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('accounts_user.id'), nullable=False, index=True)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    user = relationship('AccountsUser')


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        Index('auth_permission_content_type_id_codename_01ab375a_uniq', 'content_type_id', 'codename', unique=True),
    )

    id = Column(Integer, primary_key=True)
    content_type_id = Column(ForeignKey('flask_content_type.id'), nullable=False, index=True)
    codename = Column(String(100), nullable=False)
    name = Column(String(255), nullable=False)

    content_type = relationship('FlaskContentType')



class FlaskContentType(Base):
    __tablename__ = 'flask_content_type'
    __table_args__ = (
        Index('flask_content_type_app_label_model_76bd3d3b_uniq', 'app_label', 'model', unique=True),
    )

    id = Column(Integer, primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)






class AccountsUserUserPermission(Base):
    __tablename__ = 'accounts_user_user_permissions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('accounts_user.id'), nullable=False, index=True)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    permission = relationship('AuthPermission')
    user = relationship('AccountsUser')


class AuthGroupPermission(Base):
    __tablename__ = 'auth_group_permissions'
    

    id = Column(Integer, primary_key=True)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False, index=True)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    permission = relationship('AuthPermission')







