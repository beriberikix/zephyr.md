---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm32n6570_dk/doc/index.html
original_path: boards/st/stm32n6570_dk/doc/index.html
---

# STM32N6570-DK

Board Overview

[![../../../../_images/stm32n6570_dk.webp](https://docs.zephyrproject.org/4.2.0/_images/stm32n6570_dk.webp)
](https://docs.zephyrproject.org/4.2.0/_images/stm32n6570_dk.webp)

STM32N6570-DK

Name:
:   `stm32n6570_dk`

Vendor:
:   STMicroelectronics

Architecture:

SoC:
:   stm32n657xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32n6570_dk/doc/index.rst/../..)

## Overview

The STM32N6570\_DK Discovery kit is a complete demonstration and development platform
for the Arm® Cortex®‑M55 core‑based STM32N657X0H3Q microcontroller.

The STM32N6570\_DK Discovery kit includes a full range of hardware features that help
the user evaluate many peripherals, such as USB Type-C®, Octo‑SPI flash memory and
Hexadeca‑SPI PSRAM devices, Ethernet, camera module, LCD, microSD™, audio codec,
digital microphones, ADC, flexible extension connectors, and user button.
The four flexible extension connectors feature easy and unlimited expansion capabilities
for specific applications such as wireless connectivity, analog applications, and sensors.

The STM32N657X0H3Q microcontroller features one USB 2.0 high‑speed/full‑speed
Device/Host/OTG controller, one USB 2.0 high‑speed/full‑speed Device/Host/OTG controller
with UCPD (USB Type-C® Power Delivery), one Ethernet with TSN (time-sensitive networking),
four I2Cs, two I3Cs, six SPIs (of which four I2S‑capable), two SAIs, with four DMIC support,
five USARTs, five UARTs (ISO78916 interface, LIN, IrDA, up to 12.5 Mbit/s), one LPUART,
two SDMMCs (MMC version 4.0, CE-ATA version 1.0, and SD version 1.0.1), three CAN FD
with TTCAN capability, JTAG and SWD debugging support, and Embedded Trace Macrocell™ (ETM).

The STM32N6570\_DK Discovery kit integrates an STLINK-V3EC embedded in-circuit debugger and
programmer for the STM32 MCU, with a USB Virtual COM port bridge and the comprehensive MCU Package.

## Hardware

- STM32N657X0H3Q Arm® Cortex®‑M55‑based microcontroller featuring ST Neural-ART Accelerator,
  H264 encoder, NeoChrom 2.5D GPU, and 4.2 Mbytes of contiguous SRAM, in a VFBGA264 package
- 5” LCD module with capacitive touch panel
- USB Type-C® with USB 2.0 HS interface, dual‑role‑power (DRP)
- USB Type-A with USB 2.0 HS interface, host, 0.5 A max
- 1‑Gbit Ethernet with TSN (time-sensitive networking) compliant with IEEE‑802.3‑2002
- SAI audio codec
- One MEMS digital microphone
- 1‑Gbit Octo‑SPI flash memory
- 256-Mbit Hexadeca‑SPI PSRAM
- Two user LEDs
- User, tamper, and reset push-buttons
- Board connectors:

  - USB Type-C®
  - USB Type-A
  - Ethernet RJ45
  - Camera module
  - microSD™ card
  - LCD
  - Stereo headset jack including analog microphone input
  - Audio MEMS daughterboard expansion connector
  - ARDUINO® Uno R3 expansion connector
  - STMod+ expansion connector
- On-board STLINK-V3EC debugger/programmer with USB re-enumeration capability:
  Virtual COM port, and debug port

For more details, please refer to:

- [STM32N6570\_DK website](https://www.st.com/en/evaluation-tools/stm32n6570-dk.html)
- [STM32N657X0 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32n657x0.html)
- [STM32N657 reference manual](https://www.st.com/resource/en/reference_manual/rm0486-stm32n647657xx-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `stm32n6570_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32n6570_dk/stm32n657xx/sb` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L26) | [`arm,cortex-m55`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m55.md#std-dtcompatible-arm-cortex-m55) |
| ADC | on-chip | STM32N6 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L431)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L447) | [`st,stm32n6-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32n6-adc.md#std-dtcompatible-st-stm32n6-adc) |
| CAN | on-chip | STM32H7 series FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L463)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L474) | [`st,stm32h7-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32h7-fdcan.md#std-dtcompatible-st-stm32h7-fdcan) |
| Clock control | on-chip | STM32N6 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L235) | [`st,stm32n6-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32n6-rcc.md#std-dtcompatible-st-stm32n6-rcc) |
| on-chip | STM32N6 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L49) | [`st,stm32n6-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32n6-hse-clock.md#std-dtcompatible-st-stm32n6-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L55) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L62) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L70) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32N6 main PLL[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L77) | [`st,stm32n6-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32n6-pll-clock.md#std-dtcompatible-st-stm32n6-pll-clock) |
| on-chip | STM32N6 CPU Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L101) | [`st,stm32n6-cpu-clock-mux`](../../../../build/dts/api/bindings/clock/st%2Cstm32n6-cpu-clock-mux.md#std-dtcompatible-st-stm32n6-cpu-clock-mux) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L107) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| on-chip | STM32N6 Divider IC multiplexer[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L113)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L137) | [`st,stm32n6-ic-clock-mux`](../../../../build/dts/api/bindings/clock/st%2Cstm32n6-ic-clock-mux.md#std-dtcompatible-st-stm32n6-ic-clock-mux) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L845) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st%2Cstm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32U5 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L694) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st%2Cstm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Ethernet | on-chip | STM32 Ethernet Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L756) | [`st,stm32-ethernet-controller`](../../../../build/dts/api/bindings/ethernet/st%2Cstm32-ethernet-controller.md#std-dtcompatible-st-stm32-ethernet-controller) |
| on-chip | ST STM32N6 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L762) | [`st,stm32n6-ethernet`](../../../../build/dts/api/bindings/ethernet/st%2Cstm32n6-ethernet.md#std-dtcompatible-st-stm32n6-ethernet) |
| on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32n6570_dk/stm32n6570_dk_common.dtsi?plain=1#L403) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek%2Crtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| Flash controller | on-board | STM32 XSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32n6570_dk/stm32n6570_dk_common.dtsi?plain=1#L327) | [`st,stm32-xspi-nor`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-xspi-nor.md#std-dtcompatible-st-stm32-xspi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L334) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32n6570_dk/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on the Raspberry Pi CSI Camera connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32n6570_dk/stm32n6570_dk_common.dtsi?plain=1#L62) | [`raspberrypi,csi-connector`](../../../../build/dts/api/bindings/gpio/raspberrypi%2Ccsi-connector.md#std-dtcompatible-raspberrypi-csi-connector) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L586)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L610) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | GT9xx / GT9xxx capacitive touch panels[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32n6570_dk/stm32n6570_dk_common.dtsi?plain=1#L80) | [`goodix,gt911`](../../../../build/dts/api/bindings/input/goodix%2Cgt911.md#std-dtcompatible-goodix-gt911) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L307) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32n6570_dk/stm32n6570_dk_common.dtsi?plain=1#L48) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L772) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st%2Cstm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-board | STM32 XSPI PSRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32n6570_dk/stm32n6570_dk_common.dtsi?plain=1#L302) | [`st,stm32-xspi-psram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-xspi-psram.md#std-dtcompatible-st-stm32-xspi-psram) |
| Miscellaneous | on-chip | STM32 SRAM configuration controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L247) | [`st,stm32n6-ramcfg`](../../../../build/dts/api/bindings/misc/st%2Cstm32n6-ramcfg.md#std-dtcompatible-st-stm32n6-ramcfg) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L789)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L780) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv8.1-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L33) | [`arm,armv8.1m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu) |
| MTD | on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32n6570_dk/stm32n6570_dk_common.dtsi?plain=1#L337) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | STM32 USB HS PHY controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L838) | [`st,stm32-usbphyc`](../../../../build/dts/api/bindings/phy/st%2Cstm32-usbphyc.md#std-dtcompatible-st-stm32-usbphyc) |
| Pin control | on-chip | STM32 pin controller with “I/O synchronization”[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L328) | [`st,stm32n6-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32n6-pinctrl.md#std-dtcompatible-st-stm32n6-pinctrl) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L241) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L496)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L514) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L674)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L634) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L40) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |
| USB | on-chip | STM32N6 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L824) | [`st,stm32n6-otghs`](../../../../build/dts/api/bindings/usb/st%2Cstm32n6-otghs.md#std-dtcompatible-st-stm32n6-otghs) |
| Video | on-chip | STM32 Digital Camera Memory Interface Pixel Processor (DCMIPP)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L707) | [`st,stm32-dcmipp`](../../../../build/dts/api/bindings/video/st%2Cstm32-dcmipp.md#std-dtcompatible-st-stm32-dcmipp) |
| xSPI | on-chip | STM32 XSPI Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L798) | [`st,stm32-xspi`](../../../../build/dts/api/bindings/xspi/st%2Cstm32-xspi.md#std-dtcompatible-st-stm32-xspi) |

### USB

The USB pin assignments on the STM32N657XX microcontroller are immutable. This means that the specific
pins designated for USB functionality are fixed and cannot be changed or reassigned to other functions,
ensuring consistent and reliable USB communication.

### USB PIN (IOs)

| Name | Description |
| --- | --- |
| OTG1\_HSDM | USB OTG1 High-Speed Data- (negative) |
| OTG1\_HSDP | USB OTG1 High-Speed Data+ (positive) |
| OTG1\_ID | USB OTG1 ID Pin |
| OTG1\_TXRTUNE | USB OTG1 Transmit Retune |
| OTG2\_HSDM | USB OTG2 High-Speed Data- (negative) |
| OTG2\_HSDP | USB OTG2 High-Speed Data+ (positive) |
| OTG2\_ID | USB OTG2 ID Pin |
| OTG2\_TXRTUNE | USB OTG2 Transmit Retune |

### Connections and IOs

STM32N6570\_DK Board has 12 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to [STM32N6570\_DK User Manual](https://www.st.com/resource/en/user_manual/um3300-discovery-kit-with-stm32n657x0-mcu-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- ADC1\_INP10 : PA9
- ADC1\_INP11 : PA10
- FDCAN1\_TX : PH2
- FDCAN1\_RX : PD0
- I2C1\_SCL : PH9
- I2C1\_SDA : PC1
- I2C4\_SCL : PE13
- I2C4\_SDA : PE14
- LD1 : PO1
- LD2 : PG10
- SDMMC2\_CK : PC2
- SDMMC2\_CMD : PC3
- SDMMC2\_D0 : PC4
- SDMMC2\_D1 : PC5
- SDMMC2\_D2 : PC0
- SDMMC2\_D3 : PE4
- SPI5\_SCK : PE15
- SPI5\_MOSI : PG2
- SPI5\_MISO : PH8
- SPI5\_NSS : PA3
- USART\_1\_TX : PE5
- USART\_1\_RX : PE6
- USART\_2\_TX : PD5
- USART\_2\_RX : PF6
- XSPI1\_NCS1 : PO0
- XSPI1\_DQS0 : PO2
- XSPI1\_DQS1 : PO3
- XSPI1\_CLK : PO4
- XSPI1\_IO0 : PP0
- XSPI1\_IO1 : PP1
- XSPI1\_IO2 : PP2
- XSPI1\_IO3 : PP3
- XSPI1\_IO4 : PP4
- XSPI1\_IO5 : PP5
- XSPI1\_IO6 : PP6
- XSPI1\_IO7 : PP7
- XSPI1\_IO8 : PP8
- XSPI1\_IO9 : PP9
- XSPI1\_IO10 : PP10
- XSPI1\_IO11 : PP11
- XSPI1\_IO12 : PP12
- XSPI1\_IO13 : PP13
- XSPI1\_IO14 : PP14
- XSPI1\_IO15 : PP15
- XSPI2\_NCS1 : PN1
- XSPI2\_DQS0 : PN0
- XSPI2\_CLK : PN6
- XSPI2\_IO0 : PN2
- XSPI2\_IO1 : PN3
- XSPI2\_IO2 : PN4
- XSPI2\_IO3 : PN5
- XSPI2\_IO4 : PN8
- XSPI2\_IO5 : PN9
- XSPI2\_IO6 : PN10
- XSPI2\_IO7 : PN11

#### System Clock

STM32N6570\_DK System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
400MHz, driven by 64MHz high speed internal oscillator.

#### Serial Port

STM32N6570\_DK board has 10 U(S)ARTs. The Zephyr console output is assigned to
USART1. Default settings are 115200 8N1.

## Board variants

Three variants are available with STM32N6570\_DK:

- Default variant. Available as a chainloaded application which should be loaded by a
  bootloader, it has access to the whole AXISRAM1 and AXISRAM2 regions. It is expected to
  be built using `--sysbuild` option exclusively.
- `fsbl`: First Stage Boot Loader (FSBL) which is available as an application loaded by the
  Boot ROM and flashed using ST-Link. This is typically a bootloader image. It runs
  in RAM LOAD mode on second half of AXISRAM2. 511K are available for the whole image.
- `sb`: First Stage Boot Loader - Serial Boot. Equivalent to the FSBL image, but could be
  loaded using USB and doesn’t require switching the bootpins. This is the most practical
  for developments steps.

## Programming and Debugging

The `stm32n6570_dk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** |
| --- | --- | --- | --- | --- |
| **[stlink\_gdbserver](../../../../develop/flash_debug/host-tools.md#runner-stlink-gdbserver)** |  | ✅ (default) | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |

STM32N6570\_DK board includes an ST-LINK/V3 embedded debug tool interface.
This probe allows to flash and debug the board using various tools.

### Flashing or loading

The board is configured to be programmed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is needed.
Version 2.18.0 or later of [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) is required.

Note

Firmware is run in secure mode of execution, which requires a signature.
After build, the build system will automatically generate a signed version of the
binary using [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) utility `STM32_SigningTool_CLI`.
This utility is installed along with [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html), but make sure it is
available in your `PATH` variable.

To program the board, there are two options:

- Program the firmware in external flash. At boot, it will then be loaded on RAM
  and executed from there.
- Optionally, it can also be taken advantage from the serial boot interface provided
  by the boot ROM. In that case, firmware is directly loaded in RAM and executed from
  there. It is not retained.

#### Programming an application to STM32N6570\_DK

Here is an example to build and run [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, connect the STM32N6570\_DK to your host computer using the ST-Link USB port.

> Application imageFSBL - ST-LinkFSBL - Serial Boot Loader (USB)
>
> Build and flash an application loaded by MCUBoot.
>
> ```shell
> # From the root of the zephyr repository
> west build -b stm32n6570_dk --sysbuild samples/hello_world
> west flash
> ```
>
> By default, application runs in XIP mode. Add `-DSB_CONFIG_MCUBOOT_MODE_RAM_LOAD=y`
> to use RAMLOAD mode.
>
> Build and flash an application using `stm32n6570_dk/stm32n657xx/fsbl` target.
>
> ```shell
> # From the root of the zephyr repository
> west build -b stm32n6570_dk//fsbl samples/hello_world
> west flash
> ```
>
> Note
>
> For flashing, before powering the board, set the boot pins in the following configuration:
>
> - BOOT0: 0
> - BOOT1: 1
>
> After flashing, to run the application, set the boot pins in the following configuration:
>
> - BOOT1: 0
>
> Power off and on the board again.
>
> Additionally, connect the STM32N6570\_DK to your host computer using the USB port.
> In this configuration, ST-Link is used to power the board and for serial communication
> over the Virtual COM Port.
>
> Note
>
> Before powering the board, set the boot pins in the following configuration:
>
> - BOOT0: 1
> - BOOT1: 0
>
> Build and load an application using `stm32n6570_dk/stm32n657xx/sb` target (you
> can also use the shortened form: `stm32n6570_dk//sb`)
>
> ```shell
> # From the root of the zephyr repository
> west build -b stm32n6570_dk//sb samples/hello_world
> west flash
> ```

Run a serial host program to connect with your Disco board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! stm32n6570_dk/stm32n657xx
```

### Debugging

You can debug an application in the usual way using the [ST-LINK GDB Server](../../../../develop/flash_debug/host-tools.md#runner-stlink-gdbserver).
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32n6570_dk samples/hello_world
west debug
```

Note

To enable debugging, before powering on the board, set the boot pins in the following configuration:

- BOOT0: 0
- BOOT1: 1

Another solution for debugging is to use STM32CubeIDE:

- Go to File ‣ Import and select C/C++ ‣ STM32 Cortex-M Executable.
- In the Executable field, browse to your `<ZEPHYR_PATH>/build/zephyr/zephyr.elf`.
- In MCU field, select `STM32N657X0HxQ`.
- Click on Finish.
- Finally, click on Debug to start the debugging session.

### Running tests with twister

Due to the BOOT switches manipulation required when flashing the board using `stm32n6570_dk`
board target, it is only possible to run twister tests campaign on `stm32n6570_dk/stm32n657xx/sb`
board target which doesn’t require BOOT pins changes to load and execute binaries.
To do so, it is advised to use Twister’s hardware map feature with the following settings:

```yaml
- platform: stm32n6570_dk/stm32n657xx/sb
  product: BOOT-SERIAL
  pre_script: <path_to_zephyr>/boards/st/common/scripts/board_power_reset.sh
  runner: stm32cubeprogrammer
```
