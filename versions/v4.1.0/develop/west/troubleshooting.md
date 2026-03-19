---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/west/troubleshooting.html
original_path: develop/west/troubleshooting.html
---

# Troubleshooting West

This page covers common issues with west and how to solve them.

## `west update` fetching failures

One good way to troubleshoot fetching issues is to run `west update` in
verbose mode, like this:

```shell
west -v update
```

The output includes Git commands run by west and their outputs. Look for
something like this:

```text
=== updating your_project (path/to/your/project):
west.manifest: your_project: checking if cloned
[...other west.manifest logs...]
--- your_project: fetching, need revision SOME_SHA
west.manifest: running 'git fetch ... https://github.com/your-username/your_project ...' in /some/directory
```

The `git fetch` command example in the last line above is what needs to
succeed.

One strategy is to go to `/path/to/your/project`, copy/paste and run the entire
`git fetch` command, then debug from there using the documentation for your
credential storage helper.

If you’re behind a corporate firewall and may have proxy or other issues,
`curl -v FETCH_URL` (for HTTPS URLs) or `ssh -v FETCH_URL` (for SSH URLs)
may be helpful.

If you can get the `git fetch` command to run successfully without prompting
for a password when you run it directly, you will be able to run `west
update` without entering your password in that same shell.

## “‘west’ is not recognized as an internal or external command, operable program or batch file.’

On Windows, this means that either west is not installed, or your [`PATH`](../env_vars.md#envvar-PATH)
environment variable does not contain the directory where pip installed
`west.exe`.

First, make sure you’ve installed west; see [Installing west](install.md#west-install). Then try
running `west` from a new `cmd.exe` window. If that still doesn’t work,
keep reading.

You need to find the directory containing `west.exe`, then add it to your
[`PATH`](../env_vars.md#envvar-PATH). (This [`PATH`](../env_vars.md#envvar-PATH) change should have been done for you when
you installed Python and pip, so ordinarily you should not need to follow these
steps.)

Run this command in `cmd.exe`:

```text
pip3 show west
```

Then:

1. Look for a line in the output that looks like `Location:
   C:\foo\python\python38\lib\site-packages`. The exact location
   will be different on your computer.
2. Look for a file named `west.exe` in the `scripts` directory
   `C:\foo\python\python38\scripts`.

   Important

   Notice how `lib\site-packages` in the `pip3 show` output was changed
   to `scripts`!
3. If you see `west.exe` in the `scripts` directory, add the full path to
   `scripts` to your [`PATH`](../env_vars.md#envvar-PATH) using a command like this:

   ```text
   setx PATH "%PATH%;C:\foo\python\python38\scripts"
   ```

   **Do not just copy/paste this command**. The `scripts` directory location
   will be different on your system.
4. Close your `cmd.exe` window and open a new one. You should be able to run
   `west`.

## “Error: unexpected keyword argument ‘requires\_workspace’”

This error occurs on some Linux distributions after upgrading to west 0.7.0 or
later from 0.6.x. For example:

```text
$ west update
[... stack trace ...]
TypeError: __init__() got an unexpected keyword argument 'requires_workspace'
```

This appears to be a problem with the distribution’s pip; see [this comment in
west issue 373](https://github.com/zephyrproject-rtos/west/issues/373#issuecomment-583489272) for details. Some versions of **Ubuntu** and **Linux Mint** are known to
have this problem. Some users report issues on Fedora as well.

Neither macOS nor Windows users have reported this issue. There have been no
reports of this issue on other Linux distributions, like Arch Linux, either.

**Workaround 1**: remove the old version, then upgrade:

```text
$ pip3 show west | grep Location: | cut -f 2 -d ' '
/home/foo/.local/lib/python3.6/site-packages
$ rm -r /home/foo/.local/lib/python3.6/site-packages/west
$ pip3 install --user west==0.7.0
```

**Workaround 2**: install west in a Python virtual environment

One option is to use the [venv module](https://docs.python.org/3/library/venv.html) that’s part of the Python 3 standard
library. Some distributions remove this module from their base Python 3
packages, so you may need to do some additional work to get it installed on
your system.

## “invalid choice: ‘build’” (or ‘flash’, etc.)

If you see an unexpected error like this when trying to run a Zephyr extension
command (like [west flash](build-flash-debug.md#west-flashing), [west build](build-flash-debug.md#west-building), etc.):

```text
$ west build [...]
west: error: argument <command>: invalid choice: 'build' (choose from 'init', [...])

$ west flash [...]
west: error: argument <command>: invalid choice: 'flash' (choose from 'init', [...])
```

The most likely cause is that you’re running the command outside of a
[west workspace](basics.md#west-workspace). West needs to know where your workspace
is to find [Extensions](extensions.md#west-extensions).

To fix this, you have two choices:

1. Run the command from inside a workspace (e.g. the `zephyrproject`
   directory you created when you [got started](../getting_started/index.md#getting-started)).

   For example, create your build directory inside the workspace, or run `west
   flash --build-dir YOUR_BUILD_DIR` from inside the workspace.
2. Set the [`ZEPHYR_BASE`](../env_vars.md#envvar-ZEPHYR_BASE) [environment variable](../env_vars.md#env-vars) and re-run
   the west extension command. If set, west will use [`ZEPHYR_BASE`](../env_vars.md#envvar-ZEPHYR_BASE) to
   find your workspace.

If you’re unsure whether a command is built-in or an extension, run `west
help` from inside your workspace. The output prints extension commands
separately, and looks like this for mainline Zephyr:

```text
$ west help

built-in commands for managing git repositories:
  init:                 create a west workspace
  [...]

other built-in commands:
  help:                 get help for west or a command
  [...]

extension commands from project manifest (path: zephyr):
  build:                compile a Zephyr application
  flash:                flash and run a binary on a board
  [...]
```

## “invalid choice: ‘post-init’”

If you see this error when running `west init`:

```text
west: error: argument <command>: invalid choice: 'post-init'
(choose from 'init', 'update', 'list', 'manifest', 'diff',
'status', 'forall', 'config', 'selfupdate', 'help')
```

Then you have an old version of west installed, and are trying to use it in a
workspace that requires a more recent version.

The easiest way to resolve this issue is to upgrade west and retry as follows:

1. Install the latest west with the `-U` option for `pip3 install` as shown
   in [Installing west](install.md#west-install).
2. Back up any contents of `zephyrproject/.west/config` that you want to
   save. (If you don’t have any configuration options set, it’s safe to skip
   this step.)
3. Completely remove the `zephyrproject/.west` directory (if you don’t,
   you will get the “already in a workspace” error message discussed next).
4. Run `west init` again.

## “already in an installation”

You may see this error when running `west init` with west 0.6:

```text
FATAL ERROR: already in an installation (<some directory>), aborting
```

If this is unexpected and you’re really trying to create a new west workspace,
then it’s likely that west is using the [`ZEPHYR_BASE`](../env_vars.md#envvar-ZEPHYR_BASE) [environment
variable](../env_vars.md#env-vars) to locate a workspace elsewhere on your system.

This is intentional; it allows you to put your Zephyr applications in
any directory and still use west to build, flash, and debug them, for example.

To resolve this issue, unset [`ZEPHYR_BASE`](../env_vars.md#envvar-ZEPHYR_BASE) and try again.
