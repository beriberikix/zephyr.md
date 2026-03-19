---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/lora_lorawan/index.html
original_path: connectivity/lora_lorawan/index.html
---

# LoRa and LoRaWAN

## Overview

LoRa (abbrev. for Long Range) is a proprietary low-power wireless
communication protocol developed by the [Semtech Corporation](https://www.semtech.com/).

LoRa acts as the physical layer (PHY) based on the chirp spread spectrum
(CSS) modulation technique.

LoRaWAN (for Long Range Wide Area Network) defines a networking layer
on top of the LoRa PHY.

Zephyr provides APIs for LoRa to send raw data packets directly over the
wireless interface as well as APIs for LoRaWAN to connect the end device
to the internet through a gateway.

The Zephyr implementation is based on Semtech’s [LoRaMac-node library](https://github.com/Lora-net/LoRaMac-node), which
is included as a Zephyr module.

The LoRaWAN specification is published by the [LoRa Alliance](https://lora-alliance.org/).

## Configuration Options

### LoRa PHY

Related configuration options can be found under
[drivers/lora/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig).

- [`CONFIG_LORA`](../../kconfig.md#CONFIG_LORA "CONFIG_LORA")
- [`CONFIG_LORA_SHELL`](../../kconfig.md#CONFIG_LORA_SHELL "CONFIG_LORA_SHELL")
- [`CONFIG_LORA_INIT_PRIORITY`](../../kconfig.md#CONFIG_LORA_INIT_PRIORITY "CONFIG_LORA_INIT_PRIORITY")

### LoRaWAN

Related configuration options can be found under
[subsys/lorawan/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig).

- [`CONFIG_LORAWAN`](../../kconfig.md#CONFIG_LORAWAN "CONFIG_LORAWAN")
- [`CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR`](../../kconfig.md#CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR "CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR")
- [`CONFIG_LORAMAC_REGION_AS923`](../../kconfig.md#CONFIG_LORAMAC_REGION_AS923 "CONFIG_LORAMAC_REGION_AS923")
- [`CONFIG_LORAMAC_REGION_AU915`](../../kconfig.md#CONFIG_LORAMAC_REGION_AU915 "CONFIG_LORAMAC_REGION_AU915")
- [`CONFIG_LORAMAC_REGION_CN470`](../../kconfig.md#CONFIG_LORAMAC_REGION_CN470 "CONFIG_LORAMAC_REGION_CN470")
- [`CONFIG_LORAMAC_REGION_CN779`](../../kconfig.md#CONFIG_LORAMAC_REGION_CN779 "CONFIG_LORAMAC_REGION_CN779")
- [`CONFIG_LORAMAC_REGION_EU433`](../../kconfig.md#CONFIG_LORAMAC_REGION_EU433 "CONFIG_LORAMAC_REGION_EU433")
- [`CONFIG_LORAMAC_REGION_EU868`](../../kconfig.md#CONFIG_LORAMAC_REGION_EU868 "CONFIG_LORAMAC_REGION_EU868")
- [`CONFIG_LORAMAC_REGION_KR920`](../../kconfig.md#CONFIG_LORAMAC_REGION_KR920 "CONFIG_LORAMAC_REGION_KR920")
- [`CONFIG_LORAMAC_REGION_IN865`](../../kconfig.md#CONFIG_LORAMAC_REGION_IN865 "CONFIG_LORAMAC_REGION_IN865")
- [`CONFIG_LORAMAC_REGION_US915`](../../kconfig.md#CONFIG_LORAMAC_REGION_US915 "CONFIG_LORAMAC_REGION_US915")
- [`CONFIG_LORAMAC_REGION_RU864`](../../kconfig.md#CONFIG_LORAMAC_REGION_RU864 "CONFIG_LORAMAC_REGION_RU864")

## API Reference

### LoRa PHY

[LoRa APIs](../../doxygen/html/group__lora__api.md)

Related code samples

- [LoRa receive](../../samples/drivers/lora/receive/README.md#lora-receive "Receive packets in both synchronous and asynchronous mode using the LoRa radio.")Receive packets in both synchronous and asynchronous mode using the LoRa
  radio.
- [LoRa send](../../samples/drivers/lora/send/README.md#lora-send "Transmit a preconfigured payload every second using the LoRa radio.")Transmit a preconfigured payload every second using the LoRa radio.

### LoRaWAN

[LoRaWAN APIs](../../doxygen/html/group__lorawan__api.md)

Related code samples

- [LoRaWAN class A device](../../samples/subsys/lorawan/class_a/README.md#lorawan-class-a "Join a LoRaWAN network and send a message periodically.")Join a LoRaWAN network and send a message periodically.
- [LoRaWAN FUOTA](../../samples/subsys/lorawan/fuota/README.md#lorawan-fuota "Perform a LoRaWAN firmware-upgrade over the air (FUOTA) operation.")Perform a LoRaWAN firmware-upgrade over the air (FUOTA) operation.
