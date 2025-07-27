#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///
"""
Pre-tool use hook for Claude Code.
Validates and potentially blocks dangerous tool usage.
"""

import sys
import json
import re
from typing import Dict, Any

# Dangerous patterns to block - only the most critical
DANGEROUS_PATTERNS = [
    r'rm\s+-rf\s+/',           # rm -rf / (root deletion)
    r'rm\s+-rf\s+\*',          # rm -rf * (bulk deletion)
    r'dd\s+.*of=/dev/[sh]d',   # dd to disk devices
    r'mkfs\.',                 # Format filesystem
    r'>\s*/dev/[sh]d',         # Write to disk devices
]

# Sensitive file patterns - only block direct private key access
SENSITIVE_FILES = [
    r'id_rsa$',                # Private SSH keys
    r'id_ed25519$',            # Private SSH keys
    r'\.pem$',                 # Private certificates
    r'private.*\.key$',        # Private key files
]

def is_dangerous_command(command: str) -> bool:
    """Check if command matches dangerous patterns."""
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return True
    return False

def accesses_sensitive_file(tool_input: Dict[str, Any]) -> bool:
    """Check if tool input accesses sensitive files."""
    # Check various fields that might contain file paths
    fields_to_check = ['file_path', 'path', 'filename', 'command']
    
    for field in fields_to_check:
        if field in tool_input:
            value = str(tool_input[field])
            for pattern in SENSITIVE_FILES:
                if re.search(pattern, value, re.IGNORECASE):
                    return True
    return False

def main():
    try:
        # Read hook payload from stdin
        hook_data = json.loads(sys.stdin.read())
        
        tool_name = hook_data.get("toolName", "")
        tool_input = hook_data.get("toolInput", {})
        
        # Check for dangerous bash commands
        if tool_name == "Bash" and "command" in tool_input:
            command = tool_input["command"]
            if is_dangerous_command(command):
                print(f"BLOCKED: Dangerous command detected: {command}", file=sys.stderr)
                sys.exit(2)
        
        # Check for sensitive file access
        if accesses_sensitive_file(tool_input):
            print("BLOCKED: Access to sensitive files is not allowed", file=sys.stderr)
            sys.exit(2)
        
        # Log the tool use (optional)
        # print(f"Tool use allowed: {tool_name}", file=sys.stderr)
        
        sys.exit(0)
        
    except Exception as e:
        # On error, allow tool use but log the issue
        print(f"Hook error: {e}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()