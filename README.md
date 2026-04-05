System Monitor with Prometheus & Docker

This project is a lightweight system monitoring service built with Python. It collects CPU, memory, and disk usage metrics and exposes them for Prometheus scraping.

Features
	•	Real-time system metrics collection
	•	Prometheus metrics endpoint
	•	Docker container support
	•	Ready for monitoring stack integration

Tech Stack
	•	Python
	•	psutil
	•	prometheus_client
	•	Docker
	•	Prometheus

Usage

Run locally:
pip install -r requirements.txt
python app.py

Metrics available at:
http://localhost:8000

Docker

Build:
docker build -t system-monitor .

Run:
docker run -p 8000:8000 system-monitor

Prometheus

Run Prometheus with config:
prometheus.yml

Future Improvements
	•	Grafana dashboards
	•	Alerting system
	•	Kubernetes deployment