---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/gsm_modem/README.html
original_path: samples/net/gsm_modem/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Generic GSM modem

## Overview

The Zephyr GSM modem sample application allows user to have a connection
to GPRS network. The connection to GSM modem is done using
[PPP (Point-to-Point Protocol)](../../../connectivity/networking/api/ppp.md#ppp).

The source code of this sample application can be found at:
[samples/net/gsm\_modem](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/gsm_modem).

## Requirements

- GSM modem card. The sample has been tested with SIMCOM SIM808 card. All
  GSM modem cards should work as long as they support **AT+CGDCONT** command.
- Almost any Zephyr enabled board with sufficient resources can be used.
  The sample has been tested with [reel board](../../../boards/arm/reel_board/doc/index.md#reel-board).

## Build and Running

If you are using an external modem like the SIMCOM card, then connect
the necessary pins like RX and TX from your Zephyr target board to the
modem card. Internal modems, like what is found in [Particle Boron](../../../boards/arm/particle_boron/doc/index.md#particle-boron)
board, are not yet supported.

```shell
west build -b reel_board samples/net/gsm_modem -- -DCONFIG_MODEM_GSM_APN=\"internet\"
west flash
```

Note that you might need to change the APN name according to your GSM network
configuration.
