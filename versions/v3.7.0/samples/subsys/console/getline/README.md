---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/console/getline/README.html
original_path: samples/subsys/console/getline/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# console\_getline()

## Overview

This example shows how to use [`console_getline()`](../../../../services/console.md#c.console_getline "console_getline") function.
Similar to the well-known ANSI C gets() and fgets() functions,
[`console_getline()`](../../../../services/console.md#c.console_getline "console_getline") either returns the next available input
line or blocks waiting for one. Using this function, it should be fairly
easy to port existing ANSI C, POSIX, or Linux applications which process
console input line by line. The sample also allows to see details of how
a line is returned by the function.

If you are interested in character by character console input, see
[console\_getchar()](../getchar/README.md#console_getchar "Use console_getchar() to read an input character from the console.").

## Requirements

UART console is required to run this sample.

## Building and Running

The easiest way to run this sample is using QEMU:

```shell
west build -b qemu_x86 samples/subsys/console/getline
west build -t run
```

Now start pressing keys on a keyboard, followed by Enter. The input line
will be printed back, with a hex code of the last character, to show that
line does not include any special “end of line” characters (like LF, CR,
etc.)
Exit QEMU by pressing `CTRL+A` `x`.
