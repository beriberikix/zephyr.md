---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_k82f/doc/index.html
original_path: boards/nxp/frdm_k82f/doc/index.html
---

# FRDM-K82F

Board Overview

[![../../../../_images/frdm_k82f.jpg](../../../../_images/frdm_k82f.jpg)
](../../../../_images/frdm_k82f.jpg)

FRDM-K82F

Name:
:   `frdm_k82f`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mk82f25615

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_k82f/doc/index.rst/../..)

## Overview

The FRDM-K82F is a low-cost development platform for Kinetis K80, K81,
and K82 MCUs.

- Form-factor compatible with the Arduino R3 pin layout
- Peripherals enable rapid prototyping, including a six-axis digital
  accelerometer and magnetometer to create full eCompass capabilities, a
  tri-colored LED and two user push-buttons for direct interaction, 2x32 Mb
  QuadSPI external flash, FlexIO camera header, touchpads and headers for use
  with Bluetooth and 2.4 GHz radio add-on modules
- OpenSDAv2.1, the NXP open source hardware embedded serial and debug adapter
  running an open source bootloader, offers options for serial communication,
  flash programming, and run-control debugging

## Hardware

- MK82FN256VLL15 MCU (150 MHz, 256 KB flash memory, 256 KB RAM, low-power,
  crystal-less USB, and 100 Low profile Quad Flat Package (LQFP))
- Dual role USB interface with micro-B USB connector
- RGB LED
- FXOS8700CQ accelerometer and magnetometer
- Two user push buttons
- 2x 32 Mb QSPI flash
- Flexible power supply option - OpenSDAv2.1 USB, Kinetis K82 USB, and external source
- Easy access to MCU input/output through Arduino R3 compatible I/O connectors
- Programmable OpenSDAv2.1 debug circuit supporting the CMSIS-DAP Interface
  software that provides:

  - Mass storage device (MSD) flash programming interface
  - CMSIS-DAP debug interface over a driver-less USB HID connection providing
    run-control debugging and compatibility with IDE tools
  - Virtual serial port interface
  - Open source CMSIS-DAP software project
- FlexIO header

For more information about the K82F SoC and FRDM-K82F board:

- [K82F Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/k-series-cortex-m4/k8x-secure/kinetis-k82-150-mhz-hw-cryptographic-co-processor-quadspi-microcontrollers-mcus-based-on-arm-cortex-m4-core:K82_150)
- [K82F Datasheet](https://www.nxp.com/docs/en/data-sheet/K82P121M150SF5.pdf)
- [K82F Reference Manual](https://www.nxp.com/webapp/Download?colCode=K82P121M150SF5RM)
- [FRDM-K82F Website](https://www.nxp.com/design/development-boards/freedom-development-boards/mcu-boards/freedom-development-platform-for-kinetis-k82-k81-and-k80-mcus:FRDM-K82F)
- [FRDM-K82F User Guide](https://www.nxp.com/webapp/Download?colCode=FRDMK82FUG)
- [FRDM-K82F Schematics](https://www.nxp.com/downloads/en/schematics/FRDM-K82F-SCH.pdf)

### Supported Features

The `frdm_k82f` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_k82f/mk82f25615` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L28) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Kinetis ADC16[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L105) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp%2Ckinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| Clock control | on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L48) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L53) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L82) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L389) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L398) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L427) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module A (FTFA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L94) | [`nxp,kinetis-ftfa`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ckinetis-ftfa.md#std-dtcompatible-nxp-kinetis-ftfa) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L118) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k82f/frdm_k82f.dts?plain=1#L93) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Kinetis I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L168)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L179) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Ckinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k82f/frdm_k82f.dts?plain=1#L79) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k82f/frdm_k82f.dts?plain=1#L49) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k82f/frdm_k82f.dts?plain=1#L65) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MMU / MPU | on-chip | NXP System Memory Protection Unit (SYSMPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L42) | [`nxp,sysmpu`](../../../../build/dts/api/bindings/mmu_mpu/nxp%2Csysmpu.md#std-dtcompatible-nxp-sysmpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8xfn256vxx15.dtsi?plain=1#L33) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k82f/frdm_k82f.dts?plain=1#L156) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k82f/frdm_k82f.dts?plain=1#L223) | [`jedec,spi-nor`](../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L262) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L36) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP FlexTimer Module (FTM) PWM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L319) | [`nxp,ftm-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cftm-pwm.md#std-dtcompatible-nxp-ftm-pwm) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L367) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L328) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k82f/frdm_k82f.dts?plain=1#L189) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L252)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L212) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP DSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L337)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L357) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8xfn256vxx15.dtsi?plain=1#L26) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L292) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp%2Cftm.md#std-dtcompatible-nxp-ftm) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L373) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp%2Ckinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| Watchdog | on-chip | Kinetis watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k8x.dtsi?plain=1#L382) | [`nxp,kinetis-wdog`](../../../../build/dts/api/bindings/watchdog/nxp%2Ckinetis-wdog.md#std-dtcompatible-nxp-kinetis-wdog) |

Note

For additional features not yet supported, please also refer to the
[FRDM-K64F](../../frdm_k64f/doc/index.md#frdm_k64f), which is the superset board in NXP’s Kinetis K series.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the frdm\_k64f board may have additional features
already supported, which can also be re-used on this frdm\_k82f board.

### System Clock

The K82F SoC is configured to use the 12 MHz external oscillator on the board
with the on-chip PLL to generate a 120 MHz system clock.

### Serial Port

The K82F SoC has five UARTs. One is configured for the console, the remaining
ones are not used.

### USB

The K82F SoC has a USB OTG (USBOTG) controller that supports both
device and host functions through its micro USB connector (J11).
Only USB device function is supported in Zephyr at the moment.

## Programming and Debugging

The `frdm_k82f` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe).

Early versions of this board have an outdated version of the OpenSDA bootloader
and require an update. Please see the [DAPLink Bootloader Update](https://os.mbed.com/blog/entry/DAPLink-bootloader-update/) page for
instructions to update from the CMSIS-DAP bootloader to the DAPLink bootloader.

#### Option 1: [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) (Recommended)

Install the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) to program
the [OpenSDA DAPLink FRDM-K82F Firmware](https://www.nxp.com/downloads/en/snippets-boot-code-headers-monitors/k20dx_frdmk82f_if_crc_legacy_0x8000.bin).

#### Option 2: [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [OpenSDA J-Link Firmware for FRDM-K82F](https://www.segger.com/downloads/jlink/OpenSDA_FRDM-K82F).

Add the arguments `-DBOARD_FLASH_RUNNER=jlink` and
`-DBOARD_DEBUG_RUNNER=jlink` when you invoke `west build` to override the
default runner from pyOCD to J-Link:

```shell
# From the root of the zephyr repository
west build -b frdm_k82f samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to J5.

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
west build -b frdm_k82f samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! frdm_k82f
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_k82f samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! frdm_k82f
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
