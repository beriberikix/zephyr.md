---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/oct/osd32mp1_brk/doc/osd32mp1_brk.html
original_path: boards/oct/osd32mp1_brk/doc/osd32mp1_brk.html
---

# OSD32MP1-BRK

Board Overview

[![../../../../_images/osd32mp1_brk.webp](../../../../_images/osd32mp1_brk.webp)
](../../../../_images/osd32mp1_brk.webp)

OSD32MP1-BRK

Name:
:   `osd32mp1_brk`

Vendor:
:   Octavo Systems LLC

Architecture:
:   arm

SoC:
:   osd32mp15x

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/oct/osd32mp1_brk/doc/osd32mp1_brk.rst/../..)

## Overview

The OSD32MP1-BRK development board by Octavo Systems integrates the OSD32MP15x
System-in-Package (SiP), which contains a multicore STM32MP157F microprocessor.
Zephyr OS is ported to run on the Cortex®-M4 core of the STM32MP157F.

- Common features:

  - OSD32MP15x SiP:

    - STM32MP15x microprocessor:

      - Dual-core Arm® Cortex®-A7 up to 800 MHz, 32 bits
      - Cortex®-M4 up to 209 MHz, 32 bits
      - Embedded SRAM (448 Kbytes) for Cortex®-M4.
    - 512MB DDR3 memory
    - STPMIC1A Power Management
    - Integrated 4kB EEPROM
    - MEMS oscillator
    - Over 100 passive components
  - Small form factor:

    - Dimensions: 75 mm x 46 mm (3 in x 1.8 in)
    - Breadboard-compatible with access to 106 I/Os via two 2x30 100-mil headers
  - Built-in features:

    - μUSB
    - ST-Link header
    - UART
    - μSD card slot
    - 32 kHz crystal
    - User LEDs and reset button
    - 4 Layer Design
    - No Back Side Components

