from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Reviewer
import os
from os.path import expanduser
from flask import jsonify, render_template, request, redirect, session, flash,\
    url_for
from werkzeug.utils import secure_filename
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse


# upload_path = os.path.join(expanduser('~'), 'Desktop', 'Uploads', 'img')

# Construct the upload path relative to the app folder
upload_path = os.path.join('static', 'uploads')

# Create the directories if the don't exist
os.makedirs(upload_path, exist_ok=True)
print(upload_path)

app.config["UPLOADS"] = upload_path
app.config["ALLOWED_FILE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF", "jpg"]
# Define a secret key to enable session
# app.secret_key = os.environ.get("APP_SECRET_KEY", "default_secret_key")


# Custom decorator  to restict route to authenticated users only
def user_login_required(view_function):
    """Only authencicated users not reviwers"""
    def wrapper(*args, **kwargs):
        """wrapper function"""
        if current_user.is_authenticated and not current_user.is_reviewer:
            return view_func(*args, **kwargs)
        else:
            # Redirect to login page
            return redirect(url_for('login'))
    return wrapper


# Custom decorator  to restict route to authenticated reviwers only
def reviewer_login_required(view_function):
    """Only authencicated reviewers not users"""
    def wrapper(*args, **kwargs):
        """wrapper function"""
        if current_user.is_authenticated and current_user.is_reviewer:
            return view_func(*args, **kwargs)
        else:
            # Redirect to login page
            return redirect(url_for('login'))
    return wrapper


@app.route("/", strict_slashes=False)
@app.route('/index', strict_slashes=False)
@login_required
def index():
    """Index route"""
    return render_template('upload.html')


@app.route('/api/users', strict_slashes=False)
def all_users():
    """Returns all users in json format"""
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return jsonify(users_data)


@app.route('/api/reviewers', strict_slashes=False)
def all_reviewers():
    """Returns all Reviewers in json format"""
    reviewers = Reviewer.query.all()
    reviewers_data = [reviewer.to_dict() for reviewer in reviewers]
    return jsonify(reviewers_data)


@app.route('/api/users/<int:id>')
def user(id):
    """Returns one user when id is passed"""
    user = User.query.get(id)
    return jsonify(user.to_dict())


@app.route('/api/users', methods=['POST'])
def create_user():
    """Creates a User"""
    # Get data from request
    data = request.get_json()
    # Store data in db
    user = User()

    user.from_dict(data)

    db.session.add(user)
    db.session.commit()

    response = jsonify(user.to_dict())
    response.status_code = 201

    return response


def allowed_file(filename):
    """check if the file extension is allowed"""

    if "." not in filename:
        return False

    exten = filename.rsplit(".", 1)[1]

    if exten.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route("/", strict_slashes=False, methods=["GET", "POST"])
def upload_file():
    """defines upload file route"""
    if request.method == "POST":
        if request.files:
            f = request.files["uploaded-file"]
            if f.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config["UPLOADS"], filename))
                image_path = os.path.join(app.config["UPLOADS"], filename)
                # store image_path in session
                session["image_path"] = image_path
                print("File saved")
                return render_template('upload2.html')
            else:
                print("File exetension is not allowed")
                return redirect(request.url)
    return render_template('upload.html')


@app.route("/image_display", strict_slashes=False)
def show_image():
    """Displays the uploaded Image"""
    # Retrive image_path from session
    image_path = session.get("image_path")
    print(image_path)
    if image_path:
        return render_template('image_diplay.html', user_image=image_path)
    else:
        return "Image not found"


@app.route("/first_review", strict_slashes=False)
def first_review():
    """Displays the image and review form"""
    # Retrive image_path from session
    image_path = session.get("image_path")
    if image_path:
        return render_template('first_review.html', user_image=image_path)
    else:
        return "Image not found"


@app.route("/second_review", strict_slashes=False)
def second_review():
    """Displays the image and review form"""
    # Retrive image_path from session
    image_path = session.get("image_path")
    if image_path:
        return render_template('second_review.html', user_image=image_path)
    else:
        return "Image not found"


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login Users/Reviewers"""
    user_type = request.form.get('user_type')
    if user_type == 'user':
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data)\
                .first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    elif user_type == 'reviewer':
        if current_user.is_authenticated:
            return redirect(url_for('image_display'))
        form = LoginForm()
        if form.validate_on_submit():
            reviewer = Reviewer.query.filter_by(username=form.username
                                                .data).first()
            if reviewer is None or not \
                    reviewer.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(reviewer, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    # if it's a GET request or login fails, render the login form template
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout', strict_slashes=False)
def logout():
    """Logout Users"""
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registrations for users/reviwers"""
    user_type = request.form.get('user_type')
    if user_type == 'user':
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        registration_form = RegistrationForm()
        if registration_form.validate_on_submit():
            user = User(username=registration_form.username.data,
                        name=registration_form.name.data,
                        email=registration_form.email.data)
            user.set_password(registration_form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, your registered')
            return redirect(url_for('login'))
    if user_type == 'reviewer':
        if current_user.is_authenticated:
            return redirect(url_for('image_display'))
        registration_form = RegistrationForm()
        if registration_form.validate_on_submit():
            reviewer = Reviewer(username=registration_form.username.data,
                                name=registration_form.name.data,
                                email=registration_form.email.data)
            reviewer.set_password(registration_form.password.data)
            db.session.add(reviewer)
            db.session.commit()
            flash('Congratulations, your registered')
            return redirect(url_for('login'))
    registration_form = RegistrationForm()
    return render_template('register.html', title='Register',
                           form=registration_form)
