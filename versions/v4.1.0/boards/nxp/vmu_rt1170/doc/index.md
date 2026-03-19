---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/vmu_rt1170/doc/index.html
original_path: boards/nxp/vmu_rt1170/doc/index.html
---

# VMU RT1170

Board Overview

[![../../../../_images/vmu_rt1170.jpg](../../../../_images/vmu_rt1170.jpg)
](../../../../_images/vmu_rt1170.jpg)

VMU RT1170

Name:
:   `vmu_rt1170`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1176

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/vmu_rt1170/doc/index.rst/../..)

## Overview

The VMU RT1170 features an i.MX RT1176 dual core MCU with the
Cortex-M7 core at 1 GHz and a Cortex-M4 at 400 MHz.
The i.MX RT1176 MCU offers support over a wide temperature range
and is qualified for consumer, industrial and automotive markets.
The VMU RT1170 is the default VMU for CogniPilot’s Cerebri, a
Zephyr RTOS based Autopilot.

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
- RC IN

  - RC input connector for SBUS compatible RC receivers

For more information about the MIMXRT1176 SoC and VMU RT1170 board, see
these references:

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
| PWM | on-chip | flexpwm, qtmr |
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
| ACMP | on-chip | sensor |
| CAAM RNG | on-chip | entropy |
| FLEXSPI | on-chip | flash programming |

The default configuration can be found in
[boards/nxp/vmu\_rt1170/vmu\_rt1170\_mimxrt1176\_cm7\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/vmu_rt1170/vmu_rt1170_mimxrt1176_cm7_defconfig)

Other hardware features are not currently supported by the port.

### Connections and I/Os

