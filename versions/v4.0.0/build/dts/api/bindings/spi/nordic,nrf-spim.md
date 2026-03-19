---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/spi/nordic,nrf-spim.html
original_path: build/dts/api/bindings/spi/nordic,nrf-spim.html
---

# nordic,nrf-spim

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

These nodes are “spi” bus nodes.

```text
Nordic nRF family SPIM (SPI master with EasyDMA)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `anomaly-58-workaround` | `boolean` | ```text Enables the workaround for the nRF52832 SoC SPIM PAN 58 anomaly. Must be used in conjunction with CONFIG_SOC_NRF52832_ALLOW_SPIM_DESPITE_PAN_58=y ``` |
| `rx-delay-supported` | `boolean` | ```text Indicates if the SPIM instance has the capability of delaying MISO sampling. This property needs to be defined at SoC level DTS files. ``` |
| `rx-delay` | `int` | ```text Number of 64 MHz clock cycles (15.625 ns) delay from the sampling edge of SCK (leading or trailing, depending on the CPHA setting used) until the input serial data on MISO is actually sampled. This property does not have any effect if the rx-delay-supported property is not set. ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `max-frequency` | `int` | ```text Maximum data rate the SPI peripheral can be driven at, in Hz. This property must be set at SoC level DTS files. ```  This property is **required**. |
| `overrun-character` | `int` | ```text Configurable, defaults to 0xff (line high), the most common value used in SPI transfers. ```  Default value: `255` |
| `easydma-maxcnt-bits` | `int` | ```text Maximum number of bits available in the EasyDMA MAXCNT register. This property must be set at SoC level DTS files. ```  This property is **required**. |
| `wake-gpios` | `phandle-array` | ```text Optional bi-directional line that allows SPI master to indicate to SPI slave (by setting the line high) that a transfer is to occur, so that the latter can prepare (and indicate its readiness) for handling that transfer when it is actually needed, and stay in any desired low-power state otherwise. The protocol is as follows: - initially, SPI slave configures its WAKE line pin as an input and SPI   master keeps the line in the low state - when a transfer is to be performed, SPI master configures its WAKE   line pin as an input with pull-up; this changes the line state to   high but allows SPI slave to override that state - when SPI slave detects the high state of the WAKE line, it prepares   for the transfer and when everything is ready, it drives the WAKE   line low by configuring its pin as an output - the generated high-to-low transition on the WAKE line is a signal   to SPI master that it can proceed with the transfer - SPI slave releases the line by configuring its pin back to be an input   and SPI master again keeps the line in the low state Please note that the line must be configured and properly handled on both sides for the mechanism to work correctly. ``` |
| `clock-frequency` | `int` | ```text Clock frequency the SPI peripheral is being driven at, in Hz. ``` |
| `cs-gpios` | `phandle-array` | ```text An array of chip select GPIOs to use. Each element in the array specifies a GPIO. The index in the array corresponds to the child node that the CS gpio controls.  Example:    spi@... {           cs-gpios = <&gpio0 23 GPIO_ACTIVE_LOW>,                         <&gpio1 10 GPIO_ACTIVE_LOW>,                         ...;            spi-device@0 {                   reg = <0>;                   ...           };           spi-device@1 {                   reg = <1>;                   ...           };           ...   };  The child node "spi-device@0" specifies a SPI device with chip select controller gpio0, pin 23, and devicetree GPIO flags GPIO_ACTIVE_LOW. Similarly, "spi-device@1" has CS GPIO controller gpio1, pin 10, and flags GPIO_ACTIVE_LOW. Additional devices can be configured in the same way.  If unsure about the flags cell, GPIO_ACTIVE_LOW is generally a safe choice for a typical "CSn" pin. GPIO_ACTIVE_HIGH may be used if intervening hardware inverts the signal to the peripheral device or the line itself is active high.  If this property is not defined, no chip select GPIOs are set. SPI controllers with dedicated CS pins do not need to define the cs-gpios property. ``` |
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
may apply to the “nordic,nrf-spim” compatible.

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
