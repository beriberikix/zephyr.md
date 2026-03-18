---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/vmu_rt1170/doc/index.html
original_path: boards/arm/vmu_rt1170/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP VMU RT1170

## Overview

The VMU RT1170 features an i.MX RT1176 dual core MCU with the
Cortex-M7 core at 1 GHz and a Cortex-M4 at 400 MHz.
The i.MX RT1176 MCU offers support over a wide temperature range
and is qualified for consumer, industrial and automotive markets.
The VMU RT1170 is the default VMU for CogniPilot’s Cerebri, a
Zephyr RTOS based Autopilot.

![VMU RT1170](../../../../_images/vmu_rt1170.jpg)

## Hardware

- MIMXRT1176DVMAA MCU

  - 1GHz Cortex-M7 & 400Mhz Cortex-M4
  - 2MB SRAM with 512KB of TCM for Cortex-M7 and 256KB of TCM for Cortex-M4
- Memory

  - 512 Mbit Octal Flash
  - TF socket for SD card
- Ethernet

  - 2 wire 100BASE-T1
- USB

  - USB 2.0 connector
- Power

  - Redundant dual picoflex power ports
- Debug

  - 10 pin debug and shell adapter board to 20 Pin JTAG debugger and USB-C shell
- Sensor

  - BMI088 6-axis IMU
  - BMM150 Magnetometer
  - Dual BMP388 Barometer
  - Dual ICM-42688 6-axis IMU
  - IST8310 3-axis Magnetometer
  - U-blox NEO-M8N GNSS module
- UART JST-GH connectors
- I2C JST-GH connectors
- CAN bus JST-GH connectors

For more information about the MIMXRT1176 SoC and VMU RT1170 board, see
these references:

- [VMU RT1170 Website](https://www.nxp.com/part/VMU-RT1170)
- [VMU RT1170 User Guide](https://cognipilot.org/cerebri/boards/nxp_vmu_rt1170/)
- [VMU RT1170 Schematics](https://github.com/CogniPilot/NXP-VMU_RT117x-HW)
- [i.MX RT1170 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1170CEC.pdf)
- [i.MX RT1170 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1170RM)

### Supported Features

VMU-RT1170 is a “Vehicle Management Unit” based on the general i.MX RT1170
family of processors. The VMU RT1170 board configuration supports the
following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| GPIO | on-chip | gpio |
| COUNTER | on-chip | counter |
| CAN | on-chip | flexcan |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |
| UART | on-chip | serial port-polling; serial port-interrupt |
| DMA | on-chip | dma |
| GPT | on-chip | gpt |
| WATCHDOG | on-chip | watchdog |
| ENET | on-chip | ethernet |
| SAI | on-chip | i2s |
| USB | on-chip | USB Device |
| HWINFO | on-chip | Unique device serial number |
| DISPLAY | on-chip | display |
| ACMP | on-chip | analog comparator |
| CAAM RNG | on-chip | entropy |
| FLEXSPI | on-chip | flash programming |

The default configuration can be found in the defconfig file:
`boards/arm/vmu_rt1170/vmu_rt1170_defconfig`

Other hardware features are not currently supported by the port.

### Connections and I/Os

The MIMXRT1170 SoC has six pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| WAKEUP | GPIO | SW7 |
| GPIO\_AD\_04 | GPIO | LED |
| GPIO\_AD\_24 | LPUART1\_TX | UART Console |
| GPIO\_AD\_25 | LPUART1\_RX | UART Console |
| GPIO\_LPSR\_00 | CAN3\_TX | flexcan |
| GPIO\_LPSR\_01 | CAN3\_RX | flexcan |
| GPIO\_AD\_29 | SPI1\_CS0 | spi |
| GPIO\_AD\_28 | SPI1\_CLK | spi |
| GPIO\_AD\_30 | SPI1\_SDO | spi |
| GPIO\_AD\_31 | SPI1\_SDI | spi |
| GPIO\_AD\_08 | LPI2C1\_SCL | i2c |
| GPIO\_AD\_09 | LPI2C1\_SDA | i2c |
| GPIO\_LPSR\_05 | LPI2C5\_SCL | i2c |
| GPIO\_LPSR\_04 | LPI2C5\_SDA | i2c |
| GPIO\_AD\_04 | FLEXPWM1\_PWM2 | pwm |
| GPIO\_AD\_32 | ENET\_MDC | Ethernet |
| GPIO\_AD\_33 | ENET\_MDIO | Ethernet |
| GPIO\_DISP\_B2\_02 | ENET\_TX\_DATA00 | Ethernet |
| GPIO\_DISP\_B2\_03 | ENET\_TX\_DATA01 | Ethernet |
| GPIO\_DISP\_B2\_04 | ENET\_TX\_EN | Ethernet |
| GPIO\_DISP\_B2\_05 | ENET\_REF\_CLK | Ethernet |
| GPIO\_DISP\_B2\_06 | ENET\_RX\_DATA00 | Ethernet |
| GPIO\_DISP\_B2\_07 | ENET\_RX\_DATA01 | Ethernet |
| GPIO\_DISP\_B2\_08 | ENET\_RX\_EN | Ethernet |
| GPIO\_DISP\_B2\_09 | ENET\_RX\_ER | Ethernet |
| GPIO\_AD\_17\_SAI1\_MCLK | SAI\_MCLK | SAI |
| GPIO\_AD\_21\_SAI1\_TX\_DATA00 | SAI1\_TX\_DATA | SAI |
| GPIO\_AD\_22\_SAI1\_TX\_BCLK | SAI1\_TX\_BCLK | SAI |
| GPIO\_AD\_23\_SAI1\_TX\_SYNC | SAI1\_TX\_SYNC | SAI |
| GPIO\_AD\_17\_SAI1\_MCLK | SAI1\_MCLK | SAI |
| GPIO\_AD\_20\_SAI1\_RX\_DATA00 | SAI1\_RX\_DATA00 | SAI |

### Serial Port

The MIMXRT1170 SoC has 12 UARTs.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board.

#### Using J-Link

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Connect the J-Link debugger through the debug adapter board.

### Configuring a Console

Use the USB-C from the debug adapter board to access the console with
the following settings for your serial terminal of choice (screen, minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b vmu_rt1170 samples/hello_world
west flash
```

You should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0-xxxx-xxxxxxxxxxxxx *****
Hello World! vmu_rt1170
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b vmu_rt1170 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0-xxxx-xxxxxxxxxxxxx *****
Hello World! vmu_rt1170
```
