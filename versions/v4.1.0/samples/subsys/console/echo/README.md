---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/console/echo/README.html
original_path: samples/subsys/console/echo/README.html
---

# Console echo

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/console/echo/README.rst/..)

## Overview

This example shows how the [`console_getchar()`](../../../../doxygen/html/group__console__api.md#ga2ba36eb1081cd0b98aa43216ccd6fbd5) and
[`console_putchar()`](../../../../doxygen/html/group__console__api.md#ga7bd842f1cda6c8218cb1d41420e4de49) functions can be used to echo an input character
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

## See also

[Console API](../../../../doxygen/html/group__console__api.md)
