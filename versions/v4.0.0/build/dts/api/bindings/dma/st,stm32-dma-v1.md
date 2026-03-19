---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/dma/st,stm32-dma-v1.html
original_path: build/dts/api/bindings/dma/st,stm32-dma-v1.html
---

# st,stm32-dma-v1

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/dma/dma\_stm32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/dma_stm32.c).

## Description

These nodes are “dma” bus nodes.

```text
STM32 DMA controller (V1)

It is present on stm32 devices like stm32F4 or stm32F2.
This DMA controller includes FIFO control registers.
DMA clients connected to the STM32 DMA controller must use the format
described in the dma.txt file, using a four-cell specifier for each
channel: a phandle to the DMA controller plus the following four integer cells:
  1. channel: the dma stream from 0 to <dma-requests>
  2. slot: DMA periph request ID, which is written in the DMAREQ_ID of the DMAMUX_CxCR
  this value is 0 for Memory-to-memory transfers
  or a value between <1> .. <dma-generators> (not supported yet)
  or a value between <dma-generators>+1  ..  <dma-generators>+<dma-requests>
  3. channel-config: A 32bit mask specifying the DMA channel configuration
  which is device dependent. See stm32_dma.h:
      -bit 6-7 : Direction  (see dma.h)
             0x0: STM32_DMA_MEMORY_TO_MEMORY: MEM to MEM
             0x1: STM32_DMA_MEMORY_TO_PERIPH: MEM to PERIPH
             0x2: STM32_DMA_PERIPH_TO_MEMORY: PERIPH to MEM
             0x3: reserved for PERIPH to PERIPH
      -bit 9 : Peripheral Increment Address
             0x0: STM32_DMA_PERIPH_NO_INC: no address increment between transfers
             0x1: STM32_DMA_PERIPH_INC: increment address between transfers
      -bit 10 : Memory Increment Address
             0x0: STM32_DMA_MEM_NO_INC: no address increment between transfers
             0x1: STM32_DMA_MEM_INC: increment address between transfers
      -bit 11-12 : Peripheral data size
             0x0: STM32_DMA_PERIPH_8BITS: Byte (8 bits)
             0x1: STM32_DMA_PERIPH_16BITS: Half-word (16 bits)
             0x2: STM32_DMA_PERIPH_32BITS: Word (32 bits)
             0x3: reserved
      -bit 13-14 : Memory data size
             0x0: STM32_DMA_MEM_8BITS: Byte (8 bits)
             0x1: STM32_DMA_MEM_16BITS: Half-word (16 bits)
             0x2: STM32_DMA_MEM_32BITS: Word (32 bits)
             0x3: reserved
      -bit 15: Peripheral Increment Offset Size
             0x0: STM32_DMA_OFFSET_LINKED_BUS: offset size is linked to the peripheral bus width
             0x1: STM32_DMA_OFFSET_FIXED_4: offset size is fixed to 4 (32-bit alignment)
      -bit 16-17 : Priority level
             0x0: STM32_DMA_PRIORITY_LOW: low
             0x1: STM32_DMA_PRIORITY_MEDIUM: medium
             0x2: hSTM32_DMA_PRIORITY_HIGH: high
             0x3: STM32_DMA_PRIORITY_VERY_HIGH: very high
  4. features: A 32bit bitfield value specifying DMA features
      -bit 0-1: DMA FIFO threshold selection
             0x0: STM32_DMA_FIFO_1_4: 1/4 full FIFO
             0x1: STM32_DMA_FIFO_HALF: 1/2 full FIFO
             0x2: STM32_DMA_FIFO_3_4: 3/4 full FIFO
             0x3: STM32_DMA_FIFO_FULL: full FIFO

Example of dma usual combination for peripheral transfer
     #define STM32_DMA_PERIPH_TX     (STM32_DMA_MEMORY_TO_PERIPH | STM32_DMA_MEM_INC)
     #define STM32_DMA_PERIPH_RX     (STM32_DMA_PERIPH_TO_MEMORY | STM32_DMA_MEM_INC)

  examples for stm32f411
   dma2: dma-controller@40020400 {
       compatible = "st,stm32-dma-v1";
       ...
       st,mem2mem;
       dma-requests = <7>;
       status = "disabled";
      };

For the client part, example for stm32f411 on DMA2 instance
  Tx using stream 5 on channel 3 (stream 2 on channel 2 is also possible)
  Rx using stream 2 on channel 3 (stream 0 on channel 3 is also possible)
  spi1 {
   dmas = <&dma2 5 3 STM32_DMA_PERIPH_TX STM32_DMA_FIFO_FULL>,
         <&dma2 2 3 STM32_DMA_PERIPH_RX STM32_DMA_FIFO_FULL>;
   dma-names = "tx", "rx";
   };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#dma-cells` | `int` | ```text Number of items to expect in a DMA specifier ```  This property is **required**.  Constant value: `4` |
| `st,mem2mem` | `boolean` | ```text If the DMA controller V1 supports memory to memory transfer ``` |
| `dma-offset` | `int` | ```text offset in the table of channels when mapping to a DMAMUX for 1st dma instance, offset is 0, for 2nd dma instance, offset is the nb of dma channels of the 1st dma, for 3rd dma instance, offset is the nb of dma channels of the 2nd dma plus the nb of dma channels of the 1st dma instance, etc. ``` |
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
may apply to the “st,stm32-dma-v1” compatible.

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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

## Specifier cell names

- dma cells: channel, slot, channel-config, features
