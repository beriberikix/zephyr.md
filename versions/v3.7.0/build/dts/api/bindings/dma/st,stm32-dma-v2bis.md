---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/dma/st,stm32-dma-v2bis.html
original_path: build/dts/api/bindings/dma/st,stm32-dma-v2bis.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32-dma-v2bis

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

These nodes are “dma” bus nodes.

```text
STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families

This DMA controller includes several channels with different requests.
All the requests ar ORed before entering the DMA, so that only one request
must be enabled at a time.
DMA clients connected to the STM32 DMA controller must use the format
described in the dma.txt file, using a 2-cell specifier for each
channel: a phandle to the DMA controller plus the following four integer cells:
  1. channel: the dma stream from 1 to <dma-requests>
  2. channel-config: A 32bit mask specifying the DMA channel configuration
  A name custom DMA flags for channel configuration is used
  which is device dependent see stm32_dma.h:
    -bit 5 : DMA  cyclic mode config
              0x0: STM32_DMA_MODE_NORMAL
              0x1: STM32_DMA_MODE_CYCLIC
    -bit 6-7 : Direction (see dma.h)
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
    -bit 15: Reserved
    -bit 16-17 : Priority level
             0x0: STM32_DMA_PRIORITY_LOW: low
             0x1: STM32_DMA_PRIORITY_MEDIUM: medium
             0x2: STM32_DMA_PRIORITY_HIGH: high
             0x3: STM32_DMA_PRIORITY_VERY_HIGH: very high

Example of dma usual combination for peripheral transfer
     #define STM32_DMA_PERIPH_TX     (STM32_DMA_MEMORY_TO_PERIPH | STM32_DMA_MEM_INC)
     #define STM32_DMA_PERIPH_RX     (STM32_DMA_PERIPH_TO_MEMORY | STM32_DMA_MEM_INC)

Example of dma node for stm32f103
   dma1: dma-controller@40020400 {
       compatible = "st,stm32-dma-v2bis";
       ...
       dma-requests = <7>;
       status = "disabled";
      };

For the client part, example for stm32f103 on DMA1 instance
  Tx using channel 3
  Rx using channel 2
  spi1 {
   compatible = "st,stm32-spi";
   dmas = <&dma1 3 (STM32_DMA_PERIPH_TX | STM32_DMA_PRIORITY_HIGH)>,
          <&dma1 2 (STM32_DMA_PERIPH_RX | STM32_DMA_PRIORITY_HIGH)>;
   dma-names = "tx", "rx";
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#dma-cells` | `int` | ```text Number of items to expect in a DMA specifier ```  This property is **required**.  Constant value: `2` |
| `dma-channel-mask` | `int` | ```text Bitmask of available DMA channels in ascending order that are not reserved by firmware and are available to the kernel. i.e. first channel corresponds to LSB. ``` |
| `dma-channels` | `int` | ```text Number of DMA channels supported by the controller ``` |
| `dma-requests` | `int` | ```text Number of DMA request signals supported by the controller. ``` |
| `dma-buf-addr-alignment` | `int` | ```text Memory address alignment requirement for DMA buffers used by the controller. ``` |
| `dma-buf-size-alignment` | `int` | ```text Memory size alignment requirement for DMA buffers used by the controller. ``` |
| `dma-copy-alignment` | `int` | ```text Minimal chunk of data possible to be copied by the controller. ``` |
| `st,mem2mem` | `boolean` | ```text If the DMA controller V1 supports memory to memory transfer ``` |
| `dma-offset` | `int` | ```text offset in the table of channels when mapping to a DMAMUX for 1st dma instance, offset is 0, for 2nd dma instance, offset is the nb of dma channels of the 1st dma, for 3rd dma instance, offset is the nb of dma channels of the 2nd dma plus the nb of dma channels of the 1st dma instance, etc. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-dma-v2bis” compatible.

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
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |

## Specifier cell names

- dma cells: channel, channel-config
