---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/beagle/beagleplay/doc/beagleplay_cc1352p7.html
original_path: boards/beagle/beagleplay/doc/beagleplay_cc1352p7.html
---

# BeaglePlay (CC1352)

Board Overview

[![../../../../_images/beagle_play.webp](../../../../_images/beagle_play.webp)
](../../../../_images/beagle_play.webp)

BeaglePlay (CC1352)

Vendor:
:   BeagleBoard.org Foundation

Architecture:
:   arm

SoC:
:   cc1352p7

## Overview

BeagleBoard.org BeaglePlay is an open hardware single board computer based on a TI Sitara AM6254
quad-core ARM Cortex-A53 SoC with an external TI SimpleLink multi-standard CC1352P7 wireless MCU
providing long-range, low-power connectivity.

## Hardware

- Processors

  - TI Sitara AM6252 SoC

    - 4x ARM Cortex-A53
    - ARM Cortex-R5
    - ARM Cortex-M4
    - Dual-core 32-bit RISC Programmble Real-Time Unit (PRU)
  - TI SimpleLink CC1352P7 Wireless MCU

    - ARM Cortex-M4F programmable MCU
    - ARM Cortex-M0+ software-defined radio processor
- Memory

  - 2GB DDR4
  - 16GB eMMC flash
  - I2C EEPROM
- Wired connectivity

  - Gigabit Ethernet (RJ45)
  - Single-pair Ethernet with 5V/250mA PoDL output (RJ11)
  - HDMI
  - USB Type-A (host)
  - USB Type-C (client/power)
- Wireless connectivity

  - TI WL1807 2.4GHz/5GHz WiFi
  - BLE/SubG via CC1352P7
- Expansion

  - mikroBUS
  - Grove
  - QWIIC

BeaglePlay ARM Cortex-A53 CPUs typically run Linux, while the CC1352P7 Cortex-M4 typically runs Zephyr.

### Supported Features

The `beagleplay/cc1352p7` board target supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GPIO | on-chip | gpio |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PINMUX | on-chip | pinmux |
| UART | on-chip | serial |
| RADIO | on-chip | ieee802154 |

### Connections and IOs

CC1352 reset is connected to AM62 GPIO0\_14.

| Pin | Function | Usage |
| --- | --- | --- |
| DIO5 | N/C |  |
| DIO6 | N/C |  |
| DIO7 | N/C |  |
| DIO8 | N/C |  |
| DIO9 | N/C |  |
| DIO10 | N/C |  |
| DIO11 | N/C |  |
| DIO12 | CC1352\_RX | AM62 UART6\_TXD |
| DIO13 | CC1352\_TX | AM62 UART6\_RXD |
| DIO14 | N/C |  |
| DIO15 | CC1352\_BOOT | AM62 GPIO0\_13 |
| DIO16 | CC1352\_TDO | TAG-CONNECT TDO |
| DIO17 | CC1352\_TDI | TAG-CONNECT TDI |
| DIO18 | N/C |  |
| DIO19 | N/C |  |
| DIO20 | N/C |  |
| DIO21 | N/C |  |
| DIO22 | N/C |  |
| DIO23 | N/C |  |
| DIO24 | N/C |  |
| DIO25 | N/C |  |
| DIO26 | N/C |  |
| DIO27 | LED1 | CC1352\_LED1 yellow LED9 |
| DIO28 | LED2 | CC1352\_LED2 yellow LED8 |
| DIO29 | RF\_PA | SubG/PA Antenna mux PA enable |
| DIO30 | RF\_SUB1G | SubG/PA Antenna mux SubG enable |

## Programming and Debugging

### Flashing

To flash, disable the existing driver that ties up the serial port and use
the customized BSL Python script.

1. Ensure the bcfserial or gb-beagleplay driver isn’t blocking the serial port. This can be done by
   loading :file: `/overlays/k3-am625-beagleplay-bcfserial-no-firmware.dtbo` or selecting uboot
   entry which disables bcfserial/gb-beagleplay.
2. Now reboot the board.

   ```shell
   sudo shutdown -r now
   ```
3. Install CC1352-flasher if not already installed

   ```shell
   if ! command -v cc1352_flasher &> /dev/null; then pip install cc1352-flasher; fi
   ```
4. Flash the CC1352P7

   ```shell
   west flash
   ```

### Debugging

For debugging, you can use the serial port or JTAG. You can use OpenOCD
over the Tag-Connect header on the board.

- Tagconnect JTAG

## References
