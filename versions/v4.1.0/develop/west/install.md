---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/west/install.html
original_path: develop/west/install.html
---

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

West currently supports shell completion in the following shells:

- bash
- zsh
- fish

In order to enable shell completion, you will need to obtain the corresponding
completion script and have it sourced.
Using the completion scripts:

bashzshfish

*One-time setup*:

```shell
source <(west completion bash)
```

*Permanent setup*:

```shell
west completion bash > ~/west-completion.bash; echo "source ~/west-completion.bash" >> ~/.bashrc
```

*One-time setup*:

```zsh
source <(west completion zsh)
```

*Permanent setup*:

```zsh
west completion zsh > "${fpath[1]}/_west"
```

*One-time setup*:

```fish
west completion fish | source
```

*Permanent setup*:

```fish
west completion fish > $HOME/.config/fish/completions/west.fish
```
