---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/sdhc.html
original_path: hardware/peripherals/sdhc.html
---

# Secure Digital High Capacity (SDHC)

The SDHC api offers a generic interface for interacting with an SD host
controller device. It is used by the SD subsystem, and is not intended to be
directly used by the application

## Basic Operation

### SD Host Controller

An SD host controller is a device capable of sending SD commands to an attached
SD card. These commands can be sent using the native SD protocol, or over SPI.
Some SD host controllers are also capable of communicating with MMC devices.
The SDHC api is designed to provide a generic way to send commands to and
interact with attached SD devices.

### Requests

The core of the SDHC api is the [`sdhc_request()`](../../doxygen/html/group__sdhc__interface.md#gac708d55e92a7705f92b90ee6baa65f74) api. Requests contain a
[`sdhc_command`](../../doxygen/html/structsdhc__command.md) command structure, and an optional
[`sdhc_data`](../../doxygen/html/structsdhc__data.md) data structure. The caller may check the return code,
or the `response` field of the SD command structure to determine if the
SDHC request succeeded. The data structure allows the caller to specify a
number of blocks to transfer, and a buffer location to read or write them from.
Whether the provided buffer is used for sending or reading data depends on the
command opcode provided.

### Host Controller I/O

The [`sdhc_set_io()`](../../doxygen/html/group__sdhc__interface.md#ga0e6d8259cca442bd1356d00f668d35c4) api allows the user to change I/O settings of the SD
host controller, such as clock frequency, I/O voltage, and card power. Not all
controllers will support applying all I/O settings. For example, SPI mode
controllers typically cannot toggle power to the SD card.

Related configuration options:

- [`CONFIG_SDHC`](../../kconfig.md#CONFIG_SDHC "CONFIG_SDHC")

## API Reference

[SDHC interface](../../doxygen/html/group__sdhc__interface.md)
