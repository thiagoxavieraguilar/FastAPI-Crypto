from pydantic import BaseModel, validator
import re


class UserInput(BaseModel):
    username: str
    password: str

    @validator("username")
    def validate_username(cls, value):
        if not re.match("^[a-z0-9_@]+$", value):
            raise ValueError("Username format invalid")
        return value
