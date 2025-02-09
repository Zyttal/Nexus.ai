from typing import Any, Generator
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.db.database import Base


TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="session")
def test_engine():
    """Create engine once for all tests"""
    engine = create_engine(
        TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    return engine


@pytest.fixture(scope="function")
def test_db(test_engine) -> Generator[Session, Any, None]:
    """
    Create Fresh Database Tables for Each Test
    Ensuring each test starts with a clean Database
    """

    Base.metadata.create_all(bind=test_engine)

    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=test_engine
    )
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()

        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def override_get_db(test_db):
    """
    Override the get_db dependency for testing
    This allows FastAPI to use the test database
    """

    def _get_test_db():
        try:
            yield test_db
        finally:
            test_db.close()

    return _get_test_db
