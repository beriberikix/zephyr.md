---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/rddrone_fmuk66/doc/index.html
original_path: boards/nxp/rddrone_fmuk66/doc/index.html
---

# RDDRONE-FMUK66

Board Overview

[![../../../../_images/rddrone_fmuk66.jpg](https://docs.zephyrproject.org/4.2.0/_images/rddrone_fmuk66.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/rddrone_fmuk66.jpg)

RDDRONE-FMUK66

Name:
:   `rddrone_fmuk66`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mk66f18

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/rddrone_fmuk66/doc/index.rst/../..)

## Overview

The RDDRONE FMUK66 is an drone control board with commonly used peripheral
connectors and a Kinetis K66 on board.

- Comes with a J-Link Edu Mini for programming and UART console.

## Hardware

- MK66FN2MOVLQ18 MCU (180 MHz, 2 MB flash memory, 256 KB RAM, low-power,
  crystal-less USB, and 144 Low profile Quad Flat Package (LQFP))
- Dual role USB interface with micro-B USB connector
- RGB LED
- FXOS8700CQ accelerometer and magnetometer
- FXAS21002CQ gyro
- BMM150 magnetometer
- ML3114A2 barometer
- BMP280 barometer
- Connector for PWM servo/motor controls
- Connector for UART GPS/GLONASS
- SDHC

For more information about the K64F SoC and FRDM-K64F board:

- [K66F Website](#k66f-website)
- [K66F Datasheet](#k66f-datasheet)
- [K66F Reference Manual](#k66f-reference-manual)
- [RDDRONE-FMUK66 Website](#rddrone-fmuk66-website)
- [RDDRONE-FMUK66 User Guide](#rddrone-fmuk66-user-guide)
- [RDDRONE-FMUK66 Schematics](#rddrone-fmuk66-schematics)

### Supported Features

The `rddrone_fmuk66` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rddrone_fmuk66/mk66f18` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Kinetis ADC16[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L424) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp,kinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| CAN | on-chip | NXP FlexCAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L512) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L90) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp,kinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L112) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp,kinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L117) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L541) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L550) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DAC | on-chip | NXP Kinetis MCUX DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L450)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L459) | [`nxp,kinetis-dac`](../../../../build/dts/api/bindings/dac/nxp,kinetis-dac.md#std-dtcompatible-nxp-kinetis-dac) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L522) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L477) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L481) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L276) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L496) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module E (FTFE)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L146) | [`nxp,kinetis-ftfe`](../../../../build/dts/api/bindings/flash_controller/nxp,kinetis-ftfe.md#std-dtcompatible-nxp-kinetis-ftfe) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L287) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | Kinetis I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L164)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L186) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp,kinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L48) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L60) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L490) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L156) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L234) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-board | Simple GPIO controlled CAN transceiver[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L74) | [`can-transceiver-gpio`](../../../../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L257) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L76) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP FlexTimer Module (FTM) PWM controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L388) | [`nxp,ftm-pwm`](../../../../build/dts/api/bindings/pwm/nxp,ftm-pwm.md#std-dtcompatible-nxp-ftm-pwm) |
| Regulator | on-board | Fixed voltage regulators[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L89) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | Kinetis RNGA (Random Number Generator Accelerator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L505) | [`nxp,kinetis-rnga`](../../../../build/dts/api/bindings/rng/nxp,kinetis-rnga.md#std-dtcompatible-nxp-kinetis-rnga) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L103) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp,rtc.md#std-dtcompatible-nxp-rtc) |
| Sensors | on-board | BME280 integrated environmental sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L317) | [`bosch,bme280`](../../../../build/dts/api/compatibles/bosch,bme280.md#std-dtcompatible-bosch-bme280) |
| on-board | Bosch BMM150 Geomagnetic sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L323) | [`bosch,bmm150`](../../../../build/dts/api/compatibles/bosch,bmm150.md#std-dtcompatible-bosch-bmm150) |
| on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L352) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp,fxos8700.md#std-dtcompatible-nxp-fxos8700) |
| on-board | FXAS21002 3-axis gyroscope sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rddrone_fmuk66/rddrone_fmuk66.dts?plain=1#L362) | [`nxp,fxas21002`](../../../../build/dts/api/compatibles/nxp,fxas21002.md#std-dtcompatible-nxp-fxas21002) |
| on-chip | NXP Kinetis temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L63)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L52) | [`nxp,kinetis-temperature`](../../../../build/dts/api/bindings/sensor/nxp,kinetis-temperature.md#std-dtcompatible-nxp-kinetis-temperature) |
| Serial controller | on-chip | Kinetis UART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L197)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L227) | [`nxp,kinetis-uart`](../../../../build/dts/api/bindings/serial/nxp,kinetis-uart.md#std-dtcompatible-nxp-kinetis-uart) |
| on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k66.dtsi?plain=1#L16) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP DSPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L337) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp,dspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L47) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L397) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp,ftm.md#std-dtcompatible-nxp-ftm) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L468) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp,kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| Watchdog | on-chip | Kinetis watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L381) | [`nxp,kinetis-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,kinetis-wdog.md#std-dtcompatible-nxp-kinetis-wdog) |

### System Clock

The K66F SoC is configured to use the 16 MHz external oscillator on the board
with the on-chip PLL to generate a 160 MHz system clock.

### Serial Port

The K66F SoC has six UARTs. LPUART0 is configured for the console, UART0 is labeled Serial 2,
UART2 is labeled GPS, UART4 is labeled Serial 1. Any of these UARTs may be used as the console by
overlaying the board device tree.

### USB

The K66F SoC has a USB OTG (USBOTG) controller that supports both
device and host functions through its micro USB connector (K66F USB).
Only USB device function is supported in Zephyr at the moment.

## Programming and Debugging

The `rddrone_fmuk66` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use jlink. The board package
with accessories comes with a jlink mini edu and cable specifically for this board
along with a usb to uart that connects directly to the jlink mini edu. This is the expected
default configuration for programming and getting a console.

```shell
# From the root of the zephyr repository
west build -b rddrone-fmuk66 samples/hello_world
```

### Configuring a Console

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
west build -b rddrone-fmuk66 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.7.0 *****
Hello World! rddrone-fmuk66
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rddrone-fmuk66 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.7.0 *****
Hello World! rddrone-fmuk66
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

[https://www.nxp.com/design/designs/px4-robotic-drone-vehicle-flight-management-unit-vmu-fmu-rddrone-fmuk66:RDDRONE-FMUK66](https://www.nxp.com/design/designs/px4-robotic-drone-vehicle-flight-management-unit-vmu-fmu-rddrone-fmuk66:RDDRONE-FMUK66)

[https://nxp.gitbook.io/hovergames/userguide/getting-started](https://nxp.gitbook.io/hovergames/userguide/getting-started)

[https://www.nxp.com/webapp/Download?colCode=SPF-39053](https://www.nxp.com/webapp/Download?colCode=SPF-39053)

[https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/k-series-cortex-m4/k6x-ethernet/kinetis-k66-180-mhz-dual-high-speed-full-speed-usbs-2mb-flash-microcontrollers-mcus-based-on-arm-cortex-m4-core:K66\_180](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/k-series-cortex-m4/k6x-ethernet/kinetis-k66-180-mhz-dual-high-speed-full-speed-usbs-2mb-flash-microcontrollers-mcus-based-on-arm-cortex-m4-core:K66_180)

[https://www.nxp.com/docs/en/data-sheet/K66P144M180SF5V2.pdf](https://www.nxp.com/docs/en/data-sheet/K66P144M180SF5V2.pdf)

[https://www.nxp.com/webapp/Download?colCode=K66P144M180SF5RMV2](https://www.nxp.com/webapp/Download?colCode=K66P144M180SF5RMV2)
