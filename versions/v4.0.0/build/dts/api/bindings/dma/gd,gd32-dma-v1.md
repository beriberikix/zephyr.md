---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/dma/gd,gd32-dma-v1.html
original_path: build/dts/api/bindings/dma/gd,gd32-dma-v1.html
---

# gd,gd32-dma-v1

Vendor: [GigaDevice Semiconductor](../../bindings.md#dt-vendor-gd)

Note

An implementation of a driver matching this compatible is available in
[drivers/dma/dma\_gd32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/dma_gd32.c).

## Description

These nodes are “dma” bus nodes.

```text
GD32 DMA controller with FIFO

channel: Select channel for data transmitting

slot: Select peripheral to connect DMA

config: A 32bit mask specifying the DMA channel configuration
  - bit 6-7:   Direction  (see dma.h)
               - 0x0: MEMORY to MEMORY
               - 0x1: MEMORY to PERIPH
               - 0x2: PERIPH to MEMORY
               - 0x3: reserved for PERIPH to PERIPH

  - bit 9:     Peripheral address increase
               - 0x0: no address increment between transfers
               - 0x1: increment address between transfers

  - bit 10:    Memory address increase
               - 0x0: no address increase between transfers
               - 0x1: increase address between transfers

  - bit 11-12: Peripheral data width
               - 0x0: 8 bits
               - 0x1: 16 bits
               - 0x2: 32 bits
               - 0x3: reserved

  - bit 13-14: Memory data width
               - 0x0: 8 bits
               - 0x1: 16 bits
               - 0x2: 32 bits
               - 0x3: reserved

  - bit 15:    Peripheral Increment Offset Size
               - 0x0: offset size is linked to the peripheral bus width
               - 0x1: offset size is fixed to 4 (32-bit alignment)

  - bit 16-17: Priority
               - 0x0: low
               - 0x1: medium
               - 0x2: high
               - 0x3: very high

fifo-threshold: A 32bit bitfield value specifying FIFO threshold
  - bit 0-1:   Depth of DMA's FIFO used by burst-transfer.
               - 0x0: 1 word
               - 0x1: 2 word
               - 0x2: 3 word
               - 0x3: 4 word

Example of devicetree configuration

&spi0 {
      status = "okay";
      pinctrl-0 = <&spi0_default>;
      pinctrl-names = "default";
      cs-gpios = <&gpioa 4 GPIO_ACTIVE_LOW>;

      dmas = <&dma1 0 3 0 0>, <&dma1 5 3 GD32_DMA_PRIORITY_HIGH 0>
      dma-names = "rx", "tx";
};

"spi0" uses dma1 for transmitting and receiving in the example.
Each is named "rx" and "tx".
The first cell assigns channel 0 to receive and channel 5 to transmit.
The second cell is slot. Both channels select 3.
What the slot number '3' means depends on the DMA controller and channel.
See the Hardware manual.
The config that places on the third can take various configs.
But the setting used depends on each driver implementation.
Set the priority for the transmitting channel as HIGH, LOW(the default) for receive channel.
The fifo-threshold cell that places the fourth is configuring FIFO threshold.
The behavior of burst transfer determines by data-width in the config cell,
burst-length in the dma_config struct, and fifo-threshold.
A single burst transfer transfers [(4 * fifo-threshold)] bytes using with DMA's FIFO.
Where (data-width * burst-length) must be multiple numbers of burst transfer size.
For example, In the case of data-width is 'byte' and burst-length is 8.
If the fifo-threshold is a 2-word case, it runs one burst transfer to transfer 8 bytes.
Or the fifo-threshold is a 4-word case, runs two times burst transfer to transferring 8 bytes each
time.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#dma-cells` | `int` | ```text Number of items to expect in a DMA specifier ```  This property is **required**.  Constant value: `4` |
| `resets` | `phandle-array` | ```text Reset information ``` |
| `reset-names` | `string-array` | ```text Name of each reset ``` |
| `dma-channels` | `int` | ```text Number of DMA channels supported by the controller ```  This property is **required**. |
| `gd,mem2mem` | `boolean` | ```text The DMA controller supporting memory to memory transfer ``` |
| `dma-channel-mask` | `int` | ```text Bitmask of available DMA channels in ascending order that are not reserved by firmware and are available to the kernel. i.e. first channel corresponds to LSB. ``` |
| `dma-requests` | `int` | ```text Number of DMA request signals supported by the controller. ``` |
| `dma-buf-addr-alignment` | `int` | ```text Memory address alignment requirement for DMA buffers used by the controller. ``` |
| `dma-buf-size-alignment` | `int` | ```text Memory size alignment requirement for DMA buffers used by the controller. ``` |
| `dma-copy-alignment` | `int` | ```text Minimal chunk of data possible to be copied by the controller. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “gd,gd32-dma-v1” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
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

## Specifier cell names

- dma cells: channel, slot, config, fifo-threshold
