#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the first command-line argument
url="$1"

# Use curl to send a GET request to the URL and store the response in a variable
response=$(curl -s -w "%{http_code}" "$url")

# Extract the status code from the response
status_code=${response: -3}

# Check if the status code is 200 (OK)
if [ "$status_code" = "200" ]; then
    # Display the body of the response
    curl -s "$url"
else
    echo "Error: HTTP status code $status_code"
fi
