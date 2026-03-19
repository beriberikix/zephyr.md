---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/pinctrl/nuvoton,npcx-pinctrl-conf.html
original_path: build/dts/api/bindings/pinctrl/nuvoton,npcx-pinctrl-conf.html
---

# nuvoton,npcx-pinctrl-conf

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

## Description

```text
Nuvoton NPCX7 Pin-Mux Configuration
Configuration map from Nuvoton NPCX GPIO to pinmux controller
(SCFG) driver instances.
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `alts` | `phandle-array` | ```text A SCFG ALT (Alternative controllers) specifier for pinmuxing of npcx ec ```  This property is **required**. |
