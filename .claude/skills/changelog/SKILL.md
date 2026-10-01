---
name: changelog
description: Summarize recent commits in the repo since a tag into CHANGELOG.md.
context: fork                       # the verbose git log and diff reading stays in a fork. Only the finished summary returns to the main session
background: false                   # without this, a fork runs in the background and its result arrives later, looking like nothing happened
allowed-tools: [Bash, Read, Write]  # a real list — brackets belong here
argument-hint: "[since-tag]"        # a string - unquoted, yaml reads it as a list
---

Summarize the commits since the given tag (default: the latest tag). 
Group them under Added/Changed/Fixed, write the result to CHANGELOG.md, and return the summary in only 2 lines to the main session.