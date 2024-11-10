# utils/performance_metrics.py

import time
import logging

class PerformanceMetrics:
    def __init__(self):
        """Initialize performance metrics tracking."""
        self.start_time = time.time()
        self.metrics = {}

    def start_timer(self, metric_name):
        """Start a timer for a specific metric."""
        self.metrics[metric_name] = {'start': time.time(), 'end': None}

    def stop_timer(self, metric_name):
        """Stop the timer for a specific metric and log the duration."""
        if metric_name in self.metrics:
            self.metrics[metric_name]['end'] = time.time()
            duration = self.metrics[metric_name]['end'] - self.metrics[metric_name]['start']
            logging.info(f"Performance Metric - {metric_name}: {duration:.4f} seconds")
        else:
            logging.warning(f"Metric '{metric_name}' not found. Cannot stop timer.")

    def get_duration(self, metric_name):
        """Get the duration of a specific metric."""
        if metric_name in self.metrics and self.metrics[metric_name]['end'] is not None:
            return self.metrics[metric_name]['end'] - self.metrics[metric_name]['start']
        return None
