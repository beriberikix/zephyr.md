---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/dsa/nxp,netc-switch.html
original_path: build/dts/api/bindings/dsa/nxp,netc-switch.html
---

# nxp,netc-switch

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/ethernet/nxp\_imx\_netc/dsa\_nxp\_imx\_netc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/dsa_nxp_imx_netc.c).

## Description

```text
NXP NETC ethernet switch
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Port number ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `ethernet` | `phandle` | ```text A phandle to a valid Ethernet device node. This host device is what the switch port is connected to. ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `local-mac-address` | `uint8-array` | ```text Specifies the MAC address that was assigned to the network device ``` |
| `zephyr,random-mac-address` | `boolean` | ```text Use a random MAC address generated when the driver is initialized. Note that using this choice and rebooting a board may leave stale MAC address in peers' ARP caches and lead to issues and delays in communication.  (Use "ip neigh flush all" on Linux peers to clear ARP cache.)  It is driver specific how the OUI octets are handled.  If set we ignore any setting of the local-mac-address property. ``` |
| `phy-handle` | `phandle` | ```text Specifies a reference to a node representing a PHY device. ``` |
| `phy-connection-type` | `string` | ```text Specifies the interface connection type between ethernet MAC and PHY. ```  Legal values: `'mii'`, `'rmii'`, `'gmii'`, `'rgmii'`, `'internal'` |
