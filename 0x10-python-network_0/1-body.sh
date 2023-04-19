#!/bin/bash
# takes in a URL, sends a GET request and displays the message body
curl -sL -X GET -D h_tmp -o b_tmp "$1"; if grep -q "200 OK" h_tmp; then cat b_tmp; fi; rm h_tmp b_tmp
