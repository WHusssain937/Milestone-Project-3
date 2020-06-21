import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

if path.exists('env.py'):
    import env

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')

mongo = PyMongo(app)


@app.route('/')
@app.route('/my_books')
def my_books():
    return render_template("my-books.html", books=mongo.db.books.find())

@app.route('/add_books')
def add_books():
    return render_template("add-books.html", books=mongo.db.books.find())

@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('my_books'))

@app.route('/books_to_purchase')
def books_to_purchase():
    return render_template("books-to-purchase.html", purchases=mongo.db.purchases.find())

@app.route('/add_to_purchase')
def add_to_purchase():
    return render_template("add-to-purchase.html", purchases=mongo.db.purchases.find())

@app.route('/insert_to_purchase', methods=['POST'])
def insert_to_purchase():
    purchases = mongo.db.purchases
    purchases.insert_one(request.form.to_dict())
    return redirect(url_for('books_to_purchase'))

@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({'_id': ObjectId(book_id)})
    return render_template("edit-book.html", book=the_book)

@app.route('/update_book/<book_id>', methods=['POST'])
def update_book(book_id):
    books = mongo.db.books
    books.update( {'_id': ObjectId(book_id)},
    {
        'book_title':request.form.get('book_title'),
        'author':request.form.get('author'),
        'year_of_release': request.form.get('year_of_release'),
        'genre': request.form.get('genre'),
        'book_review':request.form.get('book_review')
    })
    return redirect(url_for('my_books'))

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('my_books'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)