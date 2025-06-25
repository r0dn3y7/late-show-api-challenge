# 🌙 Late Show API

Welcome to the Late Show API — a Flask-based RESTful backend that manages episodes, guests, and their appearances on a fictional late-night talk show. This API uses PostgreSQL, Flask-JWT for authentication, and follows an MVC architecture.

---

## 🛠 Tech Stack

- Python 3
- Flask
- SQLAlchemy + Flask-Migrate
- PostgreSQL
- Flask-JWT-Extended
- Postman (for API testing)

---

## 📁 Project Structure

```

late-show-api/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── **init**.py
│   │   ├── user.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   └── appearance.py
│   ├── controllers/
│   │   ├── **init**.py
│   │   ├── auth\_controller.py
│   │   ├── guest\_controller.py
│   │   ├── episode\_controller.py
│   │   └── appearance\_controller.py
├── migrations/
├── .env
├── .gitignore
├── README.md
└── challenge-4-lateshow\.postman\_collection.json

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/r0dn3y7/late-show-api-challenge.git
cd late-show-api-challenge
````

### 2. Install dependencies

```bash
pipenv install
pipenv shell
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```
DATABASE_URI=postgresql://your_postgres_user:your_postgres_password@localhost:5432/late_show_db
JWT_SECRET_KEY=super_secret_key
```

> Make sure PostgreSQL is running and replace `your_postgres_user` and `your_postgres_password` with your actual credentials.

### 4. Create the database

```bash
psql
CREATE DATABASE late_show_db;
\q
```

### 5. Run migrations and seed the database

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

---

## 🔐 Authentication Flow

### Register a User

```http
POST /register
Content-Type: application/json

{
  "username": "demo",
  "password": "demo123"
}
```

### Log in

```http
POST /login
Content-Type: application/json

{
  "username": "demo",
  "password": "demo123"
}
```

You’ll receive a JWT token like this:

```json
{
  "access_token": "your.jwt.token.here"
}
```

For protected routes, include the token in the header:

```
Authorization: Bearer your.jwt.token.here
```

---

## 📡 API Endpoints

| Endpoint         | Method | Description                             |
| ---------------- | ------ | --------------------------------------- |
| `/register`      | POST   | Register a new user                     |
| `/login`         | POST   | Log in and receive a JWT token          |
| `/guests`        | GET    | Get all guests                          |
| `/episodes`      | GET    | Get all episodes                        |
| `/episodes/<id>` | GET    | Get an episode with its appearances     |
| `/episodes/<id>` | DELETE | Delete an episode (and its appearances) |
| `/appearances`   | POST   | Create a new appearance                 |

---

## 🧪 Testing with Postman

1. Open Postman.
2. Import the file: `challenge-4-lateshow.postman_collection.json`
3. Test all the routes, including auth-protected ones.

For protected routes:

* Log in first and copy your token.
* Click "Authorization" tab in Postman.
* Choose "Bearer Token" and paste your token.

---

## 📝 Notes

* Cascading delete is enabled: when an episode is deleted, all its appearances are deleted too.
* Appearances have a rating from 1 to 5 only.
* Passwords are hashed using Werkzeug.

---

## 📎 GitHub Repo

[GitHub Repository](https://github.com/r0dn3y7/late-show-api-challenge)

---

