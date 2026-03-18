---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/uart/echo_bot/README.html
original_path: samples/drivers/uart/echo_bot/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# UART echo

## Overview

This sample demonstrates how to use the UART serial driver with a simple
echo bot. It reads data from the console and echoes the characters back after
an end of line (return key) is received.

The polling API is used for sending data and the interrupt-driven API
for receiving, so that in theory the thread could do something else
while waiting for incoming data.

By default, the UART peripheral that is normally used for the Zephyr shell
is used, so that almost every board should be supported.

## Building and Running

Build and flash the sample as follows, changing `nrf52840dk/nrf52840` for
your board:

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/uart/echo_bot
west flash
```

### Sample Output

```shell
Hello! I\'m your echo bot.
Tell me something and press enter:
# Type e.g. "Hi there!" and hit enter!
Echo: Hi there!
```
