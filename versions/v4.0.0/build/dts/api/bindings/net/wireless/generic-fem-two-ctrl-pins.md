---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/net/wireless/generic-fem-two-ctrl-pins.html
original_path: build/dts/api/bindings/net/wireless/generic-fem-two-ctrl-pins.html
---

# generic-fem-two-ctrl-pins

Vendor: [Generic or vendor-independent](../../../bindings.md#dt-no-vendor)

## Description

```text
This is a representation of generic radio Front-End Module (FEM)
that has a two-pin control interface (CTX, CRX).

The CTX control pin is used to enable the Power Amplifier (PA) in
the transmit path. This is therefore sometimes referred to as
the "PA pin" in other contexts.

The CRX control pin is used to enable the Low Noise Amplifier
(LNA) in the receive path, and is sometimes referred to as
the "LNA pin" in other contexts.

Each of these pins is optional, and may be omitted if not present.
(Though if you do specify a pin, you must also specify its
corresponding settle-time-us property.)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `ctx-gpios` | `phandle-array` | ```text SoC GPIO connected to the CTX input pin on the FEM device. ``` |
| `crx-gpios` | `phandle-array` | ```text SoC GPIO connected to the CRX input pin on the FEM device. ``` |
| `ctx-settle-time-us` | `int` | ```text Desired minimum settling time, in microseconds, from assertion of the CTX pin to beginning of transmission. ``` |
| `crx-settle-time-us` | `int` | ```text Desired minimum settling time, in microseconds, from assertion of the CRX pin to beginning of reception. ``` |
| `tx-gain-db` | `int` | ```text TX gain of the PA of the FEM device, in dB. ``` |
| `rx-gain-db` | `int` | ```text RX gain of the LNA of the FEM device, in dB. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “generic-fem-two-ctrl-pins” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
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
