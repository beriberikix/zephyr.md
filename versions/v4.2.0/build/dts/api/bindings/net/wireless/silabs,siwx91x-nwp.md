---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/net/wireless/silabs,siwx91x-nwp.html
original_path: build/dts/api/bindings/net/wireless/silabs,siwx91x-nwp.html
---

# silabs,siwx91x-nwp

Vendor: [Silicon Laboratories](../../../bindings.md#dt-vendor-silabs)

## Description

```text
Silicon Labs SiWx91x NWP (Network Wireless Processor)

The Network Wireless Processor (NWP) manages Wi-Fi and Bluetooth connectivity on SiWx91x devices,
offloading wireless networking tasks from the main processor and
supporting configurable power and performance modes.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `power-profile` | `string` | ```text Power/performance profile ```  This property is **required**.  Legal values: `'high-performance'`, `'associated-power-save'`, `'associated-power-save-low-latency'`, `'deep-sleep-without-ram-retention'`, `'deep-sleep-with-ram-retention'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “silabs,siwx91x-nwp” compatible.

(None)
