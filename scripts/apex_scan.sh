#!/usr/bin/env bash
set -e

subfinder -dL $1 -all | \
tee subdomains.txt | \
httpx -status-code -title -content-length -web-server -asn -location -no-color -follow-redirects -t 15 -ports 80,8080,443,8443,4443,8888 -no-fallback -probe-all-ips -random-agent | \
tee http.txt