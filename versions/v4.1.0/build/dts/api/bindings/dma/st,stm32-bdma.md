---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/dma/st,stm32-bdma.html
original_path: build/dts/api/bindings/dma/st,stm32-bdma.html
---

# st,stm32-bdma

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/dma/dma\_stm32\_bdma.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/dma_stm32_bdma.c).

## Description

These nodes are “dma” bus nodes.

```text
STM32 BDMA controller

The STM32 BDMA is a general-purpose direct memory access controller
capable of supporting 5 or 6 or 7 or 8 independent BDMA channels.
Each channel can have up to 8 requests.
BDMA clients connected to the STM32 BDMA controller must use the format
described in the dma.txt file, using a four-cell specifier for each
channel: a phandle to the BDMA controller plus the following four integer cells:
  1. channel: the bdma stream from 0 to <bdma-requests>
  2. slot: bdma request
  3. channel-config: A 32bit mask specifying the BDMA channel configuration
  which is device dependent:
      -bit 6-7 : Direction  (see dma.h)
             0x0: MEM to MEM
             0x1: MEM to PERIPH
             0x2: PERIPH to MEM
             0x3: reserved for PERIPH to PERIPH
      -bit 9 : Peripheral Increment Address
             0x0: no address increment between transfers
             0x1: increment address between transfers
      -bit 10 : Memory Increment Address
             0x0: no address increment between transfers
             0x1: increment address between transfers
      -bit 11-12 : Peripheral data size
             0x0: Byte (8 bits)
             0x1: Half-word (16 bits)
             0x2: Word (32 bits)
             0x3: reserved
      -bit 13-14 : Memory data size
             0x0: Byte (8 bits)
             0x1: Half-word (16 bits)
             0x2: Word (32 bits)
             0x3: reserved
      -bit 15: Peripheral Increment Offset Size
             0x0: offset size is linked to the peripheral bus width
             0x1: offset size is fixed to 4 (32-bit alignment)
      -bit 16-17 : Priority level
             0x0: low
             0x1: medium
             0x2: high
             0x3: very high

  examples for stm32h7
   bdma1: dma-controller@58025400 {
       compatible = "st,stm32-bdma";
       ...
       st,mem2mem;
       dma-requests = <7>;
       status = "disabled";
      };

For the client part, example for STM32H743 on BDMA1 instance
using dmamux2

  &adc3 {
     dmas = < &dmamux2 0 17 0x2C80 >;
     dma-names = "dmamux";
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `st,mem2mem` | `boolean` | ```text If the BDMA controller supports memory to memory transfer ``` |
| `dma-offset` | `int` | ```text offset in the table of channels when mapping to a DMAMUX for 1st dma instance, offset is 0, for 2nd dma instance, offset is the nb of dma channels of the 1st dma, for 3rd dma instance, offset is the nb of dma channels of the 2nd dma plus the nb of dma channels of the 1st dma instance, etc. ``` |
| `#dma-cells` | `int` | ```text Number of items to expect in a DMA specifier ```  This property is **required**.  Constant value: `4` |
| `dma-channel-mask` | `int` | ```text Bitmask of available DMA channels in ascending order that are not reserved by firmware and are available to the kernel. i.e. first channel corresponds to LSB. ``` |
| `dma-channels` | `int` | ```text Number of DMA channels supported by the controller ``` |
| `dma-requests` | `int` | ```text Number of DMA request signals supported by the controller. ``` |
| `dma-buf-addr-alignment` | `int` | ```text Memory address alignment requirement for DMA buffers used by the controller. ``` |
| `dma-buf-size-alignment` | `int` | ```text Memory size alignment requirement for DMA buffers used by the controller. ``` |
| `dma-copy-alignment` | `int` | ```text Minimal chunk of data possible to be copied by the controller. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-bdma” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
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

## Specifier cell names

- dma cells: channel, slot, channel-config
