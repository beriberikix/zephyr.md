---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_k22f/doc/index.html
original_path: boards/nxp/frdm_k22f/doc/index.html
---

# FRDM-K22F

Board Overview

[![../../../../_images/frdm_k22f.jpg](https://docs.zephyrproject.org/4.2.0/_images/frdm_k22f.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/frdm_k22f.jpg)

FRDM-K22F

Name:
:   `frdm_k22f`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mk22f51212

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_k22f/doc/index.rst/../..)

## Overview

The Freedom-K22F is an ultra-low-cost development platform for Kinetis K22
MCUs.

- Form-factor compatible with the Arduino R3 pin layout
- Peripherals enable rapid prototyping, including a 6-axis digital
  accelerometer and magnetometer to create full eCompass capabilities, a
  tri-colored LED and 2 user push-buttons for direct interaction, a optional
  microSD card slot, and headers for use with Bluetooth\* and 2.4 GHz radio
  add-on modules
- OpenSDAv2, the NXP open source hardware embedded serial and debug adapter
  running an open source bootloader, offers options for serial communication,
  flash programming, and run-control debugging

## Hardware

- MK22FN512VLH12 (120 MHz, 512 KB flash memory, 128 KB RAM, low-power,
  crystal-less USB, and 64 pin Low profile Quad Flat Package (LQFP))
- Dual role USB interface with micro-B USB connector
- RGB LED
- FXOS8700CQ accelerometer and magnetometer
- Two user push buttons
- Flexible power supply option - OpenSDAv2 USB, Kinetis K22 USB, and external source
- Easy access to MCU input/output through Arduino\* R3 compatible I/O connectors
- Programmable OpenSDAv2 debug circuit supporting the CMSIS-DAP Interface
  software that provides:

  - Mass storage device (MSD) flash programming interface
  - CMSIS-DAP debug interface over a driver-less USB HID connection providing
    run-control debugging and compatibility with IDE tools
  - Virtual serial port interface
  - Open source CMSIS-DAP software project
- Optional SDHC

For more information about the K22F SoC and FRDM-K22F board:

- [K22F Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/k-seriesperformancem4/k2x-usb/kinetis-k22-120-mhz-cost-effective-full-speed-usb-microcontrollers-mcus-based-on-arm-cortex-m4-core:K22_120)
- [K22F Datasheet](https://www.nxp.com/docs/en/data-sheet/K22P121M120SF7.pdf)
- [K22F Reference Manual](https://www.nxp.com/docs/en/reference-manual/K22P121M120SF7RM.pdf)
- [FRDM-K22F Website](https://www.nxp.com/support/developer-resources/evaluation-and-development-boards/freedom-development-boards/mcu-boards/nxp-freedom-development-platform-for-kinetis-k22-mcus:FRDM-K22F)
- [FRDM-K22F User Guide](https://www.nxp.com/webapp/Download?colCode=FRDMK22FUG)
- [FRDM-K22F Schematics](https://www.nxp.com/webapp/Download?colCode=FRDM-K22F-SCH)

### Supported Features

The `frdm_k22f` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_k22f/mk22f51212` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L30) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Kinetis ADC16[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L344) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp,kinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| Clock control | on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L64) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp,kinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L83) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp,kinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L88) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| DAC | on-chip | NXP Kinetis MCUX DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L352)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L361) | [`nxp,kinetis-dac`](../../../../build/dts/api/bindings/dac/nxp,kinetis-dac.md#std-dtcompatible-nxp-kinetis-dac) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module E (FTFE)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L117) | [`nxp,kinetis-ftfe`](../../../../build/dts/api/bindings/flash_controller/nxp,kinetis-ftfe.md#std-dtcompatible-nxp-kinetis-ftfe) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L227) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k22f/frdm_k22f.dts?plain=1#L91) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Kinetis I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L135)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L146) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp,kinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k22f/frdm_k22f.dts?plain=1#L77) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k22f/frdm_k22f.dts?plain=1#L44) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k22f/frdm_k22f.dts?plain=1#L60) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L127) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k22f/frdm_k22f.dts?plain=1#L206) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L197) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L58) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP FlexTimer Module (FTM) PWM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L304) | [`nxp,ftm-pwm`](../../../../build/dts/api/bindings/pwm/nxp,ftm-pwm.md#std-dtcompatible-nxp-ftm-pwm) |
| RNG | on-chip | Kinetis RNGA (Random Number Generator Accelerator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L387) | [`nxp,kinetis-rnga`](../../../../build/dts/api/bindings/rng/nxp,kinetis-rnga.md#std-dtcompatible-nxp-kinetis-rnga) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k22f/frdm_k22f.dts?plain=1#L139) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp,fxos8700.md#std-dtcompatible-nxp-fxos8700) |
| Serial controller | on-chip | Kinetis UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L167)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L157) | [`nxp,kinetis-uart`](../../../../build/dts/api/bindings/serial/nxp,kinetis-uart.md#std-dtcompatible-nxp-kinetis-uart) |
| SPI | on-chip | NXP DSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L277)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L287) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp,dspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L52) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L314) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp,ftm.md#std-dtcompatible-nxp-ftm) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L370) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp,kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| on-chip | NXP KHCI USB host controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L379) | [`nxp,uhc-khci`](../../../../build/dts/api/bindings/usb/nxp,uhc-khci.md#std-dtcompatible-nxp-uhc-khci) |
| Watchdog | on-chip | Kinetis watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k2x.dtsi?plain=1#L297) | [`nxp,kinetis-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,kinetis-wdog.md#std-dtcompatible-nxp-kinetis-wdog) |

Note

For additional features not yet supported, please also refer to the
[FRDM-K64F](../../frdm_k64f/doc/index.md#frdm_k64f), which is the superset board in NXP’s Kinetis K series.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the frdm\_k64f board may have additional features
already supported, which can also be re-used on this frdm\_k22f board.

### Connections and IOs

The K22F SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| PTA1 | GPIO | Red LED |
| PTA2 | GPIO | Green LED |
| PTD5 | GPIO | Blue LED |
| PTC1 | GPIO | SW2 |
| PTD0 | GPIO | FXOS8700 INT1 |
| PTD1 | GPIO | FXOS8700 INT2 |
| PTB17 | GPIO | SW3 |
| PTE1 | UART1\_RX | UART Console |
| PTE0 | UART1\_TX | UART Console |
| PTD2 | UART2\_RX | UART BT HCI |
| PTD3 | UART2\_TX | UART BT HCI |
| PTC4 | SPI0\_PCS0 | SPI |
| PTD1 | SPI0\_SCK | SPI |
| PTD2 | SPI0\_SOUT | SPI |
| PTD3 | SPI0\_SIN | SPI |
| PTB2 | I2C0\_SCL | I2C / FXOS8700 |
| PTB3 | I2C0\_SDA | I2C / FXOS8700 |

### System Clock

The K22F SoC is configured to use the 8 MHz crystal oscillator on the board
with the on-chip PLL to generate a 72 MHz system clock in its RUN mode. This
clock was selected to allow for the maximum number of peripherals to be used
with the crystal and PLL clocks. Other clock configurations are possible
through NXP SDK currently.

### Serial Port

The K22F SoC has three UARTs. One is configured for the console, another for BT
HCI, and the remaining are not used.

### USB

The K22F SoC has a USB OTG (USBOTG) controller that supports both
device and host functions through its micro USB connector (K22F USB).
Only USB device function is supported in Zephyr at the moment.

## Programming and Debugging

The `frdm_k22f` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ |  | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe).

Early versions of this board have an outdated version of the OpenSDA bootloader
and require an update. Please see the [DAPLink Bootloader Update](https://os.mbed.com/blog/entry/DAPLink-bootloader-update/) page for
instructions to update from the CMSIS-DAP bootloader to the DAPLink bootloader.

#### Option 1: [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) (Recommended)

Follow the instructions in [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) to program
the [OpenSDA DAPLink FRDM-K22F Firmware](https://www.nxp.com/downloads/en/snippets-boot-code-headers-monitors/k20dx_frdmk22f_if_crc_legacy_0x8000.bin).

Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your
search path. LinkServer works with the default CMSIS-DAP firmware included in
the on-board debugger.

Linkserver is the default for this board, `west flash` and `west debug` will
call the linkserver runner.

```shell
west flash
```

Alternatively, pyOCD can be used to flash and debug the board by using the
`-r pyocd` option with West. pyOCD is installed when you complete the
[Get Zephyr and install Python dependencies](../../../../develop/getting_started/index.md#gs-python-deps) step in the Getting Started Guide. The runners supported
by NXP are LinkServer and JLink. pyOCD is another potential option, but NXP
does not test or support the pyOCD runner.

#### Option 2: [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [Segger J-Link OpenSDA V2.1 Firmware](https://www.segger.com/downloads/jlink/OpenSDA_V2_1.bin). Note that Segger
does provide an OpenSDA J-Link Board-Specific Firmware for this board, however
it is not compatible with the DAPLink bootloader.

Add the arguments `-DBOARD_FLASH_RUNNER=jlink` and
`-DBOARD_DEBUG_RUNNER=jlink` when you invoke `west build` to override the
default runner from pyOCD to J-Link:

```shell
# From the root of the zephyr repository
west build -b frdm_k22f samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to J26.

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
west build -b frdm_k22f samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.0.0 *****
Hello World! frdm_k22f
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_k22f samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.0.0 *****
Hello World! frdm_k22f
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
