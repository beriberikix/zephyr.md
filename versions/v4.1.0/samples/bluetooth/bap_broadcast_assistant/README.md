---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/bap_broadcast_assistant/README.html
original_path: samples/bluetooth/bap_broadcast_assistant/README.html
---

# Basic Audio Profile (BAP) Broadcast Audio Assistant

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/bap_broadcast_assistant/README.rst/..)

## Overview

Application demonstrating the BAP Broadcast Assistant functionality.

The sample will automatically try to connect to a device in the BAP Scan Delegator
role (advertising support for the Broadcast Audio Scan Service (BASS)).
It will then search for a broadcast source and (if found) add the broadcast ID to
the BAP Scan Delegator.

Practical use of this sample requires a sink (e.g. the BAP Broadcast Audio Sink sample or
a set of BAP Broadcast capable earbuds) and a source (e.g. the BAP Broadcast Audio
Source sample).

This sample can be found under
[samples/bluetooth/bap\_broadcast\_assistant](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/bap_broadcast_assistant) in the Zephyr tree.

Check the [Bluetooth](../bluetooth.md#bluetooth) samples for general information.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support
- Broadcast Audio Source and Sink devices

## Building and Running

The application will act as a broadcast assistant with optionally preconfigured
filtering of broadcast sink and broadcast source names. By default, the application will
search for and connect to the first broadcast audio sink found (advertising PACS and
BASS UUIDs) and then search for and select the first broadcast audio source found
(advertising a broadcast ID).

Filter these by modifying the following configs:

`CONFIG_SELECT_SINK_NAME`: Substring of BT name of the sink.

and

`CONFIG_SELECT_SOURCE_NAME`: Substring of BT name or broadcast name of the source.

### Building for an nrf52840dk

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 samples/bluetooth/bap_broadcast_assistant/
```

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

[Bluetooth Audio](../../../doxygen/html/group__bt__audio.md)

[Bluetooth Basic Audio Profile](../../../doxygen/html/group__bt__bap.md)

[Connection management](../../../doxygen/html/group__bt__conn.md)
