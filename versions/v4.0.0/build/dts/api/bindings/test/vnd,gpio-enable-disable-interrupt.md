---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/test/vnd,gpio-enable-disable-interrupt.html
original_path: build/dts/api/bindings/test/vnd,gpio-enable-disable-interrupt.html
---

# test-gpio-enable-disable-interrupt

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
This binding provides resources required to build and run the
tests/drivers/gpio/gpio_enable_disable_interrupt test in Zephyr.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `irq-gpios` | `phandle-array` | ```text Identity of a GPIO that will be configured as an input for interrupt. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “test-gpio-enable-disable-interrupt” compatible.

(None)
