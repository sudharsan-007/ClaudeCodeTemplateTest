#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///
"""
Post-tool use hook for Claude Code.
Logs tool execution results and can provide feedback.
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

def log_tool_use(hook_data: dict):
    """Log tool use to file."""
    try:
        ensure_log_dir()
        
        # Create log entry
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": hook_data.get("sessionId", "unknown"),
            "tool_name": hook_data.get("toolName", ""),
            "tool_input": hook_data.get("toolInput", {}),
            "tool_response": hook_data.get("toolResponse", {}),
            "success": not hook_data.get("toolResponse", {}).get("error"),
        }
        
        # Append to log file
        log_file = LOG_DIR / "tool_use.jsonl"
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
    except Exception:
        # Silently fail to not disrupt Claude Code
        pass

def check_for_issues(hook_data: dict) -> tuple[bool, str]:
    """
    Check tool response for potential issues.
    Returns (has_issue, message).
    """
    tool_name = hook_data.get("toolName", "")
    tool_response = hook_data.get("toolResponse", {})
    
    # Check for common error patterns
    if tool_response.get("error"):
        return True, f"Tool {tool_name} failed with error"
    
    # Check for specific tool issues
    if tool_name == "Bash":
        output = tool_response.get("output", "")
        if "permission denied" in output.lower():
            return True, "Permission denied - check file permissions"
        if "command not found" in output.lower():
            return True, "Command not found - check if tool is installed"
    
    if tool_name in ["Write", "Edit", "MultiEdit"]:
        if not tool_response.get("success", True):
            return True, f"File operation failed - check path and permissions"
    
    return False, ""

def main():
    try:
        # Read hook payload from stdin
        hook_data = json.loads(sys.stdin.read())
        
        # Log the tool use
        log_tool_use(hook_data)
        
        # Check for issues
        has_issue, message = check_for_issues(hook_data)
        
        if has_issue:
            # Provide feedback but don't block
            output = {
                "decision": "block",
                "reason": message
            }
            print(json.dumps(output))
        
        sys.exit(0)
        
    except Exception:
        # Fail silently to not disrupt Claude Code
        sys.exit(0)

if __name__ == "__main__":
    main()