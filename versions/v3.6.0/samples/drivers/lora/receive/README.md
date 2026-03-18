---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/lora/receive/README.html
original_path: samples/drivers/lora/receive/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LoRa receive

## Overview

This sample demonstrates how to use the LoRa radio driver to receive packets
both synchronously and asynchronously.

In order to successfully receive messages, build and flash the accompanying
LoRa send sample [LoRa send](../send/README.md#lora-send "Transmit a preconfigured payload every second using the LoRa radio.") on another board within range.

As this sample receives a finite number of packets and then sleeps infinitely,
the user must be ready to inspect the console output immediately after
resetting the device.

## Building and Running

Build and flash the sample as follows, changing `b_l072z_lrwan1` for
your board, where your board has a `lora0` alias in the devicetree.

```shell
west build -b b_l072z_lrwan1 zephyr/samples/drivers/lora/receive
west flash
```

### Sample Output

```shell
[00:00:00.235,000] <inf> lora_receive: Synchronous reception
[00:00:00.956,000] <inf> lora_receive: Received data: helloworld (RSSI:-60dBm, SNR:7dBm)
[00:00:02.249,000] <inf> lora_receive: Received data: helloworld (RSSI:-57dBm, SNR:9dBm)
[00:00:03.541,000] <inf> lora_receive: Received data: helloworld (RSSI:-57dBm, SNR:9dBm)
[00:00:04.834,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:04.834,000] <inf> lora_receive: Asynchronous reception
[00:00:06.127,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:07.419,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:08.712,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:10.004,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:11.297,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:12.590,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:13.884,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:15.177,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:16.470,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:17.762,000] <inf> lora_receive: Received data: helloworld (RSSI:-55dBm, SNR:9dBm)
[00:00:17.762,000] <inf> lora_receive: Stopping packet receptions
```
