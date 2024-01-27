import time
import random
from prometheus_client import start_http_server, Summary, Counter, Histogram

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

c = Counter('my_requests_total', 'HTTP Failures', ['method', 'endpoint'])
h = Histogram('my_request_latency_seconds', 'Description of histogram')


@REQUEST_TIME.time()
def process_request(t):
    c.labels(method='get', endpoint='/fake').inc()
    h.observe(2.5 + t)
    time.sleep(t)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_request(random.random())
