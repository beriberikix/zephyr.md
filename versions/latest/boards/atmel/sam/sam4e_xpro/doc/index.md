---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/atmel/sam/sam4e_xpro/doc/index.html
original_path: boards/atmel/sam/sam4e_xpro/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SAM4E Xplained Pro

## Overview

The SAM4E Xplained Pro evaluation kit is a development platform to evaluate the
Atmel SAM4E series microcontrollers.

![SAM4E Xplained Pro](../../../../../_images/sam4e_xpro.jpg)

## Hardware

- ATSAM4E16E ARM Cortex-M4F Processor
- 12 MHz crystal oscillator
- internal 32.768 kHz crystal oscillator
- 2 x IS61WV5128BLL 4Mb SRAM
- MT29F2G08ABAEAWP 2Gb NAND
- SD card connector
- CAN-bus (TLE7250GVIOXUMA1 CAN Transceiver)
- Ethernet port (KSZ8081MNXIA phy)
- Micro-AB USB device
- Micro-AB USB debug interface supporting CMSIS-DAP, Virtual COM Port and Data
  Gateway Interface (DGI)
- One reset and one user pushbutton
- 1 yellow user LEDs

### Supported Features

The sam4e\_xpro board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| GPIO | on-chip | gpio |
| AFEC | on-chip | adc |
| COUNTER | on-chip | counter |
| ETHERNET | on-chip | ethernet |
| HWINFO | on-chip | hwinfo |
| HSMCI | on-chip | sdhc |
| I2C | on-chip | i2c |
| PWM | on-chip | pwm |
| SPI | on-chip | spi |
| UART | on-chip | serial port |
| USART | on-chip | serial port |
| WATCHDOG | on-chip | watchdog |

Other hardware features are not currently supported by Zephyr.

The default configuration can be found in the Kconfig
[boards/atmel/sam/sam4e\_xpro/sam4e\_xpro\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro_defconfig).

### Connections and IOs

The [SAM4E Xplained Pro User Guide](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro_User-Guide.pdf) [[1]](#id1) has detailed information about board
connections. Download the [SAM4E Xplained Pro documentation](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro_Design-Documentation.zip) [[2]](#id3) for more detail.

### System Clock

The SAM4E MCU is configured to use the 12 MHz internal oscillator on the board
with the on-chip PLL to generate an 120 MHz system clock.

### Serial Port

The ATSAM4E16E MCU has 2 UARTs and 2 USARTs. One of the UARTs (UART0) is
configured for the console and is available as a Virtual COM Port by EDBG USB
chip.

## Programming and Debugging

Flashing the Zephyr project onto SAM4E MCU requires the [OpenOCD tool](http://openocd.org/) [[3]](#id5).
By default a factory new SAM4E chip will boot SAM-BA boot loader located in
the ROM, not the flashed image. This is determined by the value of GPNVM1
(General-Purpose NVM bit 1). The flash procedure will ensure that GPNVM1 is
set to 1 changing the default behavior to boot from Flash.

If your chip has a security bit GPNVM0 set you will be unable to program flash
memory or connect to it via a debug interface. The only way to clear GPNVM0
is to perform a chip erase procedure that will erase all GPNVM bits and the full
contents of the SAM4E flash memory:

- With the board power off, set a jumper on the J304 header.
- Turn the board power on. The jumper can be removed soon after the power is on
  (flash erasing procedure is started when the erase line is asserted for at
  least 230ms)

### Flashing

For flash the board Zephyr provides two paths. One uses the default OpenOCD
tool and the second one uses [SAM Boot Assistant (SAM-BA)](../../../../../develop/flash_debug/host-tools.md#atmel-sam-ba-bootloader).

#### Using OpenOCD

1. Connect the SAM4E Xplained Pro board to your host computer using the USB
   debug port. Then build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello-world) application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4e_xpro samples/hello_world
   west flash
   ```

#### Using SAM-BA bootloader

1. Close the `ERASE` jumper on the SAM4E Xplained Pro board. Power on the
   board for 10s.
2. Open the `ERASE` jumper.
3. Connect the SAM4E Xplained Pro board to your host computer using the SoC
   USB port. Then build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello-world) application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4e_xpro samples/hello_world
   ```

   ```shell
   $ west flash -r bossac
   ```

#### Visualizing the message

1. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization string.
   Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
2. Press reset button

   You should see “Hello World! sam4e\_xpro” in your terminal.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b sam4e_xpro samples/hello_world
west debug
```

## References

[[1](#id2)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro\_User-Guide.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro_User-Guide.pdf)

[[2](#id4)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro\_Design-Documentation.zip](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro_Design-Documentation.zip)

[[3](#id6)]

[http://openocd.org/](http://openocd.org/)
