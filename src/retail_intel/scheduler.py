from __future__ import annotations

import sys
from pathlib import Path

from apscheduler.schedulers.blocking import BlockingScheduler

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    from src.retail_intel.config import get_settings
    from src.retail_intel.pipeline import run_pipeline
else:
    from .config import get_settings
    from .pipeline import run_pipeline


def scheduled_refresh() -> None:
    result = run_pipeline()
    print(f"Refresh completed: {result}")


def run_scheduler() -> None:
    settings = get_settings()
    scheduler = BlockingScheduler(timezone="Asia/Yangon")
    if settings.refresh_mode == "interval":
        interval_minutes = max(1, settings.refresh_interval_minutes)
        scheduler.add_job(scheduled_refresh, "interval", minutes=interval_minutes)
        print(f"Scheduler started. Retail data refresh runs every {interval_minutes} minute(s).")
    else:
        scheduler.add_job(
            scheduled_refresh,
            "cron",
            hour=settings.refresh_hour,
            minute=settings.refresh_minute,
        )
        print(
            "Scheduler started. Retail data refresh runs daily at "
            f"{settings.refresh_hour:02d}:{settings.refresh_minute:02d} Asia/Yangon."
        )
    scheduler.start()


if __name__ == "__main__":
    run_scheduler()
