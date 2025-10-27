#!/usr/bin/env python3
"""
Maritime Demo Application
A simple hello world application with external dependencies
Now includes a Flask web service for shipping logistics
"""

import requests
from datetime import datetime
from colorama import Fore, Style, init
from flask import Flask, jsonify, request

# Initialize colorama
init()

# Initialize Flask app
app = Flask(__name__)

def main():
    """Main application entry point"""
#   print(f"{Fore.CYAN}=" * 50)
    print(f"{Fore.LIGHTCYAN_EX}=" * 50)
    print(f"{Fore.LIGHTCYAN_EX}=" * 50)
    print(f"{Fore.GREEN}Hello World from Maritime Demo!{Style.RESET_ALL}")
#   print(f"{Fore.CYAN}=" * 50)

    # Display current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Fore.YELLOW}Current time: {current_time}{Style.RESET_ALL}")

    # Make a simple API call to demonstrate requests library
    try:
        print(f"\n{Fore.BLUE}Fetching a fun fact...{Style.RESET_ALL}")
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en", timeout=5)
        if response.status_code == 200:
            fact = response.json().get("text", "No fact available")
            print(f"{Fore.MAGENTA}Fun fact: {fact}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Could not fetch fun fact: {e}{Style.RESET_ALL}")

    print(f"\n{Fore.GREEN}Application completed successfully!{Style.RESET_ALL}\n")

    print(f"{Fore.LIGHTCYAN_EX}=" * 50)
    print(f"{Fore.LIGHTCYAN_EX}=" * 50)

@app.route('/health')
def health():
    """Health check endpoint for maritime services"""
    return jsonify({
        'status': 'healthy',
        'service': 'maritime-logistics',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/shipping/track/<tracking_id>')
def track_shipment(tracking_id):
    """
    Track shipment by calling external shipping API
    Uses requests library to communicate with third-party services
    VULNERABLE: Uses requests 2.25.0 which has CVE-2024-47081
    """
    try:
        # Simulate calling external shipping API
        # This demonstrates reachability - the vulnerable requests library is actively used
        api_url = f"https://api.shipping-service.example.com/track/{tracking_id}"
        response = requests.get(api_url, timeout=5)

        return jsonify({
            'tracking_id': tracking_id,
            'status': 'success',
            'message': 'Shipment tracking data retrieved'
        })
    except Exception as e:
        return jsonify({
            'tracking_id': tracking_id,
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/verify/transaction', methods=['POST'])
def verify_transaction():
    """
    Verify banking transaction by calling external verification service
    VULNERABLE: Uses requests library with CVE-2024-47081
    This is a critical path for financial transactions
    """
    try:
        data = request.get_json()
        transaction_id = data.get('transaction_id')

        # Call external banking verification API
        # This uses the vulnerable requests library - demonstrating reachability
        verification_url = "https://api.banking-verify.example.com/verify"
        response = requests.post(verification_url, json=data, timeout=10)

        return jsonify({
            'transaction_id': transaction_id,
            'verified': True,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'verified': False
        }), 500

if __name__ == "__main__":
    # Can run as CLI app or web service
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'web':
        print(f"{Fore.GREEN}Starting Maritime Web Service...{Style.RESET_ALL}")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        main()
