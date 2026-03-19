---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/lora/send/README.html
original_path: samples/drivers/lora/send/README.html
---

# LoRa send

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/lora/send/README.rst/..)

## Overview

This sample demonstrates how to use the LoRa radio driver to configure
the encoding settings and send data over the radio.

Transmitted messages can be received by building and flashing the accompanying
LoRa receive sample [LoRa receive](../receive/README.md#lora-receive "Receive packets in both synchronous and asynchronous mode using the LoRa radio.") on another board within
range.

## Building and Running

Build and flash the sample as follows, changing `b_l072z_lrwan1` for
your board, where your board has a `lora0` alias in the devicetree.

```shell
west build -b b_l072z_lrwan1 samples/drivers/lora/send
west flash
```

### Sample Output

```shell
[00:00:00.531,000] <inf> lora_send: Data sent!
[00:00:01.828,000] <inf> lora_send: Data sent!
[00:00:03.125,000] <inf> lora_send: Data sent!
```

## See also

[LoRa APIs](../../../../doxygen/html/group__lora__api.md)
