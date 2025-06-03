from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import UserCreate
from app.db import users_collection
from app.utils.token import generate_verification_token, verify_token
from app.utils.email import send_verification_email
from passlib.context import CryptContext

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow everything for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/signup")
async def signup(user: UserCreate):
    print("Received User Data:", user)
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        if existing_user.get("is_verified"):
            raise HTTPException(status_code=400, detail="Email already registered")
        else:
            # Resend token instead
            token = generate_verification_token(user.email)
            await users_collection.update_one(
                {"email": user.email},
                {"$set": {"verification_token": token}}
            )
            send_verification_email(user.email, token)
            return {"message": "Account already exists but not verified. We re-sent the verification email."}


    hashed_pw = pwd_context.hash(user.password)
    token = generate_verification_token(user.email)
    await users_collection.insert_one({
        "email": user.email,
        "hashed_password": hashed_pw,
        "is_verified": False,
        "verification_token": token
    })
    send_verification_email(user.email, token)
    return {"message": "Check your email to verify your account"}

@app.get("/verify-email")
async def verify_email(token: str):
    email = verify_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    user = await users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.get("is_verified"):
        return {"message": "Already verified"}
    await users_collection.update_one({"email": email}, {"$set": {"is_verified": True}})
    return {"message": "Email verified"}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_collection.find_one({"email": form_data.username})
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not user["is_verified"]:
        raise HTTPException(status_code=403, detail="Email not verified")
    return {"message": "Login successful"}
