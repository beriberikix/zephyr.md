---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/dma/andestech,atcdmac300.html
original_path: build/dts/api/bindings/dma/andestech,atcdmac300.html
---

# andestech,atcdmac300

Vendor: [Andes Technology Corporation](../../bindings.md#dt-vendor-andestech)

Note

An implementation of a driver matching this compatible is available in
[drivers/dma/dma\_andes\_atcdmac300.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/dma_andes_atcdmac300.c).

## Description

These nodes are “dma” bus nodes.

```text
Andes DMA controller
channel: a phandle to the DMA controller plus the following four integer cells:
  1. channel: the dma channel
  2. slot: DMA peripheral request ID
  3. channel-config: A 32bit mask specifying the DMA channel configuration
  which is device dependent:
      -bit 0-1 : Direction  (see dma.h)
             0x0: MEM to MEM
             0x1: MEM to PERIPH
             0x2: PERIPH to MEM
             0x3: reserved for PERIPH to PERIPH
      -bit 2 : Peripheral Increment Address
             0x0: no address increment between transfers
             0x1: increment address between transfers
      -bit 3 : Memory Increment Address
             0x0: no address increment between transfers
             0x1: increment address between transfers
      -bit 4-6 : Peripheral data size
             0x0: Byte (8 bits)
             0x1: Half-word (16 bits)
             0x2: Word (32 bits)
             0x3: Double word (64 bits)
             0x4: Quad word (128 bits)
             0x5: Eight word (256 bits)
             0x6-0x7: reserved
      -bit 7-9 : Memory data size
             0x0: Byte (8 bits)
             0x1: Half-word (16 bits)
             0x2: Word (32 bits)
             0x3: Double word (64 bits)
             0x4: Quad word (128 bits)
             0x5: Eight word (256 bits)
             0x6-0x7: reserved
      -bit 10 : Priority level
             0x0: lower priority
             0x1: higher priority

  examples for andes_v5_ae350 DMA instance
   dma0: dma0@f0c00000 {
       compatible = "andestech,atcdmac300";
       ...
       dma-channels = <8>;
       dma-requests = <16>;
       status = "disabled";
       label = "DMA_0";
      };

For the client part, example for andes_ae350 DMA instance
  Tx using channel 2, slot 0
  Rx using channel 3, slot 1
  spi1: spi@f0f00000 {
   compatible = "andestech,atcspi200"
   dmas = <&dma0 2 0 0x0129>,
          <&dma0 3 1 0x012A>;
   dma-names = "tx", "rx";
   };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `chain-transfer` | `int` |  |
| `#dma-cells` | `int` | ```text Number of items to expect in a DMA specifier ```  This property is **required**.  Constant value: `3` |
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
may apply to the “andestech,atcdmac300” compatible.

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

- dma cells: channel, slot, channel-config
