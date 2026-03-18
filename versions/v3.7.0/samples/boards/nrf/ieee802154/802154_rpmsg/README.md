---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/nrf/ieee802154/802154_rpmsg/README.html
original_path: samples/boards/nrf/ieee802154/802154_rpmsg/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nRF IEEE 802.15.4: Serialization RPMsg

## Overview

This sample exposes IEEE 802.15.4 radio driver support
to another device or CPU using the RPMsg transport which is
a part of [OpenAMP](https://github.com/OpenAMP/open-amp/).

## Requirements

- A board with nRF53 SoC

## Building and Running

This sample can be found under [samples/boards/nrf/ieee802154/802154\_rpmsg](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nrf/ieee802154/802154_rpmsg)
in the Zephyr tree.

To use this application, you need a board with nRF53 SoC.
You can then build this application and flash it onto your board in
the usual way. See [Supported Boards](../../../../../boards/index.md#boards) for board-specific building and
programming information.

To test this sample, you need a separate device/CPU that acts as 802.15.4
serialization RPMsg peer.
This sample is compatible with the Nordic 802.15.4 serialization. See the
[`CONFIG_NRF_802154_SER_HOST`](../../../../../kconfig.md#CONFIG_NRF_802154_SER_HOST "CONFIG_NRF_802154_SER_HOST") configuration option for more information.

The sample is configured to be energy efficient by disabling:
:   - Serial Console (in `prj.conf`)
    - Logger (in `prj.conf`)
