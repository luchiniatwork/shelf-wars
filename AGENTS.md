# finding-fit

This repo is a Pi package / Agent Skills collection of expert board game design
skills. The skills live in `.agents/skills/<skill-name>/SKILL.md` (with
`references/` beside each) and are auto-discovered from this directory by
harnesses implementing the Agent Skills spec; `package.json` also declares them
for `pi install`.

When editing skills:

- Keep each `SKILL.md` self-sufficient for the common case (≤ ~350 lines); push
  bulk catalogs and tables into that skill's `references/` files.
- Frontmatter `name` must match the directory name; `description` (≤1024 chars)
  must state what the skill does and when to use it, with trigger phrases.
- Keep skill scopes disjoint; cross-reference siblings in "Related skills".
- Flag contested numbers `[contested]` rather than inventing precision.
- `research/skill-taxonomy.md` documents the scope contract.
