---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/usb/zephyr,midi2-device.html
original_path: build/dts/api/bindings/usb/zephyr,midi2-device.html
---

# zephyr,midi2-device

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[subsys/usb/device\_next/class/usbd\_midi2.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/usbd_midi2.c).

## Description

```text
MIDI2 device
```

## Properties

### Top level properties

These property descriptions apply to “zephyr,midi2-device”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,midi2-device” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | Constant value: `1` |
| `#size-cells` | `int` | Constant value: `1` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text First MIDI2 Group number (address) and number of Group Terminals (size) in this MIDI2 Group Terminal Block. The MIDI2 Groups 1 to 16 corresponds to address 0x0 to 0xf. There are at most 16 addressable groups (of 16 chans each) per MIDI2 interface. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `protocol` | `string` | ```text Default MIDI protocol of the Group Terminals in this Block. ```  Legal values: `'use-midi-ci'`, `'midi1-up-to-64b'`, `'midi1-up-to-128b'`, `'midi2'` |
| `terminal-type` | `string` | ```text Type (data direction) of Group Terminals in this Block. ```  Default value: `bidirectional`  Legal values: `'bidirectional'`, `'input-only'`, `'output-only'` |
