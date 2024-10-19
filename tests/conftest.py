# tests/conftest.py

import pytest
from social_media_app import create_app  # Make sure to adjust the import according to your app structure
from social_media_app.shared.utils.db_utils import db 

@pytest.fixture
def app():
    # Create a new app instance for each test
    app = create_app()
    
    # Set up the app context
    with app.app_context():
        # Create the database
        db.create_all()
        yield app  # This will allow the tests to run

        # Clean up after tests
        db.drop_all()

@pytest.fixture
def client(app):
    # Create a test client for the app
    return app.test_client()
