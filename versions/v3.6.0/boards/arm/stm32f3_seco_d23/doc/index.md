---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/stm32f3_seco_d23/doc/index.html
original_path: boards/arm/stm32f3_seco_d23/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SECO SBC-3.5-PX30 (JUNO - D23) (STM32F302)

## Overview

SBC-3.5-PX30 (JUNO - D23) is a Single Board Computer based on embedded Rockchip PX30
Processor, featuring Quad-Core ARM Cortex-A35 processor. The processor
integrates a Mali-G31 GPU with High performance dedicated 2D processor,
supporting OpenGL ES 1.1 / 2.0 / 3.2, Vulkan 1.0, OpenCL 2.0 and Open VG 1.1.
Embedded VPU is able to support video decoding of the most common coding
standard (MPEG-4, H.265/HEVC, H.264, VP8, VC-1). The board is completed with up
to 4GB LPDDR4-3200 32-bit bus memory directly soldered on board and one eMMC
5.1 Flash Drive with up to 64GB of capacity. LVDS Single Channel interface and
HDMI are supported. The RMII interface and Micrel KSZ8091 Ethernet Transceiver
allow the implementation of a Fast Ethernet interface. The networking
capabilities can be extended by WiFi+BT M.2 module and external modem module.
The audio functionalities are managed by the AudioCodec embedded in the RK-809
PMIC. SBC-3.5-PX30 board is completed by a series of connectors with various
interfaces (UART, SPI, I2C) managed by the microcontroller STM32F302VCT6.

![SECO SBC-3.5-PX30](../../../../_images/stm32f3_seco_d23.jpg)

More information about the board can be found at the
[SECO SBC-3.5-PX30 website](https://edge.seco.com/sbc-3-5-px30.html).

## Hardware

SECO SBC-3.5-PX30 provides the following hardware components:

- STM32F302VCT6
  - ARM® 32-bit Cortex® -M4 CPU with FPU
  - 256 KB Flash
  - 40 KB SRAM
  - 72 MHz max CPU frequency
- 2 User LEDs
- 16 GPI
- 16 GPO
- 4 U(S)ART
  - Modbus
  - RS485
  - TTL Serial Debug
  - TTL Serial
- 8-channel General Purpose Timers
- USB 2.0 full speed interface
- CAN
- I2C (up to 2)
- SPI

More information about STM32F302VC can be found here:

- [STM32F302VC on www.st.com](https://www.st.com/en/microcontrollers/stm32f302vc.html)
- [STM32F302xC reference manual](https://www.st.com/resource/en/reference_manual/rm0365-stm32f302xbcde-and-stm32f302x68-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The Zephyr stm32f3\_seco\_d23 board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| USB | on-chip | USB device |
| CAN | on-chip | CAN |
| IWDG | on-chip | Independent WatchDoG |
| PWM | on-chip | pwm |

Other hardware features are not yet supported on Zephyr porting.

### Pin Mapping

SBC-3.5-PX30 has 6 GPIO controllers. These controllers are
responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SECO SBC-3.5-PX30 board User Manual](https://www.seco.com/Manuals/SBC-D23_Manual.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9 (debug config for UART\_1)
- UART\_1\_RX : PA10 (debug config for UART\_1)
- UART\_1\_TX : PC4 (alternate config for UART\_1)
- UART\_1\_RX : PC5 (alternate config for UART\_1)
- UART\_2\_TX : PD5
- UART\_2\_RX : PD6
- UART\_2\_CLK : PD7
- UART\_2\_CTS : PD3
- UART\_2\_RTS/DE : PD4
- UART\_3\_TX : PC10
- UART\_3\_RX : PC11
- UART\_3\_CLK : PD10
- UART\_3\_CTS : PD11
- UART\_3\_RTS/DE : PD12
- UART\_5\_TX : PC12
- UART\_5\_RX : PD2
- I2C1\_SCL : PB6
- I2C1\_SDA : PB7
- I2C2\_SCL : PA9 (alternate config for UART\_1)
- I2C2\_SDA : PA10 (alternate config for UART\_1)
- SPI1\_NSS : PA4
- SPI1\_SCK : PB3
- SPI1\_MISO : PB4
- SPI1\_MOSI : PB5
- SPI2\_NSS : PB12
- SPI2\_SCK : PB13
- SPI2\_MISO : PB14
- SPI2\_MOSI : PB15
- CAN1\_RX : PB8
- CAN1\_TX : PB9
- USB\_DM : PA11
- USB\_DP : PA12
- LD1 : PD8
- LD2 : PD9
- PWM : PA8

### System Clock

SECO SBC-3.5-PX30 System Clock could be driven by internal or external
oscillator, as well as main PLL clock. By default System clock is driven
by PLL clock at 72 MHz, driven by an external oscillator at 8 MHz.

### Serial Port

SECO SBC-3.5-PX30 has up to 4 U(S)ARTs. The Zephyr console output
is assigned to UART1. Default settings are 115200 8N1.
In debug configuration UART1 is connected to the flashing connector CN56.

UART2 provides Modbus interface to connector CN28.
UART3 provides RS-485 interface to connectors CN57 and CN48.
In alternative config, USART2 and USART3 are exposed to connector J2.

UART1 (in alternate config) and UART5 are connected to CN32.

### I2C

SECO SBC-3.5-PX30 has up to 2 I2Cs. Both are present in connector CN33.
I2C2 is available only on boards where DEBUG serial is not connected.

### USB

SECO SBC-3.5-PX30 has a USB 2.0 full-speed device interface available through
its connector CN31.

### CAN

SECO SBC-3.5-PX30 has an onboard CAN transceiver (TJA1051T), and it is
connected to both CN29 and CN30. PD0 is connected to EC\_CAN\_STBY.

### SPI

SECO SBC-3.5-PX30 has two SPI lines: SPI1 is an internal SPI line connected to the
main processor (Rockchip PX30) and SPI2 is connected to CN39.

## Programming and Debugging

### Flashing

Applications for the `stm32f3_seco_d23` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

#### Flashing an application to SECO SBC-3.5-PX30

First, connect the SECO SBC-3.5-PX30 to your host computer using
CN56 connector to an ST-Link.
The pinout is (1-8):
- VDD
- UART1\_TX
- UART1\_RX
- BOOT\_0
- SWDIO\_JTMS
- SWCLK\_JTCK
- EC\_RST#
- GND

Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b stm32f3_seco_d23 samples/hello_world
west flash
```

Run a serial host program to connect with your board.

```shell
$ minicom -D /dev/<tty device>
```

Replace <tty\_device> with the port where the SBC-3.5-PX30 board can be
found.

You should see the following message on the console:

```shell
Hello World! stm32f3_seco_d23
```
