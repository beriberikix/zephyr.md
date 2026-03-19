---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/openthread/coprocessor/README.html
original_path: samples/net/openthread/coprocessor/README.html
---

# OpenThread co-processor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/openthread/coprocessor/README.rst/..)

## Overview

OpenThread Co-Processor allows building a Thread Border Router. The code in this
sample is only the MCU target part of a complete Thread Border Router.
The Co-Processor can act in two variants: Network Co-Processor (NCP) and Radio
Co-Processor (RCP), see [https://openthread.io/platforms/co-processor](https://openthread.io/platforms/co-processor).

Additional required host-side tools (e.g. otbr-agent) to build a Thread Border
Router can be obtained by following
[https://openthread.io/guides/border-router/build#set-up-the-border-router](https://openthread.io/guides/border-router/build#set-up-the-border-router).

The preferred Co-Processor configuration of OpenThread is RCP now.

The source code for this sample application can be found at:
[samples/net/openthread/coprocessor](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coprocessor).

## Building and Running

Build the OpenThread NCP sample application like this:

```shell
west build -b <board to use> samples/net/openthread/coprocessor -- -DCONF_FILE=<config file to use>
```

Build the OpenThread NCP sample application which uses CDC ACM UART device:

```shell
west build -b nrf52840dk/nrf52840 samples/net/openthread/coprocessor -- -DDTC_OVERLAY_FILE=usb.overlay -DEXTRA_CONF_FILE=overlay-usb-nrf-br.conf
west flash
```

Example building for the nrf52840dk/nrf52840 for RCP:

```shell
west build -b nrf52840dk/nrf52840 samples/net/openthread/coprocessor -- -DCONF_FILE="prj.conf overlay-rcp.conf"
west build -t run
```

There are configuration files for different boards and setups in the
coprocessor directory:

- `prj.conf`
  Generic NCP config file. Use this, if you want the NCP configuration.
- `overlay-rcp.conf`
  :   RCP overlay file. Use this in combination with prj.conf, if you want the RCP
      configuration.
- `overlay-tri-n4m-br.conf`
  This is an overlay for the dedicated Thread Border Router hardware
  [https://www.tridonic.com/com/en/download/data\_sheets/net4more\_Borderrouter\_PoE-Thread\_en.pdf](https://www.tridonic.com/com/en/download/data_sheets/net4more_Borderrouter_PoE-Thread_en.pdf).
  The board support is not part of the Zephyr repositories, but the
  product is based on NXP K64 and AT86RF233. This file can be used as an
  example for a development set-up based on development boards.

## See also

[OpenThread L2 abstraction layer](../../../../doxygen/html/group__openthread.md)
