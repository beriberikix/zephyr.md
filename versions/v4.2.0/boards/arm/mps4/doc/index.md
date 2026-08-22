---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arm/mps4/doc/index.html
original_path: boards/arm/mps4/doc/index.html
---

# MPS4

Board Overview

Name:
:   `mps4`

Vendor:
:   ARM Ltd.

Architecture:
:   arm

SoC:
:   corstone320, corstone315

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arm/mps4/doc/index.rst/../..)

## Overview

The MPS4 board configuration is used by Zephyr applications that run
on the MPS4 board.

[Corstone-315 FVP](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)/[Corstone-320 FVP](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps) are Arm reference subsystem for
secure System on Chips containing an Armv8.1-M Cortex-M85 processor,
LCM, KMU and SAM IPs. Corstone-320 FVP have Ethos-U85 while
Corstone-315 FVP have a Ethos-U65 neural network processor.
They are available free of charge for Linux and Windows systems.
The FVPs have been selected for simulation since they provide access to the
Ethos-U65/Ethos-U85 NPU, which is unavailable in QEMU or other simulation platforms.

### Zephyr board options

MPS4 Corstone-315 (FVP)MPS4 Corstone-320 (FVP)

The MPS4 FVP is an SoC with Cortex-M85 architecture. Zephyr provides support
for building for both Secure and Non-Secure firmware.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| `mps4/corstone315/fvp` | For building Secure (or Secure-only) firmware |
| `mps4/corstone315/fvp/ns` | For building Non-Secure firmware |

FPGA Usage:
:   - N/A.

FVP Usage:
:   - To run with the FVP, first set environment variable `ARMFVP_BIN_PATH` before using it. Then you can run it with `west build -t run`.

    ```shell
    export ARMFVP_BIN_PATH=/path/to/fvp/directory
    west build -b {BOARD qualifier from table above} samples/hello_world -t run
    ```

To run the Fixed Virtual Platform simulation tool you must download “FVP model
for the Corstone-315 MPS4” from Arm and install it on your host PC.

QEMU Usage:
:   - N/A.

The MPS4 FVP is an SoC with Cortex-M85 architecture. Zephyr provides support
for building for both Secure and Non-Secure firmware.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| `mps4/corstone320/fvp` | For building Secure (or Secure-only) firmware |
| `mps4/corstone320/fvp/ns` | For building Non-Secure firmware |

FPGA Usage:
:   - N/A.

FVP Usage:
:   - To run with the FVP, first set environment variable `ARMFVP_BIN_PATH` before using it. Then you can run it with `west build -t run`.

    ```shell
    export ARMFVP_BIN_PATH=/path/to/fvp/directory
    west build -b {BOARD qualifier from table above} samples/hello_world -t run
    ```

To run the Fixed Virtual Platform simulation tool you must download “FVP model
for the Corstone-320 MPS4” from Arm and install it on your host PC. This board
has been tested with version 11.27.25 (Sep 24 2024).

QEMU Usage:
:   - N/A.

Note

- Board qualifier must include the variant name as mentioned above.
  `mps4/corstone315`/ `mps4/corstone320` without the variant name is not a valid qualifier.
- `mps4/corstone315/fvp/ns`/ `mps4/corstone320/fvp/ns` variant needs latest upstream TF-M release since Zephyr’s current
  TF-M doesn’t support Corstone-315 FVP yet.

## Hardware

No H/W available yet, only ARMFVP simulated board variants are supported for now.

### Supported Features

The `mps4` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Serial Port

The MPS4 has six UARTs. The Zephyr console output by default, uses
UART0.

Serial port 0 on the Debug USB interface is the MCC board control console.

Serial port 1 on the Debug USB interface is connected to UART 0.

Serial port 2 on the Debug USB interface is connected to UART 1.

Serial port 3 on the Debug USB interface is connected to UART 2.

## Programming and Debugging

### Flashing

- N/A since the only support available is FVP.

#### Building an application with Corstone-315

You can build applications in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application with Corstone-315.

```shell
# From the root of the zephyr repository
west build -b mps4/corstone315/fvp samples/hello_world
west build -t run
```

Run with FVP and you should see the following message:

```shell
Hello World! mps4
```

#### Building an application with Corstone-320

You can build applications in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application with Corstone-320.

```shell
# From the root of the zephyr repository
west build -b mps4/corstone320/fvp samples/hello_world
west build -t run
```

Run with FVP and you should see the following message:

```shell
Hello World! mps4
```

For more details refer to:
:   - [Corstone SSE-315 Reference Guide](https://developer.arm.com/documentation/109395/0000)
    - [Corstone SSE-320 Reference Guide](https://developer.arm.com/documentation/109760/0000/)
    - [Cortex M85 Generic User Guide](https://developer.arm.com/documentation/101924/latest)
    - [Arm Corstone-320 Reference Package Technical Overview](https://developer.arm.com/documentation/109761/0000/)
    - [Arm MPS4 FPGA Prototyping Board Technical Reference Manual](https://developer.arm.com/documentation/102577/0000/)
