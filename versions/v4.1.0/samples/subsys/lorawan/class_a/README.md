---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/lorawan/class_a/README.html
original_path: samples/subsys/lorawan/class_a/README.html
---

# LoRaWAN class A device

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/lorawan/class_a/README.rst/..)

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

## Important Notes for Multiple Runs

By default, this example will only succeed the first time it is run. On subsequent join attempts, the LoRaWAN network server may reject the join request due to a hardcoded `dev_nonce` value. According to the LoRaWAN specification, `dev_nonce` must increment for every new connection attempt.

To run this sample multiple times, choose one of the following options:

1. **Manually Increment ``dev\_nonce``:**
   Modify the sample code to increment `join_cfg.otaa.dev_nonce` before each connection attempt and ensure it is preserved across reboots.
2. **Built-in Zephyr Settings Implementation:**
   Enable [`CONFIG_LORAWAN_NVM_SETTINGS`](../../../../kconfig.md#CONFIG_LORAWAN_NVM_SETTINGS "CONFIG_LORAWAN_NVM_SETTINGS") in the Kconfig. This allows proper storage and reuse of configuration settings, including the `dev_nonce`, across multiple runs.

## See also

[LoRaWAN APIs](../../../../doxygen/html/group__lorawan__api.md)
