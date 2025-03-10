import sqlite3

# მონაცემთა ბაზის შექმნა (თუ არ არსებობს)
conn = sqlite3.connect("wine_project.db")
cursor = conn.cursor()

# 📌 ცხრილი პროექტებისთვის
cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL
)
""")

# 📌 ცხრილი საწყისი მონაცემებისთვის
cursor.execute("""
CREATE TABLE IF NOT EXISTS initial_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    grape_type TEXT NOT NULL,
    sugar FLOAT NOT NULL,
    brix FLOAT NOT NULL,
    ph FLOAT NOT NULL,
    acidity FLOAT NOT NULL,
    harvest_date TEXT NOT NULL,
    wine_style TEXT NOT NULL,
    wine_type TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
)
""")

# 📌 ცხრილი დუღილის მონიტორინგისთვის
cursor.execute("""
CREATE TABLE IF NOT EXISTS fermentation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    temperature FLOAT NOT NULL,
    residual_sugar FLOAT NOT NULL,
    acidity FLOAT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
)
""")

# ცვლილებების შენახვა
conn.commit()
conn.close()

print("✅ მონაცემთა ბაზა წარმატებით შეიქმნა!")
