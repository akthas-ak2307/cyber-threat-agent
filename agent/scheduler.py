# agent/scheduler.py

import schedule
import time
import threading
from datetime import datetime

class ThreatScheduler:
    def __init__(self, interval_minutes=10):
        self.interval_minutes = interval_minutes
        self.is_running = False
        self.job_count = 0
        self._thread = None

    def _run_job(self, agent_function):
        """Wrapper that runs the agent function and tracks execution"""
        self.job_count += 1
        print(f"\n[SCHEDULER] ⏰ Job #{self.job_count} triggered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        try:
            agent_function()
            print(f"[SCHEDULER] ✅ Job #{self.job_count} completed successfully")
        except Exception as e:
            print(f"[SCHEDULER] ❌ Job #{self.job_count} failed: {e}")

    def start(self, agent_function, run_immediately=True):
        """
        Start the scheduler.
        - agent_function: the function to run on each tick (e.g., run_agent from main.py)
        - run_immediately: if True, runs once right away before scheduling
        """
        self.is_running = True

        if run_immediately:
            print("[SCHEDULER] 🚀 Running agent immediately on startup...")
            self._run_job(agent_function)

        # Schedule the recurring job
        schedule.every(self.interval_minutes).minutes.do(self._run_job, agent_function)
        print(f"[SCHEDULER] 🔁 Scheduled to run every {self.interval_minutes} minute(s)")
        print(f"[SCHEDULER] Next run at: {self._next_run_time()}")

        # Run the loop in a background thread (non-blocking)
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _loop(self):
        """Internal loop that keeps checking for pending jobs"""
        while self.is_running:
            schedule.run_pending()
            time.sleep(10)  # Check every 10 seconds

    def stop(self):
        """Gracefully stop the scheduler"""
        self.is_running = False
        schedule.clear()
        print("[SCHEDULER] 🛑 Scheduler stopped.")

    def _next_run_time(self):
        """Return the next scheduled run time as a string"""
        jobs = schedule.get_jobs()
        if jobs:
            return jobs[0].next_run.strftime('%Y-%m-%d %H:%M:%S')
        return "Not scheduled"

    def status(self):
        """Print current scheduler status"""
        print(f"""
[SCHEDULER STATUS]
  Running        : {self.is_running}
  Interval       : Every {self.interval_minutes} minute(s)
  Jobs Completed : {self.job_count}
  Next Run       : {self._next_run_time()}
        """)