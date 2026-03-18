---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/sensor/ti,tmag5273.html
original_path: build/dts/api/bindings/sensor/ti,tmag5273.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ti,tmag5273 (on i2c bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

## Description

```text
Texas Instruments TMAG5273 Low-Power Linear 3D Hall-Effect Sensor with an I2C interface.

See the specification for the default I2C address.

The specification of the sensor can be found at:
  https://www.ti.com/lit/ds/symlink/tmag5273.pdf

  When setting the enum properties in a .dts or .dtsi file you may
  include tmag5273.h and use the macros defined there.

  Example:
  #include <zephyr/dt-bindings/sensor/tmag5273.h>

  tmag5273: tmag5273@0 {
    ...
    axis = <TMAG5273_DT_AXIS_XYZ>;
    range = <TMAG5273_DT_AXIS_RANGE_HIGH>;
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `operation-mode` | `int` | ```text Sensor mode used if set to "active". Defaults to continuous sampling (TMAG5273_DT_OPER_MODE_CONTINUOUS).  - 0 # TMAG5273_DT_OPER_MODE_CONTINUOUS (continuous) - 1 # TMAG5273_DT_OPER_MODE_STANDBY    (standby) ```  Legal values: `0`, `1` |
| `axis` | `int` | ```text Magnet axis channel inputs. Defaults to measure all axis (TMAG5273_DT_AXIS_XYZ).  - 0  # TMAG5273_DT_AXIS_NONE - 1  # TMAG5273_DT_AXIS_X - 2  # TMAG5273_DT_AXIS_Y - 3  # TMAG5273_DT_AXIS_Z - 4  # TMAG5273_DT_AXIS_XY - 5  # TMAG5273_DT_AXIS_XZ - 6  # TMAG5273_DT_AXIS_YZ - 7  # TMAG5273_DT_AXIS_XYZ - 8  # TMAG5273_DT_AXIS_XYX (pseudo-simultaneous sampling) - 9  # TMAG5273_DT_AXIS_YXY (pseudo-simultaneous sampling) - 10 # TMAG5273_DT_AXIS_YZY (pseudo-simultaneous sampling) - 11 # TMAG5273_DT_AXIS_XZX (pseudo-simultaneous sampling) ```  Default value: `7`  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11` |
| `temperature` | `boolean` | ```text Select for temperature measurement. ``` |
| `range` | `int` | ```text XYZ-measurement range for magnetic-field value. Defaults to lower range (higher resolution; TMAG5273_DT_AXIS_RANGE_LOW).  - 0 # TMAG5273_DT_AXIS_RANGE_LOW      (+/-40 mT (TMAG5273A1) or +/-133 mT (TMAG5273A2)) - 1 # TMAG5273_DT_AXIS_RANGE_HIGH     (+/-80 mT (TMAG5273A1) or +/-266 mT (TMAG5273A2)) - 2 # TMAG5273_DT_AXIS_RANGE_RUNTIME  (@runtime (initial value is: "high")) ```  Default value: `1`  Legal values: `0`, `1`, `2` |
| `int-gpios` | `phandle-array` | ```text The INT signal connection.  The signal is active-low as produced by the sensor. Either used for interrupt signaling, or triggering a conversion. ``` |
| `temperature-coefficient` | `int` | ```text Selects the magnet temperature coefficient. Defaults to none (TMAG5273_DT_TEMP_COEFF_NONE).    - 0 # TMAG5273_DT_TEMP_COEFF_NONE    (none)   - 1 # TMAG5273_DT_TEMP_COEFF_NDBFE   (0.12 %/deg C (NdBFe))   - 2 # TMAG5273_DT_TEMP_COEFF_CERAMIC (0.2 %/deg C (Ceramic))  Ignored if temperature is not measured. ```  Legal values: `0`, `1`, `2` |
| `trigger-conversion-via-int` | `boolean` | ```text Selects initiation of a single conversion based on a trigger via the INT-pin if enabled, and via I2C-command if disabled.  Used in "standby"-, "wakeup-and-sleep"- and "sleep"-mode. Using I2C-conversion trigger may result in (handled) I2C-errors. ``` |
| `angle-magnitude-axis` | `int` | ```text Enables angle calculation, magnetic gain, and offset corrections between two selected magnetic channels. Defaults to no additional calculations (TMAG5273_DT_ANGLE_MAG_NONE).  - 0 # TMAG5273_DT_ANGLE_MAG_NONE    (deactivated) - 1 # TMAG5273_DT_ANGLE_MAG_XY      (x/y) - 2 # TMAG5273_DT_ANGLE_MAG_YZ      (y/z) - 3 # TMAG5273_DT_ANGLE_MAG_XZ      (x/z) - 4 # TMAG5273_DT_ANGLE_MAG_RUNTIME (@runtime (initial value is: "deactivated")) ```  Legal values: `0`, `1`, `2`, `3`, `4` |
| `ch-mag-gain-correction` | `int` | ```text Channel for the magnitude gain correction. Defaults to 1st channel.    - 0 # TMAG5273_DT_CORRECTION_CH_1 (1st channel)   - 1 # TMAG5273_DT_CORRECTION_CH_2 (2nd channel)  Only active if angle-magnitude-calculation is active. ```  Legal values: `0`, `1` |
| `average-mode` | `int` | ```text Enables additional sampling of the sensor data to reduce the noise effect (or to increase resolution).  Note that averaging will influence the output data rate. Defaults to 2x averaging (TMAG5273_DT_AVERAGING_2X).  - 0 # TMAG5273_DT_AVERAGING_NONE  (10.0-kSPS (3-axes) or 20-kSPS   (1 axis)) - 1 # TMAG5273_DT_AVERAGING_2X    (5.7-kSPS  (3-axes) or 13.3-kSPS (1 axis)) - 2 # TMAG5273_DT_AVERAGING_4X    (3.1-kSPS  (3-axes) or 8.0-kSPS  (1 axis)) - 3 # TMAG5273_DT_AVERAGING_8X    (1.6-kSPS  (3-axes) or 4.4-kSPS  (1 axis)) - 4 # TMAG5273_DT_AVERAGING_16X   (0.8-kSPS  (3-axes) or 2.4-kSPS  (1 axis)) - 5 # TMAG5273_DT_AVERAGING_32X   (0.4-kSPS  (3-axes) or 1.2-kSPS  (1 axis)) ```  Default value: `1`  Legal values: `0`, `1`, `2`, `3`, `4`, `5` |
| `crc-enabled` | `boolean` | ```text Activate I2C CRC byte to be sent. ``` |
| `low-noise` | `boolean` | ```text Select low-noise mode when enabled, and low-power mode when disabled. ``` |
| `ignore-diag-fail` | `boolean` | ```text Ignore detected diagnostic fail. According to the manual, this should be done if VCC < 2.3V. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,tmag5273” compatible.

| Name | Type | Details |
| --- | --- | --- |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
