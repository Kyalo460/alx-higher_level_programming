#!/bin/bash
# displays the size of the response body
curl -s "$1" | wc -c
