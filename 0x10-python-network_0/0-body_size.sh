#!/bin/bash
# Takes in a URL, sends request to that URL, and displays the size of the body
curl -s -w "%{size_download}\n" -o "/dev/null" "$1"
