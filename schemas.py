# use pydantic library
from pydantic import BaseModel
from datetime import datetime

# create Booking Class
class Booking(BaseModel):
    name: str = "Aiman"
    numOfParticipants: int = 0
    eventType: str = "Wedding / Family Day / Graduation"
    eventStart: datetime = "2022-01-01 12:00:00"
    eventEnd: datetime = "2022-01-01 12:00:00"

# create UpdateBooking Class
class UpdateBooking(BaseModel):
    numOfParticipants: int = 0
    eventType: str = "Wedding / Family Day / Graduation"
    eventStart: datetime = "2022-01-01 12:00:00"
    eventEnd: datetime = "2022-01-01 12:00:00"
    
