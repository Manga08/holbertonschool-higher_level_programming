#!/bin/bash
#Script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -H "Content-Type: application/json" --data @"$2" "$1"