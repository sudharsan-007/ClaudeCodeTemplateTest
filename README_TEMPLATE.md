# Claude Start Template - PRD-Driven Development

A universal template for AI-assisted software development that transforms Product Requirements Documents (PRDs) into production-ready applications. Works with ANY tech stack and delivers complete, deployable solutions.

## 🎯 What This Template Does

1. **PRD → Production**: Converts requirements into deployable applications
2. **Universal**: Works with any programming language or framework
3. **Feature-Driven**: Implements new features from feature request documents
4. **Observable**: Optional real-time monitoring of AI development process

## 🚀 Quick Start

```bash
# 1. Clone the template
git clone https://github.com/yourusername/claude_start_template.git my-project
cd my-project

# 2. Add your requirements
cp docs/examples/PRD.md docs/PRD.md
# Edit docs/PRD.md with your product requirements

# 3. Start building with Claude
claude-code

# 4. (Optional) Monitor AI development
cd observability && ./scripts/start-system.sh
```

## 📋 How It Works

### 1. Document Your Requirements

Create one or more of these files:
- `docs/PRD.md` - Complete product requirements
- `docs/feature_request.md` - New feature to add
- `docs/requirements/*.md` - Multiple requirement docs
- `TODO.md` - Quick tasks and fixes

### 2. Claude Reads & Plans

Claude will:
1. Find and read all requirement documents
2. Create a task list from requirements
3. Ask clarifying questions if needed
4. Detect or ask about tech stack

### 3. Incremental Development

Claude builds your production-ready solution by:
- Implementing one feature at a time
- Testing each component
- Tracking progress with todos
- Following best practices for chosen stack

## 🏗️ Template Structure

```
claude_start_template/
│
├── docs/                       # Requirements & documentation
│   ├── examples/              # Example templates
│   │   ├── PRD.md            # PRD template
│   │   └── feature_request.md # Feature template
│   ├── PRD.md                # Your product requirements
│   └── feature_request.md    # Your feature requests
│
├── .claude/                   # Claude configuration
│   ├── settings.json         # Hook settings
│   └── hooks/               # Lifecycle hooks
│       ├── pre_tool_use.py  # Minimal safety checks
│       ├── post_tool_use.py # Result logging
│       └── send_event.py    # Optional observability
│
├── .mcp.json                 # MCP server configs
├── CLAUDE.md                # AI assistant instructions
├── requirements.txt         # Python dependencies
└── observability/           # Optional monitoring
```

## 📝 Writing Requirements

### PRD Structure
Your PRD should include:
- **Problem Statement**: What problem you're solving
- **User Stories**: Who uses it and why
- **Functional Requirements**: What it must do
- **Production Scope**: Complete feature set for deployment
- **Technical Preferences**: Any tech stack preferences

### Feature Request Structure
For adding features to existing projects:
- **Problem**: Why this feature is needed
- **Solution**: How it should work
- **Acceptance Criteria**: How to know it's done
- **Technical Details**: Implementation notes

See `docs/examples/` for complete templates.

## 🛠️ Supported Tech Stacks

This template works with ANY technology:

### Frontend
- React, Vue, Angular, Svelte
- Next.js, Nuxt, Astro, SvelteKit
- Vanilla HTML/CSS/JavaScript
- Mobile: React Native, Flutter

### Backend
- Node.js, Python, Ruby, Go, Rust, Java, PHP
- Express, FastAPI, Django, Rails, Spring
- REST, GraphQL, WebSockets

### Databases
- PostgreSQL, MySQL, MongoDB, SQLite
- Redis, Elasticsearch, Firebase

### Tools
- Docker, Kubernetes
- CI/CD pipelines
- Cloud services (AWS, GCP, Azure)

## 🔌 MCP Servers

Pre-configured Model Context Protocol servers:

### No API Key Required
- **filesystem**: File operations
- **memory**: Persistent context
- **git**: Version control
- **sqlite**: Database operations
- **fetch**: Web content
- **time**: Time operations
- **shell**: Shell commands
- **browser**: Web automation

