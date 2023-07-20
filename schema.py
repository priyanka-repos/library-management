from pydantic import BaseModel


class User(BaseModel):
    reg_no : int
    name : str
    phone : int
    