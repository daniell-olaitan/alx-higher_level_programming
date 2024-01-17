#!/usr/bin/env bash
# displays the methods allowed for the url
curl -sIL -X OPTIONS "$1" | grep "Allow: " | cut -d':' -f2 | sed 's/ //'
