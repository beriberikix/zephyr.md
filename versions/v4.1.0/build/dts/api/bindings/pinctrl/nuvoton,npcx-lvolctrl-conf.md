---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/pinctrl/nuvoton,npcx-lvolctrl-conf.html
original_path: build/dts/api/bindings/pinctrl/nuvoton,npcx-lvolctrl-conf.html
---

# nuvoton,npcx-lvolctrl-conf

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

## Description

```text
Nuvoton NPCX7 Low-Voltage level detection configuration map
between Nuvoton NPCX GPIO and low-voltage controller (LV_GPIO_CTL)
driver instances.
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `lvols` | `phandle-array` | ```text list of configurations map between io and low-voltage controllers ```  This property is **required**. |
