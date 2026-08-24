---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/infineon/cyw920829m2evk_02/doc/index.html
original_path: boards/infineon/cyw920829m2evk_02/doc/index.html
---

# CYW920829M2EVK-02

Board Overview

[![../../../../_images/cyw920829m2evk_02.webp](https://docs.zephyrproject.org/4.2.0/_images/cyw920829m2evk_02.webp)
](https://docs.zephyrproject.org/4.2.0/_images/cyw920829m2evk_02.webp)

CYW920829M2EVK-02

Name:
:   `cyw920829m2evk_02`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cyw20829b0lkml

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/cyw920829m2evk_02/doc/index.rst/../..)

## Overview

The AIROC™ CYW20829 Bluetooth® LE MCU Evaluation Kit (CYW920829M2EVK-02) with its included on-board
peripherals enables evaluation, prototyping, and development of a wide array of
Bluetooth® Low Energy applications, all on Infineon’s low power, high performance AIROC™ CYW20829.
The AIROC™ CYW20829’s robust RF performance and 10 dBm TX output power without an external power
amplifier (PA). This provides enough link budget for the entire spectrum of Bluetooth® LE use cases
including industrial IoT applications, smart home, asset tracking, beacons and sensors, and
medical devices.

The system features Dual Arm® Cortex® - M33s for powering the MCU and Bluetooth subsystem with
programmable and reconfigurable analog and digital blocks. In addition, on the kit, there is a
suite of on-board peripherals including six-axis inertial measurement unit (IMU), thermistor,
analog mic, user programmable buttons (2), LEDs (2), and RGB LED. There is also extensive GPIO
support with extended headers and Arduino Uno R3 compatibility for third-party shields.

## Hardware

For more information about the CYW20829 SoC and CYW920829M2EVK-02 board:

- [CYW20829 SoC Website](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-bluetooth-le-bluetooth-multiprotocol/airoc-bluetooth-le/cyw20829/)
- [CYW920829M2EVK-02 Board Website](https://www.infineon.com/cms/en/product/evaluation-boards/cyw920829m2evk-02/)

### Kit Features:

- AIROC™ CYW20829 Bluetooth® LE MCU in 56 pin QFN package
- Arduino compatible headers for hardware expansion
- On-board sensors - 6-axis IMU, Thermistor, Infineon analog microphone,
  and Infineon digital microphone
- User switches, RGB LED and user LEDs
- USB connector for power, programming and USB-UART bridge

### Kit Contents:

- CYW20829 evaluation board (CYW9BTM2BASE3+CYW920829M2IPA2)
- USB Type-A to Micro-B cable
- Six jumper wires (five inches each)
- Quick start guide

### Supported Features

The `cyw920829m2evk_02` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `cyw920829m2evk_02/cyw20829b0lkml` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L18) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Infineon Cat1 ADC Each ADC group Cat1 is assigned to a Zephyr device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L151) | [`infineon,cat1-adc`](../../../../build/dts/api/bindings/adc/infineon,cat1-adc.md#std-dtcompatible-infineon-cat1-adc) |
| ARM architecture | on-chip | Infineon Serial Communication Blocks (SCB) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L166) | [`infineon,cat1-scb`](../../../../build/dts/api/bindings/arm/infineon,cat1-scb.md#std-dtcompatible-infineon-cat1-scb) |
| Bluetooth | on-chip | Bluetooth module that uses Infineon CYW208XX HCI bluetooth interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L367) | [`infineon,cyw208xx-hci`](../../../../build/dts/api/bindings/bluetooth/infineon,cyw208xx-hci.md#std-dtcompatible-infineon-cyw208xx-hci) |
| Clock control | on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/system_clocks.dtsi?plain=1#L19)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/system_clocks.dtsi?plain=1#L121) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/system_clocks.dtsi?plain=1#L43) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | Infineon counters[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L207) | [`infineon,cat1-counter`](../../../../build/dts/api/bindings/counter/infineon,cat1-counter.md#std-dtcompatible-infineon-cat1-counter) |
| DMA | on-chip | Infineon CAT1 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L344) | [`infineon,cat1-dma`](../../../../build/dts/api/bindings/dma/infineon,cat1-dma.md#std-dtcompatible-infineon-cat1-dma) |
| Flash controller | on-chip | Infineon CAT1 QSPI flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L67) | [`infineon,cat1-qspi-flash`](../../../../build/dts/api/bindings/flash_controller/infineon,cat1-qspi-flash.md#std-dtcompatible-infineon-cat1-qspi-flash) |
| GPIO & Headers | on-chip | Infineon CAT1 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L96)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L114) | [`infineon,cat1-gpio`](../../../../build/dts/api/bindings/gpio/infineon,cat1-gpio.md#std-dtcompatible-infineon-cat1-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cyw920829m2evk_02/cyw920829m2evk_02-common.dtsi?plain=1#L29) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cyw920829m2evk_02/cyw920829m2evk_02-common.dtsi?plain=1#L16) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-board | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cyw920829m2evk_02/cyw920829m2evk_02.dts?plain=1#L105) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cyw920829m2evk_02/cyw920829m2evk_02.dts?plain=1#L121) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Infineon CAT1 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L84) | [`infineon,cat1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon,cat1-pinctrl.md#std-dtcompatible-infineon-cat1-pinctrl) |
| Power management | on-chip | Infineon CAT1B power control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/system_clocks.dtsi?plain=1#L10) | [`infineon,cat1b-power`](../../../../build/dts/api/bindings/power/infineon,cat1b-power.md#std-dtcompatible-infineon-cat1b-power) |
| PWM | on-chip | Infineon CAT1 PWM[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L271) | [`infineon,cat1-pwm`](../../../../build/dts/api/bindings/pwm/infineon,cat1-pwm.md#std-dtcompatible-infineon-cat1-pwm) |
| RTC | on-chip | Infineon CAT1 family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L199) | [`infineon,cat1-rtc`](../../../../build/dts/api/bindings/rtc/infineon,cat1-rtc.md#std-dtcompatible-infineon-cat1-rtc) |
| Serial controller | on-chip | Infineon CAT1 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L178) | [`infineon,cat1-uart`](../../../../build/dts/api/bindings/serial/infineon,cat1-uart.md#std-dtcompatible-infineon-cat1-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L40) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Infineon Cat1 low power timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L192) | [`infineon,cat1-lp-timer`](../../../../build/dts/api/bindings/timer/infineon,cat1-lp-timer.md#std-dtcompatible-infineon-cat1-lp-timer) |
| Watchdog | on-chip | Infineon CAT1 Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/cyw20829/cyw20829.dtsi?plain=1#L185) | [`infineon,cat1-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon,cat1-watchdog.md#std-dtcompatible-infineon-cat1-watchdog) |

### System Clock

The AIROC™ CYW20829 Bluetooth® MCU SoC is configured to use the internal IMO+FLL as a source for
the system clock. Other sources for the system clock are provided in the SOC, depending on your
system requirements.

## Fetch Binary Blobs

cyw920829m2evk\_02 board requires fetch binary files (e.g Bluetooth controller firmware).

To fetch Binary Blobs:

```shell
west blobs fetch hal_infineon
```

## Build blinking led sample

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b cyw920829m2evk_02 samples/basic/blinky
```

## Programming and Debugging

The `cyw920829m2evk_02` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The CYW920829M2EVK-02 includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3)) to provide debugging,
flash programming, and serial communication over USB. Flash and debug commands use OpenOCD and
require a custom Infineon OpenOCD version, that supports KitProg3, to be installed.

The CYW920829M2EVK-02 supports RTT via a SEGGER JLink device, under the target name cyw20829\_tm.
This can be enabled for an application by building with the rtt-console snippet or setting the
following config values: CONFIG\_UART\_CONSOLE=n, CONFIG\_RTT\_CONSOLE=y, and CONFIG\_USE\_SEGGER\_RTT=y.
e.g. west build -p always -b cyw920829m2evk\_02 samples/basic/blinky -S rtt-console

As an additional note there is currently a discrepancy in RAM address between SEGGER and the
CYW920829M2EVK-02 device. So, for RTT control block, do not use “Auto Detection”. Instead, set
the search range to something reflecting: RAM RangeStart at 0x20000000 and RAM RangeSize of 0x3d000.

### Infineon OpenOCD Installation

Both the full [ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) and the [ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) packages include Infineon
OpenOCD. Installing either of these packages will also install Infineon OpenOCD. If neither package
is installed, a minimal installation can be done by downloading the [Infineon OpenOCD](https://github.com/Infineon/openocd/releases/latest) release for
your system and manually extract the files to a location of your choice.

Note

Linux requires device access rights to be set up for KitProg3. This is handled
automatically by the ModusToolbox and ModusToolbox Programming Tools installations.
When doing a minimal installation, this can be done manually by executing the
script `openocd/udev_rules/install_rules.sh`.

### West Commands

The path to the installed Infineon OpenOCD executable must be available to the `west` tool
commands. There are multiple ways of doing this. The example below uses a permanent CMake argument
to set the CMake variable `OPENOCD`.

> WindowsLinux
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd.exe
>
> # Do a pristine build once after setting CMake argument
> west build -b cyw920829m2evk_02 -p always samples/basic/blinky
>
> west flash
> west debug
> ```
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd
>
> # Do a pristine build once after setting CMake argument
> west build -b cyw920829m2evk_02 -p always samples/basic/blinky
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and
perform other standard GDB debugging on the CYW20829 CM33 core.

## Operate in SECURE Lifecycle Stage

The device lifecycle stage (LCS) is a key aspect of the security of the AIROC™
CYW20829 Bluetooth® MCU. The lifecycle stages follow a strict, irreversible progression dictated by
the programming of the eFuse bits (changing the value from “0” to “1”). This system is used to
protect the device’s data and code at the level required by the user.
SECURE is the lifecycle stage of a secured device.
Follow the instructions in [AN239590 Provision CYW20829 to SECURE LCS](https://www.infineon.com/dgdl/Infineon-AN239590_Provision_CYW20829_CYW89829_to_Secure_LCS-ApplicationNotes-v02_00-EN.pdf?fileId=8ac78c8c8d2fe47b018e3677dd517258) to transition the device
to SECURE LCS. In the SECURE LCS stage, the protection state is set to secure. A secured device
will only boot if the authentication of its flash content is successful.

The following configuration options can be used to build for a device which has been provisioned
to SECURE LCS and configured to use an encrypted flash interface:

- [`CONFIG_INFINEON_SECURE_LCS`](../../../../kconfig.md#CONFIG_INFINEON_SECURE_LCS "CONFIG_INFINEON_SECURE_LCS"): Enable if the target device is in SECURE LCS
- [`CONFIG_INFINEON_SECURE_POLICY`](../../../../kconfig.md#CONFIG_INFINEON_SECURE_POLICY "CONFIG_INFINEON_SECURE_POLICY"): Path to the policy JSON file,
  which was created for provisioning the device to SECURE LCS (refer to section 3.2 “Key creation”
  of [AN239590 Provision CYW20829 to SECURE LCS](https://www.infineon.com/dgdl/Infineon-AN239590_Provision_CYW20829_CYW89829_to_Secure_LCS-ApplicationNotes-v02_00-EN.pdf?fileId=8ac78c8c8d2fe47b018e3677dd517258))
- [`CONFIG_INFINEON_SMIF_ENCRYPTION`](../../../../kconfig.md#CONFIG_INFINEON_SMIF_ENCRYPTION "CONFIG_INFINEON_SMIF_ENCRYPTION"): Enable to use encrypted flash interface when provisioned to
  SECURE LCS.

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application for SECURE LCS.

```shell
# From the root of the zephyr repository
west build -b cyw920829m2evk_02 -p always samples/basic/blinky -- -DCONFIG_INFINEON_SECURE_LCS=y -DCONFIG_INFINEON_SECURE_POLICY=\"policy/policy_secure.json\"
```

## Using MCUboot

CYW20829 devices are supported by the Cypress MCU bootloader (MCUBootApp) from the
[Cypress branch of MCUboot](https://github.com/mcu-tools/mcuboot/tree/cypress).

### Building Cypress MCU Bootloader MCUBootApp

Please refer to the [CYW20829 platform description](https://github.com/mcu-tools/mcuboot/blob/v1.9.4-cypress/boot/cypress/platforms/CYW20829.md) and follow the instructions to understand the
MCUBootApp building process for normal/secure silicon and its overall usage as a bootloader.
Place keys and policy-related folders in the cypress directory `mcuboot/boot/cypress/`.

Ensure the default memory map matches the memory map of the Zephyr application (refer to partitions
of flash0 in [boards/infineon/cyw920829m2evk\_02/cyw920829m2evk\_02.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cyw920829m2evk_02/cyw920829m2evk_02.dts)).

You can use `west flash` to flash MCUBootApp:

```shell
# Flash MCUBootApp.hex
west flash --skip-rebuild --hex-file /path/to/cypress/mcuboot/boot/cypress/MCUBootApp/out/CYW20829/Debug/MCUBootApp.hex
```

Note

`west flash` requires an existing Zephyr build directory which can be created by first
building any Zephyr application for the target board.

### Build Zephyr application

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application
for MCUboot.

```shell
# From the root of the zephyr repository
west build -b cyw920829m2evk_02 -p always samples/basic/blinky -- -DCONFIG_BOOTLOADER_MCUBOOT=y -DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"/path/to/cypress/mcuboot/boot/cypress/keys/cypress-test-ec-p256.pem\"
west flash
```

If you use [`CONFIG_MCUBOOT_ENCRYPTION_KEY_FILE`](../../../../kconfig.md#CONFIG_MCUBOOT_ENCRYPTION_KEY_FILE "CONFIG_MCUBOOT_ENCRYPTION_KEY_FILE") to generate an encrypted image then the final
hex will be `zephyr.signed.encrypted.hex` and the corresponding bin file will
be `zephyr.signed.encrypted.bin`. Use these files for flashing and ota uploading respectively.
For example, to build and flash an encrypted [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application
image for MCUboot:

```shell
# From the root of the zephyr repository
west build -b cyw920829m2evk_02 -p always samples/basic/blinky -- -DCONFIG_BOOTLOADER_MCUBOOT=y -DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"/path/to/cypress/mcuboot/boot/cypress/keys/cypress-test-ec-p256.pem\" -DCONFIG_MCUBOOT_ENCRYPTION_KEY_FILE=\"/path/to/cypress/mcuboot/enc-ec256-pub.pem\"
west flash --hex-file build/zephyr/zephyr.signed.encrypted.hex
```
