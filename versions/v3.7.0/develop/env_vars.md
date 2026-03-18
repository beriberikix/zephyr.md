---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/env_vars.html
original_path: develop/env_vars.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Environment Variables

Various pages in this documentation refer to setting Zephyr-specific
environment variables. This page describes how.

## Setting Variables

### Option 1: Just Once

To set the environment variable `MY_VARIABLE` to `foo` for the
lifetime of your current terminal window:

Linux/macOSWindows

```shell
export MY_VARIABLE=foo
```

```shell
set MY_VARIABLE=foo
```

Warning

This is best for experimentation. If you close your terminal window, use
another terminal window or tab, restart your computer, etc., this setting
will be lost forever.

Using options 2 or 3 is recommended if you want to keep using the setting.

### Option 2: In all Terminals

Linux/macOSWindows

Add the `export MY_VARIABLE=foo` line to your shell’s startup script in
your home directory. For Bash, this is usually `~/.bashrc` on Linux
or `~/.bash_profile` on macOS. Changes in these startup scripts
don’t affect shell instances already started; try opening a new terminal
window to get the new settings.

You can use the `setx` program in `cmd.exe` or the third-party RapidEE
program.

To use `setx`, type this command, then close the terminal window. Any
new `cmd.exe` windows will have `MY_VARIABLE` set to `foo`.

```shell
setx MY_VARIABLE foo
```

To install RapidEE, a freeware graphical environment variable editor,
[using Chocolatey](https://chocolatey.org/packages/RapidEE) in an Administrator command prompt:

```shell
choco install rapidee
```

You can then run `rapidee` from your terminal to launch the program and set
environment variables. Make sure to use the “User” environment variables area
– otherwise, you have to run RapidEE as administrator. Also make sure to save
your changes by clicking the Save button at top left before exiting. Settings
you make in RapidEE will be available whenever you open a new terminal window.

### Option 3: Using `zephyrrc` files

Choose this option if you don’t want to make the variable’s setting available
to all of your terminals, but still want to save the value for loading into
your environment when you are using Zephyr.

Linux/macOSWindows

Create a file named `~/.zephyrrc` if it doesn’t exist, then add this
line to it:

```shell
export MY_VARIABLE=foo
```

To get this value back into your current terminal environment, **you must
run** `source zephyr-env.sh` from the main `zephyr` repository. Among
other things, this script sources `~/.zephyrrc`.

The value will be lost if you close the window, etc.; run `source
zephyr-env.sh` again to get it back.

Add the line `set MY_VARIABLE=foo` to the file
`%userprofile%\zephyrrc.cmd` using a text editor such as Notepad to
save the value.

To get this value back into your current terminal environment, **you must
run** `zephyr-env.cmd` in a `cmd.exe` window after changing directory
to the main `zephyr` repository. Among other things, this script runs
`%userprofile%\zephyrrc.cmd`.

The value will be lost if you close the window, etc.; run
`zephyr-env.cmd` again to get it back.

These scripts:

- set [`ZEPHYR_BASE`](#envvar-ZEPHYR_BASE) to the location of the zephyr repository
- adds some Zephyr-specific locations (such as zephyr’s `scripts`
  directory) to your [`PATH`](#envvar-PATH) environment variable
- loads any settings from the `zephyrrc` files described above in
  [Option 3: Using zephyrrc files](#env-vars-zephyrrc).

You can thus use them any time you need any of these settings.

## Zephyr Environment Scripts

You can use the zephyr repository scripts `zephyr-env.sh` (for macOS and
Linux) and `zephyr-env.cmd` (for Windows) to load Zephyr-specific settings
into your current terminal’s environment. To do so, run this command from the
zephyr repository:

Linux/macOSWindows

```shell
source zephyr-env.sh
```

```shell
zephyr-env.cmd
```

These scripts:

- set [`ZEPHYR_BASE`](#envvar-ZEPHYR_BASE) to the location of the zephyr repository
- adds some Zephyr-specific locations (such as zephyr’s `scripts`
  directory) to your `PATH` environment variable
- loads any settings from the `zephyrrc` files described above in
  [Option 3: Using zephyrrc files](#env-vars-zephyrrc).

You can thus use them any time you need any of these settings.

## Important Environment Variables

Some [Important Build System Variables](application/index.md#important-build-vars) can also be set in the environment. Here
is a description of some of these important environment variables. This is not
a comprehensive list.

BOARD
:   See [Important Build System Variables](application/index.md#important-build-vars).

CONF\_FILE
:   See [Important Build System Variables](application/index.md#important-build-vars).

SHIELD
:   See [Shields](../hardware/porting/shields.md#shields).

ZEPHYR\_BASE
:   See [Important Build System Variables](application/index.md#important-build-vars).

EXTRA\_ZEPHYR\_MODULES
:   See [Important Build System Variables](application/index.md#important-build-vars).

ZEPHYR\_MODULES
:   See [Important Build System Variables](application/index.md#important-build-vars).

ZEPHYR\_BOARD\_ALIASES
:   See [Board Aliases](beyond-GSG.md#gs-board-aliases)

The following additional environment variables are significant when configuring
the [toolchain](beyond-GSG.md#gs-toolchain) used to build Zephyr applications.

ZEPHYR\_SDK\_INSTALL\_DIR
:   Path where Zephyr SDK is installed.

ZEPHYR\_TOOLCHAIN\_VARIANT
:   The name of the toolchain to use.

{TOOLCHAIN}\_TOOLCHAIN\_PATH
:   Path to the toolchain specified by [`ZEPHYR_TOOLCHAIN_VARIANT`](#envvar-ZEPHYR_TOOLCHAIN_VARIANT). For
    example, if `ZEPHYR_TOOLCHAIN_VARIANT=llvm`, use `LLVM_TOOLCHAIN_PATH`.
    (Note the capitalization when forming the environment variable name.)

You might need to update some of these variables when you
[update the Zephyr SDK toolchain](beyond-GSG.md#gs-toolchain-update).

Emulators and boards may also depend on additional programs. The build system
will try to locate those programs automatically, but may rely on additional
CMake or environment variables to do so. Please consult your emulator’s or
board’s documentation for more information. The following environment variables
may be useful in such situations:

PATH
:   `PATH` is an environment variable used on Unix-like or Microsoft Windows
    operating systems to specify a set of directories where executable programs
    are located.
