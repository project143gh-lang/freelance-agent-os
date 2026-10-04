import os
from kernel.brain import LocalBrain

class PortfolioService:
    """Service to dynamically generate high-converting HTML portfolios."""
    def __init__(self):
        self.name = "portfolio_service"
        self.output_dir = "C:/Users/ADMIN/FreelanceOS/web"
        self.brain = LocalBrain()

    def execute(self, args):
        # args should be the client name or role context
        print(f"[PortfolioService] Generating tailored portfolio for: {args}")
        
        # We use the Brain to generate the HTML/CSS content based on the context
        prompt = (
            f"Create a professional, modern, single-page HTML portfolio for a freelancer "
            f"targeting {args}. Use a clean, dark-themed design with Tailwind CSS (via CDN). "
            f"Include sections for: Hero (with a strong value prop), Skills, "
            f"Featured Projects (placeholder content), and a Call to Action. "
            f"Make the copy highly persuasive and focused on ROI. "
            f"Return ONLY the full HTML code, starting with <!DOCTYPE html>."
        )
        
        html_content = self.brain.chat(prompt)
        
        # Clean up the response in case the brain added markdown backticks
        if "```html" in html_content:
            html_content = html_content.split("```html")[1].split("```")[0].strip()
        elif "```" in html_content:
            html_content = html_content.split("```")[1].split("```")[0].strip()

        # Create a filename based on the target
        filename = f"portfolio_{args.replace(' ', '_').lower()}.html"
        file_path = os.path.join(self.output_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        return f"PORTFOLIO_SUCCESS: Tailored portfolio generated at {file_path}. You can now link this in your cold emails."

    def generate_for_client(self, client_name):
        return self.execute(client_name)
