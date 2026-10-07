# FreelanceOS

A comprehensive AI agent platform for freelancers. Manage projects, clients, and automate your workflow with intelligent agents.

## 📸 Screenshot



**Start the platform:** Run `python main.py` to begin managing your freelance business.

## Features

### 🤰 Multi-Agent System
- **Specialized agents** for different tasks
- **Persona Management**: Switch between different agent personalities
- **Service Architecture**: Modular microservices design
- **Memory System**: Persistent memory across sessions
- **Task Automation**: Automate repetitive freelance tasks

### 👥 Personas (Built-In)

#### Scout
- Finds opportunities and leads
- Researches companies
- Generates leads
- Reports market trends

#### Researcher
- Gathers information and insights
- Deep research reports
- Market analysis
- Competitive intelligence

#### Closer
- Handles client communication
- Negotiates offers
- Manages relationships
- Deals finalization

#### Accountant
- Financial tracking and billing
- Revenue analysis
- Budget management
- Invoice generation

### 📁 Services (Modular Microservices)

#### Scoring Service
- Project scoring and ranking
- Priority assignment
- Compatibility algorithms

#### Scheduler Service
- Task scheduling
- Recurring jobs
- Cron-like functionality

#### Research Service
- Market research
- Company data gathering
- Trend analysis

#### Portfolio Service
- Project tracking
- Status management
- History logging

#### Notion Service
- Database integration
- Sync with Notion
- Data persistence

#### Monitor Service
- System health monitoring
- Performance metrics
- Alert notifications

#### Email Service
- Automated emails
- Template management
- Send/Track status

#### Deployment Service
- Platform deployment
- Configuration management

#### Browser Service
- Automated browsing
- Data extraction
- Web scraping

### 📊 Dashboard
- **Overview**: Current projects, clients, earnings
- **Projects**: Active, completed, paused projects
- **Clients**: Client list, contact info, history
- **Earnings**: Income tracking, invoices, payments
- **Tasks**: To-do list, deadlines, priorities

### 🔧 Customization
- Add new personas via YAML files
- Create custom services
- Extend existing functionality
- Integrate third-party APIs

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the platform
python main.py

# 3. Access the dashboard
# Open your browser to http://localhost:5000

# 4. Choose a persona
# - Scout: Find new opportunities
# - Research: Gather market intelligence
# - Closer: Handle client negotiations
# - Accountant: Manage finances
```

## 📁 Project Structure

```
FreelanceOS/
├── main.py             # Platform entry point
├── kernel/             # Core brain and persona management
│   ├── brain.py        # Core reasoning engine
│   ├── kernel.py       # Main kernel
│   └── persona_manager.py # Persona switching
├── services/           # Microservices
│   ├── scoring_service.py
│   ├── scheduler_service.py
│   ├── research_service.py
│   ├── portfolio_service.py
│   ├── notion_service.py
│   ├── monitor_service.py
│   ├── email_service.py
│   ├── deployment_service.py
│   └── browser_service.py
├── skills/             # Agent skills
│   ├── web_intelligence.py
│   ├── outreach_pipeline.py
│   ├── lead_gen_automation.py
│   └── dynamic_portfolio_gen.py
├── personas/           # Agent persona definitions
│   ├── scout.yaml
│   ├── researcher.yaml
│   ├── closer.yaml
│   └── accountant.yaml
└── memory/             # Persistent storage
    └── store.py
```

## 📜 License

MIT

---

**K.bhalavardt, MIT Student**
