#!/bin/sh

python sitebuilder.py build

s3cmd sync build/ s3://walruswalr.us