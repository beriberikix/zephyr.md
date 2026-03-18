---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/serial/atmel,sam0-uart.html
original_path: build/dts/api/bindings/serial/atmel,sam0-uart.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# atmel,sam0-uart

Vendor: [Atmel Corporation](../../bindings.md#dt-vendor-atmel)

## Description

These nodes are “uart” bus nodes.

```text
Atmel SAM0 SERCOM UART driver
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text Clock frequency information for UART operation ``` |
| `current-speed` | `int` | ```text Initial baud rate setting for UART ``` |
| `hw-flow-control` | `boolean` | ```text Set to enable RTS/CTS flow control at boot time ``` |
| `parity` | `string` | ```text Configures the parity of the adapter. Enumeration id 0 for none, 1 for odd and 2 for even parity. Default to none if not specified. ```  Legal values: `'none'`, `'odd'`, `'even'` |
| `stop-bits` | `string` | ```text Sets the number of stop bits. ```  Legal values: `'0_5'`, `'1'`, `'1_5'`, `'2'` |
| `data-bits` | `int` | ```text Sets the number of data bits. ```  Legal values: `5`, `6`, `7`, `8`, `9` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `rxpo` | `int` | ```text Receive Data Pinout. An enumeration with the following values:  +-------+---------------+ | Value | RX Pin        | +-------+---------------+ |     0 | SERCOM_PAD[0] | +-------+---------------+ |     1 | SERCOM_PAD[1] | +-------+---------------+ |     2 | SERCOM_PAD[2] | +-------+---------------+ |     3 | SERCOM_PAD[3] | +-------+---------------+ ```  This property is **required**. |
| `txpo` | `int` | ```text Transmit Data Pinout. An enumeration with values that depend on the hardware being used. This controls both the transmit pins and if hardware flow control is used.  SAMD20:  +-------+---------------+ | Value | TX Pin        | +-------+---------------+ |     0 | SERCOM_PAD[0] | +-------+---------------+ |     1 | SERCOM_PAD[2] | +-------+---------------+  SAMD21/DA21/R21:  +-------+---------------+---------------+---------------+ | Value | TX Pin        | RTS           | CTS           | +-------+---------------+---------------+---------------+ |     0 | SERCOM_PAD[0] |           N/A |           N/A | +-------+---------------+---------------+---------------+ |     1 | SERCOM_PAD[2] |           N/A |           N/A | +-------+---------------+---------------+---------------+ |     2 | SERCOM_PAD[0] | SERCOM_PAD[2] | SERCOM_PAD[3] | +-------+---------------+---------------+---------------+ |     3 | Reserved                                      | +-------+-----------------------------------------------+  SAML2x/C2x:  +-------+----------------+---------------+--------------+ | Value | TX Pin        | RTS           | CTS           | +-------+---------------+---------------+---------------+ |     0 | SERCOM_PAD[0] |           N/A |           N/A | +-------+---------------+---------------+---------------+ |     1 | SERCOM_PAD[2] |           N/A |           N/A | +-------+---------------+---------------+---------------+ |     2 | SERCOM_PAD[0] | SERCOM_PAD[2] | SERCOM_PAD[3] | +-------+---------------+---------------+---------------+ |     3 | SERCOM_PAD[0] | SERCOM_PAD[2] |           N/A | +-------+---------------+---------------+---------------+  SAMD5/E5:  +-------+---------------+---------------+---------------+ | Value | TX Pin        | RTS           | CTS           | +-------+---------------+---------------+---------------+ |     0 | SERCOM_PAD[0] |           N/A |           N/A | +-------+---------------+---------------+---------------+ |     1 | Reserved                                      | +-------+---------------+---------------+---------------+ |     2 | SERCOM_PAD[0] | SERCOM_PAD[2] | SERCOM_PAD[3] | +-------+---------------+---------------+---------------+ |     3 | SERCOM_PAD[0] | SERCOM_PAD[2] |           N/A | +-------+---------------+---------------+---------------+ ```  This property is **required**. |
| `collision-detection` | `boolean` | ```text Enable collision detection for half-duplex mode. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “atmel,sam0-uart” compatible.

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
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `clock-names` | `string-array` | ```text name of each clock ```  This property is **required**. |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text Optional TX & RX dma specifiers.  Each specifier will have a phandle reference to the dmac controller, the channel number, and peripheral trigger source.  For example dmas for TX, RX on SERCOM3    dmas = <&dmac 0 0xb>, <&dmac 0 0xa>; ``` |
| `dma-names` | `string-array` | ```text Required if the dmas property exists.  This should be "tx" and "rx" to match the dmas property.  For example    dma-names = "tx", "rx"; ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
