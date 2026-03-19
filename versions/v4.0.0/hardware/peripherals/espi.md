---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/espi.html
original_path: hardware/peripherals/espi.html
---

# Enhanced Serial Peripheral Interface (eSPI) Bus

## Overview

The eSPI (enhanced serial peripheral interface) is a serial bus that is
based on SPI. It also features a four-wire interface (receive, transmit, clock
and target select) and three configurations: single IO, dual IO and quad IO.

The technical advancements include lower voltage signal levels (1.8V vs. 3.3V),
lower pin count, and the frequency is twice as fast (66MHz vs. 33MHz)
Because of its enhancements, the eSPI is used to replace the LPC
(lower pin count) interface, SPI, SMBus and sideband signals.

See [eSPI interface specification](https://downloadmirror.intel.com/27055/327432%20espi_base_specification%20R1-5.pdf) for additional details.

## API Reference

[ESPI Driver APIs](../../doxygen/html/group__espi__interface.md)

Related code samples

- [Enhanced Serial Peripheral Interface (eSPI)](../../samples/drivers/espi/README.md#espi "Use eSPI to connect to a slave device and exchange virtual wire packets.")Use eSPI to connect to a slave device and exchange virtual wire packets.
