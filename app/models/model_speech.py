# app/models/model_book.py
from sqlalchemy import Column, ForeignKey, Integer, String, Text

from app.models.model_base import BareBaseModel


class Speech(BareBaseModel):
    news_id = Column(Integer, ForeignKey('news.id'), nullable=False)
    speech_title = Column(String)
    summary = Column(Text)
    speech_url = Column(String)
    duration = Column(Integer)
    
   
