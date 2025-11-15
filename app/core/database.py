from typing import Iterator

from sqlmodel import Session, SQLModel, create_engine

from .config import settings


def _build_engine_url() -> str:
    return settings.database_url


def _engine_connect_args() -> dict:
    url = _build_engine_url()
    if url.startswith("sqlite"):
        return {"check_same_thread": False}
    return {}


def get_engine():
    """Create a SQLModel engine using the configured database URL."""

    engine = create_engine(
        _build_engine_url(),
        echo=settings.echo_sql,
        connect_args=_engine_connect_args(),
    )
    return engine


engine = get_engine()


def init_db() -> None:
    """Ensure database tables exist."""

    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    """Provide a database session per request."""

    with Session(engine) as session:
        yield session
