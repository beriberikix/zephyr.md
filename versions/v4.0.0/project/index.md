---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/project/index.html
original_path: project/index.html
---

# Project and Governance

The Zephyr project defines a development process workflow using GitHub
**Issues** to track feature, enhancement, and bug reports together with GitHub
**Pull Requests** (PRs) for submitting and reviewing changes. Zephyr
community members work together to review these Issues and PRs, managing
feature enhancements and quality improvements of Zephyr through its regular
releases, as outlined in the
[program management overview](https://wiki.zephyrproject.org/Program-Management).

We can only manage the volume of Issues and PRs, by requiring timely reviews,
feedback, and responses from the community and contributors, both for initial
submissions and for followup questions and clarifications. Read about the
project’s [development processes and tools](dev_env_and_tools.md#dev-environment-and-tools)
and specifics about [review timelines](dev_env_and_tools.md#review-time) to learn about the
project’s goals and guidelines for our active developer community.

[TSC Project Roles](project_roles.md#project-roles) describes in detail the Zephyr project roles and associated permissions
with respect to the development process workflow.

## Terminology

- mainline: The main tree where the core functionality and core features are
  being developed.
- subsystem/feature branch: is a branch within the same repository. In our case,
  we will use the term branch also when referencing branches not in the same
  repository, which are a copy of a repository sharing the same history.
- upstream: A parent branch the source code is based on. This is the branch you
  pull from and push to, basically your upstream.
- LTS: Long Term Support
