# Datadog MACESS Custom Agent Check

This repository contains a custom Datadog Agent Check that collects MACESS metrics by executing modular Python logic.

## ✅ Metrics Collected
- `gbd.macess.queue_length`
- `gbd.macess.jobs.failed`
- `gbd.macess.processing_time.avg`

## 🛠 Installation

1. Copy files:
   - `checks/` ➝ `/etc/datadog-agent/checks.d/`
   - `conf/macess_check.yaml` ➝ `/etc/datadog-agent/conf.d/macess_check.d/conf.yaml`

2. Set permissions:
```bash
chown dd-agent:dd-agent /etc/datadog-agent/checks.d/macess_*.py
