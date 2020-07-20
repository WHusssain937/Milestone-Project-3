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


# MyBooks Section
@app.route('/')
@app.route('/my_books')
def my_books():
    return render_template("my-books.html", books=mongo.db.books.find())

@app.route('/add_books')
def add_books():
    books = mongo.db.books
    return render_template("add-books.html", books=books.find())

@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('my_books'))

# Wishlist Section
@app.route('/wishlist')
def wishlist():
    return render_template("wishlist.html", 
                            purchases=mongo.db.purchases.find())


@app.route('/add_to_wishlist')
def add_to_wishlist():
    purchases = mongo.db.purchases
    return render_template("add-to-wishlist.html", purchases=purchases.find())

@app.route('/insert_to_wishlist', methods=['POST'])
def insert_to_wishlist():
    purchases = mongo.db.purchases
    purchases.insert_one(request.form.to_dict())
    return redirect(url_for('wishlist'))

# MyBooks Functions for editing and deleting
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
        'year_of_release':request.form.get('year_of_release'),
        'genre':request.form.get('genre'),
        'book_review':request.form.get('book_review'),
        'rating':request.form.get('book.rating')
    })
    return redirect(url_for('my_books'))

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('my_books'))
  
# Wishlist Functions for editing and deleting
@app.route('/edit_wishlist_entry/<purchase_id>')
def edit_wishlist_entry(purchase_id):
    to_purchase = mongo.db.purchases.find_one({'_id': ObjectId(purchase_id)})
    return render_template("edit-wishlist-entry.html", purchase=to_purchase)    

@app.route('/update_to_wishlist/<purchase_id>', methods=['POST'])
def update_to_wishlist(purchase_id):
    purchases = mongo.db.purchases
    purchases.update( {'_id': ObjectId(purchase_id)},
    {
        'purchase_title':request.form.get('purchase_title'),
        'name_of_author':request.form.get('name_of_author'),
        'release_year': request.form.get('release_year'),
        'purchase_genre': request.form.get('purchase_genre'),
        'why_buy':request.form.get('why_buy'),
        'purchase_link':request.form.get('purchase_link')
    })
    return redirect(url_for('wishlist'))  

@app.route('/delete_wishlist_entry/<purchase_id>')
def delete_wishlist_entry(purchase_id):
    mongo.db.purchases.remove({'_id': ObjectId(purchase_id)})
    return redirect(url_for('wishlist'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)