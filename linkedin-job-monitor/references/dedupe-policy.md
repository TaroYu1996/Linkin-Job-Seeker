# Dedupe Policy

## Keys

1. Primary key: normalized `job_url`.
2. Fallback key: normalized `title|company|location` tuple.

## State

Store per-key record with:
- `first_seen_at`
- `last_seen_at`
- `content_hash`
- last classification (`new|seen|updated`)

## Classification

- `new`: key not present within dedupe window.
- `seen`: key exists and content hash unchanged.
- `updated`: key exists and content hash changed.

## Resend rules

- Do not re-notify `seen` jobs within dedupe window.
- Allow `updated` jobs to be re-notified with update marker.
- Expire old state entries beyond retention horizon.
