# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.model_base import Base  # noqa
from app.models.model_user import User  # noqa
from app.models.model_news import News  # noqa
from app.models.model_speech import Speech  # noqa
from app.models.model_video import Video  # noqa
from app.models.model_presenter import Presenter  # noqa
from app.models.model_history import VideoHistory  # noqa