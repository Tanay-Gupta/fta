from celery.utils.log import get_task_logger
from models import db, Flight, User
from notifications import send_notification
from celery_config import make_celery
import requests

logger = get_task_logger(__name__)

def create_celery_app(app):
    celery = make_celery(app)  # Initialize Celery
    return celery

def check_flight_status(app, flight_id):
    with app.app_context():
        flight = Flight.query.get(flight_id)
        # Mock API call to get flight status
        response = requests.get(f'https://mock-flight-api.com/status/{flight.flight_id}')
        status = response.json().get('status')
        if status != flight.status:
            flight.status = status
            db.session.commit()
            send_notification(flight.user, flight)
        return status
