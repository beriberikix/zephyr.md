---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/segger/ip_k66f/doc/index.html
original_path: boards/segger/ip_k66f/doc/index.html
---

# IP Switch Board

Board Overview

[![../../../../_images/ip_k66f.jpg](../../../../_images/ip_k66f.jpg)
](../../../../_images/ip_k66f.jpg)

IP Switch Board

Name:
:   `ip_k66f`

Vendor:
:   SEGGER Microcontroller GmbH

Architecture:
:   arm

SoC:
:   mk66f18

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/segger/ip_k66f/doc/index.rst/../..)

## Overview

The Segger IP Switch Board is a Evaluation board based on NXP Kinetis K66 MCU.
It comes with Micrel/Microchip KSZ8794CNX integrated 4-port 10/100 managed
Ethernet switch with Gigabit RGMII/MII/RMII interface.

- KSZ8794CNX enables evaluation for switch functions
- On-board debug probe J-Link-OB for programming

## Hardware

- MK66FN2M0VMD18 MCU (180 MHz, 2 MB flash memory, 256 KB RAM, low-power,
  crystal-less USB
- Dual role USB interface with micro-B USB connector
- 2 User LED
- On-board debug probe J-Link-OB for programming
- Micrel/Microchip Ethernet Switch KSZ8794CNX with 3 RJ45 connectors

For more information about the K66F SoC and IP-K66F board:

- [K66F Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/k-series-cortex-m4/k6x-ethernet/kinetis-k66-180-mhz-dual-high-speed-full-speed-usbs-2mb-flash-microcontrollers-mcus-based-on-arm-cortex-m4-core:K66_180)
- [K66F Datasheet](https://www.nxp.com/docs/en/data-sheet/K66P144M180SF5V2.pdf)
- [K66F Reference Manual](https://www.nxp.com/webapp/Download?colCode=K66P144M180SF5RMV2)
- [IP-K66F Website](https://www.segger.com/evaluate-our-software/segger/embosip-switch-board/)
- [IP-K66F User Guide](https://www.segger.com/downloads/emnet/UM06002)
- [IP-K66F Schematics](https://www.segger.com/downloads/emnet/embOSIP_SwitchBoard_V2.0_WEB_Schematic.pdf)

### Supported Features

The `ip_k66f` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ip_k66f/mk66f18` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Kinetis ADC16[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L424) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp%2Ckinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| CAN | on-chip | NXP FlexCAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L512) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L90) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L112) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L117) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L541) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L550) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DAC | on-chip | NXP Kinetis MCUX DAC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L450) | [`nxp,kinetis-dac`](../../../../build/dts/api/bindings/dac/nxp%2Ckinetis-dac.md#std-dtcompatible-nxp-kinetis-dac) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L522) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| DSA | on-board | KSZ8794 ethernet switch with SPI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/segger/ip_k66f/ip_k66f.dts?plain=1#L135) | [`microchip,ksz8794`](../../../../build/dts/api/bindings/dsa/microchip%2Cksz8794.md#std-dtcompatible-microchip-ksz8794) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L477) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L481) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/segger/ip_k66f/ip_k66f.dts?plain=1#L119) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L496) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module E (FTFE)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L146) | [`nxp,kinetis-ftfe`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ckinetis-ftfe.md#std-dtcompatible-nxp-kinetis-ftfe) |
| GPIO & Headers | on-chip | Kinetis GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L287)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L307) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | Kinetis I2C[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L164) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Ckinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/segger/ip_k66f/ip_k66f.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L490) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L156) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/segger/ip_k66f/ip_k66f.dts?plain=1#L70) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L257) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L76) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| RNG | on-chip | Kinetis RNGA (Random Number Generator Accelerator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L505) | [`nxp,kinetis-rnga`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-rnga.md#std-dtcompatible-nxp-kinetis-rnga) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L103) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Sensors | on-chip | NXP Kinetis temperature sensor[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L52) | [`nxp,kinetis-temperature`](../../../../build/dts/api/bindings/sensor/nxp%2Ckinetis-temperature.md#std-dtcompatible-nxp-kinetis-temperature) |
| Serial controller | on-chip | Kinetis UART[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L197) | [`nxp,kinetis-uart`](../../../../build/dts/api/bindings/serial/nxp%2Ckinetis-uart.md#std-dtcompatible-nxp-kinetis-uart) |
| on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k66.dtsi?plain=1#L16) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP DSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L351)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L337) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L47) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L388) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp%2Cftm.md#std-dtcompatible-nxp-ftm) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L468) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp%2Ckinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| Watchdog | on-chip | Kinetis watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_k6x.dtsi?plain=1#L381) | [`nxp,kinetis-wdog`](../../../../build/dts/api/bindings/watchdog/nxp%2Ckinetis-wdog.md#std-dtcompatible-nxp-kinetis-wdog) |

Micrel/Microchip KSZ8794CNX Ethernet Switch is supported
(see [DSA (Distributed Switch Architecture)](../../../../samples/net/dsa/README.md#dsa "Test and debug Distributed Switch Architecture") sample).

### Connections and IOs

The K66F SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| PTA8 | GPIO | Red LED |
| PTA10 | GPIO | RED LED |

### System Clock

The K66F SoC is configured to use the 12 MHz low gain crystal oscillator on the
board with the on-chip PLL to generate a 180 MHz system clock.

### Serial Port

The K66F SoC has six UARTs. None of them are used.

## Programming and Debugging

The `ip_k66f` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe).

#### [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [OpenSDA J-Link Generic Firmware for V3.2 Bootloader](https://www.segger.com/downloads/jlink/OpenSDA_V3_2). Note that Segger
does provide an OpenSDA J-Link Board-Specific Firmware for this board, however
it is not compatible with the DAPLink bootloader.

The default flasher is `jlink` using the built-in SEGGER Jlink interface.

### Flashing

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ip_k66f samples/basic/blinky
west flash
```

Red LED0 should blink at 1 second delay.

### Debugging

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ip_k66f samples/basic/blinky
west debug
```

Step through the application in your debugger.

### Serial console

The `ip_k66f` board only uses Segger’s RTT console for providing serial
console. There is no physical serial port available.

- To communicate with this board one needs in one console:

`/opt/SEGGER/JLink_V664/JLinkRTTLogger -Device MK66FN2M0XXX18 -RTTChannel 1 -if SWD -Speed 4000 ~/rtt.log`

- In another one:

`nc localhost 19021`
