# app/models/model_book.py
from sqlalchemy import Column, Integer, String, DateTime, Text

from app.models.model_base import BareBaseModel


class Presenter(BareBaseModel):
    reference_image_path = Column(String)
