---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/options/openthread,config.html
original_path: build/dts/api/bindings/options/openthread,config.html
---

# openthread,config

Vendor: [OpenThread.io](../../bindings.md#dt-vendor-openthread)

## Description

```text
OpenThread configuration node.

Example usage:
options {
  openthread {
    compatible = "openthread,config";
    diag-gpios = <&gpio0 0  GPIO_ACTIVE_HIGH>,
                 <&gpio1 0  GPIO_ACTIVE_LOW>;
    bootloader-gpios = <&gpio0 1 GPIO_ACTIVE_HIGH>;
  };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `diag-gpios` | `phandle-array` | ```text This enables access to diagnostic GPIO pins. Each field consists of GPIO pin's configuration: controller's phandle, pin number and configuration flags. ``` |
| `bootloader-gpios` | `phandle-array` | ```text This enables resetting to bootloader by triggering given GPIO pin. Property represents chosen GPIO pin's configuration: controller's phandle, pin number and configuration flags. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “openthread,config” compatible.

(None)
