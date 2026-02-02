#!/bin/bash
# Script to run the echo service

# Set the port (default to 5000)
PORT=${PORT:-5000}

echo "Starting Echo Service on port $PORT..."
python3 app.py