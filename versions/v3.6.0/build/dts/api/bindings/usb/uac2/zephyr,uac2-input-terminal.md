---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/usb/uac2/zephyr,uac2-input-terminal.html
original_path: build/dts/api/bindings/usb/uac2/zephyr,uac2-input-terminal.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,uac2-input-terminal

Vendor: [Zephyr-specific binding](../../../bindings.md#dt-vendor-zephyr)

## Description

```text
USB Audio Class 2 Input Terminal entity
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `terminal-type` | `int` | ```text Terminal Type constant specified in USB Audio Terminal Types ```  This property is **required**. |
| `assoc-terminal` | `phandle` | ```text Associated terminal for bi-directional terminal types. ``` |
| `clock-source` | `phandle` | ```text Connected clock entity ```  This property is **required**. |
| `copy-protect-control` | `string` | ```text Copy Protect Control capabilities ```  Legal values: `'read-only'` |
| `connector-control` | `string` | ```text Connector Control capabilities ```  Legal values: `'read-only'` |
| `overload-control` | `string` | ```text Overload Control capabilities ```  Legal values: `'read-only'` |
| `cluster-control` | `string` | ```text Cluster Control capabilities ```  Legal values: `'read-only'` |
| `underflow-control` | `string` | ```text Underflow Control capabilities ```  Legal values: `'read-only'` |
| `overflow-control` | `string` | ```text Overflow Control capabilities ```  Legal values: `'read-only'` |
| `front-left` | `boolean` | ```text Front Left channel present in the cluster ``` |
| `front-right` | `boolean` | ```text Front Right channel present in the cluster ``` |
| `front-center` | `boolean` | ```text Front Center channel present in the cluster ``` |
| `low-frequency-effects` | `boolean` | ```text Low Frequency Effects channel present in the cluster ``` |
| `back-left` | `boolean` | ```text Back Left channel present in the cluster ``` |
| `back-right` | `boolean` | ```text Back Right channel present in the cluster ``` |
| `front-left-of-center` | `boolean` | ```text Front Left of Center channel present in the cluster ``` |
| `front-right-of-center` | `boolean` | ```text Front Right of Center channel present in the cluster ``` |
| `back-center` | `boolean` | ```text Back Center channel present in the cluster ``` |
| `side-left` | `boolean` | ```text Side Left channel present in the cluster ``` |
| `side-right` | `boolean` | ```text Side Right channel present in the cluster ``` |
| `top-center` | `boolean` | ```text Top Center channel present in the cluster ``` |
| `top-front-left` | `boolean` | ```text Top Front Left channel present in the cluster ``` |
| `top-front-center` | `boolean` | ```text Top Front Center channel present in the cluster ``` |
| `top-front-right` | `boolean` | ```text Top Front Right channel present in the cluster ``` |
| `top-back-left` | `boolean` | ```text Top Back Left channel present in the cluster ``` |
| `top-back-center` | `boolean` | ```text Top Back Center channel present in the cluster ``` |
| `top-back-right` | `boolean` | ```text Top Back Right channel present in the cluster ``` |
| `top-front-left-of-center` | `boolean` | ```text Top Front Left of Center channel present in the cluster ``` |
| `top-front-right-of-center` | `boolean` | ```text Top Front Right of Center channel present in the cluster ``` |
| `left-low-frequency-effects` | `boolean` | ```text Left Low Frequency Effects channel present in the cluster ``` |
| `right-low-frequency-effects` | `boolean` | ```text Right Low Frequency Effects channel present in the cluster ``` |
| `top-side-left` | `boolean` | ```text Top Side Left channel present in the cluster ``` |
| `top-side-right` | `boolean` | ```text Top Side Right channel present in the cluster ``` |
| `bottom-center` | `boolean` | ```text Bottom Center channel present in the cluster ``` |
| `back-left-of-center` | `boolean` | ```text Back Left of Center channel present in the cluster ``` |
| `back-right-of-center` | `boolean` | ```text Back Right of Center channel present in the cluster ``` |
| `raw-data` | `boolean` | ```text Raw Data, mutually exclusive with all other spatial locations ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,uac2-input-terminal” compatible.

(None)