For a detailed list of features, visit the [OSD32MP1-BRK product page](https://octavosystems.com/octavo_products/osd32mp1-brk/).

## Hardware

The OSD32MP15x SiP in integration with the STM32MP17 SoC provides the following hardware capabilities:

- Core:

  - 32-bit dual-core Arm® Cortex®-A7

    - L1 32-Kbyte I / 32-Kbyte D for each core
    - 256-Kbyte unified level 2 cache
    - Arm® NEON™ and Arm® TrustZone®
  - 32-bit Arm® Cortex®-M4 with FPU/MPU

    - Up to 209 MHz (Up to 703 CoreMark®)
- Memories:

  - 512 MB DDR3L memory (on SiP)
  - 708 Kbytes of internal SRAM:

    - 256 KB AXI SYSRAM
    - 384 KB AHB SRAM
    - 64 KB AHB SRAM in backup domain
  - Dual mode Quad-SPI memory interface
  - Flexible external memory controller with up to 16-bit data bus
  - Integrated 4 KB EEPROM (on SiP)
- Security/safety:

  - Secure boot, TrustZone® peripherals with Cortex®-M4 resource isolation
- Clock management:

  - Internal oscillators:

    - 64 MHz HSI oscillator
    - 4 MHz CSI oscillator
    - 32 kHz LSI oscillator
  - External oscillators:

    - 8-48 MHz HSE oscillator
    - 32.768 kHz LSE oscillator
  - 6 × PLLs with fractional mode
  - MEMS oscillator (on SiP)
- General-purpose input/outputs:

  - Up to 176 I/O ports with interrupt capability
  - 106 I/Os routed to expansion headers (on board)
- Interconnect matrix
- 3 DMA controllers
- Communication peripherals:

  - 6 × I2C FM+ (1 Mbit/s, SMBus/PMBus)
  - 4 × UART + 4 × USART (12.5 Mbit/s, ISO7816 interface, LIN, IrDA, SPI slave)
  - 6 × SPI (50 Mbit/s, including 3 with full duplex I2S audio class accuracy)
  - 4 × SAI (stereo audio: I2S, PDM, SPDIF Tx)
  - SPDIF Rx with 4 inputs
  - HDMI-CEC interface
  - MDIO Slave interface
  - 3 × SDMMC up to 8-bit (SD / e•MMC™ / SDIO)
  - 2 × CAN controllers supporting CAN FD protocol, TTCAN capability
  - 2 × USB 2.0 high-speed Host+ 1 × USB 2.0 full-speed OTG simultaneously
  - 10/100M or Gigabit Ethernet GMAC (IEEE 1588v2 hardware, MII/RMII/GMII/RGMI)
  - 8- to 14-bit camera interface up to 140 Mbyte/s
  - 6 analog peripherals
  - 2 × ADCs with 16-bit max. resolution
  - 1 × temperature sensor
  - 2 × 12-bit D/A converters (1 MHz)
  - 1 × digital filters for sigma delta modulator (DFSDM) with 8 channels/6
    filters
  - Internal or external ADC/DAC reference VREF+
- Graphics:

  - 3D GPU: Vivante® - OpenGL® ES 2.0
  - LCD-TFT controller, up to 24-bit // RGB888, up to WXGA (1366 × 768) @60 fps
  - MIPI® DSI 2 data lanes up to 1 GHz each
- Timers:

  - 2 × 32-bit timers with up to 4 IC/OC/PWM or pulse counter and quadrature
    (incremental) encoder input
  - 2 × 16-bit advanced motor control timers
  - 10 × 16-bit general-purpose timers (including 2 basic timers without PWM)
  - 5 × 16-bit low-power timers
  - RTC with sub-second accuracy and hardware calendar
  - 2 × 4 Cortex®-A7 system timers (secure, non-secure, virtual, hypervisor)
  - 1 × SysTick Cortex®-M4 timer
- Hardware acceleration:

  - AES 128, 192, 256, TDES
  - HASH (MD5, SHA-1, SHA224, SHA256), HMAC
  - 2 × true random number generator (3 oscillators each)
  - 2 × CRC calculation unit
- Debug mode:

  - Arm® CoreSight™ trace and debug: SWD and JTAG interfaces
  - 8-Kbyte embedded trace buffer
  - 3072-bit fuses including 96-bit unique ID, up to 1184-bit available for user

More information about the hardware can be found here:

- [STM32MP157F on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32mp157f.html)
- [OSD32MP15x SiP documentation](https://octavosystems.com/docs/osd32mp15x-datasheet/)

### Supported Features

The `osd32mp1_brk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `osd32mp1_brk/osd32mp15x` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L26) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| Clock control | on-chip | STM32MP1 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L45) | [`st,stm32mp1-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32mp1-rcc.md#std-dtcompatible-st-stm32mp1-rcc) |
| Counter | on-chip | STM32 counters[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L356) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L393) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st%2Cstm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V1)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L181) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L203) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L84) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L328) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/oct/osd32mp1_brk/osd32mp1_brk.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L57) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| IPM | on-chip | STM32 IPCC MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L384) | [`st,stm32-ipcc-mailbox`](../../../../build/dts/api/bindings/ipm/st%2Cstm32-ipcc-mailbox.md#std-dtcompatible-st-stm32-ipcc-mailbox) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/oct/osd32mp1_brk/osd32mp1_brk.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L78) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L350) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L50) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L265)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L274) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L310)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L283) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L404) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L245)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L215) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L33) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L340) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| Watchdog | on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L173) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

OSD32MP1-BRK Board schematic is available here:
[OSD32MP1-BRK schematics](https://octavosystems.com/docs/osd32mp1-brk-schematics/).

OSD32MP1-BRK Board pin mapping is available here:
[OSD32MP1-BRK default pin mapping](https://octavosystems.com/octavosystems.com/wp-content/uploads/2020/05/Default-Pin-Mapping.pdf).

#### Default Zephyr Peripheral Mapping:

- UART7 TX/RX: PA15/PB3 (default console)
- I2C5 SCL/SDA: PA11/PA12
- SPI4 SCK/MISO/MOSI: PE12/PE13/PE14

#### System Clock

The Cortex®-M4 Core is configured to run at a 209 MHz clock speed.
This value must match the configured mlhclk\_ck frequency.

#### Serial Port

The Zephyr console output is assigned by default to the RAM console to be dumped
by the Linux Remoteproc Framework on Cortex®-A7 core. To enable the USART2 console, modify
the board’s devicetree and the osd32mp1\_brk\_defconfig board file (or prj.conf project files)
Default USART settings are 115200 8N1.

## Programming and Debugging

The `osd32mp1_brk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The STM32MP157F doesn’t have QSPI flash for Cortex®-M4 and it needs to be
started by the Cortex®-A7 core. The Cortex®-A7 core is responsible for loading the
Cortex®-M4 binary application into the RAM, and getting Cortex®-M4 out of reset.
Cortex®-A7 can perform these steps at bootloader level or after the Linux
system has booted.

Cortex®-M4 can use up to 2 different RAMs. The program pointer starts at
the 0x00000000 (RETRAM) address, and the vector table should be loaded at this address.
The following table provides memory mappings for Cortex®-A7 and Cortex®-M4:

| Region | Cortex®-A7 | Cortex®-M4 | Size |
| --- | --- | --- | --- |
| RETRAM | 0x38000000-0x3800FFFF | 0x00000000-0x0000FFFF | 64KB |
| MCUSRAM | 0x10000000-0x1005FFFF | 0x10000000-0x1005FFFF | 384KB |
| DDR | 0xC0000000-0x20000000 |  | 512MB |

Refer to following instructions to boot Zephyr on the Cortex®-M4 core:

1. Download and install the Octavo OpenSTLinux distribution:
   [OSD32MP1 OpenSTLinux](https://octavosystems.com/files/osd32mp1-brk-openstlinux-v3-0/).

   (You can find more details about this process here: [OSD32MP1-BRK Getting Started](https://octavosystems.com/app_notes/osd32mp1-brk-getting-started/))
2. Build the Zephyr application:

   ```shell
   # From the root of the zephyr repository
   west build -b osd32mp1_brk samples/hello_world
   ```
3. Transfer the built firmware to the board via USB RNDIS:

   ```shell
   scp build/zephyr/zephyr.elf root@192.168.7.1:/lib/firmware
   ```
4. Boot Zephyr on the Cortex®-M4 core:

   ```shell
   ssh root@192.168.7.1
   echo stop > /sys/class/remoteproc/remoteproc0/state
   echo -n zephyr.elf > /sys/class/remoteproc/remoteproc0/firmware
   echo start > /sys/class/remoteproc/remoteproc0/state
   cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
   ```

   The console output should display:

   ```text
   *** Booting Zephyr OS build v4.0.0 ***
   Hello World! osd32mp1_brk/osd32mp15x
   ```

Refer to [OSD32MP1-BRK Getting Started](https://octavosystems.com/app_notes/osd32mp1-brk-getting-started/) and [stm32mp157 boot Cortex-M4 firmware](https://wiki.st.com/stm32mpu/index.php/Linux_remoteproc_framework_overview#How_to_use_the_framework) wiki page for more
detailed instructions.

### Debugging

You can debug an application using OpenOCD and GDB. The solution proposed below
is based on attaching to preloaded firmware, which is available only for a Linux
environment. The firmware must first be loaded by the Cortex®-A7. The developer
then attaches the debugger to the running Zephyr using OpenOCD.

The principle is to attach to the firmware already loaded by Linux.

- Build the sample:

  ```shell
  # From the root of the zephyr repository
  west build -b osd32mp1_brk samples/hello_world
  ```
- Copy the firmware on the target filesystem, load it and start it ([stm32mp157 boot Cortex-M4 firmware](https://wiki.st.com/stm32mpu/index.php/Linux_remoteproc_framework_overview#How_to_use_the_framework)).
- Attach to the target:

  ```shell
  west attach
  ```
