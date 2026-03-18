---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/mspi/zephyr,mspi-emul-device.html
original_path: build/dts/api/bindings/mspi/zephyr,mspi-emul-device.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# zephyr,mspi-emul-device (on mspi bus)

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
Zephyr MSPI Emulation Device
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `mspi-max-frequency` | `int` | ```text Maximum clock frequency of device to configure in Hz. In device tree, it is normally the target operating frequency after initialization. ```  This property is **required**. |
| `mspi-io-mode` | `string` | ```text MSPI I/O mode setting. In device tree, it is normally the target io mode after initialization. ```  Legal values: `'MSPI_IO_MODE_SINGLE'`, `'MSPI_IO_MODE_DUAL'`, `'MSPI_IO_MODE_DUAL_1_1_2'`, `'MSPI_IO_MODE_DUAL_1_2_2'`, `'MSPI_IO_MODE_QUAD'`, `'MSPI_IO_MODE_QUAD_1_1_4'`, `'MSPI_IO_MODE_QUAD_1_4_4'`, `'MSPI_IO_MODE_OCTAL'`, `'MSPI_IO_MODE_OCTAL_1_1_8'`, `'MSPI_IO_MODE_OCTAL_1_8_8'`, `'MSPI_IO_MODE_HEX'`, `'MSPI_IO_MODE_HEX_8_8_16'`, `'MSPI_IO_MODE_HEX_8_16_16'` |
| `mspi-data-rate` | `string` | ```text MSPI data rate setting. In device tree, it is normally the target data rate after initialization. ```  Legal values: `'MSPI_DATA_RATE_SINGLE'`, `'MSPI_DATA_RATE_S_S_D'`, `'MSPI_DATA_RATE_S_D_D'`, `'MSPI_DATA_RATE_DUAL'` |
| `mspi-hardware-ce-num` | `int` | ```text MSPI hardware CE number. MSPI controller may natively support multiple peripheral devices on the same MSPI instance by assigning designated CE numbers. ``` |
| `mspi-cpp-mode` | `string` | ```text MSPI clock polarity setting. MSPI_CPP_MODE_0: CPOL=0, CPHA=0 MSPI_CPP_MODE_1: CPOL=0, CPHA=1 MSPI_CPP_MODE_2: CPOL=1, CPHA=0 MSPI_CPP_MODE_3: CPOL=1, CPHA=1 ```  Legal values: `'MSPI_CPP_MODE_0'`, `'MSPI_CPP_MODE_1'`, `'MSPI_CPP_MODE_2'`, `'MSPI_CPP_MODE_3'` |
| `mspi-endian` | `string` | ```text MSPI transfer MSB or LSB first. ```  Legal values: `'MSPI_LITTLE_ENDIAN'`, `'MSPI_BIG_ENDIAN'` |
| `mspi-ce-polarity` | `string` | ```text MSPI CE polarity. In most cases, it is active low. ```  Legal values: `'MSPI_CE_ACTIVE_LOW'`, `'MSPI_CE_ACTIVE_HIGH'` |
| `mspi-dqs-enable` | `boolean` | ```text Enable DQS mode for a device which supports it. This will be checked against dqs-support and configure the MSPI hardware if it supports DQS mode. ``` |
| `mspi-hold-ce` | `boolean` | ```text In some cases, it is necessary for the controller to manage MSPI chip enable (under software control), so that multiple mspi transactions can be performed without releasing CE. A typical use case is variable length MSPI packets where the first mspi transaction reads the length and the second mspi transaction reads length bytes. ``` |
| `rx-dummy` | `int` | ```text The number of data or clock cycles between addr and data in RX direction. 0 means the RX dummy phase is disabled. ``` |
| `tx-dummy` | `int` | ```text The number of data or clock cycles between addr and data in TX direction. 0 means the TX dummy phase is disabled. ``` |
| `read-command` | `int` | ```text Read command to be sent in RX direction. ``` |
| `write-command` | `int` | ```text Write command to be sent in RX direction. ``` |
| `command-length` | `string` | ```text Length in bytes of the write and read commands. ```  Legal values: `'INSTR_DISABLED'`, `'INSTR_1_BYTE'`, `'INSTR_2_BYTE'` |
| `address-length` | `string` | ```text Length in bytes of address to be sent in address phase. ```  Legal values: `'ADDR_DISABLED'`, `'ADDR_1_BYTE'`, `'ADDR_2_BYTE'`, `'ADDR_3_BYTE'`, `'ADDR_4_BYTE'` |
| `xip-config` | `array` | ```text Array of parameters to configure the xip feature. enable: whether XIP feature is enabled. address_offset: The offset in bytes to the start of the                 platform specific XIP address region. size: The size in bytes of the XIP address region one       wish to enable or disable. permission: The permission granted to the region. (RW/RO)  For controller that support this feature. One may map the device memory into Soc system memory map. i.e. XIP address region So that the device may be used as an external RAM and execute code.  default = <   .enable         = false;   .address_offset = 0;   .size           = 0;   .permission     = 0; > ```  Default value: `[0, 0, 0, 0]` |
| `scramble-config` | `array` | ```text Array of parameters to configure the scrambling feature. enable: whether scrambling feature is enabled. address_offset: The offset in bytes to the start address which                 can be the offset to the start of the platform                 specific XIP address region or phyiscal device address.  size: The size in bytes of the region one wish to enable or disable. For controller that support hardware scrambling, one may use it for additional security to protect data or code stored in external devices.  default = <   .enable         = false;   .address_offset = 0;   .size           = 0; > ```  Default value: `[0, 0, 0]` |
| `ce-break-config` | `array` | ```text Array of parameters to configure the auto CE break feature. mem_boundary: Memory boundary in bytes of a device that a transfer               should't cross. time_to_break: The maximum time of a transfer should't exceed for                a device in micro seconds(us).  This is typically used with devices that has memory boundaries or requires periodic internal refresh. e.g. psram  default = <   .mem_boundary    = 0;   .time_to_break   = 0; > ```  Default value: `[0, 0]` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,mspi-emul-device” compatible.

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
