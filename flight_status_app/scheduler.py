from apscheduler.schedulers.background import BackgroundScheduler
from tasks import check_flight_status
from models import Flight

scheduler = BackgroundScheduler()
scheduler.add_job(
    func=check_all_flights,
    trigger="interval",
    seconds=60
)

def check_all_flights():
    flights = Flight.query.all()
    for flight in flights:
        check_flight_status.delay(flight.id)
