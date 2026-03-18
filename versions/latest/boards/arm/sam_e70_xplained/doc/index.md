---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/sam_e70_xplained/doc/index.html
original_path: boards/arm/sam_e70_xplained/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SAM E70(B) Xplained

## Overview

The SAM E70 Xplained evaluation kit is a development platform to evaluate the
Atmel SAM E70 series microcontrollers. The current version allows to use both
IC variations ATSAME70Q21A(B).

![SAM E70 Xplained](../../../../_images/sam_e70_xplained.jpg)

## Hardware

- ATSAME70Q21A(B) ARM Cortex-M7 Processor
- 12 MHz crystal oscillator
- 32.768 kHz crystal oscillator (not populated)
- AT24MAC402 EEPROM
- IS42S16100E 16 Mb SDRAM
- SD card connector
- Ethernet port
- Micro-AB USB device
- Micro-AB USB debug interface supporting CMSIS-DAP, Virtual COM Port and Data
  Gateway Interface (DGI)
- JTAG interface connector
- One reset and one user pushbutton
- One green user LED

### Supported Features

The sam\_e70\_xplained board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port |
| USART | on-chip | serial port |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| ETHERNET | on-chip | ethernet |
| WATCHDOG | on-chip | watchdog |
| GPIO | on-chip | gpio |
| ADC | on-chip | ADC via AFEC |
| USB | on-chip | USB device |
| PWM | on-chip | pwm |
| CAN | on-chip | canbus |
| HWINFO | on-chip | Unique device serial number |

Other hardware features are not currently supported by Zephyr.

The default configuration can be found in the Kconfig
[boards/arm/sam\_e70\_xplained/sam\_e70\_xplained\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/sam_e70_xplained/sam_e70_xplained_defconfig).

### Connections and IOs

The [SAME70-XPLD User Guide](http://www.atmel.com/Images/Atmel-44050-Cortex-M7-Microcontroller-SAM-E70-XPLD-Xplained_User-guide.pdf) has detailed information about board connections.

### System Clock

The SAM E70 MCU is configured to use the 12 MHz external oscillator on the board
with the on-chip PLL to generate a 300 MHz system clock.

### Serial Port

The ATSAME70Q21 MCU has five UARTs and three USARTs. One of the USARTs is
configured for the console and is available as a Virtual COM Port via EDBG USB
chip.

## Programming and Debugging

Flashing the Zephyr project onto SAM E70 MCU requires the [OpenOCD tool](http://openocd.org/).
Support for Atmel SAM E microcontroller series was added in OpenOCD release
0.10.0, which was added in Zephyr SDK 0.9.2.

By default a factory new SAM E70 chip will boot SAM-BA boot loader located in
the ROM, not the flashed image. This is determined by the value of GPNVM1
(General-Purpose NVM bit 1). The flash procedure will ensure that GPNVM1 is
set to 1 changing the default behavior to boot from Flash.

If your chip has a security bit GPNVM0 set you will be unable to program flash
memory or connect to it via a debug interface. The only way to clear GPNVM0
is to perform a chip erase procedure that will erase all GPNVM bits and the full
contents of the SAM E70 flash memory:

- With the board power off, set a jumper on the J200 header.
- Turn the board power on. The jumper can be removed soon after the power is on
  (flash erasing procedure is started when the erase line is asserted for at
  least 230ms)

### Flashing

1. Run your favorite terminal program to listen for output. Under Linux the
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
2. Connect the SAM E70 Xplained board to your host computer using the
   USB debug port. Then build and flash the [Hello World](../../../../samples/hello_world/README.md#hello-world)
   application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam_e70_xplained samples/hello_world
   west flash
   ```

   You should see “Hello World! sam\_e70\_xplained” in your terminal.
3. To use the SoC variation B IC, you need type “sam\_e70b\_xplained”.

   ```shell
   # From the root of the zephyr repository
   west build -b sam_e70b_xplained samples/hello_world
   west flash
   ```

   You should see “Hello World! sam\_e70b\_xplained” in your terminal.

You can flash the image using an external debug adapter such as J-Link
or ULINK, connected to the 20-pin JTAG header. Supply the name of the
debug adapter (e.g., `jlink`) via an OPENOCD\_INTERFACE environment
variable. OpenOCD will look for the appropriate interface
configuration in an `interface/$(OPENOCD_INTERFACE).cfg` file on its
internal search path.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b sam_e70_xplained samples/hello_world
west debug
```

## References

SAM E70 Product Page:
:   [http://www.atmel.com/products/microcontrollers/arm/sam-e.aspx](http://www.atmel.com/products/microcontrollers/arm/sam-e.aspx)
