#!/usr/bin/python3
"""This is the review class"""
from sqlalchemy.ext.declarative import declarative_base
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    if models.storage_tp == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
