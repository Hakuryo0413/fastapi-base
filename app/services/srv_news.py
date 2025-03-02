from app.models import News
from fastapi_sqlalchemy import db


class NewsService(object):
    _instance = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_news_list():
        return db.session.query(News).all()
    
    @staticmethod
    def get_news(news_id):
        exist_news = db.session.query(News).get(news_id)
        if exist_news is None:
            return Exception('News not found')
        return exist_news