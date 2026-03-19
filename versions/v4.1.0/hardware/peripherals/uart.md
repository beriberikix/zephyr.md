---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/uart.html
original_path: hardware/peripherals/uart.html
---

# Universal Asynchronous Receiver-Transmitter (UART)

## Overview

Zephyr provides three different ways to access the UART peripheral. Depending
on the method, different API functions are used according to below sections:

1. [Polling API](#uart-polling-api)
2. [Interrupt-driven API](#uart-interrupt-api)
3. [Asynchronous API](#uart-async-api) using [Direct Memory Access (DMA)](dma.md#dma-api)

Polling is the most basic method to access the UART peripheral. The reading
function, [`uart_poll_in()`](../../doxygen/html/group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d), is a non-blocking function and returns a character
or `-1` when no valid data is available. The writing function,
[`uart_poll_out()`](../../doxygen/html/group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c), is a blocking function and the thread waits until the given
character is sent.

With the Interrupt-driven API, possibly slow communication can happen in the
background while the thread continues with other tasks. The Kernel’s
[Data Passing](../../kernel/services/index.md#kernel-data-passing-api) features can be used to communicate between
the thread and the UART driver.

The Asynchronous API allows to read and write data in the background using DMA
without interrupting the MCU at all. However, the setup is more complex
than the other methods.

Warning

Interrupt-driven API and the Asynchronous API should NOT be used at
the same time for the same hardware peripheral, since both APIs require
hardware interrupts to function properly. Using the callbacks for both
APIs would result in interference between each other.
[`CONFIG_UART_EXCLUSIVE_API_CALLBACKS`](../../kconfig.md#CONFIG_UART_EXCLUSIVE_API_CALLBACKS "CONFIG_UART_EXCLUSIVE_API_CALLBACKS") is enabled by default
so that only the callbacks associated with one API is active at a time.

## Configuration Options

Most importantly, the Kconfig options define whether the polling API (default),
the interrupt-driven API or the asynchronous API can be used. Only enable the
features you need in order to minimize memory footprint.

Related configuration options:

- [`CONFIG_SERIAL`](../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL")
- [`CONFIG_UART_INTERRUPT_DRIVEN`](../../kconfig.md#CONFIG_UART_INTERRUPT_DRIVEN "CONFIG_UART_INTERRUPT_DRIVEN")
- [`CONFIG_UART_ASYNC_API`](../../kconfig.md#CONFIG_UART_ASYNC_API "CONFIG_UART_ASYNC_API")
- [`CONFIG_UART_WIDE_DATA`](../../kconfig.md#CONFIG_UART_WIDE_DATA "CONFIG_UART_WIDE_DATA")
- [`CONFIG_UART_USE_RUNTIME_CONFIGURE`](../../kconfig.md#CONFIG_UART_USE_RUNTIME_CONFIGURE "CONFIG_UART_USE_RUNTIME_CONFIGURE")
- [`CONFIG_UART_LINE_CTRL`](../../kconfig.md#CONFIG_UART_LINE_CTRL "CONFIG_UART_LINE_CTRL")
- [`CONFIG_UART_DRV_CMD`](../../kconfig.md#CONFIG_UART_DRV_CMD "CONFIG_UART_DRV_CMD")

## API Reference

[UART Interface](../../doxygen/html/group__uart__interface.md)

Related code samples

- [802.15.4 "serial-radio"](../../samples/net/wpan_serial/README.md#wpan-serial "Implement a slip-radio device for Contiki-based border routers.")Implement a slip-radio device for Contiki-based border routers.
- [Console over USB CDC ACM](../../samples/subsys/usb/console-next/README.md#usbd-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")Output "Hello World!" to the console over USB CDC ACM.
- [HCI 3-wire (H:5)](../../samples/bluetooth/hci_uart_3wire/README.md#bluetooth_hci_uart_3wire "Expose a Bluetooth controller to another device or CPU over H5:HCI transport.")Expose a Bluetooth controller to another device or CPU over H5:HCI transport.
- [HCI UART](../../samples/bluetooth/hci_uart/README.md#bluetooth_hci_uart "Expose a Bluetooth controller to another device or CPU over UART.")Expose a Bluetooth controller to another device or CPU over UART.
- [HCI UART async](../../samples/bluetooth/hci_uart_async/README.md#bluetooth_hci_uart_async "Expose a Bluetooth controller to another device or CPU over asynchronous UART.")Expose a Bluetooth controller to another device or CPU over asynchronous UART.
- [Native TTY UART](../../samples/drivers/uart/native_tty/README.md#uart-native-tty "Use native TTY driver to send and receive data between two UART-to-USB bridge dongles.")Use native TTY driver to send and receive data between two UART-to-USB bridge dongles.
- [Single-wire UART](../../samples/boards/st/uart/single_wire/README.md#uart-stm32-single-wire "Use single-wire/half-duplex UART functionality of STM32 devices.")Use single-wire/half-duplex UART functionality of STM32 devices.
- [UART echo](../../samples/drivers/uart/echo_bot/README.md#uart "Read data from the console and echo it back.")Read data from the console and echo it back.
- [UART Passthrough](../../samples/drivers/uart/passthrough/README.md#uart-passthrough "Pass data directly between the console and another UART interface.")Pass data directly between the console and another UART interface.
- [USB CDC-ACM](../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.")Use USB CDC-ACM driver to implement a serial port echo.

### Polling API

[Polling UART API](../../doxygen/html/group__uart__polling.md)

### Interrupt-driven API

[Interrupt-driven UART API](../../doxygen/html/group__uart__interrupt.md)

### Asynchronous API

[Async UART API](../../doxygen/html/group__uart__async.md)
