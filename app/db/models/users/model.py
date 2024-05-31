from pydantic import BaseModel, Field


class UserModel(BaseModel):
    firstName: str = Field(
        title="First Name of the user"
    )
    lastName: str = Field(
        title="Last Name of the user"
    )
    email: str = Field(
        title="Email of the user"
    )
    password: str = Field(
        title="Password of the user",
        default=None
    )
    userid: str = Field(
        title="User ID",
        description="Unique identifier of the user",
        default=None
    )

