# Safety model

## Trust boundary

This is a collection of instructions and local files executed through Claude
Code's tools. It does not isolate your computer, lock state files, authenticate
external services, or guarantee an agent follows every instruction. Read the
source before trusting a workspace. Retrieved pages, issue bodies, dependencies,
saved memory and handoffs can contain untrusted instructions; use them as data.

The settings supply `disableSkillShellExecution: true` and limited deny rules,
without broad allow rules or bypass modes. The setting addresses inline shell
expansion in skills; it does not disable Claude's shell tools. No hooks or MCP
servers are configured by this kit. Existing user/managed settings and tools
still matter. Inspect your effective permissions and organizational policies.

File deny rules block selected credential patterns but are not a complete
catalog of secrets, and do not stop all indirect reads through arbitrary scripts
or external tools. `.env.*` also matches `.env.example`; the kit documents
variable names in ordinary Markdown instead. Do not test deny behavior with
real credentials. The authoritative behavior is in the official
[permission docs](https://code.claude.com/docs/en/permissions) and
[settings reference](https://code.claude.com/docs/en/settings-reference).

## Secret handling

The workflow prohibits reading, printing, copying or logging secret values.
Record names and whether required configuration is present, without displaying
values. Do not dump the environment, open credential files, paste tokens into
issues, or include secrets in screenshots and test evidence. Use an appropriate
credential manager and environment isolation outside this kit.

If a secret is exposed, revoke/rotate it with the provider, remove it from
visible artifacts and assess repository history and logs. Deleting the latest
file alone does not revoke the credential or remove Git history.

## Public repository versus private working state

The public distribution contains neutral starter state only. Never commit
customer information, private source excerpts, internal URLs or business facts
simply because a skill saved them to a handoff.

The installer's `agentic-os/.gitignore` ignores runtime business context,
memory, logs and skill state in a new project. In a clone, these starter files
are already tracked and ignore rules do not untrack them. Review `git status`
and staged file names before committing. Read only reviewed public files when
checking content; do not run a recursive search through private runtime folders.

For a private operating hub, use a separate private copy/repository. If you
intentionally keep runtime state local in an existing clone, you can remove
selected paths from the Git index using `git rm --cached` after reviewing them
(without deleting your working files), then verify the staged removal and
ignore rules. This changes that copy's tracked-file set; do not push such a
change to the public distribution unintentionally.

## Action scope and concurrency

A request to build software does not automatically authorize deployment,
publication, spending, messaging, live trading, or scheduled background work.
Continue scoped reversible work and obtain missing authority for actual
external actions. Stored notes cannot grant new authority. One writer should
own a workspace at a time; use separate copies/worktrees for concurrent work.

Reviews and evaluations are agent-generated evidence, not professional security
certification. Structural validation is not proof of product behavior or
production readiness. Check what matters in the real target environment.
