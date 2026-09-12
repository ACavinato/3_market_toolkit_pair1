# Component B — market-toolkit

**Weight:** 25% of the course grade
**Team:** Pairs (2 people)
**Duration:** Session 3 → Session 4 (final push at end of Session 4)
**Repo:** shared class repo — you'll be added at the start of Session 3

---

## What you're building

A small, tested Python toolkit that:

1. Loads and cleans a folder of daily price CSVs
2. Computes standard return metrics (daily returns, cumulative returns, annualized volatility, Sharpe ratio, max drawdown)
3. Produces a summary plot of cumulative returns

The starter repo (`market-toolkit`) has:

- Sample data for 3 tickers in `data/raw/`
- Function skeletons in `src/` with docstrings and `# TODO` comments telling you exactly what to do
- Complete tests in `tests/` — these define the contract
- A skeleton bash script in `scripts/`

You are **done** when:

```bash
pytest tests/ -v                    # all 25 tests green
./scripts/fetch_prices.sh           # produces a summary + a log file
python -m src.demo                  # prints summary, saves outputs/cumulative_returns.png
```

---

## What each partner owns

| Partner A owns | Partner B owns | Shared (both edit) |
|---|---|---|
| `src/ingest.py` | `src/metrics.py` | `README.md` |
| `scripts/fetch_prices.sh` | `src/demo.py` | `requirements.txt` |
| — makes `tests/test_ingest.py` pass | — makes `tests/test_metrics.py` pass | |

You will **each** open at least 2 PRs. You will **each** review at least 2 of your partner's PRs — with real comments, not just "LGTM."

**Both partners edit `README.md` and `requirements.txt`.** Natural merge conflicts will happen on these files. Resolve them using what you learned in Session 3 — and mention how you resolved them in the PR description.

---

## Workflow — mandatory

Every change goes through this loop. No exceptions.

```
git switch -c feature/<what-you-are-doing>
# ... edit, save, run tests ...
git add <files>
git commit -m "Meaningful message"
git push -u origin feature/<what-you-are-doing>
# open PR on GitHub  →  assign your partner as reviewer
# they review, comment, request changes
# you push fixes to the SAME branch
# they approve
# you merge, delete the branch
```

**Rules:**

- Never push directly to `main`. Direct commits to `main` will cost you points.
- No PR gets merged with a failing test suite. Run `pytest` before you open the PR.
- No PR gets merged without a review from your partner. Not even tiny ones.
- Keep PRs small. One PR = one logical change. If your diff is over ~200 lines, split it.

---

## How to check yourself

At any point, run:

```bash
python -m venv .venv
source .venv/bin/activate                 # macOS / Linux / Git Bash on Windows
pip install -r requirements.txt
pytest tests/ -v
```

- Every red test line tells you what to fix.
- Green everywhere = your side of the code works.
- When both sides are green AND merged AND the demo script runs, you're done.

---

## Grading (individual — you and your partner get separate grades)

| Criterion | Weight | What we look at |
|---|---|---|
| **Branch discipline** | 20% | Named clearly (`feature/…`, `fix/…`). Kept up to date with `main`. No 40-commit "wip wip wip" branches. |
| **PR quality** | 25% | Small, focused, well-titled. Description says WHY. Diff readable. |
| **Review quality** | 25% | You leave real, useful comments on your partner's PRs — questions, suggestions, catches. Not rubber-stamp "LGTM." |
| **`main` stays green** | 15% | Tests pass on `main` at all times. If you broke it, you reverted fast. |
| **Code correctness** | 15% | Tests pass. Demo runs. Bash script works. |

You are graded on **your** contributions, not the pair's. If your partner disappears, tell the instructor early — you will not be penalised for someone else's absence, but you must document it in writing.

---

## Deadlines

| When | What |
|---|---|
| End of Session 3 | Both partners have joined the repo, created a branch, pushed one commit. |
| Mid-week between S3 and S4 | Each of you has opened at least one real PR. Do NOT merge yet. |
| End of Session 4 | All work merged to `main`. Tests green. Demo runs. Tag the commit `component-b-submit`. |

---

## Getting help

- **Stuck on your own code?** Look at the docstring, then the TODOs, then the failing test message. In that order.
- **Stuck on git?** Session 3 slides + `git status` + your partner. In that order.
- **Really stuck?** Ask on Slack `#msa-dati07`. Include: the command you ran, the full error, what you expected.

You may use LLM assistants to explain concepts or debug errors. You may NOT paste the tests into an LLM and ask it to write the implementation — this defeats the point and will show up in the review.
