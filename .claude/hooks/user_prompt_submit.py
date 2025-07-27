#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///
"""
User prompt submit hook for Claude Code.
Logs prompts and can add context or validate input.
"""

import sys
import json
import os
from datetime import datetime
from pathlib import Path

# Log directory
LOG_DIR = Path(".claude/logs")

def ensure_log_dir():
    """Ensure log directory exists."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)

def log_prompt(prompt: str, session_id: str):
    """Log user prompt to file."""
    try:
        ensure_log_dir()
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id,
            "prompt": prompt,
        }
        
        log_file = LOG_DIR / "prompts.jsonl"
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
    except Exception:
        # Silently fail to not disrupt Claude Code
        pass

def add_project_context() -> str:
    """Add project-specific context to prompts."""
    context_parts = []
    
    # Add project type if CLAUDE.md exists
    if Path("CLAUDE.md").exists():
        context_parts.append("Project context is available in CLAUDE.md")
    
    # Add reminder about commands
    if Path("package.json").exists():
        context_parts.append("Remember to run 'npm run lint' and 'npm run test' after changes")
    elif Path("requirements.txt").exists():
        context_parts.append("Remember to run 'black .' and 'pytest' after changes")
    
    if context_parts:
        return "\n[Context: " + ". ".join(context_parts) + "]\n"
    return ""

def validate_prompt(prompt: str) -> tuple[bool, str]:
    """
    Validate user prompt for security issues.
    Returns (is_valid, error_message).
    """
    # Check for potential security issues
    dangerous_patterns = [
        "ignore all previous instructions",
        "disregard safety guidelines",
        "bypass security",
    ]
    
    prompt_lower = prompt.lower()
    for pattern in dangerous_patterns:
        if pattern in prompt_lower:
            return False, f"Prompt contains potentially dangerous pattern: {pattern}"
    
    return True, ""

def main():
    try:
        # Read hook payload from stdin
        hook_data = json.loads(sys.stdin.read())
        
        prompt = hook_data.get("prompt", "")
        session_id = hook_data.get("sessionId", "unknown")
        
        # Log the prompt
        log_prompt(prompt, session_id)
        
        # Validate prompt (optional - disabled by default)
        # is_valid, error = validate_prompt(prompt)
        # if not is_valid:
        #     print(f"BLOCKED: {error}", file=sys.stderr)
        #     sys.exit(2)
        
        # Add context (optional - can be enabled)
        # context = add_project_context()
        # if context:
        #     print(context)
        
        sys.exit(0)
        
    except Exception:
        # Fail silently to not disrupt Claude Code
        sys.exit(0)

if __name__ == "__main__":
    main()