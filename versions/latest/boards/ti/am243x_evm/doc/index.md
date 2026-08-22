---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ti/am243x_evm/doc/index.html
original_path: boards/ti/am243x_evm/doc/index.html
---

# TI AM243x-EVM

Board Overview

[![../../../../_images/tmds243evm-angled.webp](../../../../_images/tmds243evm-angled.webp)
](../../../../_images/tmds243evm-angled.webp)

TI AM243x-EVM

Name:
:   `am243x_evm`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   am2434

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/am243x_evm/doc/index.rst/../..)

## Overview

The AM243x EVM is a development board that is based of a AM2434 SoC. The
Cortex R5F cores in the SoC run at 800 MHz. The board also includes a flash
region, DIP-Switches for the boot mode selection and 2 RJ45 Ethernet ports.

See the [TI TMDS243EVM Product Page](https://www.ti.com/tool/TMDS243EVM) for details.

## Hardware

The AM2434 SoC has 2 domains. A MAIN domain and a MCU domain. The MAIN domain
consists of 4 R5F cores and the MCU domain of one M4F core.

Zephyr currently supports the following cores:

- R5F Subsystem 0 Core 0 (R5F0\_0)
- M4F Core (M4)

The board physically contains:

- Memory.

  > - 256KB of SRAM
  > - 2GB of DDR4
- Debug

  > - XDS110 based JTAG

### Devices

#### System Clock

This board configuration uses a system clock frequency of

- 800MHz for R5F0\_0
- 400MHz for M4

#### DDR RAM

The board has 2GB of DDR RAM available. This board configuration allocates:

- 4KB Resource Table at 0xa4100000 for M4
- 4KB Resource Table at 0xa0100000 for R5F0\_0
- 8MB Shared Memory at 0xa5000000 for inter-processor communication

#### Serial Port

This board configuration uses by default:

- MAIN domain UART (UART0) for R5F0\_0
- MCU domain UART (MCU\_UART0) for M4

### Supported Features

The `am243x_evm` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `am243x_evm/am2434/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L21) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | TI AM335X ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L218) | [`ti,am335x-adc`](../../../../build/dts/api/bindings/adc/ti%2Cam335x-adc.md#std-dtcompatible-ti-am335x-adc) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L38) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Firmware | on-chip | TISCI Client Driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L14) | [`ti,k2g-sci`](../../../../build/dts/api/bindings/firmware/ti%2Ck2g-sci.md#std-dtcompatible-ti-k2g-sci) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_mcu.dtsi?plain=1#L56)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L202) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Cdavinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L166) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Comap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/am243x_evm/am243x_evm_am2434_m4.dts?plain=1#L36) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | TI Secure Proxy MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L24) | [`ti,secure-proxy`](../../../../build/dts/api/bindings/mbox/ti%2Csecure-proxy.md#std-dtcompatible-ti-secure-proxy) |
| on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L276)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L228) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti%2Comap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_mcu.dtsi?plain=1#L14)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L32) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ck3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Power domain | on-chip | TISCI-managed power domain[148 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main_power_domains.dtsi?plain=1#L8) | [`ti,sci-pm-domain`](../../../../build/dts/api/bindings/power-domain/ti%2Csci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_mcu.dtsi?plain=1#L20)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L110) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | TI Dual-Mode Timer[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L38) | [`ti,am654-timer`](../../../../build/dts/api/bindings/timer/ti%2Cam654-dmtimer.md#std-dtcompatible-ti-am654-timer) |

#### `am243x_evm/am2434/r5f0_0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R5 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L22) | [`arm,cortex-r5`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r5.md#std-dtcompatible-arm-cortex-r5) |
| ADC | on-chip | TI AM335X ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L218) | [`ti,am335x-adc`](../../../../build/dts/api/bindings/adc/ti%2Cam335x-adc.md#std-dtcompatible-ti-am335x-adc) |
| Firmware | on-chip | TISCI Client Driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L14) | [`ti,k2g-sci`](../../../../build/dts/api/bindings/firmware/ti%2Ck2g-sci.md#std-dtcompatible-ti-k2g-sci) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_mcu.dtsi?plain=1#L56)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L202) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Cdavinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L166)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L175) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Comap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | TI Vectored Interrupt Manager is a external interrupt controller (TI specific IP) which is compatible with R5F VIC port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L52) | [`ti,vim`](../../../../build/dts/api/bindings/interrupt-controller/ti%2Cvim.md#std-dtcompatible-ti-vim) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/am243x_evm/am243x_evm_am2434_r5f0_0.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | TI Secure Proxy MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L24) | [`ti,secure-proxy`](../../../../build/dts/api/bindings/mbox/ti%2Csecure-proxy.md#std-dtcompatible-ti-secure-proxy) |
| on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L276)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L228) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti%2Comap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L32) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ck3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Power domain | on-chip | TISCI-managed power domain[148 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main_power_domains.dtsi?plain=1#L8) | [`ti,sci-pm-domain`](../../../../build/dts/api/bindings/power-domain/ti%2Csci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L110)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L118) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| Timer | on-chip | TI Dual-Mode Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L86)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_main.dtsi?plain=1#L38) | [`ti,am654-timer`](../../../../build/dts/api/bindings/timer/ti%2Cam654-dmtimer.md#std-dtcompatible-ti-am654-timer) |

## Flashing

The boot process of the AM2434 SoC requires the booting image to be in a
specific format and to wait for the internal DMSC-L of the AM2434 to start up
and configure memory firewalls. Since there exists no Zephyr support it’s
required to use one of the SBL bootloader examples from the TI MCU+ SDK.

### Prerequisites

The following steps are from the time this documentation was written and might
change in the future. They also target Linux with assumption some basic things
(like python3 and openssl) are installed.

You might also want to take a look at the [Bootflow Guide](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/BOOTFLOW_GUIDE.html) for more details.

To build these you need to install the TI MCU+ SDK. To do this you need to
follow the steps described in the `mcupsdk-core` repository, which includes
cloning the repositories with west. It’s recommended to use another Python venv
for this since the MCU+ SDK has own Python dependencies that could conflict with
Zephyr dependencies. You can replace `all/dev.yml` in the `west init`
command with `am243x/dev.yml`, if you want to clone a few less repositories.

You also need to follow the “Downloading And Installing Dependencies” section
but you need to replace all `am263x` occurences in commands with `am243x`.
Please also take note of the `tools` and `mcu_plus_sdk` install path. The
`tools` install path will later be referred to as `$TI_TOOLS` and the MCU+
SDK path as `$MCUPSDK`. You can pass `--skip_doxygen=true` and
`--skip_ccs=true` to the install script since they aren’t needed. You might
encounter a error that a script can’t be executed. To fix it you need to mark it
as executable with `chmod +x <path>` and run the `download_components.sh`
again.

Summarized you will most likely want to run the following commands or similar
versions for setting up the MCU+ SDK:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip3 install west
west init -m https://github.com/TexasInstruments/mcupsdk-manifests.git --mr mcupsdk_west --mf am243x/dev.yml
west update
./mcupsdk_setup/am243x/download_components.sh --skip_doxygen=true --skip_ccs=true
```

After the script finished successfully you want to switch into the
`mcu_plus_sdk` directory and edit the
`source/drivers/bootloader/bootloader.c` file to set the `entryPoint` to
`0` inside `Bootloader_runCpu` unconditionally. This is needed due to how
Zephyr builds the image currently.

Now you can build the internal libraries with the following commands:

```shell
make gen-buildfiles DEVICE=am243x PROFILE=release
make libs DEVICE=am243x PROFILE=release
```

If you encounter compile errors you have to fix them. For that you might have to
change parameter types, remove missing source files from makefiles or download
missing headers from the TI online reference.

Depending on whether you later want to boot from flash or by loading the image
via UART either the `sbl_ospi` or the `sbl_uart` example is relevant for the
next section.

### Building the bootloader itself

The example bootloader implementation is found in the
`examples/drivers/boot/<example>/am243x-evm/r5fss0-0_nortos` directory.

You can either build the example by invoking `make -C
examples/drivers/boot/<example>/am243x-evm/r5fss0-0_nortos/ti-arm-clang/
DEVICE=am243x PROFILE=release` or use the prebuilt binaries in
`tools/boot/sbl_prebuilt/am243x-evm`

### Converting the Zephyr application

Additionally for booting you need to convert your built Zephyr binary into a
format that the TI example bootloader can boot. You can do this with the
following commands, where `$TI_TOOLS` refers to the root of where your
ti-tools (clang, sysconfig etc.) are installed (`$HOME/ti` by default) and
`$MCUPSDK` to the root of the MCU+ SDK (directory called `mcu_plus_sdk`).
You might have to change version numbers in the commands. It’s expected that the
`zephyr.elf` from the build output is in the current directory.

```shell
export BOOTIMAGE_CORE_ID_r5fss0-0=4
export BOOTIMAGE_CORE_ID_m4=14
# set CORE_ID as per your target core
export BOOTIMAGE_CORE_ID=${BOOTIMAGE_CORE_ID_desired-core}
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/out2rprc/elf2rprc.js ./zephyr.elf
$MCUPSDK/tools/boot/xipGen/xipGen.out -i ./zephyr.rprc -o ./zephyr.rprc_out -x ./zephyr.rprc_out_xip --flash-start-addr 0x60000000
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/multicoreImageGen/multicoreImageGen.js --devID 55 --out ./zephyr.appimage ./zephyr.rprc_out@${BOOTIMAGE_CORE_ID}
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/multicoreImageGen/multicoreImageGen.js --devID 55 --out ./zephyr.appimage_xip ./zephyr.rprc_out_xip@${BOOTIMAGE_CORE_ID}
python3 $MCUPSDK/source/security/security_common/tools/boot/signing/appimage_x509_cert_gen.py --bin ./zephyr.appimage --authtype 1 --key $MCUPSDK/source/security/security_common/tools/boot/signing/app_degenerateKey.pem --output ./zephyr.appimage.hs_fs
```

All these steps are also present in various Makefiles in the `examples/`
directory of MCU+ SDK source.

### Running the Zephyr image

After that you want to switch the bootmode to UART by switching the DIP-Switches
into the following configuration:

UART Boot Mode

| SW2 [0:7] | SW3 [8:15] |
| --- | --- |
| 11011100 | 10110000 |

If you want to just run the image via UART you need to run

```shell
python3 uart_bootloader.py -p /dev/ttyUSB0 --bootloader=sbl_uart.release.hs_fs.tiimage --file=zephyr.appimage.hs_fs
```

The `uart_bootloader.py` script is found in `$MCUPSDK/tools/boot` and the
`sbl_uart.release.hs_fs.tiimage` in
`$MCUPSDK/tools/boot/sbl_prebuilt/am243x-evm`. After sending the image your
Zephyr application will run after a 2 second long delay.

If you want to flash the image instead you have to take the OSPI example config
file from the `$MCUPSDK/tools/boot/sbl_prebuilt/am243x-evm` directory and
change the filepath according to your names. It should look approximately like:

```text
--flash-writer=sbl_uart_uniflash.release.hs_fs.tiimage
--operation=flash-phy-tuning-data
--file=sbl_prebuilt/am243x-evm/sbl_ospi.release.hs_fs.tiimage --operation=flash --flash-offset=0x0
--file=zephyr.appimage.hs_fs --operation=flash --flash-offset=0x80000
--file=zephyr.appimage_xip --operation=flash-xip
```

You then need to run `python3 uart_uniflash.py -p /dev/ttyUSB0
--cfg=<path/to/your-config-file>`. The scripts and images are in the same path
as described in the UART section above.

After flashing your image you can power off your board, switch the DIP-Switches
into following configuration to boot in OSPI mode and your Zephyr application
will boot immediately after powering on the board.

OSPI Boot Mode

| SW2 [0:7] | SW3 [8:15] |
| --- | --- |
| 11001110 | 01000000 |

## Debugging

### OpenOCD

The board is equipped with an XDS110 JTAG debugger. To debug a binary, utilize
the `debug` build target:

```shell
west build -b am243x_evm/<soc>/<core> <my_app>
west debug
```

Hint

To utilize this feature, you’ll need OpenOCD version 0.12 or higher. Due to the possibility of
older versions being available in package feeds, it’s advisable to [build OpenOCD from source](https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source).

### Code Composer Studio

Instead of using `sbl_ospi` from above, one may also flash `sbl_null` and load the
application ELFs using Code Composer Studio IDE to individual cores and run/debug
the application. Note that this does not require converting the Zephyr ELF to another
forma, making development much easier.

## References

AM64x/AM243x EVM Technical Reference Manual:
:   [https://www.ti.com/lit/ug/spruj63a/spruj63a.pdf](https://www.ti.com/lit/ug/spruj63a/spruj63a.pdf)

MCU+ SDK Github repository:
:   [https://github.com/TexasInstruments/mcupsdk-core](https://github.com/TexasInstruments/mcupsdk-core)

## License

This document Copyright (c) Siemens Mobility GmbH

This document Copyright (c) 2025 Texas Instruments

SPDX-License-Identifier: Apache-2.0