The MIMXRT1170 SoC has six pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_00 | FLEXCAN2\_TX | CAN2\_TX |
| GPIO\_AD\_01 | FLEXCAN2\_RX | CAN2\_RX |
| GPIO\_AD\_02 | LPUART8\_TXD | UART8\_TX\_TELEM2 |
| GPIO\_AD\_03 | LPUART8\_RXD | UART8\_RX\_TELEM2 |
| GPIO\_AD\_04 | LPUART8\_CTS\_B | UART8\_CTS\_TELEM2 |
| GPIO\_AD\_05 | LPUART8\_RTS\_B | UART8\_RTS\_TELEM2 |
| GPIO\_AD\_06 | FLEXCAN1\_TX | CAN1\_TX |
| GPIO\_AD\_07 | FLEXCAN1\_RX | CAN1\_RX |
| GPIO\_AD\_08 | LPI2C1\_SCL | I2C1\_SCL\_GPS1 |
| GPIO\_AD\_09 | LPI2C1\_SDA | I2C1\_SDA\_GPS1 |
| GPIO\_AD\_10 | LPADC1\_CH2A | SCALED\_VDD\_3V3\_SENSORS1 |
| GPIO\_AD\_11 | LPADC1\_CH2B | SCALED\_VDD\_3V3\_SENSORS2 |
| GPIO\_AD\_12 | LPADC1\_CH3A | SCALED\_VDD\_3V3\_SENSORS3 |
| GPIO\_AD\_13 | LPADC1\_CH3B | SCALED\_V5 |
| GPIO\_AD\_14 | LPADC1\_CH4A | ADC\_6V6 |
| GPIO\_AD\_15 | LPUART10\_TXD | UART10\_TX\_TELEM3 |
| GPIO\_AD\_16 | LPADC1\_CH5A | ADC\_3V3 |
| GPIO\_AD\_17 | LPADC1\_CHB | SCALED\_VDD\_3V3\_SENSORS4 |
| GPIO\_AD\_18 | LPI2C2\_SCL | I2C2\_SCL\_GPS2 |
| GPIO\_AD\_19 | LPI2C2\_SDA | I2C2\_SDA\_GPS2 |
| GPIO\_AD\_20 | GPIO3\_IO19 | SPI1\_DRDY1\_SENSOR1 |
| GPIO\_AD\_21 | GPIO3\_IO20 | SPI3\_DRDY1\_SENSOR3 |
| GPIO\_AD\_22 | LPADC2\_CH2A | HW\_VER\_SENSE |
| GPIO\_AD\_23 | LPADC2\_CH2B | HW\_REV\_SENSE |
| GPIO\_AD\_24 | LPSPI2\_SCK | SPI2\_SCK\_SENSOR2 |
| GPIO\_AD\_25 | LPSPI2\_PCS0 | SPI2\_nCS0\_SENSOR2 |
| GPIO\_AD\_26 | LPSPI2\_SOUT | SPI2\_MOSI\_SENSOR2 |
| GPIO\_AD\_27 | LPSPI2\_SIN | SPI2\_MISO\_SENSOR2 |
| GPIO\_AD\_28 | LPUART5\_TXD | UART5\_TX\_GPS2 |
| GPIO\_AD\_29 | LPUART5\_RXD | UART5\_RX\_GPS2 |
| GPIO\_AD\_30 | LPUART3\_TXD | UART3\_TX\_GPS1 |
| GPIO\_AD\_31 | LPUART3\_RXD | UART3\_RX\_GPS1 |
| GPIO\_AD\_32 | USDHC1\_CD\_B | USDHC1\_CD |
| GPIO\_AD\_33 | LPUART10\_RXD | UART10\_RX\_TELEM3 |
| GPIO\_AD\_34 | LPUART10\_CTS\_B | UART10\_CTS\_TELEM3 |
| GPIO\_AD\_35 | LPUART10\_RTS\_B | UART10\_RTS\_TELEM3 |
| GPIO\_DISP\_B1\_00 | ENET\_1G\_RX\_EN | ETH\_CRS\_DV |
| GPIO\_DISP\_B1\_01 | ENET\_1G\_RX\_ER | ETH\_RX\_ER |
| GPIO\_DISP\_B1\_02 | LPUART1\_TXD | UART1\_TX\_DEBUG |
| GPIO\_DISP\_B1\_03 | LPUART1\_RXD | UART1\_RX\_DEBUG |
| GPIO\_DISP\_B1\_04 | LPUART4\_RXD | UART4\_RX\_TELEM1 |
| GPIO\_DISP\_B1\_05 | LPUART4\_CTS\_B | UART4\_CTS\_TELEM1 |
| GPIO\_DISP\_B1\_06 | LPUART4\_TXD | UART4\_TX\_TELEM1 |
| GPIO\_DISP\_B1\_07 | LPUART4\_RTS\_B | UART4\_RTS\_TELEM1 |
| GPIO\_DISP\_B1\_08 | ENET\_1G\_TDATA1 | ETH\_TXD1 |
| GPIO\_DISP\_B1\_09 | ENET\_1G\_TDATA0 | ETH\_TXD0 |
| GPIO\_DISP\_B1\_10 | ENET\_1G\_TX\_EN | ETH\_TX\_EN |
| GPIO\_DISP\_B1\_11 | ENET\_1G\_REF\_CLK | ETH\_REF\_CLK |
| GPIO\_DISP\_B2\_00 | GPIO5\_IO01 | nLED\_RED |
| GPIO\_DISP\_B2\_01 | GPIO5\_IO02 | nLED\_GREEN |
| GPIO\_DISP\_B2\_02 | ARM\_TRACE0 | TRACED0 |
| GPIO\_DISP\_B2\_03 | ARM\_TRACE1 | TRACED1 |
| GPIO\_DISP\_B2\_04 | ARM\_TRACE2 | TRACED2 |
| GPIO\_DISP\_B2\_05 | ARM\_TRACE3 | TRACED3 |
| GPIO\_DISP\_B2\_06 | ARM\_TRACE\_CLK | TRACECLK |
| GPIO\_DISP\_B2\_07 | ARM\_TRACE\_SWO | TRACESWO |
| GPIO\_DISP\_B2\_08 | GPIO5\_IO09 | ETH\_POWER\_EN |
| GPIO\_DISP\_B2\_09 | GPIO5\_IO10 | ETH\_PHY\_nINT |
| GPIO\_DISP\_B2\_10 | LPI2C3\_SCL | I2C3\_SCL\_FMU |
| GPIO\_DISP\_B2\_11 | LPI2C3\_SDA | I2C3\_SDA\_FMU |
| GPIO\_DISP\_B2\_12 | LPSPI4\_SCK | SPI4\_SCK\_SENSOR4 |
| GPIO\_DISP\_B2\_13 | LPSPI4\_SIN | SPI4\_MISO\_SENSOR4 |
| GPIO\_DISP\_B2\_14 | LPSPI4\_SOUT | SPI4\_MOSI\_SENSOR4 |
| GPIO\_DISP\_B2\_15 | LPSPI4\_PCS0 | SPI4\_nCS0\_SENSOR4 |
| GPIO\_EMC\_B1\_00 | FLEXPWM4\_PWM0\_A + FLEXIO1\_IO00 | FMU\_CH11 |
| GPIO\_EMC\_B1\_01 | GPIO1\_IO01 | VDD\_3V3\_SD\_CARD\_EN |
| GPIO\_EMC\_B1\_02 | FLEXPWM4\_PWM1\_A + FLEXIO1\_IO02 | FMU\_CH12 |
| GPIO\_EMC\_B1\_03 | GPIO1\_IO03 | FMU\_nSAFETY\_SWITCH\_LED\_OUT |
| GPIO\_EMC\_B1\_04 | GPIO1\_IO04 | NFC\_GPIO |
| GPIO\_EMC\_B1\_05 | GPIO1\_IO05 | SPI6\_DRDY1\_EXTERNAL1 |
| GPIO\_EMC\_B1\_06 | FLEXPWM2\_PWM0\_A + FLEXIO1\_IO06 | FMU\_CH4 |
| GPIO\_EMC\_B1\_07 | GPIO1\_IO07 | SPI6\_DRDY2\_EXTERNAL1 |
| GPIO\_EMC\_B1\_08 | FLEXPWM2\_PWM1\_A + FLEXIO1\_IO08 | FMU\_CH5 |
| GPIO\_EMC\_B1\_09 | GPT5\_CAPTURE1 | FMU\_PPM\_INPUT |
| GPIO\_EMC\_B1\_10 | FLEXPWM2\_PWM2\_A + FLEXIO1\_IO10 | FMU\_CH6 |
| GPIO\_EMC\_B1\_11 | GPIO1\_IO11 | SPI6\_nRESET\_EXTERNAL1 |
| GPIO\_EMC\_B1\_12 | GPIO1\_IO12 | VDD\_5V\_HIPOWER\_nOC |
| GPIO\_EMC\_B1\_13 | GPIO1\_IO13 | nLED\_BLUE |
| GPIO\_EMC\_B1\_14 | GPIO1\_IO14 | VDD\_3V3\_SENSORS3\_EN |
| GPIO\_EMC\_B1\_15 | GPIO1\_IO15 | VDD\_5V\_PERIPH\_nOC |
| GPIO\_EMC\_B1\_16 | GPIO1\_IO16 | SPI4\_DRDY1\_SENSOR4 |
| GPIO\_EMC\_B1\_17 | GPIO1\_IO17 | nARMED |
| GPIO\_EMC\_B1\_18 | TMR2\_TIMER0 | SPIX\_SYNC |
| GPIO\_EMC\_B1\_19 | FLEXPWM2\_PWM3\_A + FLEXIO1\_IO19 | FMU\_CH7 |
| GPIO\_EMC\_B1\_20 | TMR4\_TIMER0 | FMU\_CAP1 |
| GPIO\_EMC\_B1\_21 | FLEXPWM3\_PWM3\_A + FLEXIO1\_IO21 | FMU\_CH10 |
| GPIO\_EMC\_B1\_22 | GPIO1\_IO22 | VDD\_3V3\_SENSORS2\_EN |
| GPIO\_EMC\_B1\_23 | FLEXPWM1\_PWM0\_A | FMU\_CH1 |
| GPIO\_EMC\_B1\_24 | GPIO1\_IO24 | FMU\_SAFETY\_SWITCH\_IN |
| GPIO\_EMC\_B1\_25 | FLEXPWM1\_PWM1\_A + FLEXIO1\_IO25 | FMU\_CH2 |
| GPIO\_EMC\_B1\_26 | GPIO1\_IO26 | HW\_VER\_REV\_DRIVE |
| GPIO\_EMC\_B1\_27 | FLEXPWM1\_PWM2\_A + FLEXIO1\_IO27 | FMU\_CH3 |
| GPIO\_EMC\_B1\_28 | GPIO1\_IO28 | nPOWER\_IN\_A |
| GPIO\_EMC\_B1\_29 | FLEXPWM3\_PWM0\_A + FLEXIO1\_IO29 | FMU\_CH8 |
| GPIO\_EMC\_B1\_30 | GPIO1\_IO30 | nPOWER\_IN\_B |
| GPIO\_EMC\_B1\_31 | FLEXPWM3\_PWM1\_A + FLEXIO1\_IO31 | FMU\_CH9 |
| GPIO\_EMC\_B1\_32 | GPIO2\_IO00 | nPOWER\_IN\_C |
| GPIO\_EMC\_B1\_33 | GPIO2\_IO01 | VDD\_3V3\_SENSORS1\_EN |
| GPIO\_EMC\_B1\_34 | GPIO2\_IO02 | VDD\_5V\_PERIPH\_nEN |
| GPIO\_EMC\_B1\_35 | GPIO2\_IO03 | I2C2\_DRDY1 |
| GPIO\_EMC\_B1\_36 | GPIO2\_IO04 | VDD\_3V3\_SENSORS4\_EN |
| GPIO\_EMC\_B1\_37 | GPIO2\_IO05 | VDD\_5V\_HIPOWER\_nEN |
| GPIO\_EMC\_B1\_38 | GPIO2\_IO06 | VDD\_3V3\_SPEKTRUM\_POWER\_EN |
| GPIO\_EMC\_B1\_39 | GPIO2\_IO07 | SPI2\_DRDY1\_SENSOR2 |
| GPIO\_EMC\_B1\_40 | LPUART6\_TXD | UART6\_TX\_TO\_IO\_\_RC\_INPUT |
| GPIO\_EMC\_B1\_41 | LPUART6\_RXD | UART6\_RX\_FROM\_IO\_\_NC |
| GPIO\_EMC\_B2\_00 | LPSPI1\_SCK | SPI1\_SCK\_SENSOR1 |
| GPIO\_EMC\_B2\_01 | LPSPI1\_PCS0 | SPI1\_nCS0\_SENSOR1 |
| GPIO\_EMC\_B2\_02 | LPSPI1\_SOUT | SPI1\_MOSI\_SENSOR1 |
| GPIO\_EMC\_B2\_03 | LPSPI1\_SIN | SPI1\_MISO\_SENSOR1 |
| GPIO\_EMC\_B2\_04 | LPSPI3\_SCK | SPI3\_SCK\_SENSOR3 |
| GPIO\_EMC\_B2\_05 | LPSPI3\_PCS0 | SPI3\_nCS0\_SENSOR3 |
| GPIO\_EMC\_B2\_06 | LPSPI3\_SOUT | SPI3\_MOSI\_SENSOR3 |
| GPIO\_EMC\_B2\_07 | LPSPI3\_SIN | SPI3\_MISO\_SENSOR3 |
| GPIO\_EMC\_B2\_08 | LPSPI3\_PCS1 | SPI3\_nCS1\_SENSOR3 |
| GPIO\_EMC\_B2\_09 | TMR1\_TIMER0 | BUZZER\_1 |
| GPIO\_EMC\_B2\_10 | FLEXSPI2\_A\_SCLK | FLEXSPI2\_SCK\_FRAM |
| GPIO\_EMC\_B2\_11 | FLEXSPI2\_A\_SS0\_B | FLEXSPI2\_nCS0\_FRAM |
| GPIO\_EMC\_B2\_12 | GPIO2\_IO22 | GPIO\_EMC\_B2\_12 |
| GPIO\_EMC\_B2\_13 | FLEXSPI2\_A\_DATA0 | FLEXSPI2\_DATA0\_FRAM |
| GPIO\_EMC\_B2\_14 | FLEXSPI2\_A\_DATA1 | FLEXSPI2\_DATA1\_FRAM |
| GPIO\_EMC\_B2\_15 | ENET\_1G\_RDATA0 | ETH\_RXD0 |
| GPIO\_EMC\_B2\_16 | ENET\_1G\_RDATA1 | ETH\_RXD1 |
| GPIO\_EMC\_B2\_17 | TMR3\_TIMER0 | HEATER |
| GPIO\_EMC\_B2\_18 | GPIO2\_IO28 | SPI3\_DRDY2\_SENSOR3 |
| GPIO\_EMC\_B2\_19 | ENET\_1G\_MDC | ETH\_MDC |
| GPIO\_EMC\_B2\_20 | ENET\_1G\_MDIO | ETH\_MDIO |
| GPIO\_LPSR\_00 | FLEXCAN3\_TX | CAN3\_TX |
| GPIO\_LPSR\_01 | FLEXCAN3\_RX | CAN3\_RX |
| GPIO\_LPSR\_02 | SRC\_BOOT\_MODE00 | BT\_MODE0 |
| GPIO\_LPSR\_03 | SRC\_BOOT\_MODE01 | BT\_MODE1 |
| GPIO\_LPSR\_04 | LPUART11\_TXD | UART11\_TX\_EXTERNAL2 |
| GPIO\_LPSR\_05 | LPUART11\_RXD | UART11\_RX\_EXTERNAL2 |
| GPIO\_LPSR\_06 | LPI2C6\_SDA | I2C6\_SDA\_EXTERNAL2 |
| GPIO\_LPSR\_07 | LPI2C6\_SCL | I2C6\_SCL\_EXTERNAL2 |
| GPIO\_LPSR\_08 | LPSPI6\_PCS1 | SPI6\_nCS1\_EXTERNAL1 |
| GPIO\_LPSR\_09 | LPSPI6\_PCS0 | SPI6\_nCS0 |
| GPIO\_LPSR\_10 | LPSPI6\_SCK | SPI6\_SCK\_EXTERNAL1 |
| GPIO\_LPSR\_11 | LPSPI6\_SOUT | SPI6\_MOSI\_EXTERNAL1 |
| GPIO\_LPSR\_12 | LPSPI6\_SIN | SPI6\_MISO\_EXTERNAL1 |
| GPIO\_LPSR\_13 | JTAG\_MOD | NC\_JTAG\_MOD\_PD |
| GPIO\_LPSR\_14 | SWD\_CLK | FMU\_SWCLK |
| GPIO\_LPSR\_15 | SWD\_DIO | FMU\_SWDIO |
| GPIO\_SD\_B1\_00 | USDHC1\_CMD | USDHC1\_CMD |
| GPIO\_SD\_B1\_01 | USDHC1\_CLK | USDHC1\_CLK |
| GPIO\_SD\_B1\_02 | USDHC1\_DATA0 | USDHC1\_DATA0 |
| GPIO\_SD\_B1\_03 | USDHC1\_DATA1 | USDHC1\_DATA1 |
| GPIO\_SD\_B1\_04 | USDHC1\_DATA2 | USDHC1\_DATA2 |
| GPIO\_SD\_B1\_05 | USDHC1\_DATA3 | USDHC1\_DATA3 |
| GPIO\_SD\_B2\_00 | FLEXSPI1\_B\_DATA3 | FLEXSPI1\_DATA7\_HYPERFLASH |
| GPIO\_SD\_B2\_01 | FLEXSPI1\_B\_DATA2 | FLEXSPI1\_DATA6\_HYPERFLASH |
| GPIO\_SD\_B2\_02 | FLEXSPI1\_B\_DATA1 | FLEXSPI1\_DATA5\_HYPERFLASH |
| GPIO\_SD\_B2\_03 | FLEXSPI1\_B\_DATA0 | FLEXSPI1\_DATA4\_HYPERFLASH |
| GPIO\_SD\_B2\_04 | FLEXSPI1\_B\_SCLK | FLEXSPI1\_nSCK\_HYPERFLASH |
| GPIO\_SD\_B2\_05 | FLEXSPI1\_A\_DQS | FLEXSPI1\_DQS\_HYPERFLASH |
| GPIO\_SD\_B2\_06 | FLEXSPI1\_A\_SS0\_B | FLEXSPI1\_nCS0\_HYPERFLASH |
| GPIO\_SD\_B2\_07 | FLEXSPI1\_A\_SCLK | FLEXSPI1\_SCK\_HYPERFLASH |
| GPIO\_SD\_B2\_08 | FLEXSPI1\_A\_DATA0 | FLEXSPI1\_DATA0\_HYPERFLASH |
| GPIO\_SD\_B2\_09 | FLEXSPI1\_A\_DATA0 | FLEXSPI1\_DATA1\_HYPERFLASH |
| GPIO\_SD\_B2\_10 | FLEXSPI1\_A\_DATA2 | FLEXSPI1\_DATA2\_HYPERFLASH |
| GPIO\_SD\_B2\_11 | FLEXSPI1\_A\_DATA3 | FLEXSPI1\_DATA3\_HYPERFLASH |
| USB1\_DN | USB\_OG1\_DN | USB\_D\_N |
| USB1\_DP | USB\_OTG1\_DP | USB\_D\_P |
| USB1\_VBUS | USB\_OTG1\_VBUS | VBUS |

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

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

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

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

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
