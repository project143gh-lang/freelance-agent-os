import json
import os
from memory.store import NormalizedStore

class MonitorService:
    """RAG-inspired service to monitor and query OS data."""
    def __init__(self):
        self.name = "monitor_service"
        self.store = NormalizedStore()

    def execute(self, query):
        # Simple RAG Implementation:
        # 1. Retrieve relevant data from memory and store
        # 2. Provide it as context to the Brain
        
        data = self.store.data
        sessions = data.get("sessions", {})
        global_k = data.get("global_knowledge", {})
        
        # Flatten session data for searching
        flat_history = []
        for sid, steps in sessions.items():
            for step_id, content in steps.items():
                flat_history.append(f"Session {sid} {step_id}: {content}")
        
        # Basic Keyword Retrieval (Simulating Vector Search)
        keywords = query.lower().split()
        relevant_docs = [doc for doc in flat_history if any(k in doc.lower() for k in keywords)]
        
        if not relevant_docs:
            return "MONITOR_RESULT: No specific data found in history for this query. Check Notion for external records."
        
        context_block = "\n".join(relevant_docs[-10:]) # Last 10 matches
        return f"MONITOR_RESULT: Based on internal OS logs:\n{context_block}"

    def get_earnings_summary(self):
        # Specific structured query
        return self.execute("earnings money income")

    def get_pending_apps(self):
        # Specific structured query
        return self.execute("pending application status")
