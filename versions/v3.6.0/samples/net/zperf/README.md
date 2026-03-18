---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/zperf/README.html
original_path: samples/net/zperf/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zperf: Network Traffic Generator

## Description

The zperf sample demonstrates the [zperf shell utility](../../../connectivity/networking/api/zperf.md#zperf), which
allows to evaluate network bandwidth.

## Features

- Compatible with iPerf\_2.0.5. Note that in newer iPerf versions,
  an error message like this is printed and the server reported statistics
  are missing.

```shell
LAST PACKET NOT RECEIVED!!!
```

- Client or server mode allowed without need to modify the source code.

## Supported Boards

zperf is board-agnostic. However, to run the zperf sample application,
the target platform must provide a network interface supported by Zephyr.

This sample application has been tested on the following platforms:

- Freedom Board (FRDM K64F)
- QEMU x86
- Arm FVP BaseR AEMv8-R
- ARM BASE RevC AEMv8A Fixed Virtual Platforms

## Requirements

- iPerf 2.0.5 installed on the host machine
- Supported board

Depending on the network technology chosen, extra steps may be required
to setup the network environment.

## Usage

See [zperf library documentation](../../../connectivity/networking/api/zperf.md#zperf) for more information about
the library usage.
