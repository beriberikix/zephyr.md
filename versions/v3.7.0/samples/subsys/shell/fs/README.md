---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/shell/fs/README.html
original_path: samples/subsys/shell/fs/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# File system shell

## Overview

This example provides shell access to a LittleFS file system partition in flash.

## Requirements

A board with LittleFS file system support and UART console

## Building

### native\_sim

You can build this sample for [native\_sim](../../../../boards/native/native_sim/doc/index.md#native-sim) with:

```shell
west build -b native_sim samples/subsys/shell/fs
```

Which by default will use the flash simulator. The flash simulator will use a file,
`flash.bin`, in the current directory to keep the flash content.
You have several options to control this. You can check them with:

```shell
zephyr/zephyr.exe -help
```

Check the [native\_sim UART documentation](../../../../boards/native/native_sim/doc/index.md#native-ptty-uart) for information on how to connect
to the UART.

#### With FUSE access in the host filesystem

If you enable the [host FUSE filsystem access](../../../../boards/native/native_sim/doc/index.md#native-fuse-flash)
you will also have the flash filesystem mounted and accessible from your Linux host filesystem.

Before starting a build, make sure that the i386 pkgconfig directory is in your
search path and that a 32-bit version of libfuse is installed. For more
background information on this requirement check
[the native\_sim documentation](../../../../boards/native/native_sim/doc/index.md#native-fuse-flash).

```shell
export PKG_CONFIG_PATH=/usr/lib/i386-linux-gnu/pkgconfig
```

```shell
west build -b native_sim samples/subsys/shell/fs -- -DCONFIG_FUSE_FS_ACCESS=y
```

### Reel Board

```shell
west build -b reel_board samples/subsys/shell/fs
```

### Particle Xenon

This target is customized to support the same SPI NOR partition table as
the [LittleFS filesystem](../../fs/littlefs/README.md#littlefs "Use file system API over LittleFS.") sample.

```shell
west build -b particle_xenon samples/subsys/shell/fs
```

### Flash load

If you want to use the ‘flash load’ command then build the sample with the
‘prj\_flash\_load.conf’ configuration file. It has defined a larger RX buffer.
If the buffer is too small then some data may be lost during transfer of large
files.

## Running

Once the board has booted, you will be presented with a shell prompt.
All file system related commands are available as sub-commands of fs.

Begin by mounting the LittleFS file system.

```shell
fs mount littlefs /lfs
```

### Loading filesystem from host PC to flash memory

Use command:

```shell
flash load <address> <size>
```

It allows loading the data via UART, directly into flash memory at a given
address. Data must be aligned to a value dependent on the target flash memory,
otherwise it will cause an error and nothing will be loaded.

From the host side file system must be loaded with ‘dd’ tool with ‘bs=64’
(if the file is loaded in chunks greater than 64B the data is lost and isn’t
received by the Zephyr shell).

Example in Zephyr console:

```shell
flash load 0x7a000 0x5000
```

Example in the host PC:

```shell
dd if=filesystem of=/dev/ttyACM0 bs=64
```

During the transfer there are printed messages indicating how many chunks are
already written. After the successful transfer the ‘Read all’ message is
printed.

### Files System Shell Commands

#### Mount

Mount a file system partition to a given mount point

```shell
fs mount (littlefs|fat) <path>
```

#### Ls

List all files and directories in a given path

```shell
fs ls [path]
```

#### Cd

Change current working directory to given path

```shell
fs cd [path]
```

#### Pwd

List current working directory

```shell
fs pwd
```

#### Write

Write hexadecimal numbers to a given file.
Optionally a offset in the file can be given.

```shell
fs write <path> [-o <offset>] <hex number> ...
```

#### Read

Read file and dump in hex and ASCII format

```shell
fs read <path>
```

#### Trunc

Truncate a given file

```shell
fs trunc <path>
```

#### Mkdir

Create a directory

```shell
fs mkdir <path>
```

#### Rm

Remove a file or directory

```shell
fs rm <path>
```

### Flash Host Access

For the [native sim board](../../../../boards/native/native_sim/doc/index.md#native-sim) the flash partitions can be accessed from the host
Linux system.

By default the flash partitions are accessible through the directory *flash*
relative to the directory where the build is started.
