"""
Type definitions for the pymcp package.

This module provides type definitions used throughout the pymcp package.
"""

from typing import Any

from pydantic import BaseModel


class Tool(BaseModel):
    """MCP Tool definition."""

    name: str
    description: str | None = None
    inputSchema: dict[str, Any] = {}
    outputSchema: dict[str, Any] | None = None


class TextContent(BaseModel):
    """Text content returned by an MCP tool."""

    type: str = "text"
    text: str
    mime_type: str | None = "text/plain"


class ToolResult(BaseModel):
    """Result of a tool execution."""

    content: list[TextContent | dict[str, Any]]
    isError: bool = False
