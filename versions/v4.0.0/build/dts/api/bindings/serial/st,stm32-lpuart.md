---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/serial/st,stm32-lpuart.html
original_path: build/dts/api/bindings/serial/st,stm32-lpuart.html
---

# st,stm32-lpuart

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

These nodes are “uart” bus nodes.

```text
STM32 LPUART
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `resets` | `phandle-array` | ```text Reset information ```  This property is **required**. |
| `single-wire` | `boolean` | ```text Enable the single wire half-duplex communication. Using this mode, TX and RX lines are internally connected and only TX pin is used afterwards and should be configured. RX/TX conflicts must be handled on user side. ``` |
| `tx-rx-swap` | `boolean` | ```text Swap the TX and RX pins. Used in case of a cross wired connection. ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `wakeup-line` | `int` | ```text EXTI line number matching the device wakeup interrupt mask register. This property is required on stm32 devices where the wakeup interrupt signal could be configured masked at boot (sm32wl55 for instance), preventing the device to wakeup the core from stop mode(s). Valid range: 0 - 31 ``` |
| `de-enable` | `boolean` | ```text Enable activating an external transeiver through the DE pin which must also be configured using pinctrl. ``` |
| `de-assert-time` | `int` | ```text Defines the time between the activation of the DE signal and the beginning of the start bit. It is expressed in 16th of a bit time. Valid range: 0 - 31 ``` |
| `de-deassert-time` | `int` | ```text Defines the time between the activation of the DE signal and the beginning of the start bit. It is expressed in 16th of a bit time. Valid range: 0 - 31 ``` |
| `de-invert` | `boolean` | ```text Invert the binary logic of the de pin. When enabled, physical logic levels are inverted and we use 1=Low, 0=High instead of 1=High, 0=Low. ``` |
| `fifo-enable` | `boolean` | ```text Enables transmit and receive FIFO using default FIFO configuration (typically threshold is set to 1/8). In TX, FIFO allows to work in burst mode, easing scheduling of loaded applications. It also allows more reliable communication with UART devices sensitive to variation of inter-frames delays. In RX, FIFO reduces overrun occurrences. ``` |
| `current-speed` | `int` | ```text Initial baud rate setting for UART ``` |
| `hw-flow-control` | `boolean` | ```text Set to enable RTS/CTS flow control at boot time ``` |
| `parity` | `string` | ```text Configures the parity of the adapter. Enumeration id 0 for none, 1 for odd and 2 for even parity. Default to none if not specified. ```  Legal values: `'none'`, `'odd'`, `'even'` |
| `stop-bits` | `string` | ```text Sets the number of stop bits. ```  Legal values: `'0_5'`, `'1'`, `'1_5'`, `'2'` |
| `data-bits` | `int` | ```text Sets the number of data bits. ```  Legal values: `5`, `6`, `7`, `8`, `9` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `reset-names` | `string-array` | ```text Name of each reset ``` |
| `tx-invert` | `boolean` | ```text Invert the binary logic of tx pin. When enabled, physical logic levels are inverted and we use 1=Low, 0=High instead of 1=High, 0=Low. ``` |
| `rx-invert` | `boolean` | ```text Invert the binary logic of rx pin. When enabled, physical logic levels are inverted and we use 1=Low, 0=High instead of 1=High, 0=Low. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-lpuart” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
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
