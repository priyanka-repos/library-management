from pydantic import BaseModel


class User(BaseModel):
    reg_No : int
    name : str
    phone : int
    