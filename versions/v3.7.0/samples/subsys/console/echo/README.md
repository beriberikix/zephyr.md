---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/console/echo/README.html
original_path: samples/subsys/console/echo/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Console echo

## Overview

This example shows how the [`console_getchar()`](../../../../services/console.md#c.console_getchar "console_getchar") and
[`console_putchar()`](../../../../services/console.md#c.console_putchar "console_putchar") functions can be used to echo an input character
back to the console.

## Requirements

UART console is required to run this sample.

## Building and Running

Build and flash the sample as follows, changing `nucleo_f401re` for your
board. Alternatively you can run this using QEMU, as described in
[console\_getchar()](../getchar/README.md#console_getchar "Use console_getchar() to read an input character from the console.").

```shell
west build -b nucleo_f401re samples/subsys/console/echo
west flash
```

Following the initial prompt given by the firmware, start pressing keys on a
keyboard, and they will be echoed back to the terminal program you are using.

### Sample Output

```shell
You should see another line with instructions below. If not,
the (interrupt-driven) console device doesn't work as expected:
Start typing characters to see them echoed back
```
