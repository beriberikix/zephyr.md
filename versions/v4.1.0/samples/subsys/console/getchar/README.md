---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/console/getchar/README.html
original_path: samples/subsys/console/getchar/README.html
---

# console\_getchar()

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/console/getchar/README.rst/..)

## Overview

This example shows how to use [`console_getchar()`](../../../../doxygen/html/group__console__api.md#ga2ba36eb1081cd0b98aa43216ccd6fbd5) function.
Similar to the well-known ANSI C getchar() function,
[`console_getchar()`](../../../../doxygen/html/group__console__api.md#ga2ba36eb1081cd0b98aa43216ccd6fbd5) either returns the next available input
character or blocks waiting for one. Using this function, it should be
fairly easy to port existing ANSI C, POSIX, or Linux applications which
process console input character by character. The sample also allows to
see key/character codes as returned by the function.

If you are interested in line by line console input, see
[console\_getline()](../getline/README.md#console_getline "Use console_getline() to read an input line from the console.").

## Requirements

UART console is required to run this sample.

## Building and Running

The easiest way to run this sample is using QEMU:

```shell
west build -b qemu_x86 samples/subsys/console/getchar
west build -t run
```

Now start pressing keys on a keyboard, and they will be printed both as
hex values and in character form. Be sure to press Enter, Up/Down, etc.
key to check what control characters are produced for them.
Exit QEMU by pressing `CTRL+A` `x`.
