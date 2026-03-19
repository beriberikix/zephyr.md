---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/up-bridge-the-gap/up_squared/doc/index.html
original_path: boards/up-bridge-the-gap/up_squared/doc/index.html
---

# UP Squared

Board Overview

[![../../../../_images/up_squared.jpg](../../../../_images/up_squared.jpg)
](../../../../_images/up_squared.jpg)

UP Squared

Name:
:   `up_squared`

Vendor:
:   UP Bridge the Gap

Architecture:
:   x86

SoC:
:   apollo\_lake

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/up-bridge-the-gap/up_squared/doc/index.rst/../..)

## Overview

UP² (UP Squared) is an ultra compact single board computer with high
performance and low power consumption. It features the latest Intel® Apollo
Lake Celeron™ and Pentium™ Processors with only 4W of Scenario Design Power and
a powerful and flexible Intel® FPGA Altera MAX 10 onboard.

This board configuration enables kernel support for the [UP Squared](https://www.up-board.org/upsquared/specifications) board.

Note

This board configuration works on all three variants of [UP Squared](https://www.up-board.org/upsquared/specifications)
boards containing Intel® Pentium™ SoC,
Intel® Celeron™ SoC, or Intel® Atom™ SoC.

## Hardware

General information about the board can be found at the [UP Squared](https://www.up-board.org/upsquared/specifications) website.

### Supported Features

In addition to the standard architecture devices (HPET, local and I/O APICs,
etc.), Zephyr supports the following Apollo Lake-specific SoC devices:

- HSUART
- GPIO
- I2C

#### HSUART High-Speed Serial Port Support

The Apollo Lake UARTs are NS16550-compatible, with “high-speed” capability.

Baud rates beyond 115.2kbps (up to 3.6864Mbps) are supported, with additional
configuration. The UARTs are fed a master clock which is fed into a PLL which
in turn outputs the baud master clock. The PLL is controlled by a per-UART
32-bit register called `PRV_CLOCK_PARAMS` (aka the `PCP`), the format of
which is:

| [31] | [30:16] | [15:1] | [0] |
| --- | --- | --- | --- |
| enable | `m` | `n` | toggle |

The resulting baud master clock frequency is `(n/m)` \* master.

Typically, the master clock is 100MHz, and the firmware by default sets
the `PCP` to `0x3d090240`, i.e., `n = 288`, `m =  15625`, which
results in the de-facto standard 1.8432MHz master clock and a max baud rate
of 115.2k. Higher baud rates are enabled by changing the PCP and telling
Zephyr what the resulting master clock is.

Use devicetree to set the value of the `PRV_CLOCK_PARAMS` register in
the UART block of interest. Typically a devicetree overlay file would be
present in the application directory (specific to the board, such as
`up_squared.overlay`), with contents like this:

> ```shell
> / {
>     soc {
>         uart@0 {
>             pcp = <0x3d090900>;
>             clock-frequency = <7372800>;
>             current-speed = <230400>;
>         };
>     };
> };
> ```

The relevant variables are `pcp` (the value to use for `PRV_CLOCK_PARAMS`),
and `clock-frequency` (the resulting baud master clock). The meaning of
`current-speed` is unchanged, and as usual indicates the initial baud rate.

#### GPIO

GPIOs are exposed through the HAT header, and can be referred using
predefined macros such as `UP2_HAT_PIN3`. The physical pins are
connected to the on-board FPGA acting as level shifter. Therefore,
to actually utilize these GPIO pins, the function of the pins and
directions (input/output) must be set in the BIOS. This can be
accomplished in BIOS, under menu `Advanced`, and option
`HAT Configurations`. When a corresponding pin is set to act as
GPIO, there is an option to set the direction of the pin. This needs
to be set accordingly for the GPIO to function properly.

### Connections and IOs

Refer to the [UP Squared](https://www.up-board.org/upsquared/specifications) website and [UP Squared Pinout](https://wiki.up-community.org/Pinout) website
for connection diagrams.

## Programming and Debugging

Use the following procedures for booting an image on a UP Squared board.

### [Build Zephyr application](#contents)

1. Build a Zephyr application; for instance, to build the `hello_world`
   application on UP Squared:

   ```shell
   # From the root of the zephyr repository
   west build -b up_squared samples/hello_world
   ```

   Note

   A Zephyr EFI image file named `zephyr.efi` is automatically
   created in the build directory after the application is built.

### [Booting the UP Squared Board using UEFI](#contents)

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

Note

Refer to the [UP Squared Serial Console Wiki page](https://wiki.up-community.org/Serial_console) for instructions on how to
connect serial console.

Note

You can safely ignore this message if it appears:

```shell
WARNING: no console will be available to OS
```

### [Booting the UP Squared Board over network](#contents)

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

Refer to the [UP Squared Serial Console Wiki page](https://wiki.up-community.org/Serial_console) for instructions on how to
connect serial console.

Note

To enable PXE boot for Up Squared board do the following:

1. Enable network from BIOS settings.

   ```shell
   Advanced -> Network Stack Configuration -> Enable Network Stack -> Enable Ipv4 PXE Support
   ```
2. Make network boot as the first boot option.

   ```shell
   Boot -> Boot Option #1 : [Network]
   ```
