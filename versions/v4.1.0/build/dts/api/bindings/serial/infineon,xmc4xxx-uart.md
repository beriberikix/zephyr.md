---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/serial/infineon,xmc4xxx-uart.html
original_path: build/dts/api/bindings/serial/infineon,xmc4xxx-uart.html
---

# infineon,xmc4xxx-uart

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

Note

An implementation of a driver matching this compatible is available in
[drivers/serial/uart\_xmc4xxx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/uart_xmc4xxx.c).

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
| `input-src` | `string` | ```text Connects the UART receive line (USIC DX0 input) to a specific GPIO pin. The USIC DX0 input is a multiplexer which connects to different GPIO pins. Refer to the XMC4XXX reference manual for the GPIO pin/mux mappings. DX0G is the loopback input line. ```  This property is **required**.  Legal values: `'DX0A'`, `'DX0B'`, `'DX0C'`, `'DX0D'`, `'DX0E'`, `'DX0F'`, `'DX0G'` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `fifo-start-offset` | `int` | ```text Each USIC0..2 has a fifo that is shared between two channels. For example, usic0ch0 and usic0ch1 will share the same fifo. This parameter defines an offset where the tx and rx fifos will start. When sharing the fifo, the user must properly define the offset based on the configuration of the other channel. The fifo has a capacity of 64 entries. The tx/rx fifos are created on fifo-xx-size aligned boundaries. ```  This property is **required**. |
| `fifo-tx-size` | `int` | ```text Fifo size used for buffering transmit bytes. A value of 0 implies that the fifo is not used while transmitting. transmitting. If the UART is used in async mode then fifo-tx-size should be set to 0. ```  This property is **required**.  Legal values: `0`, `2`, `4`, `8`, `16`, `32`, `64` |
| `fifo-rx-size` | `int` | ```text Fifo size used for buffering received bytes. A value of 0 implies that the fifo is not used while receiving. If the UART is used in async mode then fifo-rx-size should be set to 0. ```  This property is **required**.  Legal values: `0`, `2`, `4`, `8`, `16`, `32`, `64` |
| `clock-frequency` | `int` | ```text Clock frequency information for UART operation ``` |
| `current-speed` | `int` | ```text Initial baud rate setting for UART ``` |
| `hw-flow-control` | `boolean` | ```text Set to enable RTS/CTS flow control at boot time ``` |
| `parity` | `string` | ```text Configures the parity of the adapter. Enumeration id 0 for none, 1 for odd and 2 for even parity. Default to none if not specified. ```  Default value: `none`  Legal values: `'none'`, `'odd'`, `'even'` |
| `stop-bits` | `string` | ```text Sets the number of stop bits. ```  Legal values: `'0_5'`, `'1'`, `'1_5'`, `'2'` |
| `data-bits` | `int` | ```text Sets the number of data bits. ```  Legal values: `5`, `6`, `7`, `8`, `9` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,xmc4xxx-uart” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text IRQ number and priority to use for interrupt driven UART. USIC0..2 have their own interrupt range as follows: USIC0 = [84, 89] USIC1 = [90, 95] USIC2 = [96, 101] ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `dmas` | `phandle-array` | ```text Optional TX & RX dma specifiers used by async UART.  The dmas are referenced in the UART node using the following syntax: dmas = <&dma1 1 0 XMC4XXX_SET_CONFIG(10,6)>, <&dma1 2 0 XMC4XXX_SET_CONFIG(11,6)>; where the first entry is for the TX, and the second for RX.  The parameters in the dma entry are: dma device phandle, dma channel, dma priority (0 is lowest and 7 is highest), and an opaque entry for the dma line routing parameters set by the macro XMC4XXX_SET_CONFIG(line, request_source). Use the following steps to properly select parameters line, request_source: 1. Select a dma device and a free dma channel. 1. Select a free dma line. dma0 device can only connect to lines [0, 7] and    dma1 can connect to lines [8, 11]. 2. For a given interrupt, calculate the service request (SR) number. Note the following    simple mapping: in USIC0 interrupt 84->SR0, interrupt 85->SR1, ... etc.    In USIC1, interrupt 90->SR0, 91->SR1, etc. 3. Select request_source from Table "DMA Request Source Selection" in XMC4XXX reference    manual.  For example, say we select interrupt 85 on USIC0, dma0, channel 3, priority 4, and line 7. The interrupt would map to SR1. From Table "DMA Request Source Selection", request_source would need to be set to 10 and the dts entry would be: dma = <&dma0 3 4 XMC4XXX_SET_CONFIG(7,10) ... >; ``` |
| `dma-names` | `string-array` | ```text Required if the dmas property exists. Should be set to "tx" and "rx" to match the dmas property.  For example    dma-names = "tx", "rx"; ``` |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
