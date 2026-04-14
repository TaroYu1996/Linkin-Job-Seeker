"""Build a brief digest suitable for internal chat delivery."""

from __future__ import annotations

from score_jobs import ScoredJob


def _salary_line(job: ScoredJob) -> str:
    j = job.job
    if j.salary_min_cad is None:
        return j.salary_text or "n/a"
    if j.salary_max_cad and j.salary_max_cad != j.salary_min_cad:
        return f"CAD {j.salary_min_cad:,}-{j.salary_max_cad:,}"
    return f"CAD {j.salary_min_cad:,}"


def summarize_matches(scored_jobs: list[ScoredJob], fetched_count: int, rejected_count: int, max_items: int) -> str:
    shown = scored_jobs[:max_items]
    lines: list[str] = [
        f"LinkedIn monitor digest: fetched={fetched_count}, matched={len(scored_jobs)}, shown={len(shown)}, filtered_out={rejected_count}"
    ]

    if not shown:
        lines.append("No new or updated matches met your profile criteria in this run.")
        return "\n".join(lines)

    for idx, scored in enumerate(shown, start=1):
        job = scored.job
        reason = ", ".join(scored.reasons[:3]) if scored.reasons else "profile_match"
        lines.extend(
            [
                f"{idx}. {job.title} — {job.company}",
                f"   {job.location_text} | {job.location_type} | {_salary_line(scored)}",
                f"   Why matched: {reason} | score={scored.score} | status={scored.dedupe_status}",
                f"   Link: {job.job_url}",
            ]
        )

    return "\n".join(lines)
