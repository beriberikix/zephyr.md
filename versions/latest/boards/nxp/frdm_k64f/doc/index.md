---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_k64f/doc/index.html
original_path: boards/nxp/frdm_k64f/doc/index.html
---

# FRDM-K64F

Board Overview

[![../../../../_images/frdm_k64f.jpg](../../../../_images/frdm_k64f.jpg)
](../../../../_images/frdm_k64f.jpg)

FRDM-K64F

Name:
:   `frdm_k64f`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mk64f12

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_k64f/doc/index.rst/../..)

## Overview

The Freedom-K64F is an ultra-low-cost development platform for Kinetis K64,
K63, and K24 MCUs.

- Form-factor compatible with the Arduino R3 pin layout
- Peripherals enable rapid prototyping, including a 6-axis digital
  accelerometer and magnetometer to create full eCompass capabilities, a
  tri-colored LED and 2 user push-buttons for direct interaction, a microSD
  card slot, and connectivity using onboard Ethernet port and headers for use
  with Bluetooth\* and 2.4 GHz radio add-on modules
- OpenSDAv2, the NXP open source hardware embedded serial and debug adapter
  running an open source bootloader, offers options for serial communication,
  flash programming, and run-control debugging

## Hardware

- MK64FN1M0VLL12 MCU (120 MHz, 1 MB flash memory, 256 KB RAM, low-power,
  crystal-less USB, and 100 Low profile Quad Flat Package (LQFP))
- Dual role USB interface with micro-B USB connector
- RGB LED
- FXOS8700CQ accelerometer and magnetometer
- Two user push buttons
- Flexible power supply option - OpenSDAv2 USB, Kinetis K64 USB, and external source
- Easy access to MCU input/output through Arduino\* R3 compatible I/O connectors
- Programmable OpenSDAv2 debug circuit supporting the CMSIS-DAP Interface
  software that provides:

  - Mass storage device (MSD) flash programming interface
  - CMSIS-DAP debug interface over a driver-less USB HID connection providing
    run-control debugging and compatibility with IDE tools
  - Virtual serial port interface
  - Open source CMSIS-DAP software project
- Ethernet
- SDHC

For more information about the K64F SoC and FRDM-K64F board:

- [K64F Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/k-seriesperformancem4/k6x-ethernet/kinetis-k64-120-mhz-256kb-sram-microcontrollers-mcus-based-on-arm-cortex-m4-core:K64_120)
- [K64F Datasheet](https://www.nxp.com/docs/en/data-sheet/K64P144M120SF5.pdf)
- [K64F Reference Manual](https://www.nxp.com/docs/en/reference-manual/K64P144M120SF5RM.pdf)
- [FRDM-K64F Website](https://www.nxp.com/support/developer-resources/evaluation-and-development-boards/freedom-development-boards/mcu-boards/freedom-development-platform-for-kinetis-k64-k63-and-k24-mcus:FRDM-K64F)
- [FRDM-K64F User Guide](https://www.nxp.com/webapp/Download?colCode=FRDMK64FUG)
- [FRDM-K64F Schematics](https://www.nxp.com/webapp/Download?colCode=FRDM-K64F-SCH-E4)

### Supported Features

NXP considers the FRDM-K64F as the superset board for the Kinetis K
series of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire Kinetis K series. NXP prioritizes enabling
this board with new support for Zephyr features.

The `frdm_k64f` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_k64f/mk64f12` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Kinetis ADC16[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L424) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp%2Ckinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| CAN | on-chip | NXP FlexCAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L512) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L90) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L112) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L117) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L541) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L550) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DAC | on-chip | NXP Kinetis MCUX DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L450)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L459) | [`nxp,kinetis-dac`](../../../../build/dts/api/bindings/dac/nxp%2Ckinetis-dac.md#std-dtcompatible-nxp-kinetis-dac) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L522) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L477) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L481) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L274) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/phy/microchip%2Cksz8081.md#std-dtcompatible-microchip-ksz8081) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L496) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module E (FTFE)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L146) | [`nxp,kinetis-ftfe`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ckinetis-ftfe.md#std-dtcompatible-nxp-kinetis-ftfe) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L287) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L65) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Kinetis I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L164)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L175) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Ckinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L51) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L35) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L490) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L156) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L231) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L257) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L76) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP FlexTimer Module (FTM) PWM controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L388) | [`nxp,ftm-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cftm-pwm.md#std-dtcompatible-nxp-ftm-pwm) |
| RNG | on-chip | Kinetis RNGA (Random Number Generator Accelerator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L505) | [`nxp,kinetis-rnga`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-rnga.md#std-dtcompatible-nxp-kinetis-rnga) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L103) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_k64f/frdm_k64f.dts?plain=1#L140) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700) |
| on-chip | NXP Kinetis temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L63)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L52) | [`nxp,kinetis-temperature`](../../../../build/dts/api/bindings/sensor/nxp%2Ckinetis-temperature.md#std-dtcompatible-nxp-kinetis-temperature) |
| Serial controller | on-chip | Kinetis UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L197)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L207) | [`nxp,kinetis-uart`](../../../../build/dts/api/bindings/serial/nxp%2Ckinetis-uart.md#std-dtcompatible-nxp-kinetis-uart) |
| SPI | on-chip | NXP DSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L337)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L366) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L47) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L397) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp%2Cftm.md#std-dtcompatible-nxp-ftm) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L468) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp%2Ckinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| Watchdog | on-chip | Kinetis watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L381) | [`nxp,kinetis-wdog`](../../../../build/dts/api/bindings/watchdog/nxp%2Ckinetis-wdog.md#std-dtcompatible-nxp-kinetis-wdog) |

