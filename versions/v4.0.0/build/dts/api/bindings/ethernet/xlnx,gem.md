---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/ethernet/xlnx,gem.html
original_path: build/dts/api/bindings/ethernet/xlnx,gem.html
---

# xlnx,gem

Vendor: [Xilinx](../../bindings.md#dt-vendor-xlnx)

Note

An implementation of a driver matching this compatible is available in
[drivers/ethernet/eth\_xlnx\_gem\_priv.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_xlnx_gem_priv.h).

## Description

```text
Xilinx GEM Ethernet controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text Specifies the base clock frequency from which the GEM's TX clock frequency will be derived using two dividers in the respective GEM's clock control register in the CRL_APB. The GEM's TX clock frequency is determined by the current link speed reported by the PHY, to which it will be adjusted at run-time. Therefore, the value of this item must be set to the clock frequency of the PLL supplying the respective GEM's TX clock - by default, this is the IO PLL. ```  This property is **required**. |
| `mdc-divider` | `int` | ```text The MDC clock divider for the respective GEM. This is the divider applied to the LPD_LSBUS clock in order to derive MDIO interface clock driving communications with the attached PHY. Refer to the ZynqMP register documentation (ug1087), network_config (GEM) Register Description, bits [20:18] to determine the appropriate divider for the current target's LPD LSBUS clock frequency. ```  This property is **required**. |
| `init-mdio-phy` | `boolean` | ```text Activates the management of a PHY associated with the controller in- stance. If this parameter is activated at the board level, the de- fault values of the associated parameters mdio-phy-address, phy-poll- interval, link-speed and advertise-lower-link-speeds should be checked and overwritten at the board level if required. ``` |
| `mdio-phy-address` | `int` | ```text The address on the MDIO bus of the PHY associated with the controller instance. Set the address to 0 for auto-detection (first responding PHY will be claimed by the driver, watch out in case of shared MDIO use), or to a fixed address between 1 and 32. ```  This property is **required**. |
| `phy-poll-interval` | `int` | ```text PHY status polling interval in milliseconds for a driver instance managing an associated PHY. ```  This property is **required**. |
| `link-speed` | `int` | ```text Nominal link speed. If no PHY is managed by an instance of this driver, the respective controller will be configured to match the link speed specified here. If a PHY is managed by the driver, advertisement of the link speed specified here will be requested. If the optional pro- perty advertise-lower-link-speeds is set, advertisement of the link speed specified here plus any valid link speed below this value will be requested. ```  This property is **required**.  Legal values: `1`, `2`, `3` |
| `advertise-lower-link-speeds` | `boolean` | ```text Indicates to a driver instance which manages an associated PHY on the MDIO bus to include link speeds lower than the nominal value set in the link-speed property in the advertisement when requesting link speed auto-negotiation with a peer system. ``` |
| `handle-rx-in-isr` | `boolean` | ```text Moves the handling of the frame received interrupt including the transfer of packet data from the DMA to network packet buffers and the subsequent propagation of the received packets to the network stack into the context of the ISR. Due to the unpredictability of the runtime of the ISR whenever large amounts of data are received, handling of the RX interrupt is normally deferred to the context of the system work queue. ``` |
| `handle-tx-in-workq` | `boolean` | ```text Moves the handling of the frame transmission done interrupt into the context of the system work queue. By default, TX done handling is per- formed in the context of the ISR, as it only involves a limited number of memory accesses. This option CAN NOT be used if any component ex- ists within the current system setup that triggers the transmission of packets from within the context of the system work queue! ``` |
| `amba-ahb-dbus-width` | `int` | ```text AMBA AHB data bus width. ```  This property is **required**.  Legal values: `0`, `1`, `2` |
| `amba-ahb-burst-length` | `int` | ```text AMBA AHB burst length for DMA operations. ```  This property is **required**.  Legal values: `1`, `4`, `8`, `16` |
| `hw-rx-buffer-size` | `int` | ```text Hardware RX buffer size, scalable between 1 kB and 8 kB, where the full 8 kB should be the default. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `hw-rx-buffer-offset` | `int` | ```text Data offset in the hardware RX packet buffer (in bytes). Valid range is 0-3 bytes. ```  This property is **required**. |
| `hw-tx-buffer-size-full` | `boolean` | ```text When set, the hardware TX data buffer will make use of the full 4 kB that are available. If unset, the hardware TX data buffer will be limited to 2 kB. ``` |
| `rx-buffer-descriptors` | `int` | ```text The number of descriptors to be allocated in the RX buffer descriptor ring. Must be <= 255. ```  This property is **required**. |
| `rx-buffer-size` | `int` | ```text The size of each receive data buffer, must be a multiple of 8, highest valid value is 16320, values less than 64 are not really useful. ```  This property is **required**. |
| `tx-buffer-descriptors` | `int` | ```text The number of descriptors to be allocated in the TX buffer descriptor ring. Must be <= 255. ```  This property is **required**. |
| `tx-buffer-size` | `int` | ```text The size of each transmit data buffer, highest valid value is 16380, values less than 64 are not really useful. ```  This property is **required**. |
| `ignore-ipg-rxer` | `boolean` | ```text Optional feature flag - Ignore IPG rx_er. When set, rx_er has no effect on the GEM's operation when rx_dv is low. Set this when using the RGMII wrapper in half-duplex mode. ``` |
| `disable-reject-nsp` | `boolean` | ```text Optional feature flag - Receive bad preamble. When set, frames with non-standard preamble will not be rejected. ``` |
| `ipg-stretch` | `boolean` | ```text Optional feature flag - Enable IPG stretch. When set, the transmit IPG can be increased above 96 bit times depending on the previous frame length using the IPG stretch register. ``` |
| `sgmii-mode` | `boolean` | ```text Optional feature flag - Enable SGMII mode. Changes the behaviour of the auto-negotiation advertisement and link partner ability registers to meet the requirements of SGMII and reduces the duration of the link timer from 10 ms to 1.6 ms. ``` |
| `disable-reject-fcs-crc-errors` | `boolean` | ```text Optional feature flag - Disable rejection of FCS/CRC errors. When set, frames with FCS/CRC errors will not be rejected. FCS error statistics will still be collected for frames with bad FCS and FCS status will be recorded in the frame's DMA descriptor. This option should not be activated for normal operation. ``` |
| `rx-halfdup-while-tx` | `boolean` | ```text Optional feature flag - Enable frames to be received in half-duplex mode while transmitting. ``` |
| `rx-checksum-offload` | `boolean` | ```text Optional feature flag - Enable RX IP/TCP/UDP checksum offload to hardware. Frames with bad IP, TCP or UDP checksums will be discarded. This option is NOT supported by the QEMU implementation of the GEM! ``` |
| `tx-checksum-offload` | `boolean` | ```text Optional feature flag - Enable TX IP/TCP/UDP checksum offload to hardware. This option is NOT supported by the QEMU implementation of the GEM! ``` |
| `disable-pause-copy` | `boolean` | ```text Optional feature flag - Do not copy received pause frames to memory. Set this option in order to prevent valid pause frames from being copied to memory. When set, pause frames are not copied to memory regardless of the state of the copy all frames bit, whether a hash match is found or whether a type ID match is identified. If a desti- nation address match is found the pause frame will be copied to memory. Note that valid pause frames received will still increment pause statistics and pause the transmission of frames as required. ``` |
| `discard-rx-fcs` | `boolean` | ```text Optional feature flag - Remove FCS of received frames. When set, received frames will be written to memory without their frame check sequence (last 4 bytes). The frame length indicated will be reduced by four bytes in this mode. ``` |
| `discard-rx-length-errors` | `boolean` | ```text Optional feature flag - Discard frames with length field errors. When set, frames with a measured length shorter than the extracted length field (as indicated by bytes 13 and 14 in a non-VLAN tagged frame) will be discarded. This only applies to frames with a length field less than 0x0600. ``` |
| `pause-frame` | `boolean` | ```text Optional feature flag - Enable pause. When set, transmission will pause if a non zero 802.3 classic pause frame is received and PFC has not been negotiated. ``` |
| `tbi` | `boolean` | ```text Optional feature flag - Enable TBI. When set, the TBI interface is en- bled instead of the GMII/MII interface. ``` |
| `ext-address-match` | `boolean` | ```text Optional feature flag - Enable external address match. When set, the external address match interface can be used to copy frames to memory. ``` |
| `long-frame-rx-support` | `boolean` | ```text Optional feature flag - Enable reception of 1536 byte frames. Normally, the GEM rejects any frame above 1518 bytes. ``` |
| `unicast-hash` | `boolean` | ```text Optional feature flag - Enable unicast hash. When set, unicast frames will be accepted when the 6 bit hash function of the destination address points to a bit that is set in the hash register. ``` |
| `multicast-hash` | `boolean` | ```text Optional feature flag - Enable multicast hash. When set, multicast frames will be accepted when the 6 bit hash function of the desti- nation address points to a bit that is set in the hash register. ``` |
| `reject-broadcast` | `boolean` | ```text Optional feature flag - Reject broadcast frames. When set, frames addressed to the all-ones broadcast address will be rejected. ``` |
| `promiscuous-mode` | `boolean` | ```text Optional feature flag - Enable promiscuous mode. When set, all valid frames will be accepted. ``` |
| `discard-non-vlan` | `boolean` | ```text Optional feature flag - Discard non-VLAN frames. When set, only VLAN tagged frames will be passed to the address matching logic. ``` |
| `full-duplex` | `boolean` | ```text Optional feature flag - Enables full duplex reception and transmission. ``` |
| `discard-rx-frame-ahb-unavail` | `boolean` | ```text Optional feature flag - Discard received packets when no AHB resource is available. ``` |
| `ahb-packet-endian-swap` | `boolean` | ```text Optional feature flag - Enable AHB packet data endianness swap to big endian. If this flag is not set, data will be little endian. ``` |
| `ahb-md-endian-swap` | `boolean` | ```text Optional feature flag - Enable AHB management descriptor data endian- ness swap to big endian. If this flag is not set, data will be little endian. ``` |
| `local-mac-address` | `uint8-array` | ```text Specifies the MAC address that was assigned to the network device ``` |
| `zephyr,random-mac-address` | `boolean` | ```text Use a random MAC address generated when the driver is initialized. Note that using this choice and rebooting a board may leave stale MAC address in peers' ARP caches and lead to issues and delays in communication.  (Use "ip neigh flush all" on Linux peers to clear ARP cache.)  It is driver specific how the OUI octets are handled.  If set we ignore any setting of the local-mac-address property. ``` |
| `phy-handle` | `phandle` | ```text Specifies a reference to a node representing a PHY device. ``` |
| `phy-connection-type` | `string` | ```text Specifies the interface connection type between ethernet MAC and PHY. ```  Legal values: `'mii'`, `'rmii'`, `'gmii'`, `'rgmii'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “xlnx,gem” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
