---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/adi/max32680evkit/doc/index.html
original_path: boards/adi/max32680evkit/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MAX32680EVKIT

## Overview

The MAX32680 evaluation kit (EV kit) provides a platform
for evaluation capabilities of the MAX32680 microcontroller,
which is an advanced system-on-chip (SoC)
designed for industrial and medical sensors. Power regulation
and management is provided by a single-inductor
multiple-output (SIMO) buck regulator system and contains
the latest generation Bluetooth® 5.2 Low Energy
(LE) radio.

The Zephyr port is running on the MAX32680 MCU.

![MAX32680 EVKIT](../../../../_images/max32680evkit_img1.jpg)

## Hardware

- MAX32680 MCU:

  - Ultra-Low-Power Wireless Microcontroller

    - Internal 100MHz Oscillator
    - 512KB Flash and 128KB SRAM, Optional ECC on One 32KB SRAM Bank
  - Bluetooth 5.2 LE Radio

    - Dedicated, Ultra-Low-Power, 32-Bit RISC-VCoprocessor to Offload

    Timing-Critical Bluetooth Processing

    - Fully Open-Source Bluetooth 5.2 Stack Available
    - Supports AoA, AoD, LE Audio, and Mesh
    - High-Throughput (2Mbps) Mode•Long-Range (125kbps and 500kbps) Modes
    - Rx Sensitivity: -97.5dBm; Tx Power: +4.5dBm
    - Single-Ended Antenna Connection (50Ω)
  - Smart Integration Reduces BOM, Cost, and PCB Size

    - Two 16-Bit to 24-Bit Sigma-Delta ADCs
    - 12 Channels, Assignable to Either ADC
    - Flexible Resolution and Sample Rates
    - 24-Bits at 0.4ksps, 16-Bits at 4ksps
    - Four External Input, 10-Bit Sigma-Delta ADC 7.8ksps
    - 12-Bit DAC
    - On-Die Temperature Sensor
    - Digital Peripherals: Two SPI, Two I2C, up to FourUART, and up to 36 GPIOs
    - Timers: Six 32-Bit Timers, Two Watchdog Timers,Two Pulse Trains, 1-Wire® Master
  - Power Management Maximizes Battery Life

    - 2.0V to 3.6V Supply Voltage Range
    - Integrated SIMO Power Regulator
    - Dynamic Voltage Scaling (DVS)
    - 23.8μA/MHz ACTIVE Mode Current at 3.0VCoremark®
    - 4.4μA at 3.0V Retention Current for 32KB SRAM
    - Selectable SRAM Retention in Low-Power Modes
  - Robust Security and Reliability

    - TRNG
    - Secure Nonvolatile Key Storage and AES-128/192/256
    - Secure Boot to Protect IP/Firmware
    - Wide, -40°C to +85°C Operating Temperature
- External devices connected to the MAX32680 EVKIT:

  - SMA Connector for Attaching an External Bluetooth Antenna
  - 128 x 128 (1.45in) Color TFT Display with SPI Interface
  - Two Selectable On-Board, High-Precision Voltage References
  - USB 2.0 Micro B to Serial UARTs
  - UART1 and LPUART0 Interface is Selectable Through On-Board Jumpers
  - All GPIOs Signals Accessed Through 0.1in Headers
  - Access to Four Analog Inputs Through SMA Connectors Configured as Differential
  - Access to Eight Analog Inputs Through 0.1in Headers Configured as Single-End
  - Optional Discrete Filter for the Twelve Analog Inputs
  - DAC Accessed Through SMA Connector or Test Point
  - 10-Pin SWD Connector
  - 10-Pin RV JTAG Connector
  - Board Power Provided by USB Port
  - On-Board 3.3V LDO Regulator to Power MAX32680 Internal SIMO
  - Test Loops Provided to Supply Optional VCORE Power Externally
  - Individual Power Measurement on All IC Rails Through Jumpers
  - Two General Purpose LEDs and Two General Purpose Pushbutton Switches

### Supported Features

