#!/bin/bash
# displays the allowed methods
curl -sI "$3" | grep "Allow" | cut -d " " -f 2-
