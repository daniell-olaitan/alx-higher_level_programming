#!/bin/bash
# sends a post request with the content of  a file
curl -sL -X POST -H "Content-Type: application/json" -d "$(cat $2)" "$1"
