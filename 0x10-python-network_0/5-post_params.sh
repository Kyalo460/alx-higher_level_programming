#!/bin/bash
# sends two variables with a POST request
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
