#!/bin/bash
#Script that sends a request to a URL and displays size of body as response
curl -s "$1" | wc -c
