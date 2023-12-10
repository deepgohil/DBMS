import xml.etree.ElementTree as ET
from datetime import date
import random

def generate_dummy_data():
    titles = ["1984", "The Great Gatsby", "Pride and Prejudice", "The Catcher in the Rye", "To Kill a Mockingbird"]
    authors = ["J.D. Salinger", "F. Scott Fitzgerald", "F. Scott Fitzgerald", "J.D. Salinger", "George Orwell"]
    genres = ["Coming of Age", "Science Fiction", "Fiction", "Science Fiction", "Romance"]
    prices = [12.5, 9.99, 10.0, 9.99, 14.95]
    publish_dates = [date(2000 + i, 1, 1) for i in range(10)]

    random_title = random.choice(titles)
    random_author = random.choice(authors)
    random_genre = random.choice(genres)
    random_price = random.choice(prices)
    random_publish_date = random.choice(publish_dates)

    return {
        "title": random_title,
        "author": random_author,
        "genre": random_genre,
        "price": str(random_price),
        "publish_date": str(random_publish_date),
        "description": f"A novel about {random_title} written by {random_author}"
    }

def generate_books(num_books):
    root = ET.Element("books")

    for _ in range(num_books):
        book_data = generate_dummy_data()
        book = ET.SubElement(root, "book")
        for key, value in book_data.items():
            elem = ET.SubElement(book, key)
            elem.text = value

    return root

# Generate 10 sets of dummy data
dummy_data_list = generate_books(10)

# Create an ElementTree object and write the XML to a file
tree = ET.ElementTree(dummy_data_list)
tree.write("dummy_books.xml")
