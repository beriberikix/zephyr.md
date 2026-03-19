---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/device_mgmt/mcumgr.html
original_path: services/device_mgmt/mcumgr.html
---

# MCUmgr

## Overview

The management subsystem allows remote management of Zephyr-enabled devices.
The following management operations are available:

- Image management
- File System management
- OS management
- Settings (config) management
- Shell management
- Statistic management
- Zephyr management

over the following transports:

- BLE (Bluetooth Low Energy)
- Serial (UART)
- UDP over IP

The management subsystem is based on the Simple Management Protocol (SMP)
provided by [MCUmgr](https://github.com/apache/mynewt-mcumgr), an open source project that provides a
management subsystem that is portable across multiple real-time operating
systems.

The management subsystem is located in [subsys/mgmt/](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/) inside of
the Zephyr tree.

Additionally, there is a [sample](../../samples/subsys/mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.") server that provides
management functionality over BLE and serial.

## Tools/libraries

There are various tools and libraries available which enable usage of MCUmgr functionality on a
device which are listed below. Note that these tools are not part of or related to the Zephyr
project.

Tools and Libraries for MCUmgr

| Name | OS support | | | | | Transports | | | Groups | | | | | | | | Type | Language | License |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Windows | Linux | mac | Mobile | Embedded | Serial | Bluetooth | UDP | OS | IMG | Stat | Settings | FS | Shell | Enum | Zephyr |
| [AuTerm](https://github.com/thedjnK/AuTerm/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Application | C++ (Qt) | GPL-3.0 |
| [mcumgr-client](https://github.com/vouch-opensource/mcumgr-client/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | Application | Rust | Apache-2.0 |
| [mcumgr-web](https://github.com/boogie/mcumgr-web/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | Web page (chrome only) | Javascript | MIT |
| nRF Connect Device Manager:   [Android](https://github.com/NordicSemiconductor/Android-nRF-Connect-Device-Manager/) and [iOS](https://github.com/NordicSemiconductor/IOS-nRF-Connect-Device-Manager) | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✓ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | Library and application | Java, Kotlin, Swift | Apache-2.0 |
| [smp](https://pypi.org/project/smp/) | ✓ | ✓ | ✓ | ✓ | ✕ | N/A | N/A | N/A | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | Library | Python | Apache-2.0 |
| [smpclient](https://pypi.org/project/smpclient/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | Library | Python | Apache-2.0 |
| Zephyr MCUmgr client (in-tree) | ✕ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | Library | C | Apache-2.0 |

Note that a tick for a particular group indicates basic support for that group in the code, it is
possible that not all commands/features of a group are supported by the implementation.

## J-Link Virtual MSD Interaction Note

On boards where a J-Link OB is present which has both CDC and MSC (virtual Mass
Storage Device, also known as drag-and-drop) support, the MSD functionality can
prevent MCUmgr commands over the CDC UART port from working due to how USB
endpoints are configured in the J-Link firmware (for example on the
[Nordic nrf52840dk/nrf52840 board](../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840)) because of
limiting the maximum packet size (most likely to occur when using image
management commands for updating firmware). This issue can be
resolved by disabling MSD functionality on the J-Link device, follow the
instructions on [Disabling the Mass Storage Device functionality](../../develop/flash_debug/nordic_segger.md#nordic-segger-msd) to disable MSD support.

## Bootloader Integration

The [Device Firmware Upgrade](dfu.md#dfu) subsystem integrates the management subsystem with the
bootloader, providing the ability to send and upgrade a Zephyr image to a
device.

Currently only the MCUboot bootloader is supported. See [MCUboot](dfu.md#mcuboot) for more
information.

## Discord channel

Developers welcome!

- Discord mcumgr channel: [https://discord.com/invite/Ck7jw53nU2](https://discord.com/invite/Ck7jw53nU2)

## API Reference

[MCUmgr mgmt API](../../doxygen/html/group__mcumgr__mgmt__api.md)
