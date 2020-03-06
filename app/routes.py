from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = UserForm()
#     print("request", request)
#     # if form.validate_on_submit():

#     #     return redirect(url_for('index'))
#     user = AccountsUser()
#     db.session.add(user)
#     db.session.commit()

#     return render_template("login.html", title="Sign In", form=form)


# @app.route("/users/list/", methods=["GET", "POST"])
# def users_list():
#     # users = AccountsUser.query.all()
#     users = db.session.query(AccountsUser).all()
#     return render_template("users_list.html", title="user list", users=users)


# @app.route("/")
# def hello_world():
#     return render_template(
#         "index.html",
#         title="Sign In",
#         # form=form
#     )