Below interfaces are supported by Zephyr on MAX32680EVKIT.

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| CLOCK | on-chip | clock and reset control |
| GPIO | on-chip | gpio |
| UART | on-chip | serial |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | VREGI | | Open | | --- | | Closed | | | Disconnects 3.3V power from the MAX32680 SIMO. | | --- | | Connects 3.3V power to the MAX32680 SIMO. | |
| JP2 | REF0P | | 2-1 | | --- | | 2-3 | | | Connects the external high-precision voltage refernce to REF0P. | | --- | | Connects the internal voltage refernce to REF0P. | |
| JP3 | REF0N | | Open | | --- | | Closed | | | Disconnects REF0N from ground. | | --- | | Connects REF0N to ground. | |
| JP4 | VDDIO\_AUX | | Open | | --- | | Closed | | | Disconnects VDDIO\_AUX from pull-ups and reference voltages. | | --- | | Connects VDDIO\_AUX to pull-ups and reference voltages. | |
| JP5 | VDDIOH | | Open | | --- | | Closed | | | Connects VREGO\_A to VDDIOH. | | --- | | Connects the 3.3V from the estrenal LDO to VDDIOH. | |
| JP6 | REF1P | | 2-1 | | --- | | 2-3 | | | Connects the external high-precision voltage refernce to REF1P. | | --- | | Connects the internal voltage refernce to REF1P. | |
| JP7 | REF1N | | Open | | --- | | Closed | | | Disconnects REF1N from ground. | | --- | | Connects REF1N to ground. | |
| JP8 | I2C0\_SDA I2C0\_SCL | | 2-1 | | --- | | 2-3 | | | Connects I2C0 pullups to VDDIO\_AUX (1.8V). | | --- | | Connects I2C0 pullups to 3.3V. | |
| JP9 | I2C1\_SDA I2C1\_SCL | | 2-1 | | --- | | 2-3 | | | Connects I2C1 pullups to VDDIO\_AUX (1.8V). | | --- | | Connects I2C1 pullups to 3.3V. | |
| JP10 | P0\_24 | | Open | | --- | | Closed | | | Disconnects red LED D1 from P0\_24. | | --- | | Connects red LED D1 to P0\_24. | |
| JP11 | P0\_25 | | Open | | --- | | Closed | | | Disconnects green LED D2 from P0\_25. | | --- | | Connects green LED D2 to P0\_25. | |
| JP12 | FSK\_IN | | Open | | --- | | Closed | | | Disconnects FSK\_IN from HART analog circuitry. | | --- | | Connects FSK\_IN to HART analog circuitry. | |
| JP13 | RCV\_FSK | | Open | | --- | | Closed | | | Disconnects RCV\_FSK from CC LOOP. | | --- | | Connects RCV\_FSK to CC LOOP. | |
| JP14 | FSK\_OUT | | Open | | --- | | Closed | | | Disconnects FSK\_OUT from HART analog circuitry. | | --- | | Connects FSK\_OUT to HART analog circuitry. | |
| JP15 | RCV\_FSK | | Open | | --- | | Closed | | | Disconnects RCV\_FSK from XFMR LOOP. | | --- | | Connects RCV\_FSK to XFMR LOOP. | |
| JP16 | RLOAD | | Open | | --- | | Closed | | | Disconnects 249 ohm resistor shunt from CC LOOP. | | --- | | Connects 249 ohm resistor shunt to CC LOOP. | |
| JP17 | FSK AMP GAIN | | Open | | --- | | Closed | | | Enables FSK variable amp gain. | | --- | | Disables FSK variable amp gain. | |
| JP18 | AMP BYPASS | | 2-1 | | --- | | 2-3 | | | Enables FSK amp. | | --- | | Bypasses FSK amp. | |
| JP19 | FSK AMP GAIN | | Open | | --- | | Closed | | | Enables FSK fixed amp gain. | | --- | | Disables FSK fixed amp gain. | |
| JP20 | HART\_RTS | | Open | | --- | | Closed | | | Enables HART\_RTS optical transceiver. | | --- | | Bypasses HART\_RTS optical transceiver. | |
| JP21 | RLOAD | | Open | | --- | | Closed | | | Disconnects 249 ohm resistor shunt from XFMR LOOP. | | --- | | Connects 249 ohm resistor shunt to XFMR LOOP. | |
| JP22 | UART0\_RX | | 2-1 | | --- | | 2-3 | | | Disconnects the USB - serial bridge from UART1\_RX (P0.12). | | --- | | Connects the USB - serial bridge to LPUART\_RX (P2.6). | |
| JP23 | UART0\_TX | | 2-1 | | --- | | 2-3 | | | Disonnects the USB - serial bridge from UART1\_TX (P0.13). | | --- | | Connects the USB - serial bridge to LPUART\_TX (P2.7). | |
| JP24 | | HART\_IN | | --- | | HART\_IN | | HART\_OUT | | HART\_OUT | | HART\_RTS | | HART\_RTS | | HART\_OCD | | HART\_OCD | | | Open | | --- | | 1-2 | | Open | | 2-3 | | Open | | 3-4 | | Open | | 4-5 | | | Disconnects TX of USB - serial bridge from HART\_IN (P0.1) | | --- | | Connects TX of USB - serial bridge to HART\_IN (P0.1). | | Disconnects RX of USB - serial bridge from HART\_OUT (P0.0). | | Connects RX of USB - serial bridge to HART\_OUT (P0.0). | | Disconnects RTS of USB - serial bridge from HART\_RTS (P0.3). | | Connects TX of USB - serial bridge to HART\_RTS (P0.3). | | Disconnects RTS of USB - serial bridge from HART\_OCD (P0.2). | | Connects TX of USB - serial bridge to HART\_OCD (P0.2). | |
| JP25 | RSTN | | Open | | --- | | Close | | | Disconnects DUT\_3V3\_RSTN from RSTN. | | --- | | Connects DUT\_3V3\_RSTN to RSTN. | |

## Programming and Debugging

### Flashing

The MAX32680 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, JH10.
Logic levels are set to 1.8V (VDDIO\_AUX).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32680EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32680evkit.html#eb-overview)
