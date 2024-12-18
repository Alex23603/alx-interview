#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Generate 10,000 lines of log data
for i in range(10000):
    sleep(random.random())  # Random delay to simulate real-time logging
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),  # Random status code
        random.randint(1, 1024)  # Random file size
    ))
    sys.stdout.flush()
