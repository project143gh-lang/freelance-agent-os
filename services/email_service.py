import subprocess

class EmailService:
    """Wrapper for the Himalaya skill to handle client communications."""
    def __init__(self):
        self.name = "email_service"

    def execute(self, args):
        print(f"[EmailService] Handling email: {args}")
        # Logic to call 'hermes skill himalaya'
        return f"EMAIL_SUCCESS: Communication sent/received: {args}"

    def send_proposal(self, email, content):
        return self.execute(f"Sending proposal to {email}")

    def send_cold_email(self, email, template_id, lead_details):
        # Combines template with lead details for personalization
        personalized_content = f"Hi {lead_details.get('name', 'there')}, I noticed you are working on {lead_details.get('project', 'some great things')}..."
        return self.execute(f"Sending COLD EMAIL to {email} using template {template_id}. Content: {personalized_content[:50]}...")

    def triage_inbox(self):
        return self.execute("Triage latest client emails")
