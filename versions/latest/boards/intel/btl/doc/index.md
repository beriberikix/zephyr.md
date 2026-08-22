---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/intel/btl/doc/index.html
original_path: boards/intel/btl/doc/index.html
---

# Bartlett Lake P CRB

Board Overview

Name:
:   `intel_btl_s_crb`

Vendor:
:   Intel Corporation

Architecture:
:   x86

SoC:
:   raptor\_lake

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/intel/btl/doc/index.rst/../..)

## Overview

Bartlett Lake processor is a 64-bit multi-core processor built on Intel 7 process
Technology. Bartlett Lake is based on a Hybrid architecture, utilizing
P-cores for performance and E-Cores for efficiency.

The S-Processor line is a 2-Chip Platform that includes the Processor Die and
Platform Controller Hub (PCH-S) Die in the Package.

For more information about Raptor Lake Processor lines, P-cores, and E-cores
please refer to [BTL](https://www.intel.com/content/www/us/en/secure/content-details/839635/bartlett-lake-s-processor-external-design-specification-eds-for-edge-platforms.html?DocID=839635).

This board configuration enables kernel support for the Bartlett Lake S boards.

## Hardware

The `intel_btl_s_crb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

General information about the board can be found at the [BTL](https://www.intel.com/content/www/us/en/secure/content-details/839635/bartlett-lake-s-processor-external-design-specification-eds-for-edge-platforms.html?DocID=839635) website.

### Connections and IOs

Refer to the [BTL](https://www.intel.com/content/www/us/en/secure/content-details/839635/bartlett-lake-s-processor-external-design-specification-eds-for-edge-platforms.html?DocID=839635) website for more information.

## Programming and Debugging

Use the following procedures for booting an image for an Bartlett Lake S CRB board.

### [Build Zephyr application](#contents)

1. Build a Zephyr application; for instance, to build the `hello_world`
   application for Bartlett Lake S CRB:

   ```shell
   # From the root of the zephyr repository
   west build -b intel_btl_s_crb samples/hello_world
   ```

   Note

   A Zephyr EFI image file named `zephyr.efi` is automatically
   created in the build directory after the application is built.

#### Preparing the Boot Device

Prepare a USB flash drive to boot the Zephyr application image on
a board.

1. Format the USB flash drive as FAT32.

   On Windows, open `File Explorer`, and right-click on the USB flash drive.
   Select `Format...`. Make sure in `File System`, `FAT32` is selected.
   Click on the `Format` button and wait for it to finish.

   On Linux, graphical utilities such as `gparted` can be used to format
   the USB flash drive as FAT32. Alternatively, under terminal, find out
   the corresponding device node for the USB flash drive (for example,
   `/dev/sdd`). Execute the following command:

   ```shell
   $ mkfs.vfat -F 32 <device-node>
   ```

   Important

   Make sure the device node is the actual device node for
   the USB flash drive. Or else you may erase other storage devices
   on your system, and will render the system unusable afterwards.
2. Copy the Zephyr EFI image file `zephyr/zephyr.efi` to the USB drive.

#### Booting Zephyr on a board

Boot the board to the EFI shell with USB flash drive connected.

1. Insert the prepared boot device (USB flash drive) into the board.
2. Connect the board to the host system using the serial cable and
   configure your host system to watch for serial data. See board’s
   website for more information.

   Note

   Use a baud rate of 115200.
3. Power on the board.
4. When the following output appears, press `F7`:

   ```shell
   Press <DEL> or <ESC> to enter setup.
   ```
5. From the menu that appears, select the menu entry that describes
   that particular EFI shell.
6. From the EFI shell select Zephyr EFI image to boot.

   ```shell
   Shell> fs0:zephyr.efi
   ```
7. When the boot process completes, you have finished booting the
   Zephyr application image.
