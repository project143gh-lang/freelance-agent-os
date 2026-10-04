# FreelanceOS

A comprehensive AI agent platform for freelancers. Manage projects, clients, and automate your workflow with intelligent agents.

## Features

- **Multi-Agent System**: Specialized agents for different tasks
- **Persona Management**: Switch between different agent personalities
- **Service Architecture**: Modular microservices design
- **Memory System**: Persistent memory across sessions
- **Task Automation**: Automate repetitive freelance tasks

## Architecture

```
FreelanceOS/
├── kernel/                 # Core brain and persona management
│   ├── brain.py           # Core reasoning engine
│   ├── kernel.py          # Main kernel
│   └── persona_manager.py # Persona switching
├── services/              # Microservices
│   ├── scoring_service.py
│   ├── scheduler_service.py
│   ├── research_service.py
│   ├── portfolio_service.py
│   ├── notion_service.py
│   ├── monitor_service.py
│   ├── email_service.py
│   ├── deployment_service.py
│   └── browser_service.py
├── skills/                # Agent skills
│   ├── web_intelligence.py
│   ├── outreach_pipeline.py
│   ├── lead_gen_automation.py
│   └── dynamic_portfolio_gen.py
├── personas/              # Agent personas
│   ├── scout.yaml
│   ├── researcher.yaml
│   ├── closer.yaml
│   └── accountant.yaml
└── memory/                # Persistent storage
    └── store.py
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the platform
python main.py
```

## Personas

- **Scout**: Finds opportunities and leads
- **Researcher**: Gathers information and insights
- **Closer**: Handles client communication and deals
- **Accountant**: Manages finances and billing

## License

MIT
