"""Helpers for building and updating a validated monitor profile."""

from __future__ import annotations

from typing import Any, Mapping

from config_schema import apply_defaults, validate_profile


def parse_profile_input(conversation_fields: Mapping[str, Any]) -> dict[str, Any]:
    """Convert conversationally gathered fields into a normalized profile."""
    return validate_profile(conversation_fields)


def merge_profile_update(existing_profile: Mapping[str, Any], updates: Mapping[str, Any]) -> dict[str, Any]:
    """Apply partial field updates while preserving untouched fields."""
    merged = apply_defaults(existing_profile)
    for key, value in updates.items():
        merged[key] = value
    return validate_profile(merged)


def profile_exists(profile: Mapping[str, Any] | None) -> bool:
    """Check if a profile is available and appears minimally complete."""
    if not profile:
        return False
    candidate = apply_defaults(profile)
    return bool(candidate.get("search_url") and candidate.get("target_roles") and candidate.get("regions"))


def required_setup_fields() -> list[str]:
    """Return the minimum fields needed for first-time setup."""
    return ["search_url", "target_roles", "regions", "allowed_location_types"]
