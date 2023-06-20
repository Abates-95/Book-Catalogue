# Import necessary modules
from flask import Blueprint, request, jsonify, render_template

#  Import the token_required decorator and database models
from helpers import token_required
from models import db, User, Book, Book_schema, Books_schema

# Create a blueprint named 'api' with url prefix '/api'
api= Blueprint("api", __name__, url_prefix='/api')

# Route for creating a book with POST request and token_required decorator
@api.route('/books', methods = ['POST'])
@token_required
def create_Book(current_book_token):
    # Retrieve book data from the requested object
    year_published = request.json['year_published']
    title = request.json['title']
    genre = request.json['genre']
    author = request.json['author']
    ISBN = request.json['ISBN']
    page_count = request.json['page_count']
    availability = request.json['availability']
    book_token = current_book_token.token

    print(f'You are here things are working a book has been added: {current_book_token.token}')

    # Create a new book object with retrieved data
    book = Book(year_published, title, genre, author, ISBN, page_count, availability, book_token = book_token )

    # Add book to database and commit changes
    db.session.add(book)
    db.session.commit()

    # Serialize book object and return it as JSON response
    response = Book_schema.dump(book)
    return jsonify(response)

# Route for getting a list of books with GET request and token_required decorator
@api.route('/books', methods = ['GET'])
@token_required
def get_book(current_book_token):
    # Retrieve book token from current_user object
    a_book = current_book_token.token

    # Query database for all books with specified book token and serialize them
    books = Book.query.filter_by(book_token = a_book).all()
    response = Books_schema.dump(books)

    # Return serialized book as JSON repsonse
    return jsonify(response)

# Route for getting a single book with GET request and token_required decorator
@api.route('/books/<id>', methods = ['GET'])
@token_required
def get_single_book(current_book_token, id):
    # Query database for a book with specific ID and serialize it
    book = Book.query.get(id)
    response = Book_schema.dump(book)

    # Return serialized book as JSON response
    return jsonify(response)

# Route for updating a book using POST/PUT request and token_required decorator
@api.route('/books/<id>', methods = ['POST', 'PUT'])
@token_required
def update_book(current_book_token, id):
    # Query database for a book with specific ID
    book = Book.query.get(id)
    # Update book data with retrieved data from request object
    fields_to_update = request.json.keys()

    for field in fields_to_update:
        if hasattr(book, field):
            setattr(book, field, request.json[field])
            book.book_token = current_book_token.token

    # Commit changes to database
    db.session.commit()
    
    # Serialize updated book object and return as JSON response
    response = Book_schema.dump(book)
    return jsonify(response)

# Route for deleting a book with DELETE request and token_required decorator
@api.route('/books/<id>', methods = ['DELETE'])
@token_required
def delete_book(current_book_token, id):
    # Query database for a book with a specified ID and delte it
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    # Serialize deleted book object and return it as JSON response
    response = Book_schema.dump(book)
    return jsonify(response)