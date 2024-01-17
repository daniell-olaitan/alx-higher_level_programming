#!/usr/bin/env bash
# Takes in a URL, sends request to that URL, and displays the size of the body
curl -s -o "/dev/null" -w "%{size_download}\n" "$1"
