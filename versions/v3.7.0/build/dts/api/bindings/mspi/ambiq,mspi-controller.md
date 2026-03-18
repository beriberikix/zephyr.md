---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/mspi/ambiq,mspi-controller.html
original_path: build/dts/api/bindings/mspi/ambiq,mspi-controller.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ambiq,mspi-controller

Vendor: [Ambiq Micro, Inc.](../../bindings.md#dt-vendor-ambiq)

## Description

These nodes are “mspi” bus nodes.

```text
Ambiq MSPI controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text Clock frequency the MSPI peripheral is being driven at, in Hz. ``` |
| `op-mode` | `string` | ```text Indicate MSPI controller or peripheral mode of the controller. The controller driver may use this during initialization. ```  Legal values: `'MSPI_CONTROLLER'`, `'MSPI_PERIPHERAL'` |
| `duplex` | `string` | ```text Indicate MSPI Duplex mode, full or half. The controller driver may check this setting against its capabilities. ```  Legal values: `'MSPI_HALF_DUPLEX'`, `'MSPI_FULL_DUPLEX'` |
| `dqs-support` | `boolean` | ```text Indicate whether the hardware supports DQS. The controller driver may check this setting against its capabilities. ``` |
| `software-multiperipheral` | `boolean` | ```text Indicate whether the controller driver enables support for software managed multi peripheral feature. At the minimum, the controller driver should use it to allow or disallow calling mspi_dev_config with MSPI_DEVICE_CONFIG_NONE. ``` |
| `ce-gpios` | `phandle-array` | ```text An array of chip select GPIOs to use. Each element in the array specifies a GPIO. The index in the array corresponds to the child node that the CE gpio controls.  Example:    mspi@... {           ce-gpios = <&gpio0 23 GPIO_ACTIVE_LOW>,                         <&gpio1 10 GPIO_ACTIVE_LOW>,                         ...;            mspi-device@0 {                   reg = <0>;                   ...           };           mspi-device@1 {                   reg = <1>;                   ...           };           ...   };  The child node "mspi-device@0" specifies a mspi device with chip select controller gpio0, pin 23, and devicetree GPIO flags GPIO_ACTIVE_LOW. Similarly, "mspi-device@1" has CE GPIO controller gpio1, pin 10, and flags GPIO_ACTIVE_LOW. Additional devices can be configured in the same way.  If unsure about the flags cell, GPIO_ACTIVE_LOW is generally a safe choice for a typical "CEn" pin. GPIO_ACTIVE_HIGH may be used if intervening hardware inverts the signal to the peripheral device or the line itself is active high.  Regardless of whether the CE pin may need software control or MSPI controller has dedicated CE pin, this field should be defined to help manage multiple devices on the same MSPI controller. ```  This property is **required**. |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `ambiq,pwrcfg` | `phandle-array` | ```text Power configuration ```  This property is **required**. |
| `cmdq-buffer-location` | `string` | ```text Define the DMA command queue buffer location section ``` |
| `cmdq-buffer-size` | `int` | ```text Define the DMA command queue buffer size in (4-byte) words ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ambiq,mspi-controller” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
