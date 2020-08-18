#!/bin/bash
# show allowed methods
curl -sI $1 | grep "Allow:" | cut -d " " -f 2-
