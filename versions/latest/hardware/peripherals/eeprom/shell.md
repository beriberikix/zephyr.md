---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/eeprom/shell.html
original_path: hardware/peripherals/eeprom/shell.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# EEPROM Shell

## [Overview](#id2)

The EEPROM shell provides an `eeprom` command with a set of subcommands for the [shell](../../../services/shell/index.md#shell-api) module. It allows testing and exploring the [EEPROM](api.md#eeprom-api) driver API
through an interactive interface without having to write a dedicated application. The EEPROM shell
can also be enabled in existing applications to aid in interactive debugging of EEPROM issues.

In order to enable the EEPROM shell, the following [Kconfig](../../../build/kconfig/index.md#kconfig) options must be enabled:

- [`CONFIG_SHELL`](../../../kconfig.md#CONFIG_SHELL "CONFIG_SHELL")
- [`CONFIG_EEPROM`](../../../kconfig.md#CONFIG_EEPROM "CONFIG_EEPROM")
- [`CONFIG_EEPROM_SHELL`](../../../kconfig.md#CONFIG_EEPROM_SHELL "CONFIG_EEPROM_SHELL")

For example, building the [Hello World](../../../samples/hello_world/README.md#hello-world) sample for the [Native simulator - native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) with the EEPROM shell:

```shell
# From the root of the zephyr repository
west build -b native_sim samples/hello_world -- -DCONFIG_SHELL=y -DCONFIG_EEPROM=y -DCONFIG_EEPROM_SHELL=y
```

See the [shell](../../../services/shell/index.md#shell-api) documentation for general instructions on how to connect and
interact with the shell. The EEPROM shell comes with built-in help (unless
[`CONFIG_SHELL_HELP`](../../../kconfig.md#CONFIG_SHELL_HELP "CONFIG_SHELL_HELP") is disabled). The built-in help messages can be printed by
passing `-h` or `--help` to the `eeprom` command or any of its subcommands. All subcommands
also support tab-completion of their arguments.

Tip

All of the EEPROM shell subcommands take the name of an EEPROM peripheral as their first argument,
which also supports tab-completion. A list of all devices available can be obtained using the
`device list` shell command when [`CONFIG_DEVICE_SHELL`](../../../kconfig.md#CONFIG_DEVICE_SHELL "CONFIG_DEVICE_SHELL") is enabled. The examples
below all use the device name `eeprom@0`.

## [EEPROM Size](#id3)

The size of an EEPROM can be inspected using the `eeprom size` subcommand as shown below:

```shell
uart:~$ eeprom size eeprom@0
32768 bytes
```

## [Writing Data](#id4)

Data can be written to an EEPROM using the `eeprom write` subcommand. This subcommand takes at
least three arguments; the EEPROM device name, the offset to start writing to, and at least one data
byte. In the following example, the hexadecimal sequence of bytes `0x0d 0x0e 0x0a 0x0d 0x0b 0x0e
0x0e 0x0f` is written to offset `0x0`:

```shell
uart:~$ eeprom write eeprom@0 0x0 0x0d 0x0e 0x0a 0x0d 0x0b 0x0e 0x0e 0x0f
Writing 8 bytes to EEPROM...
Verifying...
Verify OK
```

It is also possible to fill a portion of the EEPROM with the same pattern using the `eeprom fill`
subcommand. In the following example, the pattern `0xaa` is written to 16 bytes starting at offset
`0x8`:

```shell
uart:~$ eeprom fill eeprom@0 0x8 16 0xaa
Writing 16 bytes of 0xaa to EEPROM...
Verifying...
Verify OK
```

## [Reading Data](#id5)

Data can be read from an EEPROM using the `eeprom read` subcommand. This subcommand takes three
arguments; the EEPROM device name, the offset to start reading from, and the number of bytes to
read:

```shell
uart:~$ eeprom read eeprom@0 0x0 8
Reading 8 bytes from EEPROM, offset 0...
00000000: 0d 0e 0a 0d 0b 0e 0e 0f                          |........         |
```
