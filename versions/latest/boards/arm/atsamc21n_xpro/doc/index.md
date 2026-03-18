---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/atsamc21n_xpro/doc/index.html
original_path: boards/arm/atsamc21n_xpro/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SAM C21N Xplained Pro Evaluation Kit

## Overview

The SAM C21N Xplained Pro evaluation kit is ideal for evaluation and
prototyping with the SAM C21N Cortex®-M0+ processor-based
microcontrollers. The kit includes Atmel’s Embedded Debugger (EDBG),
which provides a full debug interface without the need for additional
hardware.

![ATSAMC21N-XPRO](../../../../_images/atsamc21n_xpro.jpg)

## Hardware

- ATSAMC21N18A ARM Cortex-M0+ processor at 48 MHz
- 32.768 kHz crystal oscillator
- 256 KiB flash memory, 32 KiB of RAM, 8KB RRW flash
- One yellow user LED
- One mechanical user push button
- One reset button
- One QTouch® button
- On-board USB based EDBG unit with serial console
- Two CAN transceivers

### Supported Features

The atsamc21n\_xpro board configuration supports the following hardware
features:

| Interface | Controller | Driver / Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| Flash | on-chip | Can be used with LittleFS to store files |
| SYSTICK | on-chip | systick |
| WDT | on-chip | Watchdog |
| ADC | on-chip | Analog to Digital Converter |
| GPIO | on-chip | I/O ports |
| PWM | on-chip | Pulse Width Modulation |
| USART | on-chip | Serial ports |
| I2C | on-chip | I2C ports |
| SPI | on-chip | Serial Peripheral Interface ports |
| CAN | on-chip | CAN ports |

Other hardware features are not currently supported by Zephyr.

The default configuration can be found in the Kconfig
`boards/arm/atsamc21n_xpro/atsamc21n_xpro_defconfig`.

### Pin Mapping

The SAM C21N Xplained Pro evaluation kit has 4 GPIO controllers. These
controllers are responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SAM C21 Family Datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/SAM-C20-C21-Family-Data-Sheet-DS60001479J.pdf) [[1]](#id1) and the [SAM C21N
Xplained Pro Schematic](https://ww1.microchip.com/downloads/en/DeviceDoc/ATSAMC21N_Xplained_Pro_Design_Files.zip) [[2]](#id3).

#### Default Zephyr Peripheral Mapping:

- ADC0 : PB09
- ADC1 : PA08
- CAN0 TX : PA24
- CAN0 RX : PA25
- CAN1 TX : PB14
- CAN1 RX : PB15
- SERCOM0 USART TX : PB24
- SERCOM0 USART RX : PB25
- SERCOM1 I2C SDA : PA16
- SERCOM1 I2C SCL : PA17
- SERCOM2 USART TX : PA12
- SERCOM2 USART RX : PA13
- SERCOM4 USART TX : PB10
- SERCOM4 USART RX : PB11
- SERCOM5 SPI MISO : PB00
- SERCOM5 SPI MOSI : PB02
- SERCOM5 SPI SCK : PB01
- GPIO/PWM LED0 : PC05

### System Clock

The SAMC21 MCU is configured to use the 32.768 kHz internal oscillator
with the on-chip internal oscillator generating the 48 MHz system clock.

### Serial Port

The SAMC21 MCU has eight SERCOM based USARTs with three configured as USARTs in
this BSP. SERCOM4 is the default Zephyr console.

- SERCOM0 9600 8n1
- SERCOM2 115200 8n1
- SERCOM4 115200 8n1 connected to the onboard Atmel Embedded Debugger (EDBG)

### PWM

The SAMC21 MCU has 3 TCC based PWM units with up to 4 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC2 instead of by GPIO.

## Programming and Debugging

The SAM C21N Xplained Pro comes with a Atmel Embedded Debugger (EDBG). This
provides a debug interface to the SAMC21 chip and is supported by
OpenOCD.

### Flashing

1. Build the Zephyr kernel and the `hello_world` sample application:

   ```shell
   west build -b atsamc21n_xpro samples/hello_world
   ```
2. Connect the SAM C21N Xplained Pro to your host computer using the USB debug
   port.
3. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
4. To flash an image:

   ```shell
   west build -b atsamc21n_xpro samples/hello_world
   west flash
   ```

   You should see “Hello World! atsamc21n\_xpro” in your terminal.

## References

[[1](#id2)]

[https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/SAM-C20-C21-Family-Data-Sheet-DS60001479J.pdf](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/SAM-C20-C21-Family-Data-Sheet-DS60001479J.pdf)

[[2](#id4)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/ATSAMC21N\_Xplained\_Pro\_Design\_Files.zip](https://ww1.microchip.com/downloads/en/DeviceDoc/ATSAMC21N_Xplained_Pro_Design_Files.zip)
