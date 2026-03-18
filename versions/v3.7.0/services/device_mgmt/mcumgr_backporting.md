---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/device_mgmt/mcumgr_backporting.html
original_path: services/device_mgmt/mcumgr_backporting.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Fixing and backporting fixes to Zephyr v2.7 MCUmgr

The processes described in this document apply to both the zephyr repository itself and the MCUmgr [module](../../develop/modules.md#modules) defined in [west.yml](https://github.com/zephyrproject-rtos/zephyr/blob/main/west.yml).

Note

Currently, the backporting process, described in this document, is required only when providing
changes to Zephyr version 2.7 LTS

There are two different processes: one for issues that have also been fixed in the current
version of Zephyr (backports), and one for issues that are being fixed only in a previous version.

The upstream MCUmgr repository is located [in this page](https://github.com/apache/mynewt-mcumgr).
The Zephyr fork used in version 2.7 and earlier is [located here](https://github.com/zephyrproject-rtos/mcumgr).
Versions of Zephyr past 2.7 use the MCUmgr library that is [part of the Zephyr code base](https://github.com/zephyrproject-rtos/zephyr/tree/main/subsys/mgmt/mcumgr).

## Possible origins of a code change

In Zephyr version 2.7 and earlier, you must first apply the fix
to the upstream repository of MCUmgr and then bring it to Zephyr with snapshot updates.

As such, there are four possible ways to apply a change to the 2.7 branch:

> - The fix, done directly to the Zephyr held code of the MCUmgr library, is backported to the `v2.7-branch`.
> - The fix, ported to the Zephyr held code from the upstream repository, is backported to the `v2.7-branch`.
> - The fix, done upstream and no longer relevant to the current version, is directly backported
>   :   to the `v2.7-branch`.
> - The fix, not present upstream and not relevant for the current version of Zephyr, is
>   :   directly applied to the `v2.7-branch`.

The first three cases are cases of *backports* , the last one is a case of a *new fix* and has no
corresponding fix in the current version.

## Applying fixes to previous versions of MCUmgr

This section indicates how to apply fixes to previous versions of MCUmgr.

### Creating a bug report

Every proposed fix requires a bug report submitted for the specified version of Zephyr affected by the bug.

In case the reported bug in a previous version has already been fixed in the current version, the description
of the bug must be copied with the following:

- Additional references to the bug in the current version
- The PR for the current version
- The SHAs of the commits, if the PR has already been merged

You must also apply the `backport v2.7-branch` label to the bug report.

### Creating the pull request for the fix

You can either create a *backport pull request* or a *new-fix pull request*.

#### Creating backport pull requests

Backporting a fix means that some or all of the fix commits, as they exist in the current version,
are ported to a previous version.

Note

Backporting requires the fix for the current version to be already merged.

To create a backport pull request, do the following:

1. Port the fix commits from the current version to the previous version.
   Even if some of the commits require changes, keep the commit messages of all the ported commits
   as close to the ones in the original commits as possible, adding the following line:

```text
"Backporting commit <sha>"

``<sha>`` indicates the SHA of the commit after it has been already merged in the current version.
```

1. Create the pull request selecting `v2.7-branch` as the merge target.
2. Update `west.yml` within Zephyr, creating a pull-request to update the MCUmgr library referenced in
   Zephyr 2.7.

#### Creating new-fix pull requests

When the fix needed does not have a corresponding fix in the current version, the bug report
must follow the ordinary process.

1. Create the pull request selecting `v2.7-branch` as the merge target.
2. Update `west.yml` within Zephyr, creating a pull-request to update the MCUmgr library referenced in
   Zephyr 2.7.

## Configuration management

This chapter describes the maintainers’ side of accepting and merging fixes and backports.

### Prerequisites

As a maintainer, these are the steps required before proceeding with the merge process:

1. Check if the author has followed the correct steps that are required to apply the fix, as described in
[Applying fixes to previous versions of MCUmgr](#management-fixing-prev-mcumgr-submit).

1. Ensure that the author of the fix has also provided the `west.yml` update for Zephyr 2.7.

The specific merging process depends on where the fix comes from and whether it is a *backport* or a *new
fix*.

### Merging a backported fix

There are two possible sources of backports:

- The Zephyr code base
- A direct fix from upstream

Both cases are similar and differ only in the branch name.

To merge a backported fix after the pull request for the fix has gone through the review process,
as a maintainer, do the following:

1. Create a branch named as follow:

   ```text
   backport-<source>-<pr_num>-to_v2.7-branch
   ```

   `<source>` can be one of the following:

   - `upstream` - if the fix has originally been merged to the upstream repository.
   - `zephyr` - if the fix has been applied to the Zephyr internal MCUmgr library (past 2.7 versions).

   `<pr_num>` is the number of the original pull request that has already been merged.

   For example, a branch named `backport-upstream-137-to-v2.7-branch` indicates a backport of pull
   request 137, which has already been merged to the upstream repository of MCUmgr.
2. Push the reviewed pull-request branch to the newly created branch and merge the backport branch
   to `v2.7-branch`.

### Merging a new fix

Merging a new fix, that is not a backport of either any upstream or Zephyr fix, does not require any special
treatment. Apply the fix directly at the top of `v2.7-branch`.

### Merge west.yml

As an MCUmgr maintainer, you may not be able to merge the `west.yml` update, to introduce the fix to Zephyr.
However, you are responsible for such a merge to happen as soon as possible after the MCUmgr fixes have been
applied to the `v2.7-branch` of the MCUmgr.
