---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/qspi/nxp,s32-qspi.html
original_path: build/dts/api/bindings/qspi/nxp,s32-qspi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nxp,s32-qspi

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

These nodes are “qspi” bus nodes.

```text
NXP S32 Quad Serial Peripheral Interface (QSPI) Controller.

QSPI acts as an interface to up to two serial flash memory devices, each with
up to eight bidirectional bidirectional data lines, depending on the platform.
```

## Properties

### Top level properties

These property descriptions apply to “nxp,s32-qspi”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `data-rate` | `string` | ```text Selects the read mode: - Single Data Rate (SDR): sampling of incoming data occurs on single edges. - Double Data Rate (DDR): sampling of incoming data occurs on both edges. ```  Legal values: `'SDR'`, `'DDR'` |
| `hold-time-2x` | `boolean` | ```text Set to align incoming data with 2x serial flash half clock, when in DDR mode. Otherwise, data will be aligned to the posedge of the controller's internal reference clock. ``` |
| `sample-delay-half-cycle` | `boolean` | ```text Set to use half-cycle early DQS delay when sampling received data. ``` |
| `sample-phase-inverted` | `boolean` | ```text Set to sample received data at inverted clock. ``` |
| `cs-setup-time` | `int` | ```text Chip select setup time, in serial clock cycles. A bigger value will pull the CS signal earlier before the transaction starts. The default corresponds to the reset value of the register field. ```  Default value: `3` |
| `cs-hold-time` | `int` | ```text Chip select hold time, in serial clock cycles. A bigger value will release the CS signal later after the transaction ends. The default corresponds to the reset value of the register field. ```  Default value: `3` |
| `column-space` | `int` | ```text Column Address Space bit width. For example, if the column address is [2:0] of QSPI_SFAR/AHB address, then the column address space bit width must be 3. If there is no column address separation in any serial flash device connected to this controller, this value must be programmed to 0. The default corresponds to the reset value of the register field. ``` |
| `word-addressable` | `boolean` | ```text Set if the serial flash device connected to this controller is word (2 bytes) addressable. ``` |
| `byte-swapping` | `boolean` | ```text In case of Octal DDR mode, specifies whether a word unit composed of two bytes from posedge and negedge of a single DQS cycle needs to be swapped. ``` |
| `ahb-buffers-masters` | `array` | ```text Masters ID's for the AHB receive buffers. The master ID of every incoming request is checked and the data is returned or fetched into the corresponding associated buffer. The maximum number of buffers is SoC specific. ``` |
| `ahb-buffers-sizes` | `array` | ```text Sizes (in bytes) of the AHB receive buffers. The maximum buffer size and maximum number of buffers is SoC specific. ``` |
| `ahb-buffers-all-masters` | `boolean` | ```text Any access from a master not associated with any other buffer is routed to the last buffer. ``` |
| `a-rx-clock-source` | `string` | ```text Selects DQS clock source for sampling read data at side A: - LOOPBACK: use loopback clock from dummy internal PAD as strobe signal. - LOOPBACK DQS: use loopback clock from PAD as strobe signal. - INTERNAL DQS: use internally generated strobe signal. - EXTERNAL DQS: use external strobe signal. ```  Legal values: `'LOOPBACK'`, `'LOOPBACK DQS'`, `'INTERNAL DQS'`, `'EXTERNAL DQS'` |
| `a-io2-idle-high` | `boolean` | ```text Set if the logic level of IO2 signal output of this controller must be driven high in the inactive state. This property applies to side A of the controller. ``` |
| `a-io3-idle-high` | `boolean` | ```text Set if the logic level of IO3 signal output of this controller must be driven high in the inactive state. This property applies to side A of the controller. ``` |
| `a-dll-mode` | `string` | ```text DLL mode. The supported modes depends on the SoC. This property applies to side A of the controller. ```  Default value: `BYPASSED`  Legal values: `'BYPASSED'`, `'MANUAL UPDATE'`, `'AUTO UPDATE'` |
| `a-dll-freq-enable` | `boolean` | ```text Selects delay-chain for high frequency of operation. This property applies to side A of the controller. ``` |
| `a-dll-ref-counter` | `int` | ```text Select the "n+1" interval of DLL phase detection and reference delay updating interval. Minimum recommended value is 1 (reset value). This property applies to side A of the controller. ```  Default value: `1`  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15` |
| `a-dll-resolution` | `int` | ```text Minimum resolution for DLL phase detector to remain locked/unlocked based on flash memory clock jitter. The minimum value is 2 (reset value). This property applies to side A of the controller. ```  Default value: `2`  Legal values: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15` |
| `a-dll-coarse-delay` | `int` | ```text This field sets the number of delay elements in each delay tap. The field is used to overwrite DLL-generated delay values. Default to 0 (reset value). This property applies to side A of the controller. ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15` |
| `a-dll-fine-delay` | `int` | ```text This field sets the number of fine offset delay elements up to 16 in incoming DQS. Default to 0 (reset value). This property applies to side A of the controller. ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15` |
| `a-dll-tap-select` | `int` | ```text Selects the Nth tap provided by the slave delay-chain. Default to 0 (reset value). This property applies to side A of the controller. ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,s32-qspi” compatible.

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
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |

### Child node properties

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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `jedec-id` | `uint8-array` | ```text JEDEC ID as manufacturer ID, memory type, memory density ``` |
| `size` | `int` | ```text flash capacity in bits ``` |
| `sfdp-bfp` | `uint8-array` | ```text Contains the 32-bit words in little-endian byte order from the JESD216 Serial Flash Discoverable Parameters Basic Flash Parameters table.  This provides flash-specific configuration information in cases were runtime retrieval of SFDP data is not desired. ``` |
| `quad-enable-requirements` | `string` | ```text Quad Enable Requirements value from JESD216 BFP DW15.  Use NONE if the device detects 1-1-4 and 1-4-4 modes by the instruction.  Use S1B6 if QE is bit 6 of the first status register byte, and can be configured by reading then writing one byte with RDSR and WRSR.  For other fields see the specification. ```  Legal values: `'NONE'`, `'S2B1v1'`, `'S1B6'`, `'S2B7'`, `'S2B1v4'`, `'S2B1v5'`, `'S2B1v6'` |
| `enter-4byte-addr` | `int` | ```text Enter 4-Byte Addressing value from JESD216 BFP DW16  This property is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or to read SFDP properties at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  For CONFIG_SPI_NOR_SFDP_MINIMAL this is the 8-bit value from bits 31:24 of DW16 identifying ways a device can be placed into 4-byte addressing mode.  If provided as a non-zero value the driver assumes that 4-byte addressing is require to access the full address range, and automatically puts the device into 4-byte address mode when the device is initialized. ``` |
| `page-size` | `int` | ```text Number of bytes in a page from JESD216 BFP DW11  This property is only used in the CONFIG_SPI_NOR_SFDP_MINIMAL configuration. It is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or if the SFDP parameters are read from the device at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  The default value is 256 bytes if the value is not specified. ``` |
| `memory-alignment` | `int` | ```text Memory alignment in bytes, used to calculate padding when performing unaligned accesses. If not provided, 1 byte alignment will be selected. ``` |
