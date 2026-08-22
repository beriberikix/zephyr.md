---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/openthread_rcp_arduino/doc/index.html
original_path: boards/shields/openthread_rcp_arduino/doc/index.html
---

# OpenThread RCP over Arduino header

## Overview

This (virtual) shield can be used to connect a board with an Arduino R3 compatible header to an
external [OpenThread RCP](https://openthread.io/platforms/co-processor) [[1]](#id1) device. The RCP device would function as the Thread radio, while another
board can function as the OpenThread host.

## Requirements

An RCP radio device is needed for this shield to work. As an example, the reference from
OpenThread using the [nRF52840 DK](../../../nordic/nrf52840dk/doc/index.md#nrf52840dk) is chosen as a demonstration. Refer to the
[OpenThread on nRF52840 Example website](https://github.com/openthread/ot-nrf528xx/blob/main/src/nrf52840/README.md) [[2]](#id3).

Both UART and SPI can be used as the transport, depending on the board connections.

The following was executed on Ubuntu 24.04 to build and flash the RCP firmware:

### Preparation

```shell
git clone https://github.com/openthread/ot-nrf528xx.git --recurse-submodules
cd ot-nrf528xx
python3 -m venv .venv
source .venv/bin/activate
./script/bootstrap
```

### Building

UARTSPI

```shell
# Set -DOT_PLATFORM_DEFINES="UART_HWFC_ENABLED=1" to enable flow control
./script/build nrf52840 UART_trans -DOT_PLATFORM_DEFINES="UART_HWFC_ENABLED=0"
```

```shell
./script/build nrf52840 SPI_trans_NCP
```

### Flashing

```shell
arm-none-eabi-objcopy -O ihex build/bin/ot-rcp build/bin/ot-rcp.hex
nrfjprog -f nrf52 --chiperase --program build/bin/ot-rcp.hex --reset
```

### Pins Assignments

The RCP firmware comes with default pins assigned, the following table lists both the Arduino header
pins and the nRF52840DK pins.

UARTSPI

| Arduino Header Pin | Function (host) | nRF52840 DK Pin |
| --- | --- | --- |
| D0 | UART RX | P0.06 |
| D1 | UART TX | P0.08 |
| Host specific | UART CTS | P0.05 (flow control) |
| Host specific | UART RTS | P0.07 (flow control) |

| Arduino Header Pin | Function | nRF52840 DK Pin |
| --- | --- | --- |
| D8 | RSTn | P0.18/RESET |
| D9 | INTn | P0.30 |
| D10 | SPI CSn | P0.29 |
| D11 | SPI MOSI | P0.04 |
| D12 | SPI MISO | P0.28 |
| D13 | SPI SCK | P0.03 |

## Programming

Include `--shield openthread_rcp_arduino_serial` or `--shield openthread_rcp_arduino_spi`
when you invoke `west build` for projects utilizing this shield. For example:

UARTSPI

```shell
# From the root of the zephyr repository
west build -b stm32h573i_dk/stm32h573xx --shield openthread_rcp_arduino_serial samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-ot-rcp-host-uart.conf"
```

```shell
# From the root of the zephyr repository
west build -b stm32h573i_dk/stm32h573xx --shield openthread_rcp_aduino_spi samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-ot-rcp-host-uart.conf"
```

## References

[[1](#id2)]

[https://openthread.io/platforms/co-processor](https://openthread.io/platforms/co-processor)

[[2](#id4)]

[https://github.com/openthread/ot-nrf528xx/blob/main/src/nrf52840/README.md](https://github.com/openthread/ot-nrf528xx/blob/main/src/nrf52840/README.md)
