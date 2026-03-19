---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/lorawan/fuota/README.html
original_path: samples/subsys/lorawan/fuota/README.html
---

# LoRaWAN FUOTA

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/lorawan/fuota/README.rst/..)

## Overview

An application to demonstrate firmware-upgrade over the air (FUOTA) over LoRaWAN.

The following services specified by the LoRa Alliance are used:

- Application Layer Clock Synchronization ([TS003-2.0.0](https://resources.lora-alliance.org/technical-specifications/ts003-2-0-0-application-layer-clock-synchronization))
- Remote Multicast Setup ([TS005-1.0.0](https://resources.lora-alliance.org/technical-specifications/lorawan-remote-multicast-setup-specification-v1-0-0))
- Fragmented Data Block Transport ([TS004-1.0.0](https://resources.lora-alliance.org/technical-specifications/lorawan-fragmented-data-block-transport-specification-v1-0-0))

The FUOTA process is started by the application and afterwards runs in the background in its own
work queue thread. After a firmware upgrade is successfully received, the application is notified
via a callback and can reboot the device into MCUboot to apply the upgrade.

A LoRaWAN Application Server implementing the relevant services is required for this sample to work.

## Building and Running

This sample can be found under [samples/subsys/lorawan/fuota](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/lorawan/fuota) in the Zephyr tree.

Before building the sample, make sure to select the correct region in the `prj.conf` file.

The following commands build and flash the sample.

```shell
west build -b nucleo_wl55jc samples/subsys/lorawan/fuota
west flash
```

## See also

[LoRaWAN APIs](../../../../doxygen/html/group__lorawan__api.md)
