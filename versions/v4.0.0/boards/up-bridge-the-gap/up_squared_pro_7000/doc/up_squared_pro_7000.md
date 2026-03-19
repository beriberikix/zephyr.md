---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/up-bridge-the-gap/up_squared_pro_7000/doc/up_squared_pro_7000.html
original_path: boards/up-bridge-the-gap/up_squared_pro_7000/doc/up_squared_pro_7000.html
---

# UP Squared Pro 7000

## Overview

UP Squared Pro 7000 is the 3rd generation of palm-sized developer board of
UP Boards series. UP Squared Pro 7000 is powered by Intel Alder Lake N
(Intel N-series Platform).

For more information about Intel N-series Platform please refer to
[Alder Lake N](../../../intel/adl/doc/index.md#intel-adl-n).

This board configuration enables kernel support for the UP Squared Pro 7000 boards.

## Hardware

General information about the board can be found at the [UP Squared Pro 7000](https://up-board.org/up-squared-pro-7000/) [[1]](#id2) website.

### Connections and IOs

Refer to the [UP Squared Pro 7000](https://up-board.org/up-squared-pro-7000/) [[1]](#id2) website for more information.

## Programming and Debugging

Use the following procedures for booting an image for an UP Squared Pro 7000 board.

### [Build Zephyr application](#contents)

1. Build a Zephyr application; for instance, to build the `hello_world`
   application for UP Squared Pro 7000 board:

   ```shell
   # From the root of the zephyr repository
   west build -b up_squared_pro_7000 samples/hello_world
   ```

   Note

   A Zephyr EFI image file named `zephyr.efi` is automatically
   created in the build directory after the application is built.

### [Connect Serial Console](#contents)

Current board configuration assumes that serial console is connected to
connector `CN14 USB 2.0/UART 1x10P Wafer`. Refer to [User Manual](https://downloads.up-community.org/download/up-squared-pro-7000-user-manual/) [[2]](#id5) for
description of the connector and location on the board.

Refer to [UP Serial Console](https://github.com/up-board/up-community/wiki/Serial-Console) [[3]](#id7) for additional information about serial
connection setup.

### [Booting the UP Squared Pro 7000 Board using UEFI](#contents)

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

### [Booting the UP Squared Pro 7000 Board over network](#contents)

#### Prepare Linux host

1. Install DHCP, TFTP servers. For example `dnsmasq`

   ```shell
   $ sudo apt-get install dnsmasq
   ```
2. Configure DHCP server. Configuration for `dnsmasq` is below:

   ```shell
   # Only listen to this interface
   interface=eno2
   dhcp-range=10.1.1.20,10.1.1.30,12h
   ```
3. Configure TFTP server.

   ```shell
   # tftp
   enable-tftp
   tftp-root=/srv/tftp
   dhcp-boot=zephyr.efi
   ```

   `zephyr.efi` is a Zephyr EFI binary created above.
4. Copy the Zephyr EFI image `zephyr/zephyr.efi` to the
   `/srv/tftp` folder.

   > ```shell
   > $ cp zephyr/zephyr.efi /srv/tftp
   > ```
5. TFTP root should be looking like:

   ```shell
   $ tree /srv/tftp
   /srv/tftp
   └── zephyr.efi
   ```
6. Restart `dnsmasq` service:

   ```shell
   $ sudo systemctl restart dnsmasq.service
   ```

#### Prepare the board for network boot

1. Enable PXE network from BIOS settings.
2. Make network boot as the first boot option.

#### Booting the board

1. Connect the board to the host system using the serial cable and
   configure your host system to watch for serial data. See board’s
   website for more information.

   Note

   Use a baud rate of 115200.
2. Power on the board.
3. Verify that the board got an IP address. Run from the Linux host:

   ```shell
   $ journalctl -f -u dnsmasq
   dnsmasq-dhcp[5386]: DHCPDISCOVER(eno2) 00:07:32:52:25:88
   dnsmasq-dhcp[5386]: DHCPOFFER(eno2) 10.1.1.28 00:07:32:52:25:88
   dnsmasq-dhcp[5386]: DHCPREQUEST(eno2) 10.1.1.28 00:07:32:52:25:88
   dnsmasq-dhcp[5386]: DHCPACK(eno2) 10.1.1.28 00:07:32:52:25:88
   ```
4. Verify that network booting is started:

   ```shell
   $ journalctl -f -u dnsmasq
   dnsmasq-tftp[5386]: sent /srv/tftp/zephyr.efi to 10.1.1.28
   ```
5. When the boot process completes, you have finished booting the
   Zephyr application image.

## References

[1]
([1](#id3),[2](#id4))

[https://up-board.org/up-squared-pro-7000/](https://up-board.org/up-squared-pro-7000/)

[[2](#id6)]

[https://downloads.up-community.org/download/up-squared-pro-7000-user-manual/](https://downloads.up-community.org/download/up-squared-pro-7000-user-manual/)

[[3](#id8)]

[https://github.com/up-board/up-community/wiki/Serial-Console](https://github.com/up-board/up-community/wiki/Serial-Console)
