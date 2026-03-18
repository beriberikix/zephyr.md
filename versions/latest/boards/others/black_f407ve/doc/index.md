---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/others/black_f407ve/doc/index.html
original_path: boards/others/black_f407ve/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Black STM32 F407VE Development Board

## Overview

The BLACK\_F407VE board features an ARM Cortex-M4 based STM32F407xx MCU
with a wide range of connectivity support and configurations. There are
multiple version of this board like `black_f407ve`.
Here are some highlights of the BLACK\_F407VE board:

- STM32 microcontroller in LQFP100 package
- Extension header for all LQFP100 I/Os for quick connection to prototyping
  board and easy probing
- Flexible board power supply:

  > - USB VBUS or external source (3.3V, 5V)
  > - Power management access point
- Three LEDs:

  > - 3.3 V power on (LD0)
  > - Two user LEDs: green (LD1), green (LD2)
- Four push-buttons: RESET, K0, K1 and WK\_UP
- Mini-AB connector

![BLACK_F407VE](../../../../_images/black_f407ve.jpg)

See also board descriptions at [STM32-base website](https://stm32-base.org/boards/STM32F407VET6-STM32-F4VE-V2.0.html),
[STM32F407VET6 black board](https://os.mbed.com/users/hudakz/code/STM32F407VET6_Hello/) and [MCUDev Black STM32F407VET6](https://github.com/mcauser/BLACK_F407VE)

Warning

The +5V pins on this board are directly connected to the +5V pin
of the USB connector. There is no protection in place. Do not
power this board through USB and an external power supply at
the same time.

## Hardware

BLACK\_F407VE board provides the following hardware components:

- STM32F407VET6 in LQFP100 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 168 MHz max CPU frequency
- VDD from 1.8 V to 3.6 V
- 8MHz system crystal
- 32.768KHz RTC crystal
- JTAG/SWD header
- 512 kB Flash
- 192+4 KB SRAM including 64-Kbyte of core coupled memory
- GPIO with external interrupt capability
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- RTC battery CR1220
- Advanced-control Timer (2)
- General Purpose Timers (12)
- Watchdog Timers (2)
- USART (3), UART (2)
- I2C (3)
- I2S (2)
- SPI (3)
- SDIO (1)
- CAN (2)
- USB 2.0 OTG FS with on-chip PHY
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and ULPI
- 10/100 Ethernet MAC with dedicated DMA
- CRC calculation unit
- True random number generator
- DMA Controller
- Micro SD
- 1x 10/100 Ethernet MAC
- 1x 8 to 12-bit Parallel Camera interface
- Micro USB for power and comms
- 2x jumpers for bootloader selection
- 2x16 FMSC LCD Interface
- NRF24L01 socket
- Dimensions: 85.1mm x 72.45mm

More information about STM32F407VE SOC can be found here:
:   - [STM32F407VE on www.st.com](https://www.st.com/en/microcontrollers/stm32f407ve.html)

### Supported Features

The Zephyr black\_f407ve board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| PWM | on-chip | pwm |
| USB | on-chip | usb |
| CAN | on-chip | CAN controller |
| SPI | on-chip | spi |

Note

CAN feature requires CAN transceiver.
Zephyr default configuration uses CAN\_2 exclusively, as
simultaneous use of CAN\_1 and CAN\_2 is not yet supported.

Other hardware features are not yet supported on Zephyr porting.

The default configuration can be found in
[boards/others/black\_f407ve/black\_f407ve\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/black_f407ve/black_f407ve_defconfig)

### Pin Mapping

BLACK\_F407VE has 5 GPIO controllers. These controllers are responsible for pin
muxing, input/output, pull-up, etc.

![left pins](../../../../_images/stm32f407vet6_left02.jpg)
![right pins](../../../../_images/stm32f407vet6_right01.jpg)
![bottom and top pins](../../../../_images/stm32f407vet6_st-link02.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- USER\_PB : PA0
- LD3 : PD13
- LD4 : PD12
- LD5 : PD14
- LD6 : PD15
- USB DM : PA11
- USB DP : PA12
- CAN1\_RX : PD0
- CAN1\_TX : PD1
- CAN2\_RX : PB12
- CAN2\_TX : PB13
- SPI1 MISO : PB4
- SPI1 MOSI : PB5
- SPI1 SCK : PB3
- SPI1 Flash CS : PB0
- SPI2 MISO : PC2
- SPI2 MOSI : PC3
- SPI2 SCK : PB10

### System Clock

BLACK\_F407VE System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock
at 168MHz, driven by 8MHz high speed external clock.

### Serial Port

BLACK\_F407VE has up to 6 UARTs. The Zephyr console output is assigned to UART1.
Default settings are 115200 8N1.
Please note that ST-Link Virtual Com Port is not wired to chip serial port.
In order to enable console output you should use a serial cable and connect
it to UART1 pins (PA9/PA10).

## Programming and Debugging

Applications for the `black_f407ve` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

BLACK\_F407VE board includes an ST-LINK/V2 embedded debug tool interface.
This interface is supported by the openocd version included in Zephyr SDK.

#### Flashing an application to BLACK\_F407VE

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b black_f407ve samples/basic/blinky
west flash
```

You should see user led “LD1” blinking.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b black_f407ve samples/hello_world
west debug
```
