---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/intel/rpl/doc/index.html
original_path: boards/intel/rpl/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Raptor Lake CRB

## Overview

Raptor Lake processor is a 13th generation 64-bit multi-core processor built
on a 10-nanometer technology process. Raptor Lake is based on a Hybrid
architecture, utilizing P-cores for performance and E-Cores for efficiency.

Raptor Lake S and Raptor Lake P processor lines are supported.

The S-Processor line is a 2-Chip Platform that includes the Processor Die and
Platform Controller Hub (PCH-S) Die in the Package.

The P-Processor line is a 2-Die Multi Chip Package (MCP) that includes the
Processor Die and Platform Controller Hub (PCH-P) Die on the same package as
the Processor Die.

For more information about Raptor Lake Processor lines, P-cores, and E-cores
please refer to [RPL](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/).

Raptor Lake Customer Reference Board (RPL CRB) is an example implementation of a
compact single board computer with high performance for IoT edge devices. The
supported boards are intel\_rpl\_s\_crb and intel\_rpl\_p\_crb.

These board configurations enable kernel support for the supported Raptor Lake
boards.

## Hardware

General information about the board can be found at the [RPL](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/).

### Supported Features

In addition to the standard architecture devices (HPET, local and I/O APICs,
etc.), Zephyr supports the following Raptor Lake-specific SoC devices:

- SMBus

#### UART Serial Port Support

The Raptor Lake UARTs are NS16550-compatible. Baud rate of
115.2kbps is supported on uart0.

### Connections and IOs

Refer to the [RPL](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/) for more information.

## Programming and Debugging

Use the following procedures for booting an image on an RPL CRB board.

### [Build Zephyr application](#contents)

1. Build a Zephyr application; for instance, to build the `hello_world`
   application on Raptor Lake S CRB:

   ```shell
   # From the root of the zephyr repository
   west build -b intel_rpl_s_crb samples/hello_world
   ```

   Note

   A Zephyr EFI image file named `zephyr.efi` is automatically
   created in the build directory after the application is built.

### [Booting the Raptor Lake S CRB Board using UEFI](#contents)

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
