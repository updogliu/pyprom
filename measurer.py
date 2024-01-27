import time
import random
import numpy as np
from prometheus_client import start_http_server, Gauge, Histogram

rng = np.random.default_rng()
h = Histogram('my_request_latency_hist', 'Histogram of the latency')
g = Gauge('my_request_latency_gauge', 'Gauge of the real time latency')


def process_request(t):
    h.observe(t)
    g.set(t)
    time.sleep(t if t < 1 else 1)

def generate_latency():
    return abs(rng.normal()*5)

if __name__ == '__main__':
    print("Exporting the latency metrics at localhost:8000")
    start_http_server(8000)

    while True:
        process_request(generate_latency())
