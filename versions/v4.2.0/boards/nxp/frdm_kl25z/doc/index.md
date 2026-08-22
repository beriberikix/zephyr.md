---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_kl25z/doc/index.html
original_path: boards/nxp/frdm_kl25z/doc/index.html
---

# FRDM-KL25Z

Board Overview

[![../../../../_images/frdm_kl25z.jpg](../../../../_images/frdm_kl25z.jpg)
](../../../../_images/frdm_kl25z.jpg)

FRDM-KL25Z

Name:
:   `frdm_kl25z`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mkl25z4

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_kl25z/doc/index.rst/../..)

## Overview

The Freedom KL25Z is an ultra-low-cost development platform for
Kinetis® L Series KL1x (KL14/15) and KL2x (KL24/25) MCUs built
on ARM® Cortex®-M0+ processor.

The FRDM-KL25Z features include easy access to MCU I/O, battery-ready,
low-power operation, a standard-based form factor with expansion board
options and a built-in debug interface for flash programming and run-control.

## Hardware

- MKL25Z128VLK4 MCU @ 48 MHz, 128 KB flash, 16 KB SRAM, USB OTG (FS), 80LQFP
- On board capacitive touch “slider”, MMA8451Q accelerometer, and tri-color LED
- OpenSDA debug interface

For more information about the KL25Z SoC and FRDM-KL25Z board:

- [KL25Z Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/kinetis-kl2x-72-96mhz-usb-ultra-low-power-microcontrollers-mcus-based-on-arm-cortex-m0-plus-core:KL2x?&l)
- [KL25Z Datasheet](https://www.nxp.com/docs/en/data-sheet/KL25P80M48SF0.pdf)
- [KL25Z Reference Manual](https://www.nxp.com/webapp/Download?colCode=KL25P80M48SF0RM)
- [FRDM-KL25Z Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/freedom-development-platform-for-kinetis-kl14-kl15-kl24-kl25-mcus:FRDM-KL25Z)
- [FRDM-KL25Z User Guide](https://www.nxp.com/webapp/Download?colCode=FRDMKL25ZUM)
- [FRDM-KL25Z Schematics](https://www.nxp.com/downloads/en/schematics/FRDM-KL25Z_SCH_REV_E.pdf)

### Supported Features

The `frdm_kl25z` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_kl25z/mkl25z4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L20) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Kinetis ADC16[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L113) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp%2Ckinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| Clock control | on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L56) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L84) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L89) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module A (FTFA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L39) | [`nxp,kinetis-ftfa`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ckinetis-ftfa.md#std-dtcompatible-nxp-kinetis-ftfa) |
| GPIO & Headers | on-chip | Kinetis GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L151)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L170) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kl25z/frdm_kl25z.dts?plain=1#L59) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Kinetis I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L62)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L73) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Ckinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kl25z/frdm_kl25z.dts?plain=1#L45) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kl25z/frdm_kl25z.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L48) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L121) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L33) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kl25z/frdm_kl25z.dts?plain=1#L109) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700) |
| Serial controller | on-chip | Kinetis LPSCI UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L104) | [`nxp,kinetis-lpsci`](../../../../build/dts/api/bindings/serial/nxp%2Ckinetis-lpsci.md#std-dtcompatible-nxp-kinetis-lpsci) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L27) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kl25z.dtsi?plain=1#L198) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp%2Ckinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |

### Connections and IOs

The KL25Z SoC has five pairs of pinmux/gpio controllers, and all are currently enabled
(PORTA/GPIOA, PORTB/GPIOB, PORTC/GPIOC, PORTD/GPIOD, and PORTE/GPIOE) for the FRDM-KL25Z board.

| Name | Function | Usage |
| --- | --- | --- |
| PTB2 | ADC | ADC0 channel 12 |
| PTB18 | GPIO | Red LED |
| PTB19 | GPIO | Green LED |
| PTD1 | GPIO | Blue LED |
| PTA1 | UART0\_RX | UART Console |
| PTA2 | UART0\_TX | UART Console |
| PTE24 | I2C0\_SCL | I2C |
| PTE25 | I2C0\_SDA | I2C |

### System Clock

The KL25Z SoC is configured to use the 8 MHz external oscillator on the board
with the on-chip FLL to generate a 48 MHz system clock.

### Serial Port

The KL25Z UART0 is used for the console.

### USB

The KL25Z SoC has a USB OTG (USBOTG) controller that supports both
device and host functions through its mini USB connector (USB KL25Z).
Only USB device function is supported in Zephyr at the moment.

## Programming and Debugging

The `frdm_kl25z` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ |  | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe).

Early versions of this board have an outdated version of the OpenSDA bootloader
and require an update. Please see the [DAPLink Bootloader Update](https://os.mbed.com/blog/entry/DAPLink-bootloader-update/) page for
instructions to update from the CMSIS-DAP bootloader to the DAPLink bootloader.

#### Option 1: Linkserver: [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) (Recommended)

> Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your
> search path. LinkServer works with the CMSIS-DAP debug firmware. Please follow the
> instructions on [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) and select the latest revision
> of the firmware image.
>
> Linkserver is the default for this board, `west flash` and `west debug` will
> call the linkserver runner.
>
> ```shell
> west flash
> west debug
> ```

#### Option 2: [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [OpenSDA J-Link FRDM-KL25Z Firmware](https://www.segger.com/downloads/jlink/OpenSDA_FRDM-KL25Z).

Add the arguments `-DBOARD_FLASH_RUNNER=jlink` and
`-DBOARD_DEBUG_RUNNER=jlink` when you invoke `west build` to override the
default runner from pyOCD to J-Link:

```shell
# From the root of the zephyr repository
west build -b frdm_kl25z samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

#### Note:

The runners supported by NXP are LinkServer and JLink. pyOCD is another potential option,
but NXP does not test or support the pyOCD runner.

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to J7.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_kl25z samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_kl25z
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_kl25z samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_kl25z
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