### Connections and IOs

The K64F SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| PTB22 | GPIO | Red LED |
| PTE26 | GPIO | Green LED |
| PTB21 | GPIO | Blue LED |
| PTC6 | GPIO | SW2 / FXOS8700 INT1 |
| PTC13 | GPIO | FXOS8700 INT2 |
| PTA4 | GPIO | SW3 |
| PTB10 | ADC | ADC1 channel 14 |
| PTB16 | UART0\_RX | UART Console |
| PTB17 | UART0\_TX | UART Console |
| PTB18 | CAN0\_TX | CAN TX |
| PTB19 | CAN0\_RX | CAN RX |
| PTC8 | PWM | PWM\_3 channel 4 |
| PTC9 | PWM | PWM\_3 channel 5 |
| PTC16 | UART3\_RX | UART BT HCI |
| PTC17 | UART3\_TX | UART BT HCI |
| PTD0 | SPI0\_PCS0 | SPI |
| PTD1 | SPI0\_SCK | SPI |
| PTD2 | SPI0\_SOUT | SPI |
| PTD3 | SPI0\_SIN | SPI |
| PTE24 | I2C0\_SCL | I2C / FXOS8700 |
| PTE25 | I2C0\_SDA | I2C / FXOS8700 |
| PTA5 | MII0\_RXER | Ethernet |
| PTA12 | MII0\_RXD1 | Ethernet |
| PTA13 | MII0\_RXD0 | Ethernet |
| PTA14 | MII0\_RXDV | Ethernet |
| PTA15 | MII0\_TXEN | Ethernet |
| PTA16 | MII0\_TXD0 | Ethernet |
| PTA17 | MII0\_TXD1 | Ethernet |
| PTA28 | MII0\_TXER | Ethernet |
| PTB0 | MII0\_MDIO | Ethernet |
| PTB1 | MII0\_MDC | Ethernet |
| PTC16 | ENET0\_1588\_TMR0 | Ethernet |
| PTC17 | ENET0\_1588\_TMR1 | Ethernet |
| PTC18 | ENET0\_1588\_TMR2 | Ethernet |
| PTC19 | ENET0\_1588\_TMR3 | Ethernet |

Note

Do not enable Ethernet and UART BT HCI simultaneously because they conflict
on PTC16-17.

### System Clock

The K64F SoC is configured to use the 50 MHz external oscillator on the board
with the on-chip PLL to generate a 120 MHz system clock.

### Serial Port

The K64F SoC has six UARTs. One is configured for the console, another for BT
HCI, and the remaining are not used.

### USB

The K64F SoC has a USB OTG (USBOTG) controller that supports both
device and host functions through its micro USB connector (K64F USB).
Only USB device function is supported in Zephyr at the moment.

### CAN

The FRDM-K64F board does not come with an onboard CAN transceiver. In order to
use the CAN bus, an external CAN bus transceiver must be connected to `PTB18`
(`CAN0_TX`) and `PTB19` (`CAN0_RX`).

## Programming and Debugging

The `frdm_k64f` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **canopen** | ✅ |  |  |  |  |
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

OpenSDA DAPLink Onboard (Recommended)OpenSDA JLink Onboard

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

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

The version of J-Link firmware to program to the board depends on the version
of the DAPLink bootloader. Refer to [OpenSDA Serial and Debug Adapter](https://www.nxp.com/design/microcontrollers-developer-resources/ides-for-kinetis-mcus/opensda-serial-and-debug-adapter:OPENSDA#FRDM-K64F) for
more details. On this page, change the pull-down menu for “Choose your board to
start” to FRDM-K64F, and review the section “To update your board with OpenSDA
applications”. Note that Segger does provide an OpenSDA J-Link Board-Specific
Firmware for this board, however it is not compatible with the DAPLink
bootloader. After downloading the appropriate J-Link firmware, follow the
instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program to the
board.

Add the arguments `-DBOARD_FLASH_RUNNER=jlink` and
`-DBOARD_DEBUG_RUNNER=jlink` when you invoke `west build` to override the
default runner to J-Link:

```shell
# From the root of the zephyr repository
west build -b frdm_k64f samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
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
west build -b frdm_k64f samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_k64f
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_k64f samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_k64f
```

### Troubleshooting

If pyocd raises an uncaught `DAPAccessIntf.TransferFaultError()` exception
when you try to flash or debug, it’s possible that the K64F flash may have been
locked by a corrupt application. You can unlock it with the following sequence
of pyocd commands:

```shell
$ pyocd cmd
0001915:WARNING:target_kinetis:Forcing halt on connect in order to gain control of device
Connected to K64F [Halted]: 0240000026334e450028400d5e0e000e4eb1000097969900
>>> unlock
0016178:WARNING:target_kinetis:K64F secure state: unlocked successfully
>>> reinit
0034584:WARNING:target_kinetis:Forcing halt on connect in order to gain control of device
>>> load build/zephyr/zephyr.bin
[====================] 100%
>>> reset
Resetting target
>>> quit
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
