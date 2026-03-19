---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/usb/zephyr,hid-device.html
original_path: build/dts/api/bindings/usb/zephyr,hid-device.html
---

# zephyr,hid-device

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[subsys/usb/device\_next/class/usbd\_hid.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/usbd_hid.c).

## Description

```text
Bindings for HID device
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `interface-name` | `string` | ```text HID device name. When this property is present, a USB device will use it as the string descriptor of the interface. ``` |
| `protocol-code` | `string` | ```text This property corresponds to the protocol codes defined in Chapter 4.3 of the HID specification. Only boot devices are required to set one of the protocols, keyboard or mouse. For non-boot devices, this property is not required or can be set to none. - none:     Device does not support the boot interface - keyboard: Device supports boot interface and keyboard protocol - mouse:    Device supports boot interface and mouse protocol ```  Legal values: `'none'`, `'keyboard'`, `'mouse'` |
| `in-report-size` | `int` | ```text The size of the longest input report that the HID device can generate. This property is used to determine the buffer length used for transfers. ```  This property is **required**. |
| `in-polling-period-us` | `int` | ```text Input or output type reports polling period in microseconds. For USB full speed this could be clamped to 1ms or 255ms depending on the value. ```  This property is **required**. |
| `out-report-size` | `int` | ```text The size of the longest output report that the HID device can generate. When this property is present, a USB device will use out pipe for output reports, otherwise control pipe will be used for output reports. ``` |
| `out-polling-period-us` | `int` | ```text Output type reports polling period in microseconds. For USB full speed this could be clamped to 1ms or 255ms depending on the value. This option is only effective if the out-report-size property is defined. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,hid-device” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
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
