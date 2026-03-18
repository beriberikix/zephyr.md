---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/ethernet/infineon,xmc4xxx-ethernet.html
original_path: build/dts/api/bindings/ethernet/infineon,xmc4xxx-ethernet.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# infineon,xmc4xxx-ethernet

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

## Description

```text
XMC 4XXX Ethernet
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `local-mac-address` | `uint8-array` | ```text Specifies the MAC address that was assigned to the network device ``` |
| `zephyr,random-mac-address` | `boolean` | ```text Use a random MAC address generated when the driver is initialized. Note that using this choice and rebooting a board may leave stale MAC address in peers' ARP caches and lead to issues and delays in communication.  (Use "ip neigh flush all" on Linux peers to clear ARP cache.)  It is driver specific how the OUI octets are handled.  If set we ignore any setting of the local-mac-address property. ``` |
| `phy-handle` | `phandle` | ```text Specifies a reference to a node representing a PHY device. ``` |
| `phy-connection-type` | `string` | ```text Specifies the interface connection type between ethernet MAC and PHY. ```  This property is **required**.  Legal values: `'mii'`, `'rmii'`, `'gmii'`, `'rgmii'` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `rxd0-port-ctrl` | `string` | ```text Receive bit 0 (rxd0) signal GPIO connection. Used for RMII and MII interfaces. ```  This property is **required**.  Legal values: `'P2_2'`, `'P0_2'`, `'P14_8'`, `'P5_0'` |
| `rxd1-port-ctrl` | `string` | ```text Receive bit 1 (rxd1) signal GPIO connection. Used for RMII and MII interfaces. ```  This property is **required**.  Legal values: `'P2_3'`, `'P0_3'`, `'P14_9'`, `'P5_1'` |
| `rxd2-port-ctrl` | `string` | ```text Receive bit 2 (rxd2) signal GPIO connection. Only used for MII interface. ```  Legal values: `'P5_8'`, `'P6_4'` |
| `rxd3-port-ctrl` | `string` | ```text Receive bit 2 (rxd2) signal GPIO connection. Only used for MII interface. ```  Legal values: `'P5_9'`, `'P6_3'` |
| `rmii-rx-clk-port-ctrl` | `string` | ```text If the RMII interface is used it connects GPIO to the rmii-clk signal. Otherwise, if the MII interface is used, then it connects to the Receive clock (rx-clk) signal. ```  This property is **required**.  Legal values: `'P2_1'`, `'P0_0'`, `'P15_8'`, `'P6_5'` |
| `crs-rx-dv-port-ctrl` | `string` | ```text If the RMII interface is used it connects GPIO to the Carrier Sense Data Valid (crs-dv) signal. Otherwise, if the MII interface is used, it connects to the Receive Data Valid (rx-dv) signal. ```  This property is **required**.  Legal values: `'P2_5'`, `'P0_1'`, `'P15_9'`, `'P5_2'` |
| `crs-port-ctrl` | `string` | ```text Carrier Sense (crs) signal GPIO connection. Only used for the MII interface. ```  Legal values: `'P5_11'`, `'unused1'`, `'unused2'`, `'P5_4'` |
| `rxer-port-ctrl` | `string` | ```text Receive Error (rxer) signal GPIO connection. Used for MII and RMII interfaces. ```  This property is **required**.  Legal values: `'P2_4'`, `'P0_11'`, `'unused1'`, `'P5_3'` |
| `col-port-ctrl` | `string` | ```text Collision (col) signal GPIO connection. Only used for MII interface. ```  Legal values: `'P2_15'`, `'unused1'`, `'unused2'`, `'P5_5'` |
| `tx-clk-port-ctrl` | `string` | ```text Transmit clock (tx-clk) GPIO connection. Only used for MII interface. ```  Legal values: `'P5_10'`, `'P6_6'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,xmc4xxx-ethernet” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
