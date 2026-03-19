---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/ptp/README.html
original_path: samples/net/ptp/README.html
---

# PTP

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ptp/README.rst/..)

## Overview

The PTP sample application for Zephyr will enable PTP support.

The source code for this sample application can be found at:
[samples/net/ptp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ptp).

## Requirements

For generic host connectivity, that can be used for debugging purposes, see
[Networking with native\_sim board](../../../connectivity/networking/native_sim_setup.md#networking-with-native-sim) for details.

## Building and Running

A good way to run this sample is to run this PTP application inside
native\_sim board as described in [Networking with native\_sim board](../../../connectivity/networking/native_sim_setup.md#networking-with-native-sim) or with
embedded device like Nucleo-H743-ZI, Nucleo-H745ZI-Q, Nucleo-F767ZI or
Nucleo-H563ZI. Note that PTP is only supported for
boards that have an Ethernet port and which has support for collecting
timestamps for sent and received Ethernet frames.

Follow these steps to build the PTP sample application:

```shell
west build -b <board to use> samples/net/ptp
```

### Setting up Linux Host

By default PTP in Zephyr will not print any PTP debug messages to console.
One can enable debug prints by setting
[`CONFIG_PTP_LOG_LEVEL_DBG`](../../../kconfig.md#CONFIG_PTP_LOG_LEVEL_DBG "CONFIG_PTP_LOG_LEVEL_DBG") in the config file.

Get linuxptp project sources

```shell
git clone git://git.code.sf.net/p/linuxptp/code
```

Compile the `ptp4l` daemon and start it like this:

```shell
sudo ./ptp4l -4 -f -i zeth -m -q -l 6 -S
```

Compile Zephyr application.

```shell
west build -b native_sim samples/net/ptp
```

When the Zephyr image is build, you can start it like this:

```shell
build/zephyr/zephyr.exe -attach_uart
```

## See also

[PTP support](../../../doxygen/html/group__ptp.md)
