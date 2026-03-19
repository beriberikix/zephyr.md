---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/input/gpio-kbd-matrix.html
original_path: build/dts/api/bindings/input/gpio-kbd-matrix.html
---

# gpio-kbd-matrix

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

Note

An implementation of a driver matching this compatible is available in
[drivers/input/input\_gpio\_kbd\_matrix.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_gpio_kbd_matrix.c).

## Description

```text
GPIO based keyboard matrix input device

Implement an input device for a GPIO based keyboard matrix.

Example configuration:

kbd-matrix {
        compatible = "gpio-kbd-matrix";
        row-gpios = <&gpio0 0 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>,
                    <&gpio0 1 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>;
        col-gpios = <&gpio0 2 GPIO_ACTIVE_LOW>,
                    <&gpio0 3 GPIO_ACTIVE_LOW>,
                    <&gpio0 4 GPIO_ACTIVE_LOW>;
        no-ghostkey-check;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `row-gpios` | `phandle-array` | ```text GPIO for the keyboard matrix rows, up to 8 different GPIOs. All row GPIO pins must have interrupt support if idle-mode is set to "interrupt" (default). ```  This property is **required**. |
| `col-gpios` | `phandle-array` | ```text GPIO for the keyboard matrix columns, supports up to 32 different GPIOs. When unselected, this pin will be either driven to inactive state or configured to high impedance (input) depending on the col-drive-inactive property. ```  This property is **required**. |
| `col-drive-inactive` | `boolean` | ```text If enabled, unselected column GPIOs will be driven to inactive state. Default to configure unselected column GPIOs to high impedance. ``` |
| `idle-mode` | `string` | ```text Controls the driver behavior on idle, "interrupt" waits for a new key press using GPIO interrupts on the row lines, "poll"  periodically polls the row lines with all the columns selected, "scan" just keep scanning the matrix continuously, requires "poll-timeout-ms" to be set to 0. ```  Default value: `interrupt`  Legal values: `'interrupt'`, `'poll'`, `'scan'` |
| `poll-period-ms` | `int` | ```text Defines the poll period in msecs between between matrix scans, set to 0 to never exit poll mode. Defaults to 5ms if unspecified. ```  Default value: `5` |
| `poll-timeout-ms` | `int` | ```text How long to wait before going from polling back to idle state. Defaults to 100ms if unspecified. ```  Default value: `100` |
| `debounce-down-ms` | `int` | ```text Debouncing time for a key press event. Defaults to 10ms if unspecified. ```  Default value: `10` |
| `debounce-up-ms` | `int` | ```text Debouncing time for a key release event. Defaults to 20ms if unspecified. ```  Default value: `20` |
| `settle-time-us` | `int` | ```text Delay between setting column output and reading the row values. Defaults to 50us if unspecified. ```  Default value: `50` |
| `actual-key-mask` | `array` | ```text Keyboard scanning mask. For each keyboard column, specify which keyboard rows actually exist. Can be used to avoid triggering the ghost detection on non existing keys. No masking by default, any combination is valid. ``` |
| `no-ghostkey-check` | `boolean` | ```text Ignore the ghost key checking in the driver if the diodes are used in the matrix hardware. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “gpio-kbd-matrix” compatible.

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
