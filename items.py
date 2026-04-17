import db

def add_item(book_name, writer, review, rating, user_id):
    sql = """INSERT INTO items (book_name, writer, review, rating, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [book_name, writer, review, rating, user_id])

def get_items():
    sql = "SELECT id, book_name, writer FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.book_name,
                    items.writer,
                    items.review,
                    items.rating,
                    users.id user_id,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id AND
                   items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id, book_name, writer, review, rating):
    sql = """UPDATE items SET book_name = ?,
                              writer = ?,
                              review = ?,
                              rating = ?
                          WHERE id = ?"""
    db.execute(sql, [book_name, writer, review, rating, item_id])

def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, book_name, writer
             FROM items
             WHERE book_name LIKE ? OR review LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])