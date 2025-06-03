# 📧 FastAPI Email Verification App

This is a backend email verification system built with **FastAPI**, **MongoDB Atlas**, and **SendGrid**. It allows users to sign up with an email and password, receive a verification link, and log in only after verifying their email.

---

## 🚀 Features

- ✅ Email-based user signup  
- ✅ Secure email verification via token  
- ✅ Password hashing with bcrypt  
- ✅ MongoDB Atlas for persistent storage  
- ✅ SendGrid for transactional email  
- ✅ Simple HTML frontend (index.html)  

---

## 🗂️ Project Structure

```
.
├── app/
│   ├── main.py                # FastAPI entrypoint
│   ├── db.py                  # MongoDB connection
│   ├── models/
│   │   └── user.py            # Pydantic model
│   ├── utils/
│   │   ├── email.py           # SendGrid integration
│   │   └── token.py           # JWT-based token logic
├── .env                       # Environment variables (excluded from Git)
├── index.html                 # Frontend signup/login form
├── requirements.txt           # Python dependencies
├── sendgrid_test.py           # Standalone email tester
└── README.md                  # You're here!
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/maxamedjaamac34/Email-Verification.git
cd Email-Verification
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb+srv://<your_user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
SENDGRID_API_KEY=SG.xxxxxx.yyyyyyy
FROM_EMAIL=your_verified_sender@example.com
```

> Make sure the `FROM_EMAIL` is verified in SendGrid under **Sender Authentication**.

---

## ▶️ Running the App

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

- FastAPI docs: http://127.0.0.1:8000/docs  
- API root: http://127.0.0.1:8000  

---

## 🧪 Try the App

### 1. Open `index.html` in a browser (double-click it)  
### 2. Use the **Sign Up** form  
- You’ll receive a verification link via email

### 3. Click the verification link  
- Your email will be marked as verified

### 4. Use the **Log In** form  
- You can only log in once verified

---

## 📬 Standalone Email Test

To test SendGrid integration separately:

```bash
python sendgrid_test.py
```

This sends a test email to your inbox using the current API key and sender email.

---

## 🛡️ Notes

- Passwords are stored as bcrypt hashes  
- Tokens are signed with JWT and expire after 1 hour  
- `.env` is excluded from version control via `.gitignore`  

---

## 🧩 To-Do (Optional)

- [ ] Deploy to AWS / Render  
- [ ] Add password reset flow  
- [ ] Use database indexes for email  
- [ ] Add email resend if token expired  

---

## 👤 Author

**Mohamed Ahmed**  
[GitHub Profile](https://github.com/maxamedjaamac34)

---

## 📄 License

This project is licensed under the MIT License.
