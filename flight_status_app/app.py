from flask import Flask, request, jsonify
from models import db, Flight, User
from celery_config import make_celery
from tasks import create_celery_app, check_flight_status as check_flight_status_task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.update(
    CELERY_BROKER_URL='amqp://localhost',
    CELERY_RESULT_BACKEND='rpc://'
)

db.init_app(app)
celery = create_celery_app(app)

@app.route('/')
def home():
    return "Hello, Flask!"



@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    user = User(email=data['email'], phone=data['phone'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/add_flight', methods=['POST'])
def add_flight():
    data = request.json
    flight = Flight(
        flight_id=data['flight_id'],
        from_city=data['from_city'],
        to_city=data['to_city'],
        date=data['date'],
        user_id=data['user_id']
    )
    db.session.add(flight)
    db.session.commit()
    celery.send_task('tasks.check_flight_status', args=[app, flight.id])
    return jsonify({"message": "Flight added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)

