---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/intel/ehl/doc/index.html
original_path: boards/intel/ehl/doc/index.html
---

# Elkhart Lake CRB

## Overview

Elkhart Lake Reference Board (EHL CRB) is an example implementation of a
compact single board computer with high performance for IoT edge devices.

This board configuration enables kernel support for the [EHL](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html) board.

Note

This board configuration works on the variant of [EHL](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html)
boards containing Intel® Atom™ SoC.

## Hardware

General information about the board can be found at the [EHL](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html) website.

### Supported Features

In addition to the standard architecture devices (HPET, local and I/O APICs,
etc.), Zephyr supports the following Elkhart Lake-specific SoC devices:

- I2C
- SMBus

#### UART Serial Port Support

The Elkhart Lake UARTs are NS16550-compatible. Baud rate of
115.2kbps is supported.

### Connections and IOs

Refer to the [EHL](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html) website for more information.

## Programming and Debugging

Use the following procedures for booting an image on a EHL CRB board.

### [Build Zephyr application](#contents)

1. Build a Zephyr application; for instance, to build the `hello_world`
   application on Elkhart Lake CRB:

   ```shell
   # From the root of the zephyr repository
   west build -b intel_ehl_crb samples/hello_world
   ```

   Note

   A Zephyr EFI image file named `zephyr.efi` is automatically
   created in the build directory after the application is built.

### [Booting the Elkhart Lake CRB Board using UEFI](#contents)

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

### [Booting the Elkhart Lake CRB Board over network](#contents)

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

Note

To enable PXE boot for Elkhart Lake CRB board do the following:

1. Enable boot from PXE. Go to EFI shell and make sure that the first boot
   option is `UEFI PXEv4`.

   ```shell
   Shell> bcfg boot dump
   Option: 00. Variable: Boot0007
     Desc    - UEFI PXEv4 (MAC:6805CABC1997)
     DevPath - PciRoot(0x0)/Pci(0x1C,0x0)/Pci(0x0,0x0)/MAC(6805CABC1997,0x0)/IPv4(0.0.0.0)
     Optional- Y
   ...
   ```
2. If UEFI PXEv4 is not the first boot option use `bcfg boot mv` command to
   change boot order

   ```shell
   Shell> bcfg boot mv 7 0
   ```
