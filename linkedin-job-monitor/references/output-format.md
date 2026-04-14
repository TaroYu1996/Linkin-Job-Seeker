# Output Format

Digest must be brief and suitable for internal chat delivery.

## Header

- Short summary line: counts of fetched, matched, and shown jobs.

## Item template

For each job:
1. `Title — Company`
2. `Location | Work mode | Salary`
3. `Why matched: <short reason>`
4. `Link: <job_url>`

## Constraints

- Respect `max_results_per_digest`.
- Keep each item to a few short lines.
- Include enough detail for quick triage.
