import sqlite3 

db_name = "tasks.db"

def init_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS tasks(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL, 
                        is_complete INTEGER DEFAULT 0
                   )
                   ''')
    conn.commit() 
    conn.close() 


def get_db_connection():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn    


def add_task(data):
    conn = get_db_connection()
    cursor = conn.cursor() 
    cursor.execute('''
                        INSERT INTO tasks(description) VALUES (?)
                        ''', (data,))
    conn.commit()
    conn.close()
    
def fetch_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall() 
    conn.close()
    return tasks


def delete_task(task_id): 
    conn = get_db_connection() 
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit() 
    conn.close()


def make_complete(task_id):
    conn = get_db_connection()
    cursor = conn.cursor() 
    cursor.execute("UPDATE tasks SET is_complete = 1 WHERE id = ?", (task_id,))
    conn.commit() 
    conn.close()