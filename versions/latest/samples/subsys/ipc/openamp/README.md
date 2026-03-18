---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/ipc/openamp/README.html
original_path: samples/subsys/ipc/openamp/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# OpenAMP

## Overview

This application demonstrates how to use OpenAMP with Zephyr. It is designed to
demonstrate how to integrate OpenAMP with Zephyr both from a build perspective
and code. Note that the remote and primary core images can be flashed
independently, but sysbuild must be used in order to build the images.

## Building the application for lpcxpresso54114\_m4

```shell
# From the root of the zephyr repository
west build -b lpcxpresso54114_m4 --sysbuild samples/subsys/ipc/openamp
west debug
```

## Building the application for lpcxpresso55s69\_cpu0

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s69_cpu0 --sysbuild samples/subsys/ipc/openamp
west debug
```

## Building the application for mps2\_an521

```shell
# From the root of the zephyr repository
west build -b mps2_an521 --sysbuild samples/subsys/ipc/openamp
west debug
```

## Building the application for v2m\_musca\_b1

```shell
# From the root of the zephyr repository
west build -b v2m_musca_b1 --sysbuild samples/subsys/ipc/openamp
west debug
```

## Building the application for mimxrt1170\_evk\_cm7

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evk_cm7 --sysbuild samples/subsys/ipc/openamp
west debug
```

Open a serial terminal (minicom, putty, etc.) and connect the board with the
following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and the following message will appear on the corresponding
serial port, one is master another is remote:

```shell
**** Booting Zephyr OS build zephyr-v1.14.0-2064-g888fc98fddaa ****
Starting application thread!

OpenAMP[master] demo started
Master core received a message: 1
Master core received a message: 3
Master core received a message: 5
...
Master core received a message: 99
OpenAMP demo ended.
```

```shell
**** Booting Zephyr OS build zephyr-v1.14.0-2064-g888fc98fddaa ****
Starting application thread!

OpenAMP[remote] demo started
Remote core received a message: 0
Remote core received a message: 2
Remote core received a message: 4
...
Remote core received a message: 98
OpenAMP demo ended.
```
