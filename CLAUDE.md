# Working on Flying Words

## Rule: read code with Haiku; change and review it with the main model

This rule is required for every task in this repository.

1. **Reading is done by a Haiku subagent.** Whenever you need to read, search or understand code (explore files, find where something lives, work out how a part works, see what a diff changed), hand it to the `code-reader` agent (`.claude/agents/code-reader.md`, which runs on Haiku). If that agent isn't available, use the Agent tool with `model: "haiku"`. Don't read through code in the main session.
2. **Ask for exactly what you need.** Tell the subagent what to find, and have it report file paths, line numbers, the few snippets that matter and a short summary, not whole files.
3. **Changes are made by the main session**, on the session's own model and effort. That covers modifying, fixing, tuning and testing. Subagents only read: they never edit, write, commit or push.
4. **Only the lines you'll touch.** The Edit tool needs a fresh read of a file before it can change it. So right before an edit, the main session reads just the lines it's about to change, using the line numbers the subagent gave. That is not a reason to read whole files in the main session.
5. **Code review always uses the current model, never Haiku.** Haiku only locates and reports code and changes. Reviewing means judging whether code or a change is correct, finding bugs, assessing security, or running `/code-review` or `/security-review`. The current model (and effort) does it, in the main session or in subagents that inherit the current model. Never pass `model: "haiku"` to review work, and never hand a review to `code-reader`. A reviewer reads the code it is reviewing for itself.

## How to work

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:

- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:

- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

These guidelines are working if: fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