### API Key Required
- **perplexity**: Web search (needs PERPLEXITY_API_KEY)
- **context7**: Context management

## 🔧 Configuration

### Environment Variables
Create `.env` file:
```bash
# Required
ANTHROPIC_API_KEY=your_key

# Optional
PERPLEXITY_API_KEY=your_key  # For web search
OPENAI_API_KEY=your_key      # For GPT models
```

### Python Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 👀 Observability (Optional)

Monitor AI development in real-time:

```bash
# Start observability server
cd observability
./scripts/start-system.sh

# Open dashboard
http://localhost:5173
```

Features:
- Track all AI actions
- View decision making
- Monitor progress
- Debug issues

## 🚦 Development Workflow

### Starting a New Project

1. **Write PRD**
   ```bash
   cp docs/examples/PRD.md docs/PRD.md
   # Edit with your requirements
   ```

2. **Start Claude**
   ```bash
   claude-code
   > "Read the PRD and start building the production solution"
   ```

3. **Monitor Progress** (Optional)
   ```bash
   # In another terminal
   cd observability && ./scripts/start-system.sh
   ```

### Adding Features

1. **Create Feature Request**
   ```bash
   cp docs/examples/feature_request.md docs/feature_request.md
   # Edit with feature details
   ```

2. **Implement Feature**
   ```bash
   claude-code
   > "Implement the feature request in docs/"
   ```

## 🛡️ Security & Safety

The template includes minimal, non-intrusive safety checks:
- Prevents catastrophic commands (rm -rf /)
- Protects private keys
- Logs actions for audit
- All checks use try-except (never block development)

## 📊 Best Practices

### For PRDs
1. Be specific about MVP features
2. Include user stories
3. Define success criteria
4. List technical constraints

### For Development
1. Let Claude read requirements first
2. Review the task plan
3. Test incrementally
4. Use observability for complex projects

### For Features
1. One feature per request
2. Clear acceptance criteria
3. Include examples/mockups
4. Specify integration points

## 🤝 Tips for Success

1. **Clear Requirements**: The better your PRD, the better the output
2. **Incremental Progress**: Build features one at a time
3. **Ask Questions**: Claude will ask for clarification when needed
4. **Use Examples**: Include mockups or examples in requirements
5. **Test Often**: Verify each feature works before moving on

## 🚀 Advanced Usage

### Multiple Agents
```bash
# Terminal 1: Frontend
claude-code --chat "Focus on frontend from the PRD"

# Terminal 2: Backend
claude-code --chat "Focus on backend API from the PRD"

# Terminal 3: Testing
claude-code --chat "Write tests for implemented features"
```

### Custom Hooks
Add project-specific validations in `.claude/hooks/`

### Project Types
While universal, you can hint at preferences:
- Add "Tech Stack" section in PRD
- Include framework-specific requirements
- Reference existing code patterns

## 📚 Examples

### SaaS Application
```markdown
# PRD.md
## Overview
Multi-tenant SaaS for project management

## Tech Stack (Preferred)
- Frontend: React + TypeScript
- Backend: Node.js + Express
- Database: PostgreSQL
```

### Mobile App
```markdown
# PRD.md
## Overview
Cross-platform mobile app for fitness tracking

## Tech Stack (Preferred)
- Framework: React Native
- Backend: Firebase
```

### CLI Tool
```markdown
# PRD.md
## Overview
Command-line tool for file organization

## Tech Stack (Preferred)
- Language: Python or Go
- Distribution: pip or homebrew
```

## 🐛 Troubleshooting

### Claude Can't Find Requirements
- Ensure files are in `docs/` directory
- Check file names match expected patterns
- Verify file permissions

### Hooks Blocking Development
- Hooks use try-except, shouldn't block
- Check `.claude/settings.json` formatting
- Temporarily disable hooks if needed

### Observability Not Connecting
- Ensure server is running (port 4000)
- Check firewall settings
- Verify `.claude/settings.json` has correct project name

## 📄 License

MIT License - Use freely in your projects

---

**Transform your ideas into working software. Write requirements, let Claude build!**