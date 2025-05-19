# Importing required modules from Flask and our own files
from flask import Flask, render_template, redirect, url_for, session, request
from models import db, User, Book
from forms import LoginForm

# Setting up the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'  # Used for sessions and form security
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Just disables a warning

# Initializing the database with the app
db.init_app(app)

# Function to create tables and add a default test user
def init_db():
    with app.app_context():
        db.create_all()
        # Add a test user if it doesn't exist
        if not User.query.filter_by(username="testuser").first():
            test_user = User(username="testuser", password="testpass")
            db.session.add(test_user)
            db.session.commit()

# Call the init_db function to prepare the database
init_db()

# ---------------- ROUTES ------------------

# Route for login page (also handles login form)
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check if user exists with correct credentials
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
            session['user_id'] = user.id  # Save user's ID in session
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password"
    return render_template('login.html', form=form)

# Dashboard page after login, shows saved books
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # Get books saved by the current user
    user_books = Book.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', books=user_books)

# ---------------- SEARCH BOOK ------------------

# To make HTTP requests
import requests
from flask import flash  # Used for temporary messages

# Route to handle ISBN form submission and book search
@app.route('/search', methods=['POST'])
def search_book():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    isbn = request.form.get('isbn')
    user_id = session['user_id']

    # Call the Google Books API with the provided ISBN
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()

    try:
        # Try to get book info from the API response
        item = data['items'][0]['volumeInfo']
        title = item.get('title', 'No title')
        authors = ", ".join(item.get('authors', ['Unknown']))
        page_count = item.get('pageCount', 0)
        rating = item.get('averageRating', 0)
        thumbnail = item.get('imageLinks', {}).get('thumbnail', '')

        # Save the book to the database
        book = Book(title=title, author=authors, page_count=page_count,
                    average_rating=rating, thumbnail=thumbnail, user_id=user_id)
        db.session.add(book)
        db.session.commit()
        flash("Book added successfully!")
    except Exception as e:
        flash("Book not found or invalid ISBN.")

    return redirect(url_for('dashboard'))

# ---------------- LOGOUT ------------------

# Logs the user out by clearing the session
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ---------------- DELETE BOOK ------------------

# Route to delete a book by its ID (POST only)
@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    # Make sure the user owns the book before deleting
    if book.user_id != session.get('user_id'):
        return "Unauthorized", 403
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('dashboard'))

# ---------------- RUN APP ------------------

# Run the app in debug mode (helpful during development)
if __name__ == '__main__':
    app.run(debug=True)
