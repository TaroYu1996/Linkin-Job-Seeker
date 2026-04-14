---
name: linkedin-job-monitor
description: Monitor LinkedIn jobs with a reusable, profile-driven workflow. Use when a user wants to set up or run recurring LinkedIn job discovery, update job criteria conversationally, deduplicate previously seen postings, rank matches, and produce a concise internal chat digest for OpenClaw/QClaw delivery.
---

# LinkedIn Job Monitor

Use this skill to run an end-to-end LinkedIn job monitoring flow with reusable profile configuration and deterministic filtering/ranking.

## Workflow

1. Determine profile state.
   - If no profile exists, run conversational setup using `scripts/collect_profile.py` and validate with `scripts/config_schema.py`.
   - If profile exists, run monitor immediately with `scripts/run_monitor.py`.
   - If user requests updates, apply partial updates only to requested fields via `merge_profile_update`.
2. Fetch jobs from the authenticated LinkedIn search URL using `scripts/fetch_linkedin_jobs.py`.
3. Normalize scraped jobs with `scripts/normalize_jobs.py`.
4. Apply strict profile-driven filters via `scripts/apply_filters.py`.
5. Deduplicate against state with `scripts/dedupe_jobs.py`.
6. Score and rank matches using `scripts/score_jobs.py`.
7. Produce brief chat digest via `scripts/summarize_matches.py`.

## Required inputs

- Authenticated LinkedIn browsing/session capability in the runtime.
- Profile fields defined in `references/filter-schema.md`.

## State management guidance

- Persist profile JSON per user/workspace.
- Persist dedupe state JSON per profile/search context.
- Keep `dedupe_window_days` and `runs_per_day` in profile for scheduler integration.

## Resource map

- Setup guidance: `references/setup-flow.md`
- Profile schema semantics: `references/filter-schema.md`
- Ranking approach: `references/scoring-rules.md`
- Dedupe behavior: `references/dedupe-policy.md`
- Digest shape: `references/output-format.md`

## Execution notes

- Keep filtering and ranking configuration-driven; avoid role-specific hardcoding in scripts.
- Keep digest concise for internal chat.
- Leave LinkedIn browser/session adapter details in the fetch layer only.
