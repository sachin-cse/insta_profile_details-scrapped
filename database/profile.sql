CREATE TABLE IF NOT EXISTS user_details(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    User_Id INTEGER,
    Profile_Image TEXT,
    Followers INTEGER,
    Following INTEGER,
    Bio TEXT
);