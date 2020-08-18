#!/bin/bash
# takes in a URL, sends a POST request, displays the body of the response
curl -sX POST $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
