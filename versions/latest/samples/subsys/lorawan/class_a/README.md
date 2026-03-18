---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/lorawan/class_a/README.html
original_path: samples/subsys/lorawan/class_a/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LoRaWAN class A device

## Overview

A simple application to demonstrate the [LoRaWAN subsystem](../../../../connectivity/lora_lorawan/index.md#lorawan-api) of Zephyr.

## Building and Running

This sample can be found under
[samples/subsys/lorawan/class\_a](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/lorawan/class_a) in the Zephyr tree.

Before building the sample, make sure to select the correct region in the
`prj.conf` file.

The following commands build and flash the sample.

```shell
west build -b nucleo_wl55jc samples/subsys/lorawan/class_a
west flash
```

## Extended Configuration

This sample can be configured to run the application-layer clock
synchronization service and/or the remote multicast setup service
in the background.

The following commands build and flash the sample with clock synchronization
enabled.

```shell
west build -b nucleo_wl55jc samples/subsys/lorawan/class_a -- -DEXTRA_CONF_FILE=overlay-clock-sync.conf
west flash
```

The following commands build and flash the sample with remote multicast setup
enabled.

```shell
west build -b nucleo_wl55jc samples/subsys/lorawan/class_a -- -DEXTRA_CONF_FILE=overlay-multicast.conf
west flash
```
