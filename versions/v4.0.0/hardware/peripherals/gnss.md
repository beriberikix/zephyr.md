---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/gnss.html
original_path: hardware/peripherals/gnss.html
---

# GNSS (Global Navigation Satellite System)

## Overview

GNSS is a general term which covers satellite systems used for
navigation, like GPS (Global Positioning System). GNSS services
are usually accessed through GNSS modems which receive and
process GNSS signals to determine their position, or more
specifically, their antennas position. They usually
additionally provide a precise time synchronization mechanism,
commonly named PPS (Pulse-Per-Second).

## Subsystem support

The GNSS subsystem is based on the [Modem modules](../../services/modem/index.md#modem). The GNSS
subsystem covers everything from sending and receiving commands
to and from the modem, to parsing, creating and processing
NMEA0183 messages.

Adding support for additional NMEA0183 based GNSS modems
requires little more than implementing power management
and configuration for the specific GNSS modem.

Adding support for GNSS modems which use other protocols and/or
buses than the usual NMEA0183 over UART is possible, but will
require a bit more work from the driver developer.

## Configuration Options

Related configuration options:

- [`CONFIG_GNSS`](../../kconfig.md#CONFIG_GNSS "CONFIG_GNSS")
- [`CONFIG_GNSS_SATELLITES`](../../kconfig.md#CONFIG_GNSS_SATELLITES "CONFIG_GNSS_SATELLITES")
- [`CONFIG_GNSS_DUMP_TO_LOG`](../../kconfig.md#CONFIG_GNSS_DUMP_TO_LOG "CONFIG_GNSS_DUMP_TO_LOG")

## Navigation Reference

[Navigation](../../doxygen/html/group__navigation.md)

Related code samples

- [GNSS](../../samples/drivers/gnss/README.md#gnss "Connect to a GNSS device to obtain time, navigation data, and satellite information.")Connect to a GNSS device to obtain time, navigation data, and satellite information.

## GNSS API Reference

[GNSS Interface](../../doxygen/html/group__gnss__interface.md)

Related code samples

- [GNSS](../../samples/drivers/gnss/README.md#gnss "Connect to a GNSS device to obtain time, navigation data, and satellite information.")Connect to a GNSS device to obtain time, navigation data, and satellite information.
