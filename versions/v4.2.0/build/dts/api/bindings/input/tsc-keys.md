---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/input/tsc-keys.html
original_path: build/dts/api/bindings/input/tsc-keys.html
---

# tsc-keys

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
Input driver for STM32 Tocuh Sensing Controller (TSC).

This node is a st,stm32-tsc grandchild node and applies filters and
calculations to detect an input event on a group which is the child of
st,stm32-tsc. For more information see drivers/misc/st,stm32-tsc.yaml

Example:

#include <dt-bindings/input/input-event-codes.h>

&tsc {
  compatible = "st,stm32-tsc";

  tsc_group6: g6 {
    ...
    ts1 {
      compatible = "tsc-keys";
      sampling-interval-ms = <10>;
      oversampling = <10>;
      noise-threshold = <50>;
      zephyr,code = <INPUT_KEY_0>;
    };
  };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `sampling-interval-ms` | `int` | ```text Sampling interval in milliseconds. ```  This property is **required**. |
| `oversampling` | `int` | ```text Over sampling factor. The driver will take the average of the samples taken in the sampling interval and compare it with the previous sample. Larger values will reduce the noise but will increase the latency. The default value is 10 so the slope will be calculated every 10 * sampling-interval-ms milliseconds. ```  This property is **required**. |
| `noise-threshold` | `int` | ```text This value will be used to reject the noise for both directions of the slope. ```  This property is **required**. |
| `sticky-key-timeout-ms` | `int` | ```text Time in milliseconds to wait before releasing a key. By default a release event will be generated after 10 seconds of the last press event if the key is still pressed. ```  This property is **required**. |
| `zephyr,code` | `int` | ```text Key code to emit. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “tsc-keys” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
