---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pinctrl/nuvoton,npcx-pinctrl-conf.html
original_path: build/dts/api/bindings/pinctrl/nuvoton,npcx-pinctrl-conf.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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
