#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "httpx",
#   "pydantic",
# ]
# ///
"""
Universal event sender for Claude Code observability.
Sends events to the observability server with graceful failure handling.
"""

import sys
import json
import httpx
import argparse
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class EventPayload(BaseModel):
    """Structure for events sent to observability server."""
    source_app: str = Field(..., description="Application name")
    session_id: str = Field(..., description="Claude session ID")
    hook_event_type: str = Field(..., description="Type of hook event")
    payload: Dict[str, Any] = Field(default_factory=dict)
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    chat_transcript: Optional[str] = None
    summary: Optional[str] = None

def send_to_server(event: EventPayload, server_url: str = "http://localhost:4000") -> bool:
    """
    Send event to observability server.
    Returns True if successful, False otherwise.
    """
    try:
        with httpx.Client(timeout=2.0) as client:
            response = client.post(
                f"{server_url}/events",
                json=event.model_dump(exclude_none=True),
                headers={"Content-Type": "application/json"}
            )
            return response.status_code == 200
    except Exception:
        # Silently fail if server is not available
        return False

def main():
    parser = argparse.ArgumentParser(description="Send events to observability server")
    parser.add_argument("--source-app", required=True, help="Source application name")
    parser.add_argument("--event-type", required=True, help="Event type")
    parser.add_argument("--server-url", default="http://localhost:4000", help="Server URL")
    parser.add_argument("--add-chat", action="store_true", help="Include chat transcript")
    parser.add_argument("--summarize", action="store_true", help="Add AI summary")
    
    args = parser.parse_args()
    
    try:
        # Read hook payload from stdin
        hook_data = json.loads(sys.stdin.read())
        
        # Extract session ID
        session_id = hook_data.get("sessionId", "unknown")
        
        # Create event payload
        event = EventPayload(
            source_app=args.source_app,
            session_id=session_id,
            hook_event_type=args.event_type,
            payload=hook_data
        )
        
        # Add chat transcript if requested
        if args.add_chat and "chatTranscript" in hook_data:
            event.chat_transcript = json.dumps(hook_data["chatTranscript"])
        
        # Send to server (fails gracefully)
        success = send_to_server(event, args.server_url)
        
        # Exit successfully regardless of server status
        sys.exit(0)
        
    except Exception:
        # Fail silently to not disrupt Claude Code
        sys.exit(0)

if __name__ == "__main__":
    main()