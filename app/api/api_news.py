
import logging
from typing import Any
from fastapi import APIRouter, Depends, HTTPException

from app.helpers.exception_handler import CustomException
from app.helpers.paging import Page, PaginationParams, paginate
from app.models.model_news import News
from app.schemas.sche_base import DataResponse
from app.schemas.sche_news import NewsItemResponse
from app.services.srv_news import NewsService
from fastapi_sqlalchemy import db

logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=Page[NewsItemResponse])
def get_news(params: PaginationParams = Depends()) -> Any:
    """
    API Get list News
    """
    try:
        _query = db.session.query(News)
        news = paginate(model=News, query=_query, params=params)
        return news
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
    

@router.get("/{news_id}", response_model=DataResponse[NewsItemResponse])
def get_news_by_id(news_id: int, news_service: NewsService = Depends()) -> Any:
    """
    API Get detail News
    """
    try:
        return DataResponse().success_response(data=news_service.get(news_id))  
    except Exception as e:
        return CustomException(http_code=400, code='400', message=str(e))