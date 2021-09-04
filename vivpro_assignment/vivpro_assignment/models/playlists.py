from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,

)

from .meta import Base


class Playlist(Base):
    __tablename__ = 'playlist'
    id = Column(Text, primary_key=True)


Index('my_index', Playlist.id, unique=True)
