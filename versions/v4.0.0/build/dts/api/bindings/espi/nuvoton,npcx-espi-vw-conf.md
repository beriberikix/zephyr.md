---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/espi/nuvoton,npcx-espi-vw-conf.html
original_path: build/dts/api/bindings/espi/nuvoton,npcx-espi-vw-conf.html
---

# nuvoton,npcx-espi-vw-conf

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

## Description

```text
Nuvoton NPCX eSPI Virtual Wire (VW) mapping child node
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `vw-reg` | `array` | ```text vw signal's register index and vw bitmask. ```  This property is **required**. |
| `vw-wui` | `phandle` | ```text Mapping table between Wake-Up Input (WUI) and vw input signal.  For example the WUI mapping on NPCX7 for VW_SLP5 would be    vw-wui = <&wui_vw_slp_s5>; ``` |
