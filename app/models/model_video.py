# app/models/model_book.py
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text

from app.models.model_base import BareBaseModel


class Video(BareBaseModel):
    speech_id = Column(Integer, ForeignKey('speech.id'), nullable=False)
    video_title = Column(String)
    video_url = Column(String)
    presenter_id = Column(Integer, ForeignKey('presenter.id'), nullable=False)
    duration = Column(Integer)
    uploaded_time = Column(DateTime)
    status = Column(String)
    
