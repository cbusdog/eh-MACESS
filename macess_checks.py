from datadog_checks.base import AgentCheck
from .macess_utils import get_queue_length, get_failed_jobs, get_avg_processing_time

class MacessCheck(AgentCheck):
    def check(self, instance):
        try:
            queue_length = get_queue_length()
            failed_jobs = get_failed_jobs()
            avg_processing_time = get_avg_processing_time()

            self.gauge("gbd.macess.queue_length", queue_length, tags=["app:macess", "env:prod"])
            self.gauge("gbd.macess.jobs.failed", failed_jobs, tags=["app:macess", "env:prod"])
            self.gauge("gbd.macess.processing_time.avg", avg_processing_time, tags=["app:macess", "env:prod"])

        except Exception as e:
            self.log.error(f"MACESS metric collection failed: {e}")
