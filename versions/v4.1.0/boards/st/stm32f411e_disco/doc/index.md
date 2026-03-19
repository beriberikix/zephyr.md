---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32f411e_disco/doc/index.html
original_path: boards/st/stm32f411e_disco/doc/index.html
---

# STM32F411E Discovery

Board Overview

[![../../../../_images/stm32f411e_disco.jpg](../../../../_images/stm32f411e_disco.jpg)
](../../../../_images/stm32f411e_disco.jpg)

STM32F411E Discovery

Name:
:   `stm32f411e_disco`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f411xe

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32f411e_disco/doc/index.rst/../..)

## Overview

The STM32F411E Discovery kit features an ARM Cortex-M4 based STM32F411VE MCU
with a wide range of connectivity support and configurations.
Here are some highlights of the STM32F411E-DISCO board:

- STM32F411VET6 microcontroller featuring 512 KB of Flash memory, 128 KB of RAM in an LQFP100 package
- On-board ST-LINK/V2 with selection mode switch to use the kit as a standalone STLINK/V2 (with SWD connector for programming and debugging)
- Board power supply: through USB bus or from an external 5 V supply voltage
- External application power supply: 3 V and 5 V
- L3GD20(rev B) or I3G4250D(rev D): ST MEMS motion sensor, 3-axis digital output gyroscope.
- LSM303DLHC(rev B) or LSM303AGR(rev D): ST MEMS system-in-package featuring a 3D digital linear acceleration sensor and a 3D digital magnetic sensor.
- MP45DT02(rev B) or IMP34DT05(rev D), ST MEMS audio sensor, omnidirectional digital microphone
- CS43L22, audio DAC with integrated class D speaker driver
- Eight LEDs:
  :   - LD1 (red/green) for USB communication
      - LD2 (red) for 3.3 V power on
      - Four user LEDs:
        :   LD3 (orange), LD4 (green), LD5 (red) and LD6 (blue)
      - Two USB OTG LEDs:
        :   LD7 (green) VBus and LD8 (red) over-current
- Two pushbuttons (user and reset)
- USB OTG with micro-AB connector
- Extension header for LQFP100 I/Os for a quick connection to the prototyping board and an easy probing

More information about the board can be found at the [32F411EDISCOVERY website](https://www.st.com/en/evaluation-tools/32f411ediscovery.html) [[1]](#id2).

## Hardware

STM32F411E-DISCO Discovery kit provides the following hardware components:

- STM32F411VET6 in LQFP100 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 100 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 512 KB Flash
- 128 KB SRAM
- GPIO with external interrupt capability
- 1x12-bit, 2.4 MSPS ADC with 16 channels
- DMA Controller
- Up to 11 Timers (six 16-bit, two 32-bit, two watchdog timers and a SysTick timer)
- USART/UART (3)
- I2C (3)
- SPI/I2S (5)
- SDIO
- USB 2.0 full-speed device/host/OTG controller with on-chip PHY
- CRC calculation unit
- 96-bit unique ID
- RTC

More information about STM32F411VE can be found here:
:   - [STM32F411VE website](https://www.st.com/en/microcontrollers/stm32f411ve.html) [[3]](#id6)
    - [STM32F411x reference manual](https://www.st.com/resource/en/reference_manual/dm00119316.pdf) [[4]](#id8)

### Supported Features

The `stm32f411e_disco` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

STM32F411E-DISCO Discovery kit has 5 GPIO controllers. These controllers are
responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [32F411EDISCOVERY board User Manual](https://www.st.com/resource/en/user_manual/dm00148985.pdf) [[2]](#id4).

#### Default Zephyr Peripheral Mapping:

- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- LD3 : PD13 (PWM4 CH2)
- LD4 : PD12 (PWM4 CH1)
- LD5 : PD14 (PWM4 CH3)
- LD6 : PD15 (PWM4 CH4)

### System Clock

STM32F411E-DISCO System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 100MHz, driven by the internal oscillator.

### Serial Port

The STM32F411G Discovery kit has up to 3 UARTs. The Zephyr console output is
assigned to UART2. Default settings are 115200 8N1.

## Programming and Debugging

STM32F411E-DISCO Discovery kit includes an ST-LINK/V2 embedded debug tool interface.

Applications for the `stm32f411e_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[5]](#id10) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to STM32F411E-DISCO

Connect the STM32F411E-DISCO Discovery kit to your host computer using the
USB port. Then build and flash an application.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f411e_disco samples/basic/blinky
west flash
```

In case you are using PCB revision B, you have to use an
adapted board definition as the default PCB rev here is D:

```shell
# From the root of the zephyr repository
west build -b stm32f411e_disco@B samples/basic/blinky
west flash
```

You should see the orange led (LD3) blinking every second.

### Debugging

You can debug applications in the usual way. Here is an example for
the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f411e_disco samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/32f411ediscovery.html](https://www.st.com/en/evaluation-tools/32f411ediscovery.html)

[[2](#id5)]

[https://www.st.com/resource/en/user\_manual/dm00148985.pdf](https://www.st.com/resource/en/user_manual/dm00148985.pdf)

[[3](#id7)]

[https://www.st.com/en/microcontrollers/stm32f411ve.html](https://www.st.com/en/microcontrollers/stm32f411ve.html)

[[4](#id9)]

[https://www.st.com/resource/en/reference\_manual/dm00119316.pdf](https://www.st.com/resource/en/reference_manual/dm00119316.pdf)

[[5](#id11)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)
