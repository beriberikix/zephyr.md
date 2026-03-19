---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/i2c/nordic,nrf-twim.html
original_path: build/dts/api/bindings/i2c/nordic,nrf-twim.html
---

# nordic,nrf-twim

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

These nodes are “i2c” bus nodes.

```text
Nordic nRF family TWIM (TWI master with EasyDMA).

This binding can be used for nodes which can represent TWIM
peripherals. A single SoC peripheral ID is often associated with
multiple I2C peripherals, like a TWIM and a TWIS. You can choose
TWIM by setting the node's "compatible" to "nordic,nrf-twim"
and "status" to "okay", e.g. using an overlay file like this one:

    /* This is for TWIM0 -- change to "i2c1" for TWIM1, etc. */
    &i2c0 {
            compatible = "nordic,nrf-twim";
            status = "okay";
            /* other property settings can go here */
    };

This works on any supported SoC, for all TWIM instances.

Note: on nRF51 SoCs, use the "nordic,nrf-twi" binding instead.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `zephyr,concat-buf-size` | `int` | ```text Size of a concatenation buffer that the driver is to use for merging multiple same direction I2C messages that have no RESTART or STOP flag between them (see e.g. the i2c_burst_write() function) into one transfer on the bus.  This property must be provided when interacting with devices like the SSD1306 display that cannot tolerate a repeated start and address appearing on the bus between message fragments. For many devices a concatenation buffer is not necessary. ```  Default value: `16` |
| `zephyr,flash-buf-max-size` | `int` | ```text TWIM peripherals cannot perform write transactions from buffers located in flash. If such buffers are expected to be used with a given instance of the TWIM peripheral, this property must be set to the maximum possible size of those buffers, so that the driver can reserve enough space in RAM to copy there the contents of particular buffers before requesting the actual transfers.  If this property is not set to a value adequate for a given application, write transactions may fail for buffers that are located in flash, what in turn may cause certain components, like the DPS310 sensor driver, to not work.  It is recommended to use the same value for this property and for the zephyr,concat-buf-size one, as both these buffering mechanisms can utilize the same space in RAM. ```  Default value: `16` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `easydma-maxcnt-bits` | `int` | ```text Maximum number of bits available in the EasyDMA MAXCNT register. This property must be set at SoC level DTS files. ```  This property is **required**. |
| `clock-frequency` | `int` | ```text Initial clock frequency in Hz ``` |
| `sq-size` | `int` | ```text Size of the submission queue for blocking requests ```  Default value: `4` |
| `cq-size` | `int` | ```text Size of the completion queue for blocking requests ```  Default value: `4` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `nordic,clockpin-enable` | `array` | ```text List of signals that require CLOCKPIN setting enablement. ``` |
| `memory-regions` | `phandle-array` | ```text List of memory region phandles ``` |
| `memory-region-names` | `string-array` | ```text A list of names, one for each corresponding phandle in memory-region ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-twim” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
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
