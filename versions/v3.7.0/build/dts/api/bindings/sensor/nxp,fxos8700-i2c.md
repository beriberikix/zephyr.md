---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/sensor/nxp,fxos8700-i2c.html
original_path: build/dts/api/bindings/sensor/nxp,fxos8700-i2c.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nxp,fxos8700 (on i2c bus)

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
FXOS8700 6-axis accelerometer/magnetometer sensor
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `reset-gpios` | `phandle-array` | ```text RST pin This pin defaults to active high when consumed by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `int1-gpios` | `phandle-array` | ```text INT1 pin This pin defaults to active low when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `int2-gpios` | `phandle-array` | ```text INT2 pin This pin defaults to active low when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `range` | `int` | ```text Range in g ```  Default value: `8`  Legal values: `8`, `4`, `2` |
| `power-mode` | `int` | ```text Power mode ```  Legal values: `0`, `1`, `2`, `3` |
| `pulse-cfg` | `int` | ```text Pulse configuration register ```  Default value: `63` |
| `pulse-thsx` | `int` | ```text Pulse X-axis threshold Threshold to start the pulse-event detection procedure on the X-axis. Threshold values for each axis are unsigned 7-bit numbers with a fixed resolution of 0.063 g/LSB, corresponding to an 8g acceleration full-scale range. ```  Default value: `32` |
| `pulse-thsy` | `int` | ```text Pulse Y-axis threshold Threshold to start the pulse-event detection procedure on the Y-axis. Threshold values for each axis are unsigned 7-bit numbers with a fixed resolution of 0.063 g/LSB, corresponding to an 8g acceleration full-scale range. ```  Default value: `32` |
| `pulse-thsz` | `int` | ```text Pulse Z-axis threshold Threshold to start the pulse-event detection procedure on the Z-axis. Threshold values for each axis are unsigned 7-bit numbers with a fixed resolution of 0.063 g/LSB, corresponding to an 8g acceleration full-scale range. ```  Default value: `64` |
| `pulse-tmlt` | `int` | ```text Pulse time limit The maximum time interval that can elapse between the start of the acceleration on the selected channel exceeding the specified threshold and the end when the channel acceleration goes back below the specified threshold. The resolution depends upon the sample rate (ODR) and the high-pass filter configuration (HP_FILTER_CUTOFF[pls_hpf_en]). For ODR=800 Hz and pls_hpf_en=0, the resolution is 0.625 ms/LSB. ```  Default value: `24` |
| `pulse-ltcy` | `int` | ```text Pulse latency The time interval that starts after the first pulse detection where the pulse-detection function ignores the start of a new pulse. The resolution depends upon the sample rate (ODR) and the high-pass filter configuration (HP_FILTER_CUTOFF[pls_hpf_en]). For ODR=800 Hz and pls_hpf_en=0, the resolution is 1.25 ms/LSB. ```  Default value: `40` |
| `pulse-wind` | `int` | ```text Pulse window The maximum interval of time that can elapse after the end of the latency interval in which the start of the second pulse event must be detected provided the device has been configured for double pulse detection. The detected second pulse width must be shorter than the time limit constraint specified by the PULSE_TMLT register, but the end of the double pulse need not finish within the time specified by the PULSE_WIND register. The resolution depends upon the sample rate (ODR) and the high-pass filter configuration (HP_FILTER_CUTOFF[pls_hpf_en]). For ODR=800 Hz and pls_hpf_en=0, the resolution is 1.25 ms/LSB. ```  Default value: `60` |
| `mag-vecm-cfg` | `int` | ```text Magnetic vector-magnitude configuration register ```  Default value: `78` |
| `mag-vecm-ths-msb` | `int` | ```text Magnetic vector-magnitude threshold most significant byte. Resolution is 0.1 uT/LSB. ``` |
| `mag-vecm-ths-lsb` | `int` | ```text Magnetic vector-magnitude threshold least significant byte. Resolution is 0.1 uT/LSB. ```  Default value: `90` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,fxos8700” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text device address on i2c bus ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
