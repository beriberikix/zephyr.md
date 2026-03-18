---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/shell/index.html
original_path: services/shell/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Shell

## [Overview](#id5)

This module allows you to create and handle a shell with a user-defined command
set. You can use it in examples where more than simple button or LED user
interaction is required. This module is a Unix-like shell with these features:

- Support for multiple instances.
- Advanced cooperation with the [Logging](../logging/index.md#logging-api).
- Support for static and dynamic commands.
- Support for dictionary commands.
- Smart command completion with the `Tab` key.
- Built-in commands: **clear**, **shell**, **colors**,
  **echo**, **history** and **resize**.
- Viewing recently executed commands using keys: `↑` `↓` or meta keys.
- Text edition using keys: `←`, `→`, `Backspace`,
  `Delete`, `End`, `Home`, `Insert`.
- Support for ANSI escape codes: `VT100` and `ESC[n~` for cursor control
  and color printing.
- Support for editing multiline commands.
- Built-in handler to display help for the commands.
- Support for wildcards: `*` and `?`.
- Support for meta keys.
- Support for getopt and getopt\_long.
- Kconfig configuration to optimize memory usage.

Note

Some of these features have a significant impact on RAM and flash usage,
but many can be disabled when not needed. To default to options which
favor reduced RAM and flash requirements instead of features, you should
enable [`CONFIG_SHELL_MINIMAL`](../../kconfig.md#CONFIG_SHELL_MINIMAL "CONFIG_SHELL_MINIMAL") and selectively enable just the
features you want.

## [Backends](#id6)

The module can be connected to any transport for command input and output.
At this point, the following transport layers are implemented:

- MQTT
- Segger RTT
- SMP
- Telnet
- UART
- USB
- Bluetooth LE (NUS)
- RPMSG
- DUMMY - not a physical transport layer.

### [Telnet](#id7)

Enabling [`CONFIG_SHELL_BACKEND_TELNET`](../../kconfig.md#CONFIG_SHELL_BACKEND_TELNET "CONFIG_SHELL_BACKEND_TELNET") will allow users to use telnet
as a shell backend. Connecting to it can be done using PuTTY or any `telnet` client.
For example:

```text
telnet <ip address> <port>
```

By default the telnet client won’t handle telnet commands and configuration. Although
command support can be enabled with [`CONFIG_SHELL_TELNET_SUPPORT_COMMAND`](../../kconfig.md#CONFIG_SHELL_TELNET_SUPPORT_COMMAND "CONFIG_SHELL_TELNET_SUPPORT_COMMAND").
This will give the telnet client access to a very limited set of supported commands but
still can be turned on if needed. One of the command options it supports is the `ECHO`
option. This will allow the client to be in character mode (character at a time),
similar to a UART backend in that regard. This will make the client send a character
as soon as it is typed having the effect of increasing the network traffic
considerably. For that cost, it will enable the line editing,
[tab completion](#tab-feature), and [history](#history-feature)
features of the shell.

### [USB CDC ACM](#id8)

To configure Shell USB CDC ACM backend, simply add the snippet `cdc-acm-console`
to your build:

```shell
west build -S cdc-acm-console [...]
```

Details on the configuration settings are captured in the following files:

- [snippets/cdc-acm-console/cdc-acm-console.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/snippets/cdc-acm-console/cdc-acm-console.conf).
- [snippets/cdc-acm-console/cdc-acm-console.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/snippets/cdc-acm-console/cdc-acm-console.overlay).

### [Bluetooth LE (NUS)](#id9)

To configure Bluetooth LE (NUS) backend, simply add the snippet `nus-console`
to your build:

```shell
west build -S nus-console [...]
```

Details on the configuration settings are captured in the following files:

- [snippets/nus-console/nus-console.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/snippets/nus-console/nus-console.conf).
- [snippets/nus-console/nus-console.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/snippets/nus-console/nus-console.overlay).

### [Segget RTT](#id10)

To configure Segger RTT backend, add the following configurations to your build:

- [`CONFIG_USE_SEGGER_RTT`](../../kconfig.md#CONFIG_USE_SEGGER_RTT "CONFIG_USE_SEGGER_RTT")
- [`CONFIG_SHELL_BACKEND_RTT`](../../kconfig.md#CONFIG_SHELL_BACKEND_RTT "CONFIG_SHELL_BACKEND_RTT")
- [`CONFIG_SHELL_BACKEND_SERIAL`](../../kconfig.md#CONFIG_SHELL_BACKEND_SERIAL "CONFIG_SHELL_BACKEND_SERIAL")

Details on additional configuration settings are captured in:
[samples/subsys/shell/shell\_module/prj\_minimal\_rtt.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/prj_minimal_rtt.conf).

#### Connecting to Segger RTT via TCP (on macOS, for example)

On macOS JLinkRTTClient won’t let you enter input. Instead, please use following
procedure:

- Open up a first Terminal window and enter:

  ```text
  JLinkRTTLogger -Device NRF52840_XXAA -RTTChannel 1 -if SWD -Speed 4000 ~/rtt.log
  ```

  (change device if required)
- Open up a second Terminal window and enter:

  ```text
  nc localhost 19021
  ```
- Now you should have a network connection to RTT that will let you enter input
  to the shell.

## [Commands](#id11)

Shell commands are organized in a tree structure and grouped into the following
types:

- Root command (level 0): Gathered and alphabetically sorted in a dedicated
  memory section.
- Static subcommand (level > 0): Number and syntax must be known during compile
  time. Created in the software module.
- Dynamic subcommand (level > 0): Number and syntax does not need to be known
  during compile time. Created in the software module.

### [Commonly-used command groups](#id12)

The following list is a set of useful command groups and how to enable them:

#### GPIO

- [`CONFIG_GPIO`](../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO")
- [`CONFIG_GPIO_SHELL`](../../kconfig.md#CONFIG_GPIO_SHELL "CONFIG_GPIO_SHELL")

#### I2C

- [`CONFIG_I2C`](../../kconfig.md#CONFIG_I2C "CONFIG_I2C")
- [`CONFIG_I2C_SHELL`](../../kconfig.md#CONFIG_I2C_SHELL "CONFIG_I2C_SHELL")

#### Sensor

- [`CONFIG_SENSOR`](../../kconfig.md#CONFIG_SENSOR "CONFIG_SENSOR")
- [`CONFIG_SENSOR_SHELL`](../../kconfig.md#CONFIG_SENSOR_SHELL "CONFIG_SENSOR_SHELL")

#### Flash

- [`CONFIG_FLASH`](../../kconfig.md#CONFIG_FLASH "CONFIG_FLASH")
- [`CONFIG_FLASH_SHELL`](../../kconfig.md#CONFIG_FLASH_SHELL "CONFIG_FLASH_SHELL")

#### File-System

- [`CONFIG_FILE_SYSTEM`](../../kconfig.md#CONFIG_FILE_SYSTEM "CONFIG_FILE_SYSTEM")
- [`CONFIG_FILE_SYSTEM_SHELL`](../../kconfig.md#CONFIG_FILE_SYSTEM_SHELL "CONFIG_FILE_SYSTEM_SHELL")

### [Creating commands](#id13)

Use the following macros for adding shell commands:

- [`SHELL_CMD_REGISTER`](#c.SHELL_CMD_REGISTER) - Create root command. All root commands must
  have different name.
- [`SHELL_COND_CMD_REGISTER`](#c.SHELL_COND_CMD_REGISTER) - Conditionally (if compile time flag is
  set) create root command. All root commands must have different name.
- [`SHELL_CMD_ARG_REGISTER`](#c.SHELL_CMD_ARG_REGISTER) - Create root command with arguments.
  All root commands must have different name.
- [`SHELL_COND_CMD_ARG_REGISTER`](#c.SHELL_COND_CMD_ARG_REGISTER) - Conditionally (if compile time flag
  is set) create root command with arguments. All root commands must have
  different name.
- [`SHELL_CMD`](#c.SHELL_CMD) - Initialize a command.
- [`SHELL_COND_CMD`](#c.SHELL_COND_CMD) - Initialize a command if compile time flag is set.
- [`SHELL_EXPR_CMD`](#c.SHELL_EXPR_CMD) - Initialize a command if compile time expression is
  non-zero.
- [`SHELL_CMD_ARG`](#c.SHELL_CMD_ARG) - Initialize a command with arguments.
- [`SHELL_COND_CMD_ARG`](#c.SHELL_COND_CMD_ARG) - Initialize a command with arguments if compile
  time flag is set.
- [`SHELL_EXPR_CMD_ARG`](#c.SHELL_EXPR_CMD_ARG) - Initialize a command with arguments if compile
  time expression is non-zero.
- [`SHELL_STATIC_SUBCMD_SET_CREATE`](#c.SHELL_STATIC_SUBCMD_SET_CREATE) - Create a static subcommands
  array.
- [`SHELL_SUBCMD_DICT_SET_CREATE`](#c.SHELL_SUBCMD_DICT_SET_CREATE) - Create a dictionary subcommands
  array.
- [`SHELL_DYNAMIC_CMD_CREATE`](#c.SHELL_DYNAMIC_CMD_CREATE) - Create a dynamic subcommands array.

Commands can be created in any file in the system that includes
[include/zephyr/shell/shell.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell.h). All created commands are available for all
shell instances.

#### Static commands

Example code demonstrating how to create a root command with static
subcommands.

![Command tree with static commands.](../../_images/static_cmd.PNG)

```c
/* Creating subcommands (level 1 command) array for command "demo". */
SHELL_STATIC_SUBCMD_SET_CREATE(sub_demo,
        SHELL_CMD(params, NULL, "Print params command.",
                                               cmd_demo_params),
        SHELL_CMD(ping,   NULL, "Ping command.", cmd_demo_ping),
        SHELL_SUBCMD_SET_END
);
/* Creating root (level 0) command "demo" */
SHELL_CMD_REGISTER(demo, &sub_demo, "Demo commands", NULL);
```

Example implementation can be found under following location:
[samples/subsys/shell/shell\_module/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/src/main.c).

### [Dictionary commands](#id14)

This is a special kind of static commands. Dictionary commands can be used
every time you want to use a pair: (string <-> corresponding data) in
a command handler. The string is usually a verbal description of a given data.
The idea is to use the string as a command syntax that can be prompted by the
shell and corresponding data can be used to process the command.

Let’s use an example. Suppose you created a command to set an ADC gain.
It is a perfect place where a dictionary can be used. The dictionary would
be a set of pairs: (string: gain\_value, int: value) where int value could
be used with the ADC driver API.

Abstract code for this task would look like this:

```c
static int gain_cmd_handler(const struct shell *sh,
                            size_t argc, char **argv, void *data)
{
        int gain;

        /* data is a value corresponding to called command syntax */
        gain = (int)data;
        adc_set_gain(gain);

        shell_print(sh, "ADC gain set to: %s\n"
                           "Value send to ADC driver: %d",
                           argv[0],
                           gain);

        return 0;
}

SHELL_SUBCMD_DICT_SET_CREATE(sub_gain, gain_cmd_handler,
        (gain_1, 1, "gain 1"), (gain_2, 2, "gain 2"),
        (gain_1_2, 3, "gain 1/2"), (gain_1_4, 4, "gain 1/4")
);
SHELL_CMD_REGISTER(gain, &sub_gain, "Set ADC gain", NULL);
```

This is how it would look like in the shell:

![Dictionary commands example.](../../_images/dict_cmd.png)

#### Dynamic commands

Example code demonstrating how to create a root command with static and dynamic
subcommands. At the beginning dynamic command list is empty. New commands
can be added by typing:

```text
dynamic add <new_dynamic_command>
```

Newly added commands can be prompted or autocompleted with the `Tab` key.

![Command tree with static and dynamic commands.](../../_images/dynamic_cmd.PNG)

```c
/* Buffer for 10 dynamic commands */
static char dynamic_cmd_buffer[10][50];

/* commands counter */
static uint8_t dynamic_cmd_cnt;

/* Function returning command dynamically created
 * in  dynamic_cmd_buffer.
 */
static void dynamic_cmd_get(size_t idx,
                            struct shell_static_entry *entry)
{
        if (idx < dynamic_cmd_cnt) {
                entry->syntax = dynamic_cmd_buffer[idx];
                entry->handler  = NULL;
                entry->subcmd = NULL;
                entry->help = "Show dynamic command name.";
        } else {
                /* if there are no more dynamic commands available
                 * syntax must be set to NULL.
                 */
                entry->syntax = NULL;
        }
}

SHELL_DYNAMIC_CMD_CREATE(m_sub_dynamic_set, dynamic_cmd_get);
SHELL_STATIC_SUBCMD_SET_CREATE(m_sub_dynamic,
        SHELL_CMD(add, NULL,"Add new command to dynamic_cmd_buffer and"
                  " sort them alphabetically.",
                  cmd_dynamic_add),
        SHELL_CMD(execute, &m_sub_dynamic_set,
                  "Execute a command.", cmd_dynamic_execute),
        SHELL_CMD(remove, &m_sub_dynamic_set,
                  "Remove a command from dynamic_cmd_buffer.",
                  cmd_dynamic_remove),
        SHELL_CMD(show, NULL,
                  "Show all commands in dynamic_cmd_buffer.",
                  cmd_dynamic_show),
        SHELL_SUBCMD_SET_END
);
SHELL_CMD_REGISTER(dynamic, &m_sub_dynamic,
           "Demonstrate dynamic command usage.", cmd_dynamic);
```

Example implementation can be found under following location:
[samples/subsys/shell/shell\_module/src/dynamic\_cmd.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/src/dynamic_cmd.c).

### [Commands execution](#id15)

Each command or subcommand may have a handler. The shell executes the handler
that is found deepest in the command tree and further subcommands (without a
handler) are passed as arguments. Characters within parentheses are treated
as one argument. If shell won’t find a handler it will display an error message.

Commands can be also executed from a user application using any active backend
and a function [`shell_execute_cmd()`](#c.shell_execute_cmd), as shown in this example:

```c
int main(void)
{
        /* Below code will execute "clear" command on a DUMMY backend */
        shell_execute_cmd(NULL, "clear");

        /* Below code will execute "shell colors off" command on
         * an UART backend
         */
        shell_execute_cmd(shell_backend_uart_get_ptr(),
                          "shell colors off");
}
```

Enable the DUMMY backend by setting the Kconfig
[`CONFIG_SHELL_BACKEND_DUMMY`](../../kconfig.md#CONFIG_SHELL_BACKEND_DUMMY "CONFIG_SHELL_BACKEND_DUMMY") option.

#### Commands execution example

Let’s assume a command structure as in the following figure, where:

- `root_cmd` - root command without a handler
- `cmd_xxx_h` - command has a handler
- `cmd_xxx` - command does not have a handler

![Command tree with static commands.](../../_images/execution.png)

##### Example 1

Sequence: `root_cmd` `cmd_1_h` `cmd_12_h`
`cmd_121_h` `parameter` will execute command
`cmd_121_h` and `parameter` will be passed as an argument.

##### Example 2

Sequence: `root_cmd` `cmd_2` `cmd_22_h`
`parameter1` `parameter2` will execute command
`cmd_22_h` and `parameter1` `parameter2`
will be passed as an arguments.

##### Example 3

Sequence: `root_cmd` `cmd_1_h` `parameter1`
`cmd_121_h` `parameter2` will execute command
`cmd_1_h` and `parameter1`, `cmd_121_h` and
`parameter2` will be passed as an arguments.

##### Example 4

Sequence: `root_cmd` `parameter` `cmd_121_h`
`parameter2` will not execute any command.

#### Command handler

Simple command handler implementation:

```c
static int cmd_handler(const struct shell *sh, size_t argc,
                        char **argv)
{
        ARG_UNUSED(argc);
        ARG_UNUSED(argv);

        shell_fprintf(shell, SHELL_INFO, "Print info message\n");

        shell_print(sh, "Print simple text.");

        shell_warn(sh, "Print warning text.");

        shell_error(sh, "Print error text.");

        return 0;
}
```

Function [`shell_fprintf()`](#c.shell_fprintf) or the shell print macros:
[`shell_print`](#c.shell_print), [`shell_info`](#c.shell_info), [`shell_warn`](#c.shell_warn) and
[`shell_error`](#c.shell_error) can be used from the command handler or from threads,
but not from an interrupt context. Instead, interrupt handlers should use
[Logging](../logging/index.md#logging-api) for printing.

#### Command help

Every user-defined command or subcommand can have its own help description.
The help for commands and subcommands can be created with respective macros:
[`SHELL_CMD_REGISTER`](#c.SHELL_CMD_REGISTER), [`SHELL_CMD_ARG_REGISTER`](#c.SHELL_CMD_ARG_REGISTER),
[`SHELL_CMD`](#c.SHELL_CMD), and [`SHELL_CMD_ARG`](#c.SHELL_CMD_ARG).

Shell prints this help message when you call a command
or subcommand with `-h` or `--help` parameter.

#### Parent commands

In the subcommand handler, you can access both the parameters passed to
commands or the parent commands, depending on how you index `argv`.

- When indexing `argv` with positive numbers, you can access the parameters.
- When indexing `argv` with negative numbers, you can access the parent
  commands.
- The subcommand to which the handler belongs has the `argv` index of 0.

```c
static int cmd_handler(const struct shell *sh, size_t argc,
                       char **argv)
{
        ARG_UNUSED(argc);

        /* If it is a subcommand handler parent command syntax
         * can be found using argv[-1].
         */
        shell_print(sh, "This command has a parent command: %s",
                      argv[-1]);

        /* Print this command syntax */
        shell_print(sh, "This command syntax is: %s", argv[0]);

        /* Print first argument */
        shell_print(sh, "%s", argv[1]);

        return 0;
}
```

### [Built-in commands](#id16)

These commands are activated by [`CONFIG_SHELL_CMDS`](../../kconfig.md#CONFIG_SHELL_CMDS "CONFIG_SHELL_CMDS") set to `y`.

- **clear** - Clears the screen.
- **history** - Shows the recently entered commands.
- **resize** - Must be executed when terminal width is different than 80
  characters or after each change of terminal width. It ensures proper
  multiline text display and `←`, `→`, `End`, `Home` keys
  handling. Currently this command works only with UART flow control switched
  on. It can be also called with a subcommand:

  > - **default** - Shell will send terminal width = 80 to the
  >   terminal and assume successful delivery.

  These command needs extra activation:
  [`CONFIG_SHELL_CMDS_RESIZE`](../../kconfig.md#CONFIG_SHELL_CMDS_RESIZE "CONFIG_SHELL_CMDS_RESIZE") set to `y`.
- **select** - It can be used to set new root command. Exit to main
  command tree is with alt+r. This command needs extra activation:
  [`CONFIG_SHELL_CMDS_SELECT`](../../kconfig.md#CONFIG_SHELL_CMDS_SELECT "CONFIG_SHELL_CMDS_SELECT") set to `y`.
- **shell** - Root command with useful shell-related subcommands like:

  > - **echo** - Toggles shell echo.
  > - **colors** - Toggles colored syntax. This might be helpful in
  >   case of Bluetooth shell to limit the amount of transferred bytes.
  > - **stats** - Shows shell statistics.

## [Tab Feature](#id17)

The Tab button can be used to suggest commands or subcommands. This feature
is enabled by [`CONFIG_SHELL_TAB`](../../kconfig.md#CONFIG_SHELL_TAB "CONFIG_SHELL_TAB") set to `y`.
It can also be used for partial or complete auto-completion of commands.
This feature is activated by
[`CONFIG_SHELL_TAB_AUTOCOMPLETION`](../../kconfig.md#CONFIG_SHELL_TAB_AUTOCOMPLETION "CONFIG_SHELL_TAB_AUTOCOMPLETION") set to `y`.
When user starts writing a command and presses the `Tab` button then
the shell will do one of 3 possible things:

- Autocomplete the command.
- Prompts available commands and if possible partly completes the command.
- Will not do anything if there are no available or matching commands.

![Tab Feature usage example](../../_images/tab_prompt.png)

## [History Feature](#id18)

This feature enables commands history in the shell. It is activated by:
[`CONFIG_SHELL_HISTORY`](../../kconfig.md#CONFIG_SHELL_HISTORY "CONFIG_SHELL_HISTORY") set to `y`. History can be accessed
using keys: `↑` `↓` or `Ctrl+n` and `Ctrl+p`
if meta keys are active.
Number of commands that can be stored depends on size
of [`CONFIG_SHELL_HISTORY_BUFFER`](../../kconfig.md#CONFIG_SHELL_HISTORY_BUFFER "CONFIG_SHELL_HISTORY_BUFFER") parameter.

## [Wildcards Feature](#id19)

The shell module can handle wildcards. Wildcards are interpreted correctly
when expanded command and its subcommands do not have a handler. For example,
if you want to set logging level to `err` for the `app` and `app_test`
modules you can execute the following command:

```text
log enable err a*
```

![Wildcard usage example](../../_images/wildcard.png)

This feature is activated by [`CONFIG_SHELL_WILDCARD`](../../kconfig.md#CONFIG_SHELL_WILDCARD "CONFIG_SHELL_WILDCARD") set to `y`.

## [Meta Keys Feature](#id20)

The shell module supports the following meta keys:

Implemented meta keys

| Meta keys | Action |
| --- | --- |
| `Ctrl+a` | Moves the cursor to the beginning of the line. |
| `Ctrl+b` | Moves the cursor backward one character. |
| `Ctrl+c` | Preserves the last command on the screen and starts a new command in a new line. |
| `Ctrl+d` | Deletes the character under the cursor. |
| `Ctrl+e` | Moves the cursor to the end of the line. |
| `Ctrl+f` | Moves the cursor forward one character. |
| `Ctrl+k` | Deletes from the cursor to the end of the line. |
| `Ctrl+l` | Clears the screen and leaves the currently typed command at the top of the screen. |
| `Ctrl+n` | Moves in history to next entry. |
| `Ctrl+p` | Moves in history to previous entry. |
| `Ctrl+u` | Clears the currently typed command. |
| `Ctrl+w` | Removes the word or part of the word to the left of the cursor. Words separated by period instead of space are treated as one word. |
| `Alt+b` | Moves the cursor backward one word. |
| `Alt+f` | Moves the cursor forward one word. |

This feature is activated by [`CONFIG_SHELL_METAKEYS`](../../kconfig.md#CONFIG_SHELL_METAKEYS "CONFIG_SHELL_METAKEYS") set to `y`.

## [Getopt Feature](#id21)

Some shell users apart from subcommands might need to use options as well.
the arguments string, looking for supported options. Typically, this task
is accomplished by the `getopt` family functions.

For this purpose shell supports the getopt and getopt\_long libraries available
in the FreeBSD project. This feature is activated by:
[`CONFIG_POSIX_C_LIB_EXT`](../../kconfig.md#CONFIG_POSIX_C_LIB_EXT "CONFIG_POSIX_C_LIB_EXT") set to `y` and [`CONFIG_GETOPT_LONG`](../../kconfig.md#CONFIG_GETOPT_LONG "CONFIG_GETOPT_LONG")
set to `y`.

This feature can be used in thread safe as well as non thread safe manner.
The former is full compatible with regular getopt usage while the latter
a bit differs.

An example non-thread safe usage:

```c
char *cvalue = NULL;
while ((char c = getopt(argc, argv, "abhc:")) != -1) {
      switch (c) {
      case 'c':
              cvalue = optarg;
              break;
      default:
              break;
      }
}
```

An example thread safe usage:

```c
char *cvalue = NULL;
struct getopt_state *state;
while ((char c = getopt(argc, argv, "abhc:")) != -1) {
      state = getopt_state_get();
      switch (c) {
      case 'c':
              cvalue = state->optarg;
              break;
      default:
              break;
      }
}
```

Thread safe getopt functionality is activated by
[`CONFIG_SHELL_GETOPT`](../../kconfig.md#CONFIG_SHELL_GETOPT "CONFIG_SHELL_GETOPT") set to `y`.

## [Obscured Input Feature](#id22)

With the obscured input feature, the shell can be used for implementing a login
prompt or other user interaction whereby the characters the user types should
not be revealed on screen, such as when entering a password.

Once the obscured input has been accepted, it is normally desired to return the
shell to normal operation. Such runtime control is possible with the
`shell_obscure_set` function.

An example of login and logout commands using this feature is located in
[samples/subsys/shell/shell\_module/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/src/main.c) and the config file
[samples/subsys/shell/shell\_module/prj\_login.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/prj_login.conf).

This feature is activated upon startup by [`CONFIG_SHELL_START_OBSCURED`](../../kconfig.md#CONFIG_SHELL_START_OBSCURED "CONFIG_SHELL_START_OBSCURED")
set to `y`. With this set either way, the option can still be controlled later
at runtime. [`CONFIG_SHELL_CMDS_SELECT`](../../kconfig.md#CONFIG_SHELL_CMDS_SELECT "CONFIG_SHELL_CMDS_SELECT") is useful to prevent entry
of any other command besides a login command, by means of the
`shell_set_root_cmd` function. Likewise, [`CONFIG_SHELL_PROMPT_UART`](../../kconfig.md#CONFIG_SHELL_PROMPT_UART "CONFIG_SHELL_PROMPT_UART")
allows you to set the prompt upon startup, but it can be changed later with the
`shell_prompt_change` function.

## [Shell Logger Backend Feature](#id23)

Shell instance can act as the [Logging](../logging/index.md#logging-api) backend. Shell ensures that log
messages are correctly multiplexed with shell output. Log messages from logger
thread are enqueued and processed in the shell thread. Logger thread will block
for configurable amount of time if queue is full, blocking logger thread context
for that time. Oldest log message is removed from the queue after timeout and
new message is enqueued. Use the `shell stats show` command to retrieve
number of log messages dropped by the shell instance. Log queue size and timeout
are [`SHELL_DEFINE`](#c.SHELL_DEFINE) arguments.

This feature is activated by: [`CONFIG_SHELL_LOG_BACKEND`](../../kconfig.md#CONFIG_SHELL_LOG_BACKEND "CONFIG_SHELL_LOG_BACKEND") set to `y`.

Warning

Enqueuing timeout must be set carefully when multiple backends are used
in the system. The shell instance could have a slow transport or could
block, for example, by a UART with hardware flow control. If timeout is
set too high, the logger thread could be blocked and impact other logger
backends.

Warning

As the shell is a complex logger backend, it can not output logs if
the application crashes before the shell thread is running. In this
situation, you can enable one of the simple logging backends instead,
such as UART ([`CONFIG_LOG_BACKEND_UART`](../../kconfig.md#CONFIG_LOG_BACKEND_UART "CONFIG_LOG_BACKEND_UART")) or
RTT ([`CONFIG_LOG_BACKEND_RTT`](../../kconfig.md#CONFIG_LOG_BACKEND_RTT "CONFIG_LOG_BACKEND_RTT")), which are available earlier
during system initialization.

## [RTT Backend Channel Selection](#id24)

Instead of using the shell as a logger backend, RTT shell backend and RTT log
backend can also be used simultaneously, but over different channels. By
separating them, the log can be captured or monitored without shell output or
the shell may be scripted without log interference. Enabling both the Shell RTT
backend and the Log RTT backend does not work by default, because both default
to channel `0`. There are two options:

1. The Shell buffer can use an alternate channel, for example using
[`CONFIG_SHELL_BACKEND_RTT_BUFFER`](../../kconfig.md#CONFIG_SHELL_BACKEND_RTT_BUFFER "CONFIG_SHELL_BACKEND_RTT_BUFFER") set to `1`.
This allows monitoring the log using [JLinkRTTViewer](https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/#j-link-rtt-viewer)
while a script interfaces over channel 1.

2. The Log buffer can use an alternate channel, for example using
[`CONFIG_LOG_BACKEND_RTT_BUFFER`](../../kconfig.md#CONFIG_LOG_BACKEND_RTT_BUFFER "CONFIG_LOG_BACKEND_RTT_BUFFER") set to `1`.
This allows interactive use of the shell through JLinkRTTViewer, while the log
is written to file.

See [shell backends](#backends) for details on how to enable RTT as a Shell backend.

## [Usage](#id25)

The following code shows a simple use case of this library:

```c
int main(void)
{

}

static int cmd_demo_ping(const struct shell *sh, size_t argc,
                         char **argv)
{
        ARG_UNUSED(argc);
        ARG_UNUSED(argv);

        shell_print(sh, "pong");
        return 0;
}

static int cmd_demo_params(const struct shell *sh, size_t argc,
                           char **argv)
{
        int cnt;

        shell_print(sh, "argc = %d", argc);
        for (cnt = 0; cnt < argc; cnt++) {
                shell_print(sh, "  argv[%d] = %s", cnt, argv[cnt]);
        }
        return 0;
}

/* Creating subcommands (level 1 command) array for command "demo". */
SHELL_STATIC_SUBCMD_SET_CREATE(sub_demo,
        SHELL_CMD(params, NULL, "Print params command.",
                                               cmd_demo_params),
        SHELL_CMD(ping,   NULL, "Ping command.", cmd_demo_ping),
        SHELL_SUBCMD_SET_END
);
/* Creating root (level 0) command "demo" without a handler */
SHELL_CMD_REGISTER(demo, &sub_demo, "Demo commands", NULL);

/* Creating root (level 0) command "version" */
SHELL_CMD_REGISTER(version, NULL, "Show kernel version", cmd_version);
```

Users may use the `Tab` key to complete a command/subcommand or to see the
available subcommands for the currently entered command level.
For example, when the cursor is positioned at the beginning of the command
line and the `Tab` key is pressed, the user will see all root (level 0)
commands:

```text
clear  demo  shell  history  log  resize  version
```

Note

To view the subcommands that are available for a specific command, you
must first type a `space` after this command and then hit
`Tab`.

These commands are registered by various modules, for example:

- **clear**, **shell**, **history**, and **resize**
  are built-in commands which have been registered by
  [subsys/shell/shell.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell.c)
- **demo** and **version** have been registered in example code
  above by main.c
- **log** has been registered by [subsys/logging/log\_cmds.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/log_cmds.c)

Then, if a user types a **demo** command and presses the `Tab` key,
the shell will only print the subcommands registered for this command:

```text
params  ping
```

## [API Reference](#id26)

Related code samples

[Custom Shell module](../../samples/subsys/shell/shell_module/README.md#shell-module "Register shell commands using the Shell API")
:   Register shell commands using the Shell API

[Telnet console](../../samples/net/telnet/README.md#telnet-console "Access Zephyr shell over telnet.")
:   Access Zephyr shell over telnet.

*group* Shell API
:   Shell API.

    **Since**
    :   1.14

    **Version**
    :   1.0.0

    Defines

    SHELL\_CMD\_ARG\_REGISTER(syntax, subcmd, help, handler, mandatory, optional)
    :   Macro for defining and adding a root command (level 0) with required number of arguments.

        Note

        Each root command shall have unique syntax. If a command will be called with wrong number of arguments shell will print an error message and command handler will not be called.

        Parameters:
        :   - **syntax** – **[in]** Command syntax (for example: history).
            - **subcmd** – **[in]** Pointer to a subcommands array.
            - **help** – **[in]** Pointer to a command help string.
            - **handler** – **[in]** Pointer to a function handler.
            - **mandatory** – **[in]** Number of mandatory arguments including command name.
            - **optional** – **[in]** Number of optional arguments.

    SHELL\_COND\_CMD\_ARG\_REGISTER(flag, syntax, subcmd, help, handler, mandatory, optional)
    :   Macro for defining and adding a conditional root command (level 0) with required number of arguments.

        Macro can be used to create a command which can be conditionally present. It is and alternative to #ifdefs around command registration and command handler. If command is disabled handler and subcommands are removed from the application.

        See also

        [SHELL\_CMD\_ARG\_REGISTER](#group__shell__api_1gae8a8bbcbb842027c02a319b3fb976a3d) for details.

        Parameters:
        :   - **flag** – **[in]** Compile time flag. Command is present only if flag exists and equals 1.
            - **syntax** – **[in]** Command syntax (for example: history).
            - **subcmd** – **[in]** Pointer to a subcommands array.
            - **help** – **[in]** Pointer to a command help string.
            - **handler** – **[in]** Pointer to a function handler.
            - **mandatory** – **[in]** Number of mandatory arguments including command name.
            - **optional** – **[in]** Number of optional arguments.

    SHELL\_CMD\_REGISTER(syntax, subcmd, help, handler)
    :   Macro for defining and adding a root command (level 0) with arguments.

        Note

        All root commands must have different name.

        Parameters:
        :   - **syntax** – **[in]** Command syntax (for example: history).
            - **subcmd** – **[in]** Pointer to a subcommands array.
            - **help** – **[in]** Pointer to a command help string.
            - **handler** – **[in]** Pointer to a function handler.

    SHELL\_COND\_CMD\_REGISTER(flag, syntax, subcmd, help, handler)
    :   Macro for defining and adding a conditional root command (level 0) with arguments.

        See also

        [SHELL\_COND\_CMD\_ARG\_REGISTER](#group__shell__api_1ga6a3ed4ea9051ac138d22cc39134fb2e5).

        Parameters:
        :   - **flag** – **[in]** Compile time flag. Command is present only if flag exists and equals 1.
            - **syntax** – **[in]** Command syntax (for example: history).
            - **subcmd** – **[in]** Pointer to a subcommands array.
            - **help** – **[in]** Pointer to a command help string.
            - **handler** – **[in]** Pointer to a function handler.

    SHELL\_STATIC\_SUBCMD\_SET\_CREATE(name, ...)
    :   Macro for creating a subcommand set.

        It must be used outside of any function body.

        Example usage:

        ```c
        SHELL_STATIC_SUBCMD_SET_CREATE(
           foo,
           SHELL_CMD(abc, ...),
           SHELL_CMD(def, ...),
           SHELL_SUBCMD_SET_END
        )
        ```

        Parameters:
        :   - **name** – **[in]** Name of the subcommand set.
            - **...** – **[in]** List of commands created with [SHELL\_CMD\_ARG](#group__shell__api_1gad762c496a2ced65069b6d1d02a4d925c) or or [SHELL\_CMD](#group__shell__api_1ga24ade9db85af9a8776a45ba0084f4cca)

    SHELL\_SUBCMD\_SET\_CREATE(\_name, \_parent)
    :   Create set of subcommands.

        Commands to this set are added using [SHELL\_SUBCMD\_ADD](#group__shell__api_1ga85b0afcacd3831bf5c724590765e035f) and [SHELL\_SUBCMD\_COND\_ADD](#group__shell__api_1gab1b643efbaee748be0256e904642e310). Commands can be added from multiple files.

        Parameters:
        :   - **\_name** – **[in]** Name of the set. `_name` is used to refer the set in the parent command.
            - **\_parent** – **[in]** Set of comma separated parent commands in parenthesis, e.g. (foo\_cmd) if subcommands are for the root command “foo\_cmd”.

    SHELL\_SUBCMD\_COND\_ADD(\_flag, \_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt)
    :   Conditionally add command to the set of subcommands.

        Add command to the set created with [SHELL\_SUBCMD\_SET\_CREATE](#group__shell__api_1ga1e314886b70ee2e7e0763cd945a1a988).

        Note

        The name of the section is formed as concatenation of number of parent commands, names of all parent commands and own syntax. Number of parent commands is added to ensure that section prefix is unique. Without it subcommands of (foo) and (foo, cmd1) would mix.

        Parameters:
        :   - **\_flag** – **[in]** Compile time flag. Command is present only if flag exists and equals 1.
            - **\_parent** – **[in]** Parent command sequence. Comma separated in parenthesis.
            - **\_syntax** – **[in]** Command syntax (for example: history).
            - **\_subcmd** – **[in]** Pointer to a subcommands array.
            - **\_help** – **[in]** Pointer to a command help string.
            - **\_handler** – **[in]** Pointer to a function handler.
            - **\_mand** – **[in]** Number of mandatory arguments including command name.
            - **\_opt** – **[in]** Number of optional arguments.

    SHELL\_SUBCMD\_ADD(\_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt)
    :   Add command to the set of subcommands.

        Add command to the set created with [SHELL\_SUBCMD\_SET\_CREATE](#group__shell__api_1ga1e314886b70ee2e7e0763cd945a1a988).

        Parameters:
        :   - **\_parent** – **[in]** Parent command sequence. Comma separated in parenthesis.
            - **\_syntax** – **[in]** Command syntax (for example: history).
            - **\_subcmd** – **[in]** Pointer to a subcommands array.
            - **\_help** – **[in]** Pointer to a command help string.
            - **\_handler** – **[in]** Pointer to a function handler.
            - **\_mand** – **[in]** Number of mandatory arguments including command name.
            - **\_opt** – **[in]** Number of optional arguments.

    SHELL\_SUBCMD\_SET\_END
    :   Define ending subcommands set.

    SHELL\_DYNAMIC\_CMD\_CREATE(name, get)
    :   Macro for creating a dynamic entry.

        Parameters:
        :   - **name** – **[in]** Name of the dynamic entry.
            - **get** – **[in]** Pointer to the function returning dynamic commands array

    SHELL\_CMD\_ARG(syntax, subcmd, help, handler, mand, opt)
    :   Initializes a shell command with arguments.

        Note

        If a command will be called with wrong number of arguments shell will print an error message and command handler will not be called.

        Parameters:
        :   - **syntax** – **[in]** Command syntax (for example: history).
            - **subcmd** – **[in]** Pointer to a subcommands array.
            - **help** – **[in]** Pointer to a command help string.
            - **handler** – **[in]** Pointer to a function handler.
            - **mand** – **[in]** Number of mandatory arguments including command name.
            - **opt** – **[in]** Number of optional arguments.

    SHELL\_COND\_CMD\_ARG(flag, syntax, subcmd, help, handler, mand, opt)
    :   Initializes a conditional shell command with arguments.

        See also

        [SHELL\_CMD\_ARG](#group__shell__api_1gad762c496a2ced65069b6d1d02a4d925c). Based on the flag, creates a valid entry or an empty command which is ignored by the [shell](#structshell). It is an alternative to #ifdefs around command registration and command handler. However, empty structure is present in the flash even if command is disabled (subcommands and handler are removed). Macro internally handles case if flag is not defined so flag must be provided without any wrapper, e.g.: [SHELL\_COND\_CMD\_ARG(CONFIG\_FOO, …)](#group__shell__api_1ga68229f89484c3459d77cebb450ee1f24)

        Parameters:
        :   - **flag** – **[in]** Compile time flag. Command is present only if flag exists and equals 1.
            - **syntax** – **[in]** Command syntax (for example: history).
            - **subcmd** – **[in]** Pointer to a subcommands array.
            - **help** – **[in]** Pointer to a command help string.
            - **handler** – **[in]** Pointer to a function handler.
            - **mand** – **[in]** Number of mandatory arguments including command name.
            - **opt** – **[in]** Number of optional arguments.

    SHELL\_EXPR\_CMD\_ARG(\_expr, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt)
    :   Initializes a conditional shell command with arguments if expression gives non-zero result at compile time.

        See also

        [SHELL\_CMD\_ARG](#group__shell__api_1gad762c496a2ced65069b6d1d02a4d925c). Based on the expression, creates a valid entry or an empty command which is ignored by the [shell](#structshell). It should be used instead of [SHELL\_COND\_CMD\_ARG](#group__shell__api_1ga68229f89484c3459d77cebb450ee1f24) if condition is not a single configuration flag, e.g.: [SHELL\_EXPR\_CMD\_ARG](#group__shell__api_1ga6b07c55dd7d42873d604ae299b3cfdf9)([IS\_ENABLED(CONFIG\_FOO)](../../kernel/util/index.md#group__sys-util_1ga111fe4e9d63758262fc6810a782cb32a) && [IS\_ENABLED(CONFIG\_FOO\_SETTING\_1)](../../kernel/util/index.md#group__sys-util_1ga111fe4e9d63758262fc6810a782cb32a), …)

        Parameters:
        :   - **\_expr** – **[in]** Expression.
            - **\_syntax** – **[in]** Command syntax (for example: history).
            - **\_subcmd** – **[in]** Pointer to a subcommands array.
            - **\_help** – **[in]** Pointer to a command help string.
            - **\_handler** – **[in]** Pointer to a function handler.
            - **\_mand** – **[in]** Number of mandatory arguments including command name.
            - **\_opt** – **[in]** Number of optional arguments.

    SHELL\_CMD(\_syntax, \_subcmd, \_help, \_handler)
    :   Initializes a shell command.

        Parameters:
        :   - **\_syntax** – **[in]** Command syntax (for example: history).
            - **\_subcmd** – **[in]** Pointer to a subcommands array.
            - **\_help** – **[in]** Pointer to a command help string.
            - **\_handler** – **[in]** Pointer to a function handler.

    SHELL\_COND\_CMD(\_flag, \_syntax, \_subcmd, \_help, \_handler)
    :   Initializes a conditional shell command.

        See also

        [SHELL\_COND\_CMD\_ARG](#group__shell__api_1ga68229f89484c3459d77cebb450ee1f24).

        Parameters:
        :   - **\_flag** – **[in]** Compile time flag. Command is present only if flag exists and equals 1.
            - **\_syntax** – **[in]** Command syntax (for example: history).
            - **\_subcmd** – **[in]** Pointer to a subcommands array.
            - **\_help** – **[in]** Pointer to a command help string.
            - **\_handler** – **[in]** Pointer to a function handler.

    SHELL\_EXPR\_CMD(\_expr, \_syntax, \_subcmd, \_help, \_handler)
    :   Initializes shell command if expression gives non-zero result at compile time.

        See also

        [SHELL\_EXPR\_CMD\_ARG](#group__shell__api_1ga6b07c55dd7d42873d604ae299b3cfdf9).

        Parameters:
        :   - **\_expr** – **[in]** Compile time expression. Command is present only if expression is non-zero.
            - **\_syntax** – **[in]** Command syntax (for example: history).
            - **\_subcmd** – **[in]** Pointer to a subcommands array.
            - **\_help** – **[in]** Pointer to a command help string.
            - **\_handler** – **[in]** Pointer to a function handler.

    SHELL\_CMD\_DICT\_CREATE(\_data, \_handler)

    SHELL\_SUBCMD\_DICT\_SET\_CREATE(\_name, \_handler, ...)
    :   Initializes shell dictionary commands.

        This is a special kind of static commands. Dictionary commands can be used every time you want to use a pair: (string <-> corresponding data) in a command handler. The string is usually a verbal description of a given data. The idea is to use the string as a command syntax that can be prompted by the shell and corresponding data can be used to process the command.

        Example usage:

        ```c
        static int my_handler(const struct shell *sh,
                         size_t argc, char **argv, void *data)
        {
           int val = (int)data;

           shell_print(sh, "(syntax, value) : (%s, %d)", argv[0], val);
           return 0;
        }

        SHELL_SUBCMD_DICT_SET_CREATE(sub_dict_cmds, my_handler,
           (value_0, 0, "value 0"), (value_1, 1, "value 1"),
           (value_2, 2, "value 2"), (value_3, 3, "value 3")
        );
        SHELL_CMD_REGISTER(dictionary, &sub_dict_cmds, NULL, NULL);
        ```

        See also

        [shell\_dict\_cmd\_handler](#group__shell__api_1ga182f247052041f1236d13726589885e2)

        Parameters:
        :   - **\_name** – **[in]** Name of the dictionary subcommand set
            - **\_handler** – **[in]** Command handler common for all dictionary commands.
            - **...** – **[in]** Dictionary triplets: (command\_syntax, value, helper). Value will be passed to the \_handler as user data.

    SHELL\_DEFAULT\_BACKEND\_CONFIG\_FLAGS

    SHELL\_DEFINE(\_name, \_prompt, \_transport\_iface, \_log\_queue\_size, \_log\_timeout, \_shell\_flag)
    :   Macro for defining a shell instance.

        Parameters:
        :   - **\_name** – **[in]** Instance name.
            - **\_prompt** – **[in]** Shell default prompt string.
            - **\_transport\_iface** – **[in]** Pointer to the transport interface.
            - **\_log\_queue\_size** – **[in]** Logger processing queue size.
            - **\_log\_timeout** – **[in]** Logger thread timeout in milliseconds on full log queue. If queue is full logger thread is blocked for given amount of time before log message is dropped.
            - **\_shell\_flag** – **[in]** Shell output newline sequence.

    SHELL\_NORMAL
    :   Terminal default text color for shell\_fprintf function.

    SHELL\_INFO
    :   Green text color for shell\_fprintf function.

    SHELL\_OPTION
    :   Cyan text color for shell\_fprintf function.

    SHELL\_WARNING
    :   Yellow text color for shell\_fprintf function.

    SHELL\_ERROR
    :   Red text color for shell\_fprintf function.

    shell\_fprintf(sh, color, fmt, ...)

    shell\_info(\_sh, \_ft, ...)
    :   Print info message to the shell.

        See shell\_fprintf.

        Parameters:
        :   - **\_sh** – **[in]** Pointer to the shell instance.
            - **\_ft** – **[in]** Format string.
            - **...** – **[in]** List of parameters to print.

    shell\_print(\_sh, \_ft, ...)
    :   Print normal message to the shell.

        See shell\_fprintf.

        Parameters:
        :   - **\_sh** – **[in]** Pointer to the shell instance.
            - **\_ft** – **[in]** Format string.
            - **...** – **[in]** List of parameters to print.

    shell\_warn(\_sh, \_ft, ...)
    :   Print warning message to the shell.

        See shell\_fprintf.

        Parameters:
        :   - **\_sh** – **[in]** Pointer to the shell instance.
            - **\_ft** – **[in]** Format string.
            - **...** – **[in]** List of parameters to print.

    shell\_error(\_sh, \_ft, ...)
    :   Print error message to the shell.

        See shell\_fprintf.

        Parameters:
        :   - **\_sh** – **[in]** Pointer to the shell instance.
            - **\_ft** – **[in]** Format string.
            - **...** – **[in]** List of parameters to print.

    SHELL\_CMD\_HELP\_PRINTED
    :   Command’s help has been printed.

    Typedefs

    typedef void (\*shell\_dynamic\_get)(size\_t idx, struct [shell\_static\_entry](#c.shell_static_entry) \*entry)
    :   Shell dynamic command descriptor.

        Function shall fill the received [shell\_static\_entry](#structshell__static__entry) structure with requested (idx) dynamic subcommand data. If there is more than one dynamic subcommand available, the function shall ensure that the returned commands: entry->syntax are sorted in alphabetical order. If idx exceeds the available dynamic subcommands, the function must write to entry->syntax NULL value. This will indicate to the shell module that there are no more dynamic commands to read.

    typedef bool (\*shell\_device\_filter\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Filter callback type, for use with shell\_device\_lookup\_filter.

        This is used as an argument of shell\_device\_lookup\_filter to only return devices that match a specific condition, implemented by the filter.

        Param dev:
        :   pointer to a struct device.

        Return:
        :   bool, true if the filter matches the device type.

    typedef int (\*shell\_cmd\_handler)(const struct [shell](#c.shell) \*sh, size\_t argc, char \*\*argv)
    :   Shell command handler prototype.

        Param sh:
        :   Shell instance.

        Param argc:
        :   Arguments count.

        Param argv:
        :   Arguments.

        Retval 0:
        :   Successful command execution.

        Retval 1:
        :   Help printed and command not executed.

        Retval -EINVAL:
        :   Argument validation failed.

        Retval -ENOEXEC:
        :   Command not executed.

    typedef int (\*shell\_dict\_cmd\_handler)(const struct [shell](#c.shell) \*sh, size\_t argc, char \*\*argv, void \*data)
    :   Shell dictionary command handler prototype.

        Param sh:
        :   Shell instance.

        Param argc:
        :   Arguments count.

        Param argv:
        :   Arguments.

        Param data:
        :   Pointer to the user data.

        Retval 0:
        :   Successful command execution.

        Retval 1:
        :   Help printed and command not executed.

        Retval -EINVAL:
        :   Argument validation failed.

        Retval -ENOEXEC:
        :   Command not executed.

    typedef void (\*shell\_transport\_handler\_t)(enum [shell\_transport\_evt](#c.shell_transport_evt) evt, void \*context)

    typedef void (\*shell\_uninit\_cb\_t)(const struct [shell](#c.shell) \*sh, int res)

    typedef void (\*shell\_bypass\_cb\_t)(const struct [shell](#c.shell) \*sh, uint8\_t \*data, size\_t len)
    :   Bypass callback.

        Param sh:
        :   Shell instance.

        Param data:
        :   Raw data from transport.

        Param len:
        :   Data length.

    Enums

    enum shell\_receive\_state
    :   *Values:*

        enumerator SHELL\_RECEIVE\_DEFAULT

        enumerator SHELL\_RECEIVE\_ESC

        enumerator SHELL\_RECEIVE\_ESC\_SEQ

        enumerator SHELL\_RECEIVE\_TILDE\_EXP

    enum shell\_state
    :   *Values:*

        enumerator SHELL\_STATE\_UNINITIALIZED

        enumerator SHELL\_STATE\_INITIALIZED

        enumerator SHELL\_STATE\_ACTIVE

        enumerator SHELL\_STATE\_PANIC\_MODE\_ACTIVE
        :   Panic activated.

        enumerator SHELL\_STATE\_PANIC\_MODE\_INACTIVE
        :   Panic requested, not supported.

    enum shell\_transport\_evt
    :   Shell transport event.

        *Values:*

        enumerator SHELL\_TRANSPORT\_EVT\_RX\_RDY

        enumerator SHELL\_TRANSPORT\_EVT\_TX\_RDY

    enum shell\_signal
    :   *Values:*

        enumerator SHELL\_SIGNAL\_RXRDY

        enumerator SHELL\_SIGNAL\_LOG\_MSG

        enumerator SHELL\_SIGNAL\_KILL

        enumerator SHELL\_SIGNAL\_TXDONE

        enumerator SHELL\_SIGNALS

    enum shell\_flag
    :   Flags for setting shell output newline sequence.

        *Values:*

        enumerator SHELL\_FLAG\_CRLF\_DEFAULT = (1 << 0)
        :   Do not map CR or LF.

        enumerator SHELL\_FLAG\_OLF\_CRLF = (1 << 1)
        :   Map LF to CRLF on output.

    Functions

    const struct [device](../../kernel/drivers/index.md#c.device "device") \*shell\_device\_lookup(size\_t idx, const char \*prefix)
    :   Get by index a device that matches .

        This can be used, for example, to identify I2C\_1 as the second I2C device.

        Devices that failed to initialize or do not have a non-empty name are excluded from the candidates for a match.

        Parameters:
        :   - **idx** – the device number starting from zero.
            - **prefix** – optional name prefix used to restrict candidate devices. Indexing is done relative to devices with names that start with this text. Pass null if no prefix match is required.

    const struct [device](../../kernel/drivers/index.md#c.device "device") \*shell\_device\_filter(size\_t idx, [shell\_device\_filter\_t](#c.shell_device_filter_t) filter)
    :   Get a device by index and filter.

        This can be used to return devices matching a specific type.

        Devices that the filter returns false for, failed to initialize or do not have a non-empty name are excluded from the candidates for a match.

        Parameters:
        :   - **idx** – the device number starting from zero.
            - **filter** – a pointer to a [shell\_device\_filter\_t](#group__shell__api_1gaa2b8cf8ac78b8355408ef94958ebdc70) function that returns true if the device matches the filter.

    int shell\_init(const struct [shell](#c.shell) \*sh, const void \*transport\_config, struct [shell\_backend\_config\_flags](#c.shell_backend_config_flags) cfg\_flags, bool log\_backend, uint32\_t init\_log\_level)
    :   Function for initializing a transport layer and internal shell state.

        Parameters:
        :   - **sh** – **[in]** Pointer to shell instance.
            - **transport\_config** – **[in]** Transport configuration during initialization.
            - **cfg\_flags** – **[in]** Initial backend configuration flags. Shell will copy this data.
            - **log\_backend** – If true, the console will be used as logger backend.
            - **init\_log\_level** – **[in]** Default severity level for the logger.

        Returns:
        :   Standard error code.

    void shell\_uninit(const struct [shell](#c.shell) \*sh, [shell\_uninit\_cb\_t](#c.shell_uninit_cb_t) cb)
    :   Uninitializes the transport layer and the internal shell state.

        Parameters:
        :   - **sh** – Pointer to shell instance.
            - **cb** – Callback called when uninitialization is completed.

    int shell\_start(const struct [shell](#c.shell) \*sh)
    :   Function for starting shell processing.

        Parameters:
        :   - **sh** – Pointer to the shell instance.

        Returns:
        :   Standard error code.

    int shell\_stop(const struct [shell](#c.shell) \*sh)
    :   Function for stopping shell processing.

        Parameters:
        :   - **sh** – Pointer to shell instance.

        Returns:
        :   Standard error code.

    void shell\_fprintf\_impl(const struct [shell](#c.shell) \*sh, enum shell\_vt100\_color color, const char \*fmt, ...)
    :   printf-like function which sends formatted data stream to the shell.

        This function can be used from the command handler or from threads, but not from an interrupt context.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **color** – **[in]** Printed text color.
            - **fmt** – **[in]** Format string.
            - **...** – **[in]** List of parameters to print.

    void shell\_vfprintf(const struct [shell](#c.shell) \*sh, enum shell\_vt100\_color color, const char \*fmt, va\_list args)
    :   vprintf-like function which sends formatted data stream to the shell.

        This function can be used from the command handler or from threads, but not from an interrupt context. It is similar to [shell\_fprintf()](#group__shell__api_1ga1fd1671311b112f0c87ab2dafd801105) but takes a va\_list instead of variable arguments.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **color** – **[in]** Printed text color.
            - **fmt** – **[in]** Format string.
            - **args** – **[in]** List of parameters to print.

    void shell\_hexdump\_line(const struct [shell](#c.shell) \*sh, unsigned int offset, const uint8\_t \*data, size\_t len)
    :   Print a line of data in hexadecimal format.

        Each line shows the offset, bytes and then ASCII representation.

        For example:

        00008010: 20 25 00 20 2f 48 00 08 80 05 00 20 af 46 00 | %. /H.. … .F. |

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **offset** – **[in]** Offset to show for this line.
            - **data** – **[in]** Pointer to data.
            - **len** – **[in]** Length of data.

    void shell\_hexdump(const struct [shell](#c.shell) \*sh, const uint8\_t \*data, size\_t len)
    :   Print data in hexadecimal format.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **data** – **[in]** Pointer to data.
            - **len** – **[in]** Length of data.

    void shell\_process(const struct [shell](#c.shell) \*sh)
    :   Process function, which should be executed when data is ready in the transport interface.

        To be used if shell thread is disabled.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.

    int shell\_prompt\_change(const struct [shell](#c.shell) \*sh, const char \*prompt)
    :   Change displayed shell prompt.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **prompt** – **[in]** New shell prompt.

        Returns:
        :   0 Success.

        Returns:
        :   -EINVAL Pointer to new prompt is not correct.

    void shell\_help(const struct [shell](#c.shell) \*sh)
    :   Prints the current command help.

        Function will print a help string with: the currently entered command and subcommands (if they exist).

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.

    int shell\_execute\_cmd(const struct [shell](#c.shell) \*sh, const char \*cmd)
    :   Execute command.

        Pass command line to shell to execute.

        Note: This by no means makes any of the commands a stable interface, so this function should only be used for debugging/diagnostic.

        This function must not be called from shell command context!

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance. It can be NULL when the  [`CONFIG_SHELL_BACKEND_DUMMY`](../../kconfig.md#CONFIG_SHELL_BACKEND_DUMMY "CONFIG_SHELL_BACKEND_DUMMY") option is enabled.
            - **cmd** – Command to be executed.

        Returns:
        :   Result of the execution

    int shell\_set\_root\_cmd(const char \*cmd)
    :   Set root command for all shell instances.

        It allows setting from the code the root command. It is an equivalent of calling select command with one of the root commands as the argument (e.g “select log”) except it sets command for all shell instances.

        Parameters:
        :   - **cmd** – String with one of the root commands or null pointer to reset.

        Return values:
        :   - **0** – if root command is set.
            - **-EINVAL** – if invalid root command is provided.

    void shell\_set\_bypass(const struct [shell](#c.shell) \*sh, [shell\_bypass\_cb\_t](#c.shell_bypass_cb_t) bypass)
    :   Set bypass callback.

        Bypass callback is called whenever data is received. Shell is bypassed and data is passed directly to the callback. Use null to disable bypass functionality.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **bypass** – **[in]** Bypass callback or null to disable.

    bool shell\_ready(const struct [shell](#c.shell) \*sh)
    :   Get shell readiness to execute commands.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.

        Return values:
        :   - **true** – Shell backend is ready to execute commands.
            - **false** – Shell backend is not initialized or not started.

    int shell\_insert\_mode\_set(const struct [shell](#c.shell) \*sh, bool val)
    :   Allow application to control text insert mode.

        Value is modified atomically and the previous value is returned.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **val** – **[in]** Insert mode.

        Return values:
        :   - **0** – or 1: previous value
            - **-EINVAL** – if shell is NULL.

    int shell\_use\_colors\_set(const struct [shell](#c.shell) \*sh, bool val)
    :   Allow application to control whether terminal output uses colored syntax.

        Value is modified atomically and the previous value is returned.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **val** – **[in]** Color mode.

        Return values:
        :   - **0** – or 1: previous value
            - **-EINVAL** – if shell is NULL.

    int shell\_use\_vt100\_set(const struct [shell](#c.shell) \*sh, bool val)
    :   Allow application to control whether terminal is using vt100 commands.

        Value is modified atomically and the previous value is returned.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **val** – **[in]** vt100 mode.

        Return values:
        :   - **0** – or 1: previous value
            - **-EINVAL** – if shell is NULL.

    int shell\_echo\_set(const struct [shell](#c.shell) \*sh, bool val)
    :   Allow application to control whether user input is echoed back.

        Value is modified atomically and the previous value is returned.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **val** – **[in]** Echo mode.

        Return values:
        :   - **0** – or 1: previous value
            - **-EINVAL** – if shell is NULL.

    int shell\_obscure\_set(const struct [shell](#c.shell) \*sh, bool obscure)
    :   Allow application to control whether user input is obscured with asterisks &#8212; useful for implementing passwords.

        Value is modified atomically and the previous value is returned.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **obscure** – **[in]** Obscure mode.

        Return values:
        :   - **0** – or 1: previous value.
            - **-EINVAL** – if shell is NULL.

    int shell\_mode\_delete\_set(const struct [shell](#c.shell) \*sh, bool val)
    :   Allow application to control whether the delete key backspaces or deletes.

        Value is modified atomically and the previous value is returned.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance.
            - **val** – **[in]** Delete mode.

        Return values:
        :   - **0** – or 1: previous value
            - **-EINVAL** – if shell is NULL.

    int shell\_get\_return\_value(const struct [shell](#c.shell) \*sh)
    :   Retrieve return value of most recently executed shell command.

        Parameters:
        :   - **sh** – **[in]** Pointer to the shell instance

        Return values:
        :   **return** – value of previous command

    Variables

    const struct [log\_backend\_api](../logging/index.md#c.log_backend_api "log_backend_api") log\_backend\_shell\_api

    union shell\_cmd\_entry
    :   *#include <shell.h>*

        Shell command descriptor.

        Public Members

        [shell\_dynamic\_get](#c.shell_dynamic_get) dynamic\_get
        :   Pointer to function returning dynamic commands.

        const struct [shell\_static\_entry](#c.shell_static_entry) \*entry
        :   Pointer to array of static commands.

    struct shell\_static\_args
    :   *#include <shell.h>*

        Public Members

        uint8\_t mandatory
        :   Number of mandatory arguments.

        uint8\_t optional
        :   Number of optional arguments.

    struct shell\_static\_entry
    :   *#include <shell.h>*

        Public Members

        const char \*syntax
        :   Command syntax strings.

        const char \*help
        :   Command help string.

        const union [shell\_cmd\_entry](#c.shell_cmd_entry) \*subcmd
        :   Pointer to subcommand.

        [shell\_cmd\_handler](#c.shell_cmd_handler) handler
        :   Command handler.

        struct [shell\_static\_args](#c.shell_static_args) args
        :   Command arguments.

    struct shell\_transport\_api
    :   *#include <shell.h>*

        Unified shell transport interface.

        Public Members

        int (\*init)(const struct [shell\_transport](#c.shell_transport) \*transport, const void \*config, [shell\_transport\_handler\_t](#c.shell_transport_handler_t) evt\_handler, void \*context)
        :   Function for initializing the shell transport interface.

            Param transport:
            :   **[in]** Pointer to the transfer instance.

            Param config:
            :   **[in]** Pointer to instance configuration.

            Param evt\_handler:
            :   **[in]** Event handler.

            Param context:
            :   **[in]** Pointer to the context passed to event handler.

            Return:
            :   Standard error code.

        int (\*uninit)(const struct [shell\_transport](#c.shell_transport) \*transport)
        :   Function for uninitializing the shell transport interface.

            Param transport:
            :   **[in]** Pointer to the transfer instance.

            Return:
            :   Standard error code.

        int (\*enable)(const struct [shell\_transport](#c.shell_transport) \*transport, bool blocking\_tx)
        :   Function for enabling transport in given TX mode.

            Function can be used to reconfigure TX to work in blocking mode.

            Param transport:
            :   Pointer to the transfer instance.

            Param blocking\_tx:
            :   If true, the transport TX is enabled in blocking mode.

            Return:
            :   NRF\_SUCCESS on successful enabling, error otherwise (also if not supported).

        int (\*write)(const struct [shell\_transport](#c.shell_transport) \*transport, const void \*data, size\_t length, size\_t \*cnt)
        :   Function for writing data to the transport interface.

            Param transport:
            :   **[in]** Pointer to the transfer instance.

            Param data:
            :   **[in]** Pointer to the source buffer.

            Param length:
            :   **[in]** Source buffer length.

            Param cnt:
            :   **[out]** Pointer to the sent bytes counter.

            Return:
            :   Standard error code.

        int (\*read)(const struct [shell\_transport](#c.shell_transport) \*transport, void \*data, size\_t length, size\_t \*cnt)
        :   Function for reading data from the transport interface.

            Param transport:
            :   **[in]** Pointer to the transfer instance.

            Param data:
            :   **[in]** Pointer to the destination buffer.

            Param length:
            :   **[in]** Destination buffer length.

            Param cnt:
            :   **[out]** Pointer to the received bytes counter.

            Return:
            :   Standard error code.

        void (\*update)(const struct [shell\_transport](#c.shell_transport) \*transport)
        :   Function called in shell thread loop.

            Can be used for backend operations that require longer execution time

            Param transport:
            :   **[in]** Pointer to the transfer instance.

    struct shell\_transport
    :   *#include <shell.h>*

    struct shell\_stats
    :   *#include <shell.h>*

        Shell statistics structure.

        Public Members

        atomic\_t log\_lost\_cnt
        :   Lost log counter.

    struct shell\_backend\_config\_flags
    :   *#include <shell.h>*

        Public Members

        uint32\_t insert\_mode
        :   Controls insert mode for text introduction.

        uint32\_t echo
        :   Controls shell echo.

        uint32\_t obscure
        :   If echo on, print asterisk instead.

        uint32\_t mode\_delete
        :   Operation mode of backspace key.

        uint32\_t use\_colors
        :   Controls colored syntax.

        uint32\_t use\_vt100
        :   Controls VT100 commands usage in shell.

    struct shell\_backend\_ctx\_flags
    :   *#include <shell.h>*

        Public Members

        uint32\_t processing
        :   Shell is executing process function.

        uint32\_t history\_exit
        :   Request to exit history mode.

        uint32\_t last\_nl
        :   Last received new line character.

        uint32\_t cmd\_ctx
        :   Shell is executing command.

        uint32\_t print\_noinit
        :   Print request from not initialized shell.

        uint32\_t sync\_mode
        :   Shell in synchronous mode.

        uint32\_t handle\_log
        :   Shell is handling logger backend.

    union shell\_backend\_cfg
    :   *#include <shell.h>*

        Public Members

        atomic\_t value

        struct [shell\_backend\_config\_flags](#c.shell_backend_config_flags) flags

    union shell\_backend\_ctx
    :   *#include <shell.h>*

        Public Members

        uint32\_t value

        struct [shell\_backend\_ctx\_flags](#c.shell_backend_ctx_flags) flags

    struct shell\_ctx
    :   *#include <shell.h>*

        Shell instance context.

        Public Members

        enum [shell\_state](#c.shell_state) state
        :   Internal module state.

        enum [shell\_receive\_state](#c.shell_receive_state) receive\_state
        :   Escape sequence indicator.

        struct [shell\_static\_entry](#c.shell_static_entry) active\_cmd
        :   Currently executed command.

        const struct [shell\_static\_entry](#c.shell_static_entry) \*selected\_cmd
        :   New root command.

            If NULL shell uses default root commands.

        struct shell\_vt100\_ctx vt100\_ctx
        :   VT100 color and cursor position, terminal width.

        [shell\_uninit\_cb\_t](#c.shell_uninit_cb_t) uninit\_cb
        :   Callback called from shell thread context when unitialization is completed just before aborting shell thread.

        [shell\_bypass\_cb\_t](#c.shell_bypass_cb_t) bypass
        :   When bypass is set, all incoming data is passed to the callback.

            Logging level for a backend.

        uint16\_t cmd\_buff\_len
        :   Command length.

        uint16\_t cmd\_buff\_pos
        :   Command buffer cursor position.

        uint16\_t cmd\_tmp\_buff\_len
        :   Command length in tmp buffer.

        char cmd\_buff[0]
        :   Command input buffer.

        char temp\_buff[0]
        :   Command temporary buffer.

        char printf\_buff[0]
        :   Printf buffer size.

        struct [k\_poll\_event](../../kernel/services/polling.md#c.k_poll_event "k_poll_event") events[[SHELL\_SIGNALS](#c.shell_signal.SHELL_SIGNALS)]
        :   Events that should be used only internally by shell thread.

            Event for SHELL\_SIGNAL\_TXDONE is initialized but unused.

    struct shell
    :   *#include <shell.h>*

        Shell instance internals.

        Public Members

        const char \*default\_prompt
        :   shell default prompt.

        const struct [shell\_transport](#c.shell_transport) \*iface
        :   Transport interface.

        struct [shell\_ctx](#c.shell_ctx) \*ctx
        :   Internal context.
