from pydantic import BaseModel


class MessageBase(BaseModel):
    content: str
    role: str


class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int
    conversationt_int: int

    class Config:
        from_attributes = True


class ConversationCreate(BaseModel):
    title: str


class ConversationResponse(BaseModel):
    id: int
    title: str
    messages: list[MessageResponse]

    class Config:
        from_attributes = True
