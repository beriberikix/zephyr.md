---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/device_mgmt/dfu.html
original_path: services/device_mgmt/dfu.html
---

# Device Firmware Upgrade

## Overview

The Device Firmware Upgrade subsystem provides the necessary frameworks to
upgrade the image of a Zephyr-based application at run time. It currently
consists of two different modules:

- [subsys/dfu/boot/](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/boot/): Interface code to bootloaders
- [subsys/dfu/img\_util/](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/img_util/): Image management code

The DFU subsystem deals with image management, but not with the transport
or management protocols themselves required to send the image to the target
device. For information on these protocols and frameworks please refer to the
[Device Management](index.md#device-mgmt) section.

### Flash Image

The flash image API as part of the Device Firmware Upgrade (DFU) subsystem
provides an abstraction on top of Flash Stream to simplify writing firmware
image chunks to flash.

#### API Reference

[Flash image API](../../doxygen/html/group__flash__img__api.md)

### MCUBoot API

The MCUboot API is provided to get version information and boot status of
application images. It allows to select application image and boot type
for the next boot.

#### API Reference

[MCUboot image control API](../../doxygen/html/group__mcuboot__api.md)

## Bootloaders

### MCUboot

Zephyr is directly compatible with the open source, cross-RTOS
[MCUboot boot loader](https://mcuboot.com/). It interfaces with MCUboot and is aware of the image
format required by it, so that Device Firmware Upgrade is available when MCUboot
is the boot loader used with Zephyr. The source code itself is hosted in the
[MCUboot GitHub Project](https://github.com/runtimeco/mcuboot) page.

In order to use MCUboot with Zephyr you need to take the following into account:

1. You will need to define the flash partitions required by MCUboot; see
   [Flash map](../storage/flash_map/flash_map.md#flash-map-api) for details.
2. You will have to specify your flash partition as the chosen code partition

```devicetree
/ {
   chosen {
      zephyr,code-partition = &slot0_partition;
   };
};
```

3. Your application’s `.conf` file needs to enable the
   [`CONFIG_BOOTLOADER_MCUBOOT`](../../kconfig.md#CONFIG_BOOTLOADER_MCUBOOT "CONFIG_BOOTLOADER_MCUBOOT") Kconfig option in order for Zephyr to
   be built in an MCUboot-compatible manner
4. You need to build and flash MCUboot itself on your device
5. You might need to take precautions to avoid mass erasing the flash and also
   to flash the Zephyr application image at the correct offset (right after the
   bootloader)

More detailed information regarding the use of MCUboot with Zephyr can be found
in the [MCUboot with Zephyr](https://docs.mcuboot.com/readme-zephyr) documentation page on the MCUboot website.
