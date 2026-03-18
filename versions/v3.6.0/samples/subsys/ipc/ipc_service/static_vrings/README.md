---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/ipc/ipc_service/static_vrings/README.html
original_path: samples/subsys/ipc/ipc_service/static_vrings/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# IPC service: static vrings backend

## Overview

This application demonstrates how to use IPC Service and the static vrings
backend with Zephyr. It is designed to demonstrate how to integrate it with
Zephyr both from a build perspective and code.

## Building the application for nrf5340dk\_nrf5340\_cpuapp

```shell
# From the root of the zephyr repository
west build -b nrf5340dk_nrf5340_cpuapp --sysbuild samples/subsys/ipc/ipc_service/static_vrings
west debug
```

Open a serial terminal (minicom, putty, etc.) and connect the board with the
following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and the following message will appear on the corresponding
serial port, one is host another is remote:

```shell
*** Booting Zephyr OS build zephyr-v3.1.0-2383-g147aee22f273  ***
IPC-service HOST [INST 0 - ENDP A] demo started
IPC-service HOST [INST 0 - ENDP B] demo started
IPC-service HOST [INST 1] demo started
HOST [1]: 1
HOST [1]: 3
HOST [1]: 5
HOST [1]: 7
HOST [1]: 9
...
```

```shell
*** Booting Zephyr OS build zephyr-v3.1.0-2383-g147aee22f273  ***
IPC-service REMOTE [INST 0 - ENDP A] demo started
IPC-service REMOTE [INST 0 - ENDP B] demo started
IPC-service REMOTE [INST 1] demo started
REMOTE [1]: 0
REMOTE [1]: 2
REMOTE [1]: 4
REMOTE [1]: 6
REMOTE [1]: 8
...
```
