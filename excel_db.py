import os
import pandas as pd
from datetime import datetime

# Excel ფაილების მდებარეობა
PROJECTS_FILE = r"C:\Users\levan.avaliani\Desktop\wine_project\db\projects.xlsx"
INITIAL_DATA_FILE = r"C:\Users\levan.avaliani\Desktop\wine_project\db\initial_data.xlsx"

# თუ ფაილი არ არსებობს, ვქმნით ცარიელ ცხრილს
def create_empty_excel(file_path, columns):
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=columns)
        df.to_excel(file_path, index=False)

# 📌 პროექტების ფაილი (ID, სახელი, შექმნის თარიღი)
create_empty_excel(PROJECTS_FILE, ["ID", "Project Name", "Created At"])

# 📌 საწყისი მონაცემები (ID, შაქარი, pH, ტიტრული მჟავიანობა და ა.შ.)
create_empty_excel(INITIAL_DATA_FILE, ["Project ID", "Sugar", "pH", "Titratable Acidity"])

# ✅ ახალი პროექტის დამატება
def add_project(project_name):
    df = pd.read_excel(PROJECTS_FILE)
    project_id = len(df) + 1  # მარტივი ID გენერაცია
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_project = pd.DataFrame([[project_id, project_name, created_at]], columns=df.columns)
    df = pd.concat([df, new_project], ignore_index=True)
    df.to_excel(PROJECTS_FILE, index=False)
    return project_id

# ✅ საწყისი მონაცემების დამატება (პროექტისთვის)
def add_initial_data(project_id, sugar, pH, acidity):
    df = pd.read_excel(INITIAL_DATA_FILE)
    new_data = pd.DataFrame([[project_id, sugar, pH, acidity]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(INITIAL_DATA_FILE, index=False)

# ✅ ყველა პროექტის ჩამონათვალი
def get_all_projects():
    df = pd.read_excel(PROJECTS_FILE)
    return df.to_dict(orient="records")

# ✅ კონკრეტული პროექტის საწყისი მონაცემების მიღება
def get_initial_data(project_id):
    df = pd.read_excel(INITIAL_DATA_FILE)
    return df[df["Project ID"] == project_id].to_dict(orient="records")

# ტესტისთვის
if __name__ == "__main__":
    pid = add_project("Example Project")
    add_initial_data(pid, 23.5, 3.2, 7.1)
    print(get_all_projects())
    print(get_initial_data(pid))
