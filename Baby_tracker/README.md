# Baby Tracker Flask App
This is a simple Flask application for tracking baby events using a MySQL database. It provides a RESTful API to perform CRUD (Create, Read, Update, Delete) operations on baby events.

# Prerequisites
Before you begin, ensure you have met the following requirements:

- Python (>= 3.6) is installed.
- Flask is installed (pip install Flask).
- Flask-SQLAlchemy is installed (pip install Flask-SQLAlchemy).
- MySQL server is running, and you have the necessary credentials to access it.
Setup
Clone this repository:

```bash
git clone <repository-url>
Install the required packages:
```

```bash
pip install Flask Flask-SQLAlchemy pymysql
Configure the MySQL database URI in the app.py file:
```

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3306/baby_tracker'
Create the database tables:
```
```bash
from app import db
db.create_all()
```
#Usage
#Start the Flask development server:

```bash
python app.py
The server will start, and you can access the API at http://localhost:5000.
```
Endpoints
- GET /: Returns a simple greeting message.

- POST /events: Create a new event.
 - Request body: { "description": "Event description" }
- GET /events: Retrieve a list of all events.

- GET /events/<id>: Retrieve details of a specific event.

- PUT /events/<id>: Update an event.

Request body: { "description": "Updated description" }
- DELETE /events/<id>: Delete an event.

# Data Format
The API uses JSON for data exchange. Here's the format of an event:
```json
{
  "id": 1,
  "description": "Event description",
  "created_at": "2023-08-04T12:34:56Z"
}
```
# Example Requests
##Create Event
```bash
curl -X POST -H "Content-Type: application/json" -d '{"description": "Feeding"}' http://localhost:5000/events
```
# Get All Events
```bash
curl http://localhost:5000/events
```
# Get Specific Event
```bash
curl http://localhost:5000/events/1
```
# update Event

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"description": "New feeding event"}' http://localhost:5000/events/1
```
# Delete Event
```bash
curl -X DELETE http://localhost:5000/events/1
```
# Closing Notes
This Flask app serves as a basic foundation for tracking baby events in a MySQL database. You can further enhance and customize it according to your needs.