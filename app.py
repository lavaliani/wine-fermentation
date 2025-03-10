from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("wine_project.db")
    conn.row_factory = sqlite3.Row
    return conn

# 📌 მთავარი გვერდი
@app.route('/')
def home():
    return render_template("index.html")

# 📌 ახალი პროექტის დამატება
@app.route('/new_project', methods=['GET', 'POST'])
def new_project():
    if request.method == 'POST':
        name = request.form['name']
        start_date = request.form['start_date']
        
        conn = get_db_connection()
        conn.execute("INSERT INTO projects (name, start_date) VALUES (?, ?)", (name, start_date))
        conn.commit()
        conn.close()
        
        return redirect(url_for('projects_list'))
    
    return render_template("add_project.html")  # შეცვლილი სახელი

# 📌 ყველა პროექტის სია
@app.route('/projects')
def projects_list():
    conn = get_db_connection()
    projects = conn.execute("SELECT * FROM projects").fetchall()
    conn.close()
    return render_template("projects.html", projects=projects)

# 📌 პროექტის რედაქტირება
@app.route('/edit_project/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    conn = get_db_connection()
    project = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    
    if not project:
        conn.close()
        return "Project not found", 404
    
    if request.method == 'POST':
        name = request.form['name']
        start_date = request.form['start_date']
        conn.execute("UPDATE projects SET name = ?, start_date = ? WHERE id = ?", (name, start_date, project_id))
        conn.commit()
        conn.close()
        return redirect(url_for('projects_list'))
    
    conn.close()
    return render_template("edit_project.html", project=project)

# 📌 პროექტის წაშლა
@app.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('projects_list'))

# 📌 დუღილის მონაცემების დამატება
@app.route('/fermentation/<int:project_id>', methods=['GET', 'POST'])
def fermentation(project_id):
    conn = get_db_connection()
    project = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    
    if not project:
        conn.close()
        return "Project not found", 404
    
    if request.method == 'POST':
        date = request.form['date']
        temperature = request.form['temperature']
        sugar = request.form['sugar']
        acidity = request.form['acidity']
        
        conn.execute("INSERT INTO fermentation (project_id, date, temperature, sugar, acidity) VALUES (?, ?, ?, ?, ?)",
                     (project_id, date, temperature, sugar, acidity))
        conn.commit()
        
    fermentation_data = conn.execute("SELECT * FROM fermentation WHERE project_id = ?", (project_id,)).fetchall()
    conn.close()
    return render_template("fermentation.html", project=project, fermentation_data=fermentation_data)

if __name__ == '__main__':
    app.run(debug=True)