---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/shell/shell_module/README.html
original_path: samples/subsys/shell/shell_module/README.html
---

# Custom Shell module

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/shell/shell_module/README.rst/..)

## Overview

This is a simple application demonstrating how to write and register commands
using the [Shell API](../../../../services/shell/index.md#shell-api):

Register Static commands
:   `version` is a static command that prints the kernel version.

Conditionally Register commands
:   `login` and `logout` are conditionally registered commands depending
    on [`CONFIG_SHELL_START_OBSCURED`](../../../../kconfig.md#CONFIG_SHELL_START_OBSCURED "CONFIG_SHELL_START_OBSCURED").

Register Dynamic commands
:   See `dynamic` command and [samples/subsys/shell/shell\_module/src/dynamic\_cmd.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/src/dynamic_cmd.c)
    for details on how dynamic commands are implemented.

Register Dictionary commands
:   `dictionary` implements subsect of dictionary commands.

Set a Bypass callback
:   `bypass` implements the bypass callback.

Set a Login command
:   `login` and `logout` implement the login and logout mechanism, respectively.

Obscure user-input with asterisks
:   `login` and `logout` implement the feature of enabling and disabling
    this functionality, respectively.

## Requirements

- A target configured with the shell interface, exposed through any of
  its [backends](../../../../services/shell/index.md#backends).

## Building and Running

This sample can be found under [samples/subsys/shell/shell\_module](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module)
in the Zephyr tree.

The sample can be built for several platforms.

### Emulation Targets

The sample may run on emulation targets. The following commands build the
application for the qemu\_x86.

```shell
west build -b qemu_x86 samples/subsys/shell/shell_module
west build -t run
```

After running the application, the console displays the shell interface, and
shows the shell prompt, at which point the user may start the interaction.

### On-Hardware

```shell
west build -b nrf52840dk/nrf52840 samples/subsys/shell/shell_module
west flash
```

## Sample Output

```shell
uart:~$
  bypass              clear               date
  demo                device              devmem
  dynamic             help                history
  kernel              log                 log_test
  rem                 resize              retval
  section_cmd         shell               shell_uart_release
  stats               version
uart:~$ demo
demo - Demo commands
Subcommands:
  dictionary  : Dictionary commands
  hexdump     : Hexdump params command.
  params      : Print params command.
  ping        : Ping command.
  board       : Show board name command.
uart:~$ dynamic
dynamic - Demonstrate dynamic command usage.
Subcommands:
  add      : Add a new dynamic command.
            Example usage: [ dynamic add test ] will add a dynamic command
            'test'.
            In this example, command name length is limited to 32 chars. You can
            add up to 20 commands. Commands are automatically sorted to ensure
            correct shell completion.
  execute  : Execute a command.
  remove   : Remove a command.
  show     : Show all added dynamic commands.
uart:~$
```

### Details on Shell Subsystem

For more details on the Shell subsystem, check the general [Shell documentation](../../../../services/shell/index.md#shell-api).

## See also

[Shell API](../../../../doxygen/html/group__shell__api.md)
