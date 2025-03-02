import enum


class UserRole(enum.Enum):
    ADMIN = 'admin'
    GUEST = 'guest'

class VideoStatus(enum.Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    DONE = 'done'
    ERROR = 'error'

class HistoryStatus(enum.Enum):
    PENDING = 'pending'
    DONE = 'done'
    ERROR = 'error'