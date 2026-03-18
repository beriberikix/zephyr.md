---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/sensor/st,lps28dfw-i3c.html
original_path: build/dts/api/bindings/sensor/st,lps28dfw-i3c.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,lps28dfw (on i3c bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STMicroelectronics LPS28DFW pressure and temperature sensor connected to
I3C bus
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `assigned-address` | `int` | ```text Dynamic address to be assigned to the device. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `drdy-gpios` | `phandle-array` | ```text DRDY pin  This pin defaults to active high when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `drdy-pulsed` | `boolean` | ```text Selects the pulsed mode for data-ready interrupt when enabled, and the latched mode when disabled. ``` |
| `odr` | `int` | ```text Specify the output data rate expressed in samples per second (Hz). The default is the power-on reset value.  - 0 # LPS2xDF_DT_ODR_POWER_DOWN - 1 # LPS2xDF_DT_ODR_1HZ - 2 # LPS2xDF_DT_ODR_4HZ - 3 # LPS2xDF_DT_ODR_10HZ - 4 # LPS2xDF_DT_ODR_25HZ - 5 # LPS2xDF_DT_ODR_50HZ - 6 # LPS2xDF_DT_ODR_75HZ - 7 # LPS2xDF_DT_ODR_100HZ - 8 # LPS2xDF_DT_ODR_200HZ ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` |
| `lpf` | `int` | ```text Specify the low pass filter value to be applied to pressure data. The default is the power-on reset value.  - 0 # LPS2xDF_DT_LP_FILTER_OFF - 1 # LPS2xDF_DT_LP_FILTER_ODR_4 - 3 # LPS2xDF_DT_LP_FILTER_ODR_9 ```  Legal values: `0`, `1`, `3` |
| `avg` | `int` | ```text Specify the average filter value (i.e. number of samples) to be applied to pressure and temperature data. The default is the power-on reset value.  - 0 # LPS2xDF_DT_AVG_4_SAMPLES - 1 # LPS2xDF_DT_AVG_8_SAMPLES - 2 # LPS2xDF_DT_AVG_16_SAMPLES - 3 # LPS2xDF_DT_AVG_32_SAMPLES - 4 # LPS2xDF_DT_AVG_64_SAMPLES - 5 # LPS2xDF_DT_AVG_128_SAMPLES - 6 # LPS2xDF_DT_AVG_256_SAMPLES - 7 # LPS2xDF_DT_AVG_512_SAMPLES ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7` |
| `fs` | `int` | ```text Specify the full-scale mode. The default is the power-on reset value.  - 0 # LPS28DFW_DT_FS_MODE_1_1260 - 1 # LPS28DFW_DT_FS_MODE_2_4060 ```  Legal values: `0`, `1` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,lps28dfw” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Contains 3 fields.  For I3C devices, the 3 fields are static address, first half of Provisioned ID, and the second half of the Provisioned ID.   1. The static address can be assigned to be the target device's      dynamic address before Dynamic Address Assignment (DAA)      starts. Can be zero if static address is not used, and      target address is determined via DAA.   2. First half of the Provisioned ID contains the manufacturer      ID left-shifted by 1, where the manufacturer ID is      the bits 33-47 (zero-based) of the 48-bit Provisioned ID.   3. Second half of the Provisioned ID contains the combination of      the part ID (bits 16-31 of the Provisioned ID) left-shifted      by 16, and the instance ID (bits 12-15 of the Provisioned ID)      left-shifted by 12. Basically, this is the lower 32 bits      of the Provisioned ID.  Note that the DT node of a I3C target device should be in format "<node name>@<address + PID>", e.g. "sensor@4200001234012345678", where the PID part is expanded to be a 64-bit integer.  For I2C devices, the 3 fields are static address, 0x00, and value of the Legacy Virtual Register (LVR).    1. 7-bit address of the I2C device. (Note that 10-bit       addressing is not supported.)    2. Always 0x00.    3. LVR describes the I2C device where,       * bit[31:8]: unused.       * bit[7:5]: I2C device index:           * Index 0: I2C device has a 50 ns spike filter where                      it is not affected by high frequency on SCL.           * Index 1: I2C device does not have a 50 ns spike filter                      but can work with high frequency on SCL.           * Index 2: I2C device does not have a 50 ns spike filter                      and cannot work with high frequency on SCL.           * Other values are reserved.       * bit[4]: I2C mode indicator:           * 0: FM+ mode           * 1: FM mode       * bit[3:0]: reserved.  The DT node of a I2C device should be in format "<node name>@<address + 00000000 + LVR>", e.g. "sensor@5000000000000000FF", where the middle 0x00 and LVR are both expanded to 32-bit integers. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
