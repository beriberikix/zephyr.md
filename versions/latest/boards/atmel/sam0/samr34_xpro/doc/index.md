---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/atmel/sam0/samr34_xpro/doc/index.html
original_path: boards/atmel/sam0/samr34_xpro/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SAM R34 Xplained Pro Evaluation Kit

## Overview

The SAM R34 Xplained Pro evaluation kit is ideal for evaluation and
prototyping with the SAM R34 Cortex®-M0+ processor-based
microcontrollers. The kit includes Atmel’s Embedded Debugger (EDBG),
which provides a full debug interface without the need for additional
hardware.

The SAMR34 and SAMR35 parts are produced as a System-in-Package (SiP),
including both a SAML21 die, and a Semtech SX1276 LoRa radio die.

This board is also referred to as DM320111.

![SAMR34-XPRO](../../../../../_images/atsamr34-xpro.jpg)

## Hardware

- SAMR34J18 ARM Cortex-M0+ processor at 48 MHz
- 32.768 kHz crystal oscillator
- 256 KiB flash memory, 32 KiB of SRAM, 8KB Low Power SRAM
- One yellow user LED
- One mechanical user push button
- One reset button
- On-board USB based EDBG unit with serial console

### Supported Features

The samr34\_xpro board configuration supports the following hardware
features:

| Interface | Controller | Driver / Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| Flash | on-chip | Can be used with LittleFS to store files |
| SYSTICK | on-chip | systick |
| WDT | on-chip | Watchdog |
| GPIO | on-chip | I/O ports |
| PWM | on-chip | Pulse Width Modulation |
| USART | on-chip | Serial ports |
| I2C | on-chip | I2C ports |
| SPI | on-chip | Serial Peripheral Interface ports |
| TRNG | on-chip | True Random Number Generator |

The following hardware features are supported by Zephyr, but not yet fully
supported by the SOC:

| Interface | Controller | Driver / Component |
| --- | --- | --- |
| LoRa Radio | on-chip | Internal SX1276 LoRa Radio |

Other hardware features are not currently supported by Zephyr.

The default configuration can be found in the Kconfig
[boards/atmel/sam0/samr34\_xpro/samr34\_xpro\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/samr34_xpro/samr34_xpro_defconfig).

### Pin Mapping

The SAM R34 Xplained Pro evaluation kit has 3 GPIO controllers. These
controllers are responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SAM R34 Family Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/SAM-R34-R35-Low-Power-LoRa-Sub-GHz-SiP-Data-Sheet-DS70005356C.pdf) [[1]](#id1) and the [SAM R34
Xplained Pro Schematic](https://ww1.microchip.com/downloads/Secure/en/DeviceDoc/SAMR34_SiP_Reference_Design_Package_V3.0.exe) [[2]](#id3).

![SAMR34-XPRO-pinout](../../../../../_images/atsamr34-xpro-pinout.jpg)

#### Default Zephyr Peripheral Mapping:

- SERCOM0 UART TX : PA04
- SERCOM0 UART RX : PA05
- SERCOM1 I2C SDA : PA16
- SERCOM1 I2C SCL : PA17
- SERCOM4 SPI MISO : PC19
- SERCOM4 SPI MOSI : PB30
- SERCOM4 SPI SCK : PC18
- SERCOM4 GPIO CS : PB31
- SERCOM5 SPI MISO : PB02
- SERCOM5 SPI MOSI : PB22
- SERCOM5 SPI SCK : PB23
- SERCOM5 GPIO CS0 : PA23
- SERCOM5 GPIO CS1 : PA14
- USB DP : PA25
- USB DM : PA24
- GPIO/PWM LED0 : PA19

### System Clock

The SAMR34 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 48 MHz system clock.

### Serial Port

The SAMR34 MCU has six SERCOM based USARTs with one configured as USART in
this BSP. SERCOM0 is the default Zephyr console.

- SERCOM0 115200 8n1 - connected to the onboard Atmel Embedded Debugger (EDBG)

### PWM

The SAMR34 MCU has 3 TCC based PWM units with up to 4 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC0 instead of by GPIO.

### SPI Port

The SAMR34 MCU has 6 SERCOM based SPIs, with two configured as SPI in this BSP.

- SERCOM4 - connected to the internal LoRa radio
- SERCOM5 - connected to EXT1 and EXT3

## Programming and Debugging

The SAM R34 Xplained Pro comes with a Atmel Embedded Debugger (EDBG). This
provides a debug interface to the SAMR34 chip and is supported by
OpenOCD.

### Flashing

1. Build the Zephyr kernel and the `hello_world` sample application:

   ```shell
   west build -b samr34_xpro samples/hello_world
   ```
2. Connect the SAM R34 Xplained Pro to your host computer using the USB debug
   port.
3. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ picocom -b 115200 /dev/ttyACM0
   ```

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
4. To flash an image:

   ```shell
   west build -b samr34_xpro samples/hello_world
   west flash
   ```

   You should see “Hello World! samr34\_xpro” in your terminal.

## References

[[1](#id2)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/SAM-R34-R35-Low-Power-LoRa-Sub-GHz-SiP-Data-Sheet-DS70005356C.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/SAM-R34-R35-Low-Power-LoRa-Sub-GHz-SiP-Data-Sheet-DS70005356C.pdf)

[[2](#id4)]

[https://ww1.microchip.com/downloads/Secure/en/DeviceDoc/SAMR34\_SiP\_Reference\_Design\_Package\_V3.0.exe](https://ww1.microchip.com/downloads/Secure/en/DeviceDoc/SAMR34_SiP_Reference_Design_Package_V3.0.exe)
