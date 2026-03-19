---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/ipc/rpmsg_service/README.html
original_path: samples/subsys/ipc/rpmsg_service/README.html
---

# RPMsg service

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/ipc/rpmsg_service/README.rst/..)

## Overview

RPMsg Service is an abstraction created over OpenAMP that makes initialization
and endpoints creation process easier.
This application demonstrates how to use RPMsg Service in Zephyr. It is designed
to demonstrate how to integrate RPMsg Service with Zephyr both from a build
perspective and code. Note that the remote and primary image core images can be
flashed independently, but sysbuild must be used in order to flash them in one
step.

## Building the application for nrf5340dk/nrf5340/cpuapp

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/subsys/ipc/rpmsg_service
west debug
```

## Building the application for mps2/an521/cpu0

```shell
# From the root of the zephyr repository
west build -b mps2/an521/cpu0 samples/subsys/ipc/rpmsg_service
west debug
```

## Building the application for v2m\_musca\_b1/musca\_b1

```shell
# From the root of the zephyr repository
west build -b v2m_musca_b1/musca_b1 samples/subsys/ipc/rpmsg_service
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

RPMsg Service [master] demo started
Master core received a message: 1
Master core received a message: 3
Master core received a message: 5
...
Master core received a message: 99
RPMsg Service demo ended.
```

```shell
**** Booting Zephyr OS build zephyr-v1.14.0-2064-g888fc98fddaa ****
Starting application thread!

RPMsg Service [remote] demo started
Remote core received a message: 0
Remote core received a message: 2
Remote core received a message: 4
...
Remote core received a message: 98
RPMsg Service demo ended.
```

## Building the application for bl5340\_dvk/nrf5340/cpuapp

```shell
# From the root of the zephyr repository
west build -b bl5340_dvk/nrf5340/cpuapp samples/subsys/ipc/rpmsg_service
west debug
```

```shell
# From the root of the zephyr repository
west build -b bl5340_dvk/nrf5340/cpunet samples/subsys/ipc/rpmsg_service
west debug
```

Open a serial terminal (for example Minicom or PuTTY) and connect to the board
with the following settings on both serial ports:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

When you reset the development kit after having flashed both the application
and network core images, the following messages (one for master and one for
remote) will appear on the corresponding serial ports:

```shell
*** Booting Zephyr OS build v2.7.0-rc1-103-ge19875c88916  ***
Starting application thread!

RPMsg Service [master] demo started
Master core received a message: 1
Master core received a message: 3
Master core received a message: 5
...
Master core received a message: 99
RPMsg Service demo ended.
```

```shell
*** Booting Zephyr OS build v2.7.0-rc1-103-ge19875c88916  ***
Starting application thread!

RPMsg Service [remote] demo started
Remote core received a message: 0
Remote core received a message: 2
Remote core received a message: 4
...
Remote core received a message: 98
RPMsg Service demo ended.
```

## Building the application for stm32h747i\_disco/stm32h7xx

```shell
# From the root of the zephyr repository
west build -b stm32h747i_disco/stm32h7xx/m7 samples/subsys/ipc/rpmsg_service
west debug
```

The serial output should now look like this:

```shell
*** Booting Zephyr OS build 15736b7415be ***
Starting application thread!

RPMsg Service [master] demo started
Master core received a message: 1
Master core received a message: 3
Master core received a message: 5
...
Master core received a message: 99
RPMsg Service demo ended.
```

## See also

[RPMsg service APIs](../../../../doxygen/html/group__rpmsg__service__api.md)
