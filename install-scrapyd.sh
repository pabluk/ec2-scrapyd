#!/bin/bash

# Add Scrapy repositories and key
echo "deb http://archive.scrapy.org/ubuntu precise main" > /etc/apt/sources.list.d/scrapy.list
curl -s http://archive.scrapy.org/ubuntu/archive.key | apt-key add -

# Install debian package
apt-get update && apt-get -y install scrapyd-0.16

# Restart scrapyd
service scrapyd restart
