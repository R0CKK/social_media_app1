# tests/test_models.py

import pytest
from shared.utils.db_utils import db
from shared.models.user_model import User

def test_user_creation(client):
    new_user = User(username='test_user', email='test_user@example.com', password_hash='hashed_password')
    db.session.add(new_user)
    db.session.commit()

    # Assert that the user was created
    assert new_user in db.session
