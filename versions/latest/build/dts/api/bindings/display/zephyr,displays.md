---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/display/zephyr,displays.html
original_path: build/dts/api/bindings/display/zephyr,displays.html
---

# zephyr,displays

Vendor: [The Zephyr Project](../../bindings.md#dt-vendor-zephyr)

## Description

```text
Display controllers to pass to graphical libraries like LVGL.
Only one node with this compatible is allowed in the DeviceTree
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `displays` | `phandles` | ```text Nodes of display controllers for graphical libraries to use ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,displays” compatible.

(None)
