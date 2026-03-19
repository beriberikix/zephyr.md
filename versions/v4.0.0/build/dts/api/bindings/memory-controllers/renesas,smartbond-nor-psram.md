---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/memory-controllers/renesas,smartbond-nor-psram.html
original_path: build/dts/api/bindings/memory-controllers/renesas,smartbond-nor-psram.html
---

# renesas,smartbond-nor-psram

Vendor: [Renesas Electronics Corporation](../../bindings.md#dt-vendor-renesas)

Note

An implementation of a driver matching this compatible is available in
[drivers/memc/memc\_smartbond\_nor\_psram.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_smartbond_nor_psram.c).

## Description

```text
Renesas Smartbond(tm) NOR/PSRAM controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `is-ram` | `boolean` | ```text If present, the memory controller will be configured to drive PSRAM devices. ``` |
| `dev-size` | `int` | ```text Memory size/capacity in bits. ```  This property is **required**. |
| `dev-type` | `int` | ```text Device type, part of device ID, used to verify the memory device used. ```  This property is **required**. |
| `dev-density` | `int` | ```text Device density, part of device ID, used to verify the memory device used. [7:0] should reflect the density value itself and [15:8] should reflect the mask that should be applied to the returned device ID value. This is because part of its byte value might contain invalid bits. ```  This property is **required**. |
| `dev-id` | `int` | ```text Manufacturer ID, part of device ID, used to verify the memory device used. ```  This property is **required**. |
| `reset-delay-us` | `int` | ```text Time in microseconds (us) the memory device can accept the next command following a SW reset. ```  This property is **required**. |
| `read-cs-idle-min-ns` | `int` | ```text Min. time, in nanoseconds, the #CS line should remain inactive between the transmission of two different instructions. ```  This property is **required**. |
| `erase-cs-idle-min-ns` | `int` | ```text Min. time, in nanoseconds, the #CS line should remain inactive after the execution of a write enable, erase, erase suspend or erase resume instruction. This setting is not used if is-ram property is present. ``` |
| `enter-qpi-cmd` | `int` | ```text Command to enter the QPI mode supported by a memory device (should be transmitted in single bus mode). ``` |
| `exit-qpi-cmd` | `int` | ```text Command to exit the QPI mode supported by a memory device (should be transmitted in quad bus mode). ``` |
| `enter-qpi-mode` | `boolean` | ```text If present, the memory device will enter the QPI mode which typically reflects that all bytes be sent in quad bus mode. It's a pre-requisite that read and write commands, that should be read-cmd and write-cmd respectively, reflect the QPI mode. ``` |
| `read-cmd` | `int` | ```text Read command for single/burst read accesses in auto mode. Default value is the opcode for single mode which is supported by all memory devices. ```  Default value: `3` |
| `write-cmd` | `int` | ```text Write command for single/burst write accesses in auto mode. Default value is the opcode for single mode which is supported by all memory devices. ```  Default value: `2` |
| `clock-mode` | `string` | ```text Clock mode when #CS is idle/inactive  - Mode0: #CLK is low when #CS is inactive - Mode3: #CLK is high when #CS is inactive  Mode0 is selected by default as it should be supported by all memory devices. ```  Default value: `spi-mode0`  Legal values: `'spi-mode0'`, `'spi-mode3'` |
| `addr-range` | `string` | ```text Address size to use in auto mode. In 24-bit mode up to 16MB can be accessed whilst in 32-bit mode up to 32MB can be accessed which is the max. address space supported by QSPICx. Default value is 24-bit mode which is supported by all memory devices. ```  Default value: `addr-range-24bit`  Legal values: `'addr-range-24bit'`, `'addr-range-32bit'` |
| `clock-div` | `int` | ```text Clock divider for QSPIC2 controller. The clock path of this block is always DIV1 which reflects the current system clock. ``` |
| `tcem-max-us` | `int` | ```text If a non zero value is applied, then Tcem should be taken into consideration by QSPIC2 so that it can split a burst read/write access in case the total time exceeds the defined value (at the cost of extra cycles required for re-sending the instruction, address and dummy bytes, if any). This setting is meaningful only if is-ram is present. This value reflects the max. time in microseconds the #CS line can be driven low in a write/read burst access (required for the auto-refresh mechanism, when supported). ``` |
| `dummy-bytes-count` | `string` | ```text Number of dummy bytes to send for single/burst read access in auto mode. ```  This property is **required**.  Legal values: `'dummy-bytes-count0'`, `'dummy-bytes-count1'`, `'dummy-bytes-count2'`, `'dummy-bytes-count4'` |
| `extra-byte-enable` | `boolean` | ```text If present, the extra byte will be sent after the dummy bytes, if any. This should be useful if 3 dummy bytes are required. In such a case, dummy-bytes-count should be set to 2. ``` |
| `extra-byte` | `int` | ```text Extra byte to be sent, if extra-byte-enable is present. ``` |
| `rx-addr-mode` | `string` | ```text Describes the mode of SPI bus during the address phase for single/burst read accesses in auto mode. Default value is single mode which should be supported by all memory devices. ```  Default value: `single-spi`  Legal values: `'single-spi'`, `'dual-spi'`, `'quad-spi'` |
| `rx-inst-mode` | `string` | ```text Describes the mode of SPI bus during the instruction phase for single/burst read accesses in auto mode. Default value is single mode which should be supported by all memory devices. ```  Default value: `single-spi`  Legal values: `'single-spi'`, `'dual-spi'`, `'quad-spi'` |
| `rx-data-mode` | `string` | ```text Describes the mode of SPI bus during the data phase for single/burst read accesses in auto mode. Default value is single mode which should be supported by all memory devices. ```  Default value: `single-spi`  Legal values: `'single-spi'`, `'dual-spi'`, `'quad-spi'` |
| `rx-dummy-mode` | `string` | ```text Describes the mode of SPI bus during the dummy bytes phase for single/burst read accesses in auto mode. The single mode should be supported by all memory devices. ```  Default value: `single-spi`  Legal values: `'single-spi'`, `'dual-spi'`, `'quad-spi'` |
| `rx-extra-mode` | `string` | ```text Describes the mode of SPI bus during the extra byte phase for single/burst read accesses in auto mode. Default value is single mode which should be supported by all memory devices. ```  Legal values: `'single-spi'`, `'dual-spi'`, `'quad-spi'` |
| `tx-addr-mode` | `string` | ```text Describes the mode of SPI bus during the address phase for single/burst write accesses in auto mode. Default value is single mode which should be supported by all memory devices. ```  Default value: `single-spi`  Legal values: `'single-spi'`, `'dual-spi'`, `'quad-spi'` |
| `tx-inst-mode` | `string` | ```text Describes the mode of SPI bus during the instruction phase for single/burst write accesses in auto mode. The single mode should be supported by all memory devices. ```  Default value: `single-spi`  Legal values: `'single-spi'`, `'dual-spi'`, `'quad-spi'` |
| `tx-data-mode` | `string` | ```text Describes the mode of SPI bus during the data phase for single/burst write accesses in auto mode. Default value is single mode which should be supported by all memory devices. ```  Default value: `single-spi`  Legal values: `'single-spi'`, `'dual-spi'`, `'quad-spi'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “renesas,smartbond-nor-psram” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
