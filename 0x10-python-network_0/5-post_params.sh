#!/usr/bin/env bash
# sends a post request to a url with a set of data
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
