---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/ist,tsic-xx6.html
original_path: build/dts/api/bindings/sensor/ist,tsic-xx6.html
---

# ist,tsic-xx6

Vendor: [Innovative Sensor Technology IST AG](../../bindings.md#dt-vendor-ist)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/tsic\_xx6/tsic\_xx6.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tsic_xx6/tsic_xx6.c).

## Description

```text
TSic xx6 temperature sensor.
https://www.ist-ag.com/sites/default/files/downloads/ATTSic_E.pdf

Example:
  tsic_716: tsic_716 {
    status = "okay";
    compatible = "ist,tsic-xx6";
    pwms = <&pwm2 1 PWM_USEC(5) PWM_POLARITY_NORMAL>;
    data-bits = <14>;
    lower-temperature-limit = <(-10)>;
    higher-temperature-limit = <60>;
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pwms` | `phandle-array` | ```text Reference to a PWM instance with PWM capture support. ```  This property is **required**. |
| `lower-temperature-limit` | `int` | ```text Lowest temperature supported by the device in celcius degrees. ```  This property is **required**. |
| `higher-temperature-limit` | `int` | ```text Highest temperature supported by the device in celcius degrees. ```  This property is **required**. |
| `data-bits` | `int` | ```text Data bits per reading. ```  This property is **required**.  Legal values: `11`, `14` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ist,tsic-xx6” compatible.

(None)
