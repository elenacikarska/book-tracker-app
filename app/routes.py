from flask import Blueprint, render_template, request, redirect, url_for
from .models import Book
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@main.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        status = request.form['status']
        new_book = Book(title=title, author=author, status=status)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add.html')


@main.route('/delete/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('main.index'))
