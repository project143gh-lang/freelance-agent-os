import json
import os
from datetime import datetime

class SchedulerService:
    """Service to manage autonomous background workers for Freelance-OS."""
    def __init__(self):
        self.name = "scheduler_service"
        self.schedule_file = "C:/Users/ADMIN/FreelanceOS/memory/schedule.json"
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if os.path.exists(self.schedule_file):
            with open(self.schedule_file, 'r') as f:
                return json.load(f)
        return []

    def _save_tasks(self):
        with open(self.schedule_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def execute(self, args):
        # Expected args: "SCHEDULE <time> <action>" (e.g., "SCHEDULE 08:00 scout_gigs")
        parts = args.split()
        if len(parts) < 3 or parts[0].upper() != "SCHEDULE":
            return "SCHEDULER_ERROR: Use format 'SCHEDULE <HH:MM> <action_name>'"

        time, action = parts[1], " ".join(parts[2:])
        task = {"time": time, "action": action, "last_run": None, "status": "active"}
        self.tasks.append(task)
        self._save_tasks()
        
        return f"SCHEDULE_SUCCESS: Task '{action}' scheduled for {time} daily."

    def list_tasks(self):
        return f"ACTIVE_SCHEDULE: {json.dumps(self.tasks, indent=2)}"

    def run_due_tasks(self, kernel):
        """This would be called by a background system process."""
        now = datetime.now().strftime("%H:%M")
        executed = []
        for task in self.tasks:
            if task['time'] == now and task['status'] == 'active':
                print(f"[Scheduler] Triggering autonomous task: {task['action']}")
                result = kernel.run(task['action'])
                executed.append(f"{task['action']} -> {result}")
                task['last_run'] = now
        
        self._save_tasks()
        return executed if executed else None
