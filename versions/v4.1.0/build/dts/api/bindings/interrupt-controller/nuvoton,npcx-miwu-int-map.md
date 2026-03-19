---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/interrupt-controller/nuvoton,npcx-miwu-int-map.html
original_path: build/dts/api/bindings/interrupt-controller/nuvoton,npcx-miwu-int-map.html
---

# nuvoton,npcx-miwu-int-map

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

## Description

```text
NPCX-MIWU group-interrupt mapping child node
```

## Properties

### Top level properties

These property descriptions apply to “nuvoton,npcx-miwu-int-map”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `parent` | `phandle` | ```text parent device node of miwu groups ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,npcx-miwu-int-map” compatible.

(None)

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `irq` | `int` | ```text irq for miwu group ```  This property is **required**. |
| `irq-prio` | `int` | ```text irq's priority for miwu group. The valid number is from 0 to 7. ```  This property is **required**. |
| `group-mask` | `int` | ```text group bit-mask for miwu interrupts ```  This property is **required**. |
| `groups` | `array` | ```text groups shared the same interrupt ``` |
