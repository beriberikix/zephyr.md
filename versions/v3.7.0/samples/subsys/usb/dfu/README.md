---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/usb/dfu/README.html
original_path: samples/subsys/usb/dfu/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB DFU (Device Firmware Upgrade)

## Overview

This sample app demonstrates use of a USB DFU Class driver provided
by the Zephyr project.

## Requirements

This project requires an USB device driver. Currently, the USB DFU
class provided by the Zephyr project depends on DFU image manager and
partition layout. Refer to [Flash map](../../../../services/storage/flash_map/flash_map.md#flash-map-api) for details about
partition layout. You SoC must run MCUboot as the stage 1 bootloader.
This sample is built as an application for the MCUboot bootloader.

Note

This example explicitly turns [`CONFIG_USB_DFU_ENABLE_UPLOAD`](../../../../kconfig.md#CONFIG_USB_DFU_ENABLE_UPLOAD "CONFIG_USB_DFU_ENABLE_UPLOAD") on.

## Building and Testing

### Building and signing the application

This sample can be built in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
for more details) and flashed with regular flash tools, but will need
to be loaded at the offset of SLOT-0.

Application images (such as this sample) must be signed.
The build system can do this for you by setting the [`CONFIG_MCUBOOT_SIGNATURE_KEY_FILE`](../../../../kconfig.md#CONFIG_MCUBOOT_SIGNATURE_KEY_FILE "CONFIG_MCUBOOT_SIGNATURE_KEY_FILE") symbol.

For example:

```shell
west build -b nrf52840dk/nrf52840 zephyr/samples/subsys/usb/dfu -d build-dfu -- \
-DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"bootloader/mcuboot/root-rsa-2048.pem\"
```

Build and flash MCUboot bootloader for Zephyr project as it is described in
the [Using MCUboot with Zephyr](https://docs.mcuboot.com/readme-zephyr) documentation. Then build, sign and flash
the USB DFU sample at the offset of SLOT-0.

Build and sign a second application image e.g. [Hello World](../../../hello_world/README.md#hello-world),
which will be used as an image for the update.
Do not forget to enable the required [`CONFIG_BOOTLOADER_MCUBOOT`](../../../../kconfig.md#CONFIG_BOOTLOADER_MCUBOOT "CONFIG_BOOTLOADER_MCUBOOT") option (as described
in [MCUboot](../../../../services/device_mgmt/dfu.md#mcuboot)). For example:

```shell
west build -b nrf52840dk/nrf52840 zephyr/samples/hello_world -d build-hello_world -- \
-DCONFIG_BOOTLOADER_MCUBOOT=y '-DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE="bootloader/mcuboot/root-rsa-2048.pem"'
```

### Testing

The Linux `dfu-util` tool can be used to backup or update the application
image.

Use the following command to backup the SLOT-0 image:

```shell
dfu-util --alt 0 --upload slot0_backup.bin
```

Use the following command to update the application:

```shell
dfu-util --alt 1 --download build-hello_world/zephyr/zephyr.signed.bin
```

Reset the SoC. MCUboot boot will swap the images and boot the new application,
showing this output to the console:

```shell
*** Booting Zephyr OS build zephyr-v3.0.0-360-gc0dd594d4d3d  ***
I: Starting bootloader
I: Primary image: magic=good, swap_type=0x3, copy_done=0x1, image_ok=0x1
I: Secondary image: magic=good, swap_type=0x2, copy_done=0x3, image_ok=0x3
I: Boot source: none
I: Swap type: test
I: Bootloader chainload address offset: 0xc000
I: Jumping to the first image slot
*** Booting Zephyr OS build zephyr-v3.0.0-361-gb987e6daa2f9  ***
Hello World! nrf52840dk
```

Reset the SoC again and MCUboot should revert the images and boot
USB DFU sample, showing this output to the console:

```shell
*** Booting Zephyr OS build zephyr-v3.0.0-360-gc0dd594d4d3d  ***
I: Starting bootloader
I: Primary image: magic=good, swap_type=0x2, copy_done=0x1, image_ok=0x3
I: Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Boot source: none
I: Swap type: revert
I: Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Bootloader chainload address offset: 0xc000
I: Jumping to the first image slot
*** Booting Zephyr OS build zephyr-v3.0.0-361-gb987e6daa2f9  ***
[00:00:00.005,920] <inf> main: This device supports USB DFU class.
```

### Permanent download and automatic reboot

There are some symbols that can be used to enable a hands free download:

To mark SLOT-1 as permanent after the download completes,
enable the [`CONFIG_USB_DFU_PERMANENT_DOWNLOAD`](../../../../kconfig.md#CONFIG_USB_DFU_PERMANENT_DOWNLOAD "CONFIG_USB_DFU_PERMANENT_DOWNLOAD") symbol.

To automatically reboot after the download completes,
enable the [`CONFIG_USB_DFU_REBOOT`](../../../../kconfig.md#CONFIG_USB_DFU_REBOOT "CONFIG_USB_DFU_REBOOT") symbol.

Warning

Enabling [`CONFIG_USB_DFU_PERMANENT_DOWNLOAD`](../../../../kconfig.md#CONFIG_USB_DFU_PERMANENT_DOWNLOAD "CONFIG_USB_DFU_PERMANENT_DOWNLOAD") can lead to a bricked device!
Make sure there is another way to download firmware.
For example via a debugger or Mcuboot’s recovery mode.

Both symbols can be enabled with the `overlay-permanent-download.conf` overlay. For example:

```shell
west build -b nrf52840dk/nrf52840 zephyr/samples/subsys/usb/dfu -d build-dfu -- \
-DCONFIG_BOOTLOADER_MCUBOOT=y '-DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE="bootloader/mcuboot/root-rsa-2048.pem"' \
-DEXTRA_CONF_FILE=overlay-permanent-download.conf
```

The listing below shows the output to the console when downloading via dfu-util.
Note the `Swap type: perm`.

```shell
*** Booting Zephyr OS build zephyr-v3.0.0-361-ge6900e2451d5  ***
[00:00:00.005,920] <inf> main: This device supports USB DFU class.

*** Booting Zephyr OS build zephyr-v3.0.0-360-gc0dd594d4d3d  ***
I: Starting bootloader
I: Primary image: magic=good, swap_type=0x4, copy_done=0x1, image_ok=0x1
I: Secondary image: magic=good, swap_type=0x3, copy_done=0x3, image_ok=0x1
I: Boot source: none
I: Swap type: perm
I: Bootloader chainload address offset: 0xc000
I: Jumping to the first image slot
*** Booting Zephyr OS build zephyr-v3.0.0-361-gb987e6daa2f9  ***
Hello World! nrf52840dk
```
