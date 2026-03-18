---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/input/ite,it8xxx2-kbd.html
original_path: build/dts/api/bindings/input/ite,it8xxx2-kbd.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ite,it8xxx2-kbd

Vendor: [ITE Tech. Inc.](../../bindings.md#dt-vendor-ite)

## Description

```text
ITE it8xxx2 keyboard matrix controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `wucctrl` | `phandles` | ```text Configure wakeup controller, this controller is used to set that when the interrupt is triggered in EC low power mode, it can wakeup EC or not. Via this controller, we set the wakeup trigger edge, enable, disable, and clear wakeup status for the specific pin which may be gpio pins or alternate pins. ``` |
| `kso16-gpios` | `phandle-array` | ```text The KSO16 pin for the selected port. ```  This property is **required**. |
| `kso17-gpios` | `phandle-array` | ```text The KSO17 pin for the selected port. ```  This property is **required**. |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `row-size` | `int` | ```text The number of rows in the keyboard matrix. ```  This property is **required**. |
| `col-size` | `int` | ```text The number of column in the keyboard matrix. ```  This property is **required**. |
| `poll-period-ms` | `int` | ```text Defines the poll period in msecs between between matrix scans, set to 0 to never exit poll mode. Defaults to 5ms if unspecified. ```  Default value: `5` |
| `poll-timeout-ms` | `int` | ```text How long to wait before going from polling back to idle state. Defaults to 100ms if unspecified. ```  Default value: `100` |
| `debounce-down-ms` | `int` | ```text Debouncing time for a key press event. Defaults to 10ms if unspecified. ```  Default value: `10` |
| `debounce-up-ms` | `int` | ```text Debouncing time for a key release event. Defaults to 20ms if unspecified. ```  Default value: `20` |
| `settle-time-us` | `int` | ```text Delay between setting column output and reading the row values. Defaults to 50us if unspecified. ```  Default value: `50` |
| `actual-key-mask` | `array` | ```text Keyboard scanning mask. For each keyboard column, specify which keyboard rows actually exist. Can be used to avoid triggering the ghost detection on non existing keys. No masking by default, any combination is valid. ``` |
| `no-ghostkey-check` | `boolean` | ```text Ignore the ghost key checking in the driver if the diodes are used in the matrix hardware. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ite,it8xxx2-kbd” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
