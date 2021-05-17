-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1234 That Street, Tucson, AZ 85708');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Book 1', 'The First Author', 'This is the first book');

INSERT INTO book(book_name, author, details)
    VALUES('Book number 2', 'The Second Author', 'This is the book number 2');

INSERT INTO book(book_name, author, details)
    VALUES('Wow Book 3', 'Author Of The Third ', 'We are now 3 books in');

INSERT INTO book(book_name, author)
    VALUES('I Cannot Believe This Is Book 4', '4th Author');

INSERT INTO book(book_name, author)
    VALUES('Book 5', 'Author 5');

INSERT INTO book(book_name, author)
    VALUES('This is book number 6 ', '6th Author');

INSERT INTO book(book_name, author)
    VALUES('Book number 7 is pretty great', 'Author of the 7th');

INSERT INTO book(book_name, author)
    VALUES('Book 8: The Series Is Almost Complete', 'Author 8');

INSERT INTO book(book_name, author)
    VALUES('Book 9: Series Complete', 'Final Boss');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Zachary', 'Hunn');

INSERT INTO user(first_name, last_name)
    VALUES('Zayden', 'Hunn');

INSERT INTO user(first_name, last_name)
    VALUES('Zamir', 'Hunn');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Zachary'), 
        (SELECT book_id FROM book WHERE book_name = 'Book 1')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Zayden'),
        (SELECT book_id FROM book WHERE book_name = 'Wow Book 3')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Zamir'),
        (SELECT book_id FROM book WHERE book_name = 'Book 9: Series Complete')
    );