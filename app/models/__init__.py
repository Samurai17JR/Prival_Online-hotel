
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


from .base import Base
from .users import User
from .rooms import Room
from .hotels import Hotel
from .bookings import Booking
from .reviews import Review
from .roles import Role
__all__ = ["Base", "User", "Hotel", "Room","Review","Role"]