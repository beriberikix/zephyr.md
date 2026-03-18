---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/west/install.html
original_path: develop/west/install.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Installing west

West is written in Python 3 and distributed through [PyPI](https://pypi.org/project/west/).
Use `pip3` to install or upgrade west:

On Linux:

```text
pip3 install --user -U west
```

On Windows and macOS:

```text
pip3 install -U west
```

Note

See [Python and pip](../beyond-GSG.md#python-pip) for additional clarification on using the
`--user` switch.

Afterwards, you can run `pip3 show -f west` for information on where the west
binary and related files were installed.

Once west is installed, you can use it to [clone the Zephyr repositories](../getting_started/index.md#clone-zephyr).

## Structure

West’s code is distributed via PyPI in a Python package named `west`.
This distribution includes a launcher executable, which is also named
`west` (or `west.exe` on Windows).

When west is installed, the launcher is placed by `pip3` somewhere in
the user’s filesystem (exactly where depends on the operating system, but
should be on the `PATH` [environment variable](../env_vars.md#env-vars)). This
launcher is the command-line entry point to running both built-in commands
like `west init`, `west update`, along with any extensions discovered
in the workspace.

In addition to its command-line interface, you can also use west’s Python
APIs directly. See [West APIs](west-apis.md#west-apis) for details.

## Enabling shell completion

West currently supports shell completion in the following combinations of
platform and shell:

- Linux: bash
- macOS: bash
- Windows: not available

In order to enable shell completion, you will need to obtain the corresponding
completion script and have it sourced every time you enter a new shell session.

To obtain the completion script you can use the `west completion` command:

```text
cd /path/to/zephyr/
west completion bash > ~/west-completion.bash
```

Note

Remember to update your local copy of the completion script using `west
completion` when you update Zephyr.

Next, you need to import `west-completion.bash` into your bash shell.

On Linux, you have the following options:

- Copy `west-completion.bash` to `/etc/bash_completion.d/`.
- Copy `west-completion.bash` to
  `/usr/share/bash-completion/completions/`.
- Copy `west-completion.bash` to a local folder and source it from your
  `~/.bashrc`.

On macOS, you have the following options:

- Copy `west-completion.bash` to a local folder and source it from your
  `~/.bash_profile`
- Install the `bash-completion` package with `brew`:

  ```text
  brew install bash-completion
  ```

  then source the main bash completion script in your `~/.bash_profile`:

  ```text
  source /usr/local/etc/profile.d/bash_completion.sh
  ```

  and finally copy `west-completion.bash` to
  `/usr/local/etc/bash_completion.d/`.
