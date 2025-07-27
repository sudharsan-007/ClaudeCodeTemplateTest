# Observability System

This is an optional monitoring system for tracking Claude's development process in real-time.

## Quick Start

```bash
# Clone the observability system
git clone https://github.com/disler/claude-code-hooks-multi-agent-observability.git .

# Or copy from the existing example if available
# cp -r ../claude-code-hooks-multi-agent-observability/* .

# Start the system
./scripts/start-system.sh

# View dashboard
open http://localhost:5173
```

## Features

- Real-time event tracking
- Session visualization
- Tool usage monitoring
- Chat transcript viewing
- Performance metrics

## Integration

The template's hooks are already configured to send events to this server when it's running. If the server is not running, the hooks fail silently and don't interrupt development.

## Ports

- Server: http://localhost:4000
- Client: http://localhost:5173

For full documentation, see the README in claude-code-hooks-multi-agent-observability/