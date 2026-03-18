---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/memory-controllers/st,stm32-fmc-nor-psram.html
original_path: build/dts/api/bindings/memory-controllers/st,stm32-fmc-nor-psram.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# st,stm32-fmc-nor-psram

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 Flexible Memory Controller (NOR Flash/PSRAM/SRAM controller).

The FMC generates the appropriate signal timings to drive the
following types of memories:

* Asynchronous SRAM and ROM
  - 8 bits
  - 16 bits
  - 32 bits
* PSRAM (Cellular RAM)
  - Asynchronous mode
  - Burst mode for synchronous accesses with configurable option to split burst
    access when crossing boundary page for CRAM 1.5.
  - Multiplexed or non-multiplexed
* NOR Flash memory
  - Asynchronous mode
  - Burst mode for synchronous accesses
  - Multiplexed or non-multiplexed

A unique Chip Select signal (NE) is used per bank. All the other
signals (addresses, data and control) are shared. A wide range of
devices is supported through programmable timings.

Refer to the reference manual for more details.

The FMC NOR/PSRAM controller is defined below the FMC node and banks are
defined as child nodes of the FMC NOR/PSRAM controller node.

You can enable the controller in devicetree as follows:

&fmc {
  status = "okay";
  pinctrl-0 = <&fmc_nwe_pd5 &fmc_noe_pd4 ...>;
  pinctrl-names = "default";

  sram {
    status = "okay";
    compatible = "st,stm32-fmc-nor-psram";

    #address-cells = <1>;
    #size-cells = <0>;

    sram2@2 {
      reg = <0x2>;
      st,control = <STM32_FMC_DATA_ADDRESS_MUX_DISABLE
                    STM32_FMC_MEMORY_TYPE_SRAM
                    STM32_FMC_NORSRAM_MEM_BUS_WIDTH_16
                    STM32_FMC_BURST_ACCESS_MODE_DISABLE
                    STM32_FMC_WAIT_SIGNAL_POLARITY_LOW
                    STM32_FMC_WAIT_TIMING_BEFORE_WS
                    STM32_FMC_WRITE_OPERATION_ENABLE
                    STM32_FMC_WAIT_SIGNAL_DISABLE
                    STM32_FMC_EXTENDED_MODE_DISABLE
                    STM32_FMC_ASYNCHRONOUS_WAIT_DISABLE
                    STM32_FMC_WRITE_BURST_DISABLE
                    STM32_FMC_CONTINUOUS_CLOCK_SYNC_ONLY
                    STM32_FMC_WRITE_FIFO_DISABLE
                    STM32_FMC_PAGE_SIZE_NONE>;
      st,timing = <4 2 3 0 16 17 STM32_FMC_ACCESS_MODE_A>;
    };
  };
};

Use constants defined in dt-bindings/memory-controller/stm32-fmc-nor-psram.h.
```

## Properties

### Top level properties

These property descriptions apply to “st,stm32-fmc-nor-psram”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-fmc-nor-psram” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `int` | This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `st,control` | `array` | ```text SRAM/NOR-Flash control register (FMC_BCRx).  Contains control information of each memory bank, used for SRAMs, PSRAM and NOR Flash memories.  Expected fields, in order:  * MUXEN - Address/data multiplexing enable bit. * MTYP  - Memory type. * MWID  - Memory data bus width. * FACCEN - Flash access enable. * BURSTEN - Burst enable bit. * WAITPOL - Wait signal polarity bit. * WAITCFG - Wait timing configuration. * WREN - Write enable bit. * WAITEN - Wait enable bit. * EXTMOD - Extended mode enable.            If set, then 'st,timing-ext' shall be provided. * ASYNCWAIT -  Wait signal during asynchronous transfers. * CPSIZE - Cellular RAM (CRAM) 1.5 Page Size. * CBURSTRW - Write burst enable. * CCLKEN - Continuous Clock Enable. * WFDIS - Write FIFO Disable. * BMAP - FMC bank mapping. ```  This property is **required**. |
| `st,timing` | `array` | ```text SRAM/NOR-Flash (read) timing register (FMC_BTRx).  If the EXTMOD is set (see control register FMC_BCRx), then FMC_BTRx register is partitioned for write and read access. That means, use this property to configure read accesses and 'st,timing-ext' to configure write accesses.  Expected fields, in order:  * ADDSET  - Address setup phase duration.             Number of HCLK cycles to configure the duration of             the address setup time. This parameter can be a value             between Min_Data = 0 and Max_Data = 15.             Note: Not used with synchronous NOR Flash memories. * ADDHLD  - Address-hold phase duration.             Number of HCLK cycles to configure the duration of             the address hold time. This parameter can be a value             between Min_Data = 1 and Max_Data = 15.             Note: Not used with synchronous NOR Flash memories. * DATAST  - Data-phase duration.             Number of HCLK cycles to configure the duration of             the data setup time. This parameter can be a value             between Min_Data = 1 and Max_Data = 255.             Note: Used for SRAMs, ROMs and asynchronous multiplexed             NOR Flash memories. * BUSTURN - Bus turnaround phase duration.             Number of HCLK cycles to configure the duration of             the bus turnaround. This parameter can be a value             between Min_Data = 0 and Max_Data = 15.             Note: Only used for multiplexed NOR Flash memories. * CLKDIV  - Clock divide ratio (for FMC_CLK signal).             Period of CLK clock output signal, expressed in number of             HCLK cycles. This parameter can be a value             between Min_Data = 2 and Max_Data = 16.             Note: Not used for asynchronous NOR Flash, SRAM or ROM             accesses. * DATLAT  - Data latency for synchronous memory.             Number of memory clock cycles to issue to the memory             before getting the first data.             The value depends on the memory type as shown below:             - It must be set to 0 in case of a CRAM             - It is don't care in asynchronous NOR, SRAM or ROM accesses             - It may assume a value between Min_Data = 2 and Max_Data = 17               in NOR Flash memories with synchronous burst mode enable * ACCMOD  - Access mode.             See access mode defines             in dt-bindings/memory-controller/stm32-fmc-nor-psram.h. ```  This property is **required**. |
| `st,timing-ext` | `array` | ```text SRAM/NOR-Flash (write) timing register (FMC_BWTRx).  Expected fields, in order:  * ADDSET  - Address setup phase duration.             Reset state: 15 (0xF). * ADDHLD  - Address-hold phase duration.             Reset state: 15 (0xF). * DATAST  - Data-phase duration.             Reset state: 255 (0xFF). * BUSTURN - Bus turnaround phase duration.             Reset state: 15 (0xF). * ACCMOD  - Access mode.             Reset state: 0 (0x0).  Refer to 'st,timing' for detailed field descriptions.  This property is applied only when EXTMOD is set (see control register FMC_BCRx).  If absent, then reset state values are used. ```  Default value: `[15, 15, 255, 15, 0]` |
