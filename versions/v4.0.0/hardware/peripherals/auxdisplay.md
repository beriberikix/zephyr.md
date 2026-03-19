---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/auxdisplay.html
original_path: hardware/peripherals/auxdisplay.html
---

# Auxiliary Display (auxdisplay)

## Overview

Auxiliary Displays are text-based displays that have simple interfaces for
displaying textual, numeric or alphanumeric data, as opposed to the
[Display Interface](display/index.md#display-api), auxiliary displays do not support custom
graphical output to displays (and most often monochrome), the most
advanced custom feature supported is generation of custom characters.
These inexpensive displays are commonly found with various configurations
and sizes, a common display size is 16 characters by 2 lines.

This API is unstable and subject to change.

## Configuration Options

Related configuration options:

- [`CONFIG_AUXDISPLAY`](../../kconfig.md#CONFIG_AUXDISPLAY "CONFIG_AUXDISPLAY")
- [`CONFIG_AUXDISPLAY_INIT_PRIORITY`](../../kconfig.md#CONFIG_AUXDISPLAY_INIT_PRIORITY "CONFIG_AUXDISPLAY_INIT_PRIORITY")

## API Reference

[Text Display Interface](../../doxygen/html/group__auxdisplay__interface.md)

Related code samples

- [Auxiliary display](../../samples/drivers/auxdisplay/README.md#auxdisplay "Output "Hello  World" to an auxiliary display.")Output "Hello World" to an auxiliary display.
