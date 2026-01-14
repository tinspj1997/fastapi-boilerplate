from datetime import datetime, timedelta, timezone
from typing import Annotated
from functools import singledispatchmethod
import json
import base64
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel
from cryptography.fernet import Fernet

# Import constants from DefaultConfig
from src.core.artifacts.constants.default import DefaultConfig

SECRET_KEY = DefaultConfig.SECRET_KEY.value
ALGORITHM = DefaultConfig.ALGORITHM.value
ACCESS_TOKEN_EXPIRE_MINUTES = int(DefaultConfig.ACCESS_TOKEN_EXPIRE_MINUTES.value)
password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Generate encryption key from SECRET_KEY
encryption_key = base64.urlsafe_b64encode(SECRET_KEY.encode().ljust(32)[:32])
cipher_suite = Fernet(encryption_key)


class DataEncryptor:
    """Encrypts and decrypts various data types (str, dict, list, etc.)"""
    
    def __init__(self):
        self.cipher_suite = cipher_suite
    
    @singledispatchmethod
    def encrypt(self, data):
        """Base encrypt method - converts data to string first"""
        data_str = str(data)
        encrypted = self.cipher_suite.encrypt(data_str.encode())
        return encrypted.decode()
    
    @encrypt.register(str)
    def _(self, data: str):
        """Encrypt string data"""
        encrypted = self.cipher_suite.encrypt(data.encode())
        return encrypted.decode()
    
    @encrypt.register(dict)
    def _(self, data: dict):
        """Encrypt dictionary data - converts to JSON first"""
        json_str = json.dumps(data)
        encrypted = self.cipher_suite.encrypt(json_str.encode())
        return encrypted.decode()
    
    @encrypt.register(list)
    def _(self, data: list):
        """Encrypt list data - converts to JSON first"""
        json_str = json.dumps(data)
        encrypted = self.cipher_suite.encrypt(json_str.encode())
        return encrypted.decode()
    
    @encrypt.register(int)
    def _(self, data: int):
        """Encrypt integer data"""
        encrypted = self.cipher_suite.encrypt(str(data).encode())
        return encrypted.decode()
    
    @encrypt.register(float)
    def _(self, data: float):
        """Encrypt float data"""
        encrypted = self.cipher_suite.encrypt(str(data).encode())
        return encrypted.decode()
    
    @encrypt.register(bool)
    def _(self, data: bool):
        """Encrypt boolean data"""
        encrypted = self.cipher_suite.encrypt(str(data).encode())
        return encrypted.decode()
    
    def decrypt(self, encrypted_data: str):
        """Decrypt encrypted data and return as string"""
        if isinstance(encrypted_data, str):
            encrypted_data = encrypted_data.encode()
        decrypted = self.cipher_suite.decrypt(encrypted_data)
        return decrypted.decode()
    
    def decrypt_to_dict(self, encrypted_data: str) -> dict:
        """Decrypt encrypted data and parse as JSON dictionary"""
        decrypted_str = self.decrypt(encrypted_data)
        return json.loads(decrypted_str)
    
    def decrypt_to_list(self, encrypted_data: str) -> list:
        """Decrypt encrypted data and parse as JSON list"""
        decrypted_str = self.decrypt(encrypted_data)
        return json.loads(decrypted_str)


# Create a global encryptor instance
encryptor = DataEncryptor()

# Function to create a token
def create_token(data: dict, expires_delta: timedelta | None = None):
    """Create a JWT token with the provided data."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Function to encrypt a token
def encrypt_token(token: str) -> str:
    """Encrypt a token using the DataEncryptor."""
    return encryptor.encrypt(token)


# Function to get the current user
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        return payload
    except InvalidTokenError:
        raise credentials_exception
    


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def create_password_hash(password):
    return password_hash.hash(password)




