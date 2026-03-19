---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/modules/mctp/mctp_endpoint/README.html
original_path: samples/modules/mctp/mctp_endpoint/README.html
---

# MCTP Endpoint Sample

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/modules/mctp/mctp_endpoint/README.rst/..)

## Overview

Sets up an MCTP node that listens on a UART for messages targeting a particular
MCTP endpoint id with the message “hello”. Responds to this “hello” message with
“world”.

## Requirements

A board and SoC that provide access to a UART and a driver that implements the
UART async API.

## Wiring

The listening UART pins should be wired to a board which will run the MCTP host
sample such that this board’s UART tx pin connects to the host board’s rx pin,
and this board’s UART rx pin connects to the host board’s tx pin. The boards’
grounds should also be wired together.

Optionally a logic analyzer can be wired up and listening to the UART to inspect
the data flowing.

## Building and Running

```shell
west build -b nrf52840_nrf52840dk samples/modules/mctp/mctp_endpoint
west build -t run
```

## References

[MCTP Base Specification 2019](https://www.dmtf.org/sites/default/files/standards/documents/DSP0236_1.3.1.pdf)
