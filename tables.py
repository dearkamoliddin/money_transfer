from connect_db import Database


def create_tables():
    users = """
    CREATE TABLE if not exists users(
        user_id SERIAL PRIMARY KEY,
        full_name VARCHAR(30),
        card_number VARCHAR(16),
        phone_number VARCHAR(9),
        password VARCHAR(4),
        balance NUMERIC,
        created_date TIMESTAMP DEFAULT now());
    """

    transactions = """
    CREATE TABLE if not exists transactions(
        transaction_id SERIAL PRIMARY KEY,
        from_user_id INT REFERENCES users(user_id),
        to_user_id INT REFERENCES users(user_id),
        money NUMERIC,
        status BOOLEAN,
        created_date TIMESTAMP DEFAULT now());
    """

    print(Database.connect(users, "create"))
    print(Database.connect(transactions, "create"))


if __name__ == "__main__":
    create_tables()
