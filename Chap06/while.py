#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    # Break
    if count > max_attempt: break
    # Continue
    if count == 3: continue
    pw = input(f"{count}: What's the secret word? ")
# When condition is not true
else:
    auth = True

print("Authorized" if auth else "Calling the FBI...")
# Break loop
