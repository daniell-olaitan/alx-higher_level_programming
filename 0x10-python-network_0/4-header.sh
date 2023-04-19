#!/bin/bash
# sends a header with a get request
curl -sL -X GET -H "X-School-User-Id: 98" "$1"
