# Wine Fermentation

ქართული Django აპლიკაცია ღვინის ფერმენტაციის აღრიცხვისთვის.

## ფუნქციები

- მომხმარებლის რეგისტრაცია და შესვლა
- ღვინის ფერმენტაციის პროექტების CRUD
- ფერმენტაციის დღიური: თარიღი/დრო, ტემპერატურა, Brix, შაქარი, pH, მჟავიანობა, ქმედება და კომენტარი
- გრაფიკები ტემპერატურის, Brix-ის და pH-ის დინამიკისთვის
- Render deployment კონფიგურაცია

## ლოკალურად გაშვება

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

გახსენი `http://127.0.0.1:8000/`.
