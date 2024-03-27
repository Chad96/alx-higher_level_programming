#!/usr/bin/env bash
# Check if a URL is provided as an argument

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send a request and retrieve the size of the response body
response_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n')

# Check if Content-Length header is present in the response
if [ -z "$response_size" ]; then
    echo "Content-Length header not found in the response."
    exit 1
fi
