---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pcie/host/pci-host-ecam-generic.html
original_path: build/dts/api/bindings/pcie/host/pci-host-ecam-generic.html
---

# pci-host-ecam-generic

Vendor: [Generic or vendor-independent](../../../bindings.md#dt-no-vendor)

Note

An implementation of a driver matching this compatible is available in
[drivers/pcie/host/pcie\_ecam.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/pcie_ecam.c).

## Description

These nodes are “pcie” bus nodes.

```text
PCIe Controller in ECAM mode
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `msi-parent` | `phandle` |  |
| `ranges` | `array` | ```text As described in IEEE Std 1275-1994, but must provide at least a definition of non-prefetchable memory. One or both of prefetchable Memory and IO Space may also be provided. ```  This property is **required**. |
| `interrupt-map-mask` | `array` |  |
| `interrupt-map` | `compound` |  |
| `bus-range` | `array` |  |
| `acpi-hid` | `string` | ```text Used to supply OSPM with the device’s PNP ID or ACPI ID. A node is consder as acpi based or not based on whether this property is present or not. ``` |
| `acpi-uid` | `string` | ```text Provides OSPM with a logical device ID that does not change across reboots. This object is optional, but is required when the device has no other way to report a persistent unique device ID. The _UID must be unique across all devices with either a common _HID or _CID. ``` |
| `acpi-comp-id` | `string-array` | ```text Used to supply OSPM with a device’s Plug and Play-Compatible Device ID ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “pci-host-ecam-generic” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**. |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
