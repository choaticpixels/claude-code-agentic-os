# Builder workflow

Request → target inspection → brief and assumptions → real file changes →
relevant validation → documented setup → evidence and handoff.

The next user-invoked auditor compares the result against the brief, reports
concrete defects and records unknowns. A repair request starts another build
increment. Wrap-up captures the actual result, even if it remains partial.

Default new app target: projects/<name>/ under the current workspace. Installed
kits work in the selected target repository. Parent workspace instructions are
not automatically a portable installation in a sibling repository.
