# Book Catalogue App 📚

Hi! I'm **Shreejana Ghalan Lama**, and this is my final project for **IS211**, taught by **Professor Alain Ledon** at Baruch College.

This project was a great way for me to put together everything we’ve learned this semester — from Flask and routing, to using APIs and building interactive web apps. I chose to create a **Book Catalogue Application** where users can log in, search for books by ISBN, and save their collection.

---

## Features

- User login
- Search for books using the Google Books API
- Save book details to a personal list (title, author, pages, rating, thumbnail)
- View and delete saved books

---

## Extra Credit Features

- Multi-user login system (simple username + password)
- Book thumbnail images displayed
- Session-based user authentication

---

## How to Run the App

To run this app on your computer:

1. Make sure you have Python installed.
2. Open your terminal or command prompt and navigate to the project folder.
3. Install the required packages by running:
   ```bash
   pip install -r requirements.txt

4. Run the Flask App:
    ```bash
   python app.py

5. Once it's running, go to your browser and open:  
`http://127.0.0.1:5000`

6. Use the following test credentials to log in:
- Username: `testuser`
- Password: `testpass`

Once you're logged in, you can search for books by ISBN, save them, and see your personal list.

## Project Structure

Here's a simple breakdown of the main files and folders in this project:

- `app.py` – Main Flask application with all the routes and logic
- `models.py` – Database models for users and books
- `forms.py` – Login form using Flask-WTF
- `templates/` – Folder for HTML files (`login.html` and `dashboard.html`)
- `books.db` – SQLite database file (created automatically)
- `requirements.txt` – File with the list of packages needed to run the app
- `README.md` – This file

## Notes

Right now, the passwords are stored in plain text just to keep the project simple. In a real application, I would definitely use password hashing and proper security practices.

## Final Thoughts

This project helped me apply what I’ve learned in class and really showed me how everything connects in a real web application — from Flask routes to databases and using external APIs. I’m happy with how it turned out, and it gave me a lot more confidence with backend development.

Thank you, Professor Ledon, for all your guidance this semester.

— Shreejana Ghalan Lama
"""