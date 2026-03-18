---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/ipc/ipc_service/multi_endpoint/README.html
original_path: samples/subsys/ipc/ipc_service/multi_endpoint/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# IPC Service - Multi-endpoint Sample Application

This application demonstrates how to use IPC Service with multiple endpoints.
By default, it uses the `icmsg_me` backend.
You can also configure it to use the `icbmsg` backend.

## Building the application for nrf5340dk/nrf5340/cpuapp

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/subsys/ipc/ipc_service/multi_endpoint
west debug
```

Open a serial terminal (for example Minicom or PuTTY) and connect the board with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

After resetting the board, the following message will appear on the corresponding
serial port:

```shell
*** Booting Zephyr OS build v3.4.0-rc1-108-gccfbac8b0721 ***
IPC-service HOST [INST 0 - ENDP A] demo started
IPC-service HOST [INST 0 - ENDP B] demo started
IPC-service HOST [INST 1] demo started
HOST [0A]: 1
HOST [0A]: 3
HOST [0B]: 1
HOST [1]: 1
...
HOST [0A]: 99
IPC-service HOST [INST 0 - ENDP A] demo ended.
HOST [0B]: 99
IPC-service HOST [INST 0 - ENDP B] demo ended.
HOST [1]: 99
IPC-service HOST [INST 1] demo ended.
```

```shell
*** Booting Zephyr OS build v3.4.0-rc1-108-gccfbac8b0721 ***
IPC-service REMOTE [INST 0 - ENDP A] demo started
IPC-service REMOTE [INST 0 - ENDP B] demo started
IPC-service REMOTE [INST 1] demo started
REMOTE [0A]: 0
REMOTE [0A]: 2
...
REMOTE [0A]: 98
IPC-service REMOTE [INST 0 - ENDP A] demo ended.
REMOTE [0B]: 98
IPC-service REMOTE [INST 0 - ENDP B] demo ended.
REMOTE [1]: 98
IPC-service REMOTE [INST 1] demo ended.
```

## Changing the backend

To change the backend to `icbmsg`, switch the devicetree
overlay files as follows:

```shell
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild -- \
-DDTC_OVERLAY_FILE=boards/nrf5340dk_nrf5340_cpuapp_icbmsg.overlay \
-Dremote_DTC_OVERLAY_FILE=boards/nrf5340dk_nrf5340_cpunet_icbmsg.overlay
```
