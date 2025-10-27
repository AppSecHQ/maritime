# Maritime Application

A Python application for maritime shipping logistics and banking transaction verification.

## Features

- **CLI Mode**: Colorful terminal output with fun facts and timestamps
- **Web Service Mode**: Flask-based REST API for shipping tracking and transaction verification
- Fetches random fun facts from an API
- Displays current timestamp
- Demonstrates usage of external dependencies
- RESTful API endpoints for integration with banking systems

## Dependencies

This application uses the following Python packages:
- `requests` - For making HTTP requests to external APIs
- `Flask` - Web framework for REST API endpoints
- `Jinja2` - Template engine (Flask dependency)
- `colorama` - For colored terminal output
- `python-dateutil` - For enhanced date/time handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AppSecHQ/maritime.git
cd maritime
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### CLI Mode (Default)
Run the application in CLI mode:
```bash
python app.py
```

### Web Service Mode
Run the application as a Flask web service:
```bash
python app.py web
```

The web service will start on `http://localhost:5000` with the following endpoints:

- **GET /health** - Health check endpoint
- **GET /api/shipping/track/<tracking_id>** - Track shipment by ID
- **POST /api/verify/transaction** - Verify banking transaction

### Example API Calls

```bash
# Health check
curl http://localhost:5000/health

# Track shipment
curl http://localhost:5000/api/shipping/track/ABC123

# Verify transaction
curl -X POST http://localhost:5000/api/verify/transaction \
  -H "Content-Type: application/json" \
  -d '{"transaction_id": "TXN-12345", "amount": 100.00}'
```

## Requirements

- Python 3.6 or higher
- Internet connection (for fetching fun facts and external API calls)
