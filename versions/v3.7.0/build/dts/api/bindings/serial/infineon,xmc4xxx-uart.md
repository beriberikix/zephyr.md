---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/serial/infineon,xmc4xxx-uart.html
original_path: build/dts/api/bindings/serial/infineon,xmc4xxx-uart.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# infineon,xmc4xxx-uart

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

## Description

These nodes are “uart” bus nodes.

```text
INFINEON XMC4XXX UART
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
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `input-src` | `string` | ```text Connects the UART receive line (USIC DX0 input) to a specific GPIO pin. The USIC DX0 input is a multiplexer which connects to different GPIO pins. Refer to the XMC4XXX reference manual for the GPIO pin/mux mappings. DX0G is the loopback input line. ```  This property is **required**.  Legal values: `'DX0A'`, `'DX0B'`, `'DX0C'`, `'DX0D'`, `'DX0E'`, `'DX0F'`, `'DX0G'` |
| `fifo-start-offset` | `int` | ```text Each USIC0..2 has a fifo that is shared between two channels. For example, usic0ch0 and usic0ch1 will share the same fifo. This parameter defines an offset where the tx and rx fifos will start. When sharing the fifo, the user must properly define the offset based on the configuration of the other channel. The fifo has a capacity of 64 entries. The tx/rx fifos are created on fifo-xx-size aligned boundaries. ```  This property is **required**. |
| `fifo-tx-size` | `int` | ```text Fifo size used for buffering transmit bytes. A value of 0 implies that the fifo is not used while transmitting. transmitting. If the UART is used in async mode then fifo-tx-size should be set to 0. ```  This property is **required**.  Legal values: `0`, `2`, `4`, `8`, `16`, `32`, `64` |
| `fifo-rx-size` | `int` | ```text Fifo size used for buffering received bytes. A value of 0 implies that the fifo is not used while receiving. If the UART is used in async mode then fifo-rx-size should be set to 0. ```  This property is **required**.  Legal values: `0`, `2`, `4`, `8`, `16`, `32`, `64` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,xmc4xxx-uart” compatible.

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
| `interrupts` | `array` | ```text IRQ number and priority to use for interrupt driven UART. USIC0..2 have their own interrupt range as follows: USIC0 = [84, 89] USIC1 = [90, 95] USIC2 = [96, 101] ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text Optional TX & RX dma specifiers used by async UART.  The dmas are referenced in the UART node using the following syntax: dmas = <&dma1 1 0 XMC4XXX_SET_CONFIG(10,6)>, <&dma1 2 0 XMC4XXX_SET_CONFIG(11,6)>; where the first entry is for the TX, and the second for RX.  The parameters in the dma entry are: dma device phandle, dma channel, dma priority (0 is lowest and 7 is highest), and an opaque entry for the dma line routing parameters set by the macro XMC4XXX_SET_CONFIG(line, request_source). Use the following steps to properly select parameters line, request_source: 1. Select a dma device and a free dma channel. 1. Select a free dma line. dma0 device can only connect to lines [0, 7] and    dma1 can connect to lines [8, 11]. 2. For a given interrupt, calculate the service request (SR) number. Note the following    simple mapping: in USIC0 interrupt 84->SR0, interrupt 85->SR1, ... etc.    In USIC1, interrupt 90->SR0, 91->SR1, etc. 3. Select request_source from Table "DMA Request Source Selection" in XMC4XXX reference    manual.  For example, say we select interrupt 85 on USIC0, dma0, channel 3, priority 4, and line 7. The interrupt would map to SR1. From Table "DMA Request Source Selection", request_source would need to be set to 10 and the dts entry would be: dma = <&dma0 3 4 XMC4XXX_SET_CONFIG(7,10) ... >; ``` |
| `dma-names` | `string-array` | ```text Required if the dmas property exists. Should be set to "tx" and "rx" to match the dmas property.  For example    dma-names = "tx", "rx"; ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
