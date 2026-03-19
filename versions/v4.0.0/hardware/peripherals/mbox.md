---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/mbox.html
original_path: hardware/peripherals/mbox.html
---

# Multi-Channel Inter-Processor Mailbox (MBOX)

## Overview

An MBOX device is a peripheral capable of passing signals (and data depending
on the peripheral) between CPUs and clusters in the system. Each MBOX instance
is providing one or more channels, each one targeting one other CPU cluster
(multiple channels can target the same cluster).

## API Reference

[MBOX Interface](../../doxygen/html/group__mbox__interface.md)

Related code samples

- [MBOX](../../samples/drivers/mbox/README.md#mbox "Perform inter-processor mailbox communication using the MBOX API.")Perform inter-processor mailbox communication using the MBOX API.
- [MBOX Data](../../samples/drivers/mbox_data/README.md#mbox_data "Perform inter-processor mailbox communication using the MBOX API with data.")Perform inter-processor mailbox communication using the MBOX API with data.
