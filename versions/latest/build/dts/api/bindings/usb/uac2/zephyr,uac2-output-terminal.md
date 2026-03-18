---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/usb/uac2/zephyr,uac2-output-terminal.html
original_path: build/dts/api/bindings/usb/uac2/zephyr,uac2-output-terminal.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,uac2-output-terminal

Vendor: [Zephyr-specific binding](../../../bindings.md#dt-vendor-zephyr)

## Description

```text
USB Audio Class 2 Output Terminal entity
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `terminal-type` | `int` | ```text Terminal Type constant specified in USB Audio Terminal Types ```  This property is **required**. |
| `assoc-terminal` | `phandle` | ```text Associated terminal, e.g. for bidirectional terminal types. ``` |
| `data-source` | `phandle` | ```text Unit or Terminal this terminal receives data from ```  This property is **required**. |
| `clock-source` | `phandle` | ```text Connected clock entity ```  This property is **required**. |
| `copy-protect-control` | `string` | ```text Copy Protect Control capabilities ```  Legal values: `'host-programmable'` |
| `connector-control` | `string` | ```text Connector Control capabilities ```  Legal values: `'read-only'` |
| `overload-control` | `string` | ```text Overload Control capabilities ```  Legal values: `'read-only'` |
| `underflow-control` | `string` | ```text Underflow Control capabilities ```  Legal values: `'read-only'` |
| `overflow-control` | `string` | ```text Overflow Control capabilities ```  Legal values: `'read-only'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,uac2-output-terminal” compatible.

(None)
