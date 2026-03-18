---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/misc/nuvoton,npcx-soc-id.html
original_path: build/dts/api/bindings/misc/nuvoton,npcx-soc-id.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nuvoton,npcx-soc-id

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

## Description

```text
Nuvoton, NPCX soc ID node
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `family-id` | `int` | ```text NPCX family ID ```  This property is **required**. |
| `chip-id` | `int` | ```text NPCX chip ID ```  This property is **required**. |
| `device-id` | `int` | ```text NPCX device ID ```  This property is **required**. |
| `revision-reg` | `array` | ```text NPCX revision register address & length in byte ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,npcx-soc-id” compatible.

(None)
