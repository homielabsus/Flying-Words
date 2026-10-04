# Working on Flying Words

## Rule: read code with Haiku, change it with the main model

This rule is required for every task in this repository.

1. **Reading is done by a Haiku subagent.** Whenever you need to read, search or understand code (explore files, find where something lives, work out how a part works, look over a diff), hand it to the `code-reader` agent (`.claude/agents/code-reader.md`, which runs on Haiku). If that agent isn't available, use the Agent tool with `model: "haiku"`. Don't read through code in the main session.
2. **Ask for exactly what you need.** Tell the subagent what to find, and have it report file paths, line numbers, the few snippets that matter and a short summary, not whole files.
3. **Changes are made by the main session**, on the session's own model and effort. That covers modifying, fixing, tuning and testing. Subagents only read: they never edit, write, commit or push.
4. **Only the lines you'll touch.** The Edit tool needs a fresh read of a file before it can change it. So right before an edit, the main session reads just the lines it's about to change, using the line numbers the subagent gave. That is not a reason to read whole files in the main session.
