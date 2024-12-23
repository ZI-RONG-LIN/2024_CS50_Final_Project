from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gym.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    birthday = db.Column(db.String(150), nullable=False)
    contact = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(150), nullable=False)


class TrainingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    training_date = db.Column(db.String(150), nullable=False)
    training_type = db.Column(db.String(150), nullable=False)
    training_part = db.Column(db.String(150), nullable=False)
    training_load = db.Column(db.String(150), nullable=False)
    training_repetitions = db.Column(db.String(150), nullable=False)
    training_sets = db.Column(db.String(150), nullable=False)

# Routes


@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    members = Member.query.all()
    return render_template('index.html', members=members)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

# Register Page


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check password
        if password != confirm_password:
            flash("Passwords do not match!", 'danger')
            return redirect(url_for('register'))

        # Check username
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists!", 'danger')
            return redirect(url_for('register'))

        # Hash passwords and add new users
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.", 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash("An error occurred. Please try again.", 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/check_username', methods=['POST'])
def check_username():
    username = request.form.get('username')
    # Check if the username exists in the database
    user = User.query.filter_by(username=username).first()
    if user:
        return {"exists": True}, 200  # Return username already exists
    return {"exists": False}, 200  # Return username does not exist


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/member/<int:id>')
def view_member(id):
    member = Member.query.get_or_404(id)
    training_sessions = TrainingSession.query.filter_by(member_id=id).all()
    return render_template('member.html', member=member, training_sessions=training_sessions)


@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        birthday = request.form['birthday']
        gender = request.form['gender']
        contact = request.form['contact']
        member = Member(name=name, birthday=birthday, gender=gender, contact=contact)
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_member.html')


@app.route('/delete_member/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    member = Member.query.get(member_id)
    if member:
        db.session.delete(member)
        db.session.commit()
        flash(f'Member {member.name} deleted successfully!', 'success')
    else:
        flash('Member not found.', 'danger')
    return redirect(url_for('index'))


@app.route('/add_training/<int:member_id>', methods=['GET', 'POST'])
def add_training(member_id):
    member = Member.query.get(member_id)
    if not member:
        flash('Member not found!', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        training_date = request.form['training_date']
        training_type = request.form['training_type']
        training_part = request.form['training_part']
        training_load = request.form['training_load']
        training_repetitions = request.form['training_repetitions']
        training_sets = request.form['training_sets']
        session = TrainingSession(member_id=member_id, training_date=training_date, training_type=training_type, training_part=training_part,
                                  training_load=training_load, training_repetitions=training_repetitions, training_sets=training_sets)
        db.session.add(session)
        db.session.commit()
        return redirect(url_for('view_member', id=member_id))
    return render_template('add_training.html', member_id=member_id)

# Initialize database


def setup():
    with app.app_context():
        # Create all tables
        db.create_all()

        # Check if an administrator account already exists
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                password=generate_password_hash('admin', method='pbkdf2:sha256', salt_length=16)
            )
            db.session.add(admin)
            db.session.commit()


if __name__ == '__main__':
    setup()
    app.run(debug=True)
