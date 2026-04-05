import time
import psutil
from prometheus_client import start_http_server, Gauge

# METRICS
cpu_usage = Gauge('system_cpu_usage_percent', 'CPU usage in percent')
memory_usage = Gauge('system_memory_usage_percent', 'Memory usage in percent')
disk_usage = Gauge('system_disk_usage_percent', 'Disk usage in percent')


def collect_metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    cpu_usage.set(cpu)
    memory_usage.set(memory)
    disk_usage.set(disk)

    print(f"CPU: {cpu}% | RAM: {memory}% | Disk: {disk}%")


if __name__ == "__main__":
    # pornește server Prometheus
    start_http_server(8000)
    print("Metrics available at http://localhost:8000")

    while True:
        collect_metrics()
        time.sleep(5)
