from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    # Code worked without the below code
    # Now, in the Pydantic models for reading, Item and User, add an internal Config class.
    # This Config class is used to provide configurations to Pydantic.
    # In the Config class, set the attribute orm_mode = True.
    # class Config:
    #     orm_mode = True

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id : int
    owner: UserOut

    class Config:
        # orm_mode = True
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        # orm_mode = True
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore

        