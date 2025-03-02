# app/models/model_book.py
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from app.models.model_base import BareBaseModel


class VideoHistory(BareBaseModel):
    video_id = Column(Integer, ForeignKey('video.id'), nullable=False)
    status = Column(String(255))
    reviewed_at = Column(DateTime)
    