import pytest
from flask import Flask
from shared.app import create_app  # Assuming you have a function to create your Flask app
from shared.models import db

@pytest.fixture
def app():
    app = create_app(testing=True)  # Pass a testing flag
    with app.app_context():
        db.create_all()  # Create the database
        yield app
        db.drop_all()  # Clean up after tests

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Social Media App' in response.data  # Adjust based on your home page content

def test_create_user(client):
    response = client.post('/create_user', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201  # Expecting a created status
    assert b'User created successfully' in response.data  # Adjust based on your response message
