---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/regulator/silabs,series2-dcdc.html
original_path: build/dts/api/bindings/regulator/silabs,series2-dcdc.html
---

# silabs,series2-dcdc

Vendor: [Silicon Laboratories](../../bindings.md#dt-vendor-silabs)

## Description

```text
Silicon Labs Series 2 DC-DC converter.

Include the bindings header file <zephyr/dt-bindings/regulator/silabs_dcdc.h> to get
access to relevant symbols for configuration.

The following standard properties are supported:

`regulator-boot-on`
  Enable DC-DC converter at boot. If not set, the DC-DC converter is powered off.
`regulator-allow-bypass`
  Enable bypass mode. If combined with `regulator-boot-on`, the DC-DC converter
  is initialized to bypass mode.
`regulator-initial-mode`
  DCDC operating mode. One of `SILABS_DCDC_MODE_BUCK` or `SILABS_DCDC_MODE_BOOST`.
`regulator-init-microvolt`
  Output voltage for boost mode. Not used in buck mode.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `regulator-initial-mode` | `int` | ```text Initial operating mode. The set of possible operating modes depends on the capabilities of every hardware so each device binding documentation explains which values the regulator supports. ```  Legal values: `0`, `1` |
| `regulator-init-microvolt` | `int` | ```text Voltage set during initialisation ```  Legal values: `1800000`, `1900000`, `2000000`, `2100000`, `2200000`, `2300000`, `2400000` |
| `silabs,pfmx-peak-current-milliamp` | `int` | ```text Peak current draw in PFMX mode (CCM, continuous conduction mode). ```  Legal values: `50`, `65`, `73`, `80`, `86`, `93`, `100`, `106`, `113`, `120` |
| `regulator-boot-on` | `boolean` | ```text bootloader/firmware enabled regulator. It's expected that this regulator was left on by the bootloader. If the bootloader didn't leave it on then OS should turn it on at boot but shouldn't prevent it from being turned off later. This property is intended to only be used for regulators where software cannot read the state of the regulator. ``` |
| `regulator-allow-bypass` | `boolean` | ```text allow the regulator to go into bypass mode ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “silabs,series2-dcdc” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
