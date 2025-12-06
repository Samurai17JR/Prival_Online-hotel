
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


from .base import Base
from .users import User          
from .hotels import Hotel       
from .rooms import Room         
from .bookings import Booking    
from .reviews import Review      
from .roles import Role         
__all__ = ["Base", "User", "Hotel", "Room","Review","Role"]