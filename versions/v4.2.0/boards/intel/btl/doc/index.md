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

### `intel_btl_s_crb/raptor_lake` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Intel Bartlett Lake CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L17) | [`intel,bartlett-lake`](../../../../build/dts/api/bindings/cpu/intel,bartlett-lake.md#std-dtcompatible-intel-bartlett-lake) |
| DMA | on-chip | LPSS DMA Controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L65) | [`intel,lpss`](../../../../build/dts/api/bindings/dma/intel,lpss.md#std-dtcompatible-intel-lpss) |
| GPIO & Headers | on-chip | Intel GPIO[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L370) | [`intel,gpio`](../../../../build/dts/api/bindings/gpio/intel,gpio.md#std-dtcompatible-intel-gpio) |
| I2C | on-chip | Synopsys DesignWare I2C[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L72) | [`snps,designware-i2c`](../../../../build/dts/api/bindings/i2c/snps,designware-i2c.md#std-dtcompatible-snps-designware-i2c) |
| Interrupt controller | on-chip | Intel I/O Advanced Programmable Interrupt Controller (APIC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L30) | [`intel,ioapic`](../../../../build/dts/api/bindings/interrupt-controller/intel,ioapic.md#std-dtcompatible-intel-ioapic) |
| on-chip | Local Advanced Programmable Interrupt Controller (APIC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L38) | [`intel,loapic`](../../../../build/dts/api/bindings/interrupt-controller/intel,loapic.md#std-dtcompatible-intel-loapic) |
| on-chip | Intel VT-D Interrupt Remapping Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L350) | [`intel,vt-d`](../../../../build/dts/api/bindings/interrupt-controller/intel,vt-d.md#std-dtcompatible-intel-vt-d) |
| Miscellaneous | on-chip | Intel TGPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L573) | [`intel,timeaware-gpio`](../../../../build/dts/api/bindings/misc/intel,timeaware-gpio.md#std-dtcompatible-intel-timeaware-gpio) |
| PCIe | on-chip | Generic PCIe host controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L46) | [`pcie-controller`](../../../../build/dts/api/bindings/pcie/host/pcie-controller.md#std-dtcompatible-pcie-controller) |
| PWM | on-chip | Intel blinky PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L552) | [`intel,blinky-pwm`](../../../../build/dts/api/bindings/pwm/intel,blinky-pwm.md#std-dtcompatible-intel-blinky-pwm) |
| RTC | on-chip | Motorola MC146818 compatible Real Timer Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L563) | [`motorola,mc146818`](../../../../build/dts/api/bindings/rtc/motorola,mc146818.md#std-dtcompatible-motorola-mc146818) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L357)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L293) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SMbus | on-chip | Intel Platform Controller Hub SMBus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L53) | [`intel,pch-smbus`](../../../../build/dts/api/bindings/smbus/intel,pch-smbus.md#std-dtcompatible-intel-pch-smbus) |
| SPI | on-chip | Intel Penwell SPI[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L235) | [`intel,penwell-spi`](../../../../build/dts/api/bindings/spi/intel,penwell-spi.md#std-dtcompatible-intel-penwell-spi) |
| Timer | on-chip | HPET (High-Precision Event Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L582) | [`intel,hpet`](../../../../build/dts/api/bindings/timer/intel,hpet.md#std-dtcompatible-intel-hpet) |
| Watchdog | on-chip | Intel TCO Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/bartlett_lake_s.dtsi?plain=1#L591) | [`intel,tco-wdt`](../../../../build/dts/api/bindings/watchdog/intel,tco-wdt.md#std-dtcompatible-intel-tco-wdt) |

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
