---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/canbus/isotp/README.html
original_path: samples/subsys/canbus/isotp/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ISO-TP library

## Overview

This sample demonstrates how to use the [ISO-TP library](../../../../connectivity/canbus/isotp.md#can-isotp).

Messages are exchanged between two boards. A long message, that is sent with
a block-size (BS) of eight frames, and a short one that has a minimal
separation-time (STmin) of five milliseconds.

The send function call for the short message is non-blocking, and the send
function call for the long message is blocking.

## Building and Running

Use these instructions with integrated CAN controller like in the NXP TWR-KE18F
or Nucleo-F746ZG board.

For the NXP TWR-KE18F board:

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/subsys/canbus/isotp
west flash
```

## Requirements

- Two boards with CAN bus support, connected together

### Sample output

```shell
Start sending data
[00:00:00.000,000] <inf> can_driver: Init of CAN_1 done
========================================
|   ____  ___  ____       ____  ____   |
|  |_  _|/ __||    | ___ |_  _||  _ \  |
|   _||_ \__ \| || | ___   ||  | ___/  |
|  |____||___/|____|       ||  |_|     |
========================================
Got 248 bytes in total
This is the sample test for the short payload
TX complete cb [0]
```

Note

The values shown above might differ.
