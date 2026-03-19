---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/intel/adl/doc/index.html
original_path: boards/intel/adl/doc/index.html
---

# Alder Lake N

## Overview

Alder Lake processor is a 64-bit multi-core processor built on 10-nanometer
technology process.

Currently supported is N-processor line, Single Chip Platform that consists of
the Processor Die and Alder Lake N Platform Controller Hub (ADL-N PCH) Die on
the same package as Multi-Chip Package (MCP).

Proposed branding for Adler Lake N is Intel Processor (N100,N200) and
Intel Core i3 (N300, N305).

Alder Lake N Customer Reference Board (ADL-N CRB) and Alder Lake Reference
Validation Platform (ADL-N RVP) are example implementations of compact single
board computer with high performance for IoT edge devices.

This board configuration enables kernel support for the Alder Lake N boards.

## Hardware

General information about the board can be found at the [INTEL\_ADL](https://edc.intel.com/content/www/us/en/design/products/platforms/processor-and-core-i3-n-series-datasheet-volume-1-of-2/) website.

### Connections and IOs

Refer to the [INTEL\_ADL](https://edc.intel.com/content/www/us/en/design/products/platforms/processor-and-core-i3-n-series-datasheet-volume-1-of-2/) website for more information.

## Programming and Debugging

Use the following procedures for booting an image for an Alder Lake N CRB board.

### [Build Zephyr application](#contents)

1. Build a Zephyr application; for instance, to build the `hello_world`
   application for Alder Lake N CRB:

   ```shell
   # From the root of the zephyr repository
   west build -b intel_adl_crb samples/hello_world
   ```

   Note

   A Zephyr EFI image file named `zephyr.efi` is automatically
   created in the build directory after the application is built.

### [Booting the Alder Lake N CRB Board using UEFI](#contents)

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
