---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/ethernet/snps,dwcxgmac.html
original_path: build/dts/api/bindings/ethernet/snps,dwcxgmac.html
---

# snps,dwcxgmac

Vendor: [Synopsys, Inc.](../../bindings.md#dt-vendor-snps)

Note

An implementation of a driver matching this compatible is available in
[drivers/ethernet/dwc\_xgmac/eth\_dwc\_xgmac.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/eth_dwc_xgmac.c).

## Description

```text
Synopsys DesignWareCore XGMAC
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `max-frame-size` | `int` | ```text Maximum ethernet frame size.  The current ethernet frame sizes supported by hardware are standard and jumbo (up to 16KB) frames. This means that normally xgmac will reject any frame above max-frame-size value.  The default value is 1518, which represents an usual IEEE 802.3 ethernet frame:   Ethernet Frame [ 14 MAC HEADER | 1500 MTU | 4 FCS ] = 1518 bytes ```  Default value: `1518` |
| `max-speed` | `int` | ```text This specifies maximum speed in Mbit/s supported by the device.  The xgmac driver supports 10Mbit/s, 100Mbit/s, 1000Mbit/s, and 2500Mbit/s.  Using 1000, as default value, enables driver to configure 10 and 100Mbit/s speeds. 2500Mbit/s speed can be used only with Soft PCS. When selected driver assumes soft PCS is connected to XGMAC through GMII. make sure the phy-connection-type is selected as gmii when 2500Mbit/s speed is selected. ```  Default value: `1000`  Legal values: `10`, `100`, `1000`, `2500` |
| `tx-fifo-size` | `int` | ```text Specifies the size of the MTL Transmit FIFO ```  Default value: `32768`  Legal values: `1024`, `2048`, `4096`, `8192`, `16384`, `32768`, `65536`, `131072`, `262144` |
| `rx-fifo-size` | `int` | ```text Specifies the size of the MTL Receive FIFO ```  Default value: `32768`  Legal values: `1024`, `2048`, `4096`, `8192`, `16384`, `32768`, `65536`, `131072`, `262144` |
| `num-dma-ch` | `int` | ```text Number of dma channels range: 1 to 8. ```  This property is **required**. |
| `num-tx-queues` | `int` | ```text Number of hardware TX queues range: 1 to 8. ```  This property is **required**. |
| `num-rx-queues` | `int` | ```text Number of hardware RX queues range: 1 to 8. ```  This property is **required**. |
| `num-tc` | `int` | ```text Number of traffic classes range: 1 to 7. ```  Default value: `1` |
| `full-duplex-mode-en` | `boolean` | ```text MAC communication mode to full duplex mode. ```  This property is **required**. |
| `wr-osr-lmt` | `int` | ```text AXI Maximum Write Outstanding Request Limit.This value limits the maximum outstanding request on the AXI write interface. Maximum outstanding requests = WR_OSR_LMT + 1 ```  Default value: `31` |
| `rd-osr-lmt` | `int` | ```text AXI Maximum Read Outstanding Request Limit.This value limits the maximum outstanding request on the AXI read interface. Maximum outstanding requests = WR_OSR_LMT + 1 ```  Default value: `31` |
| `pbl` | `int` | ```text Programmable burst length range: 4,5,16,32,64,128,256 ```  Default value: `32` |
| `edma-tdps` | `int` | ```text Tx Descriptor Pre-fetch threshold Size. This field controls the threshold in the Descriptor cache after which the DMA starts pre-fetching the TxDMA descriptors. The DMA engine for all TxDMA channels initiate requests for the descriptor fetches as soon as the number of descriptors in the cache memory for that DMA channel, falls below or equal to the programmed threshold (each descriptor is 16 bytes) Range: 0,1,2,3,4,5 ```  Default value: `1` |
| `edma-rdps` | `int` | ```text Rx Descriptor Pre-fetch threshold Size. This field controls the threshold in the Descriptor cache after which the DMA starts pre-fetching the RxDMA descriptors. The DMA engine for all RxDMA channels initiate requests for the descriptor fetches as soon as the number of descriptors in the cache memory for that DMA channel, falls below or equal to the programmed threshold (each descriptor is 16 bytes) Range: 0,1,2,3,4,5 ```  Default value: `1` |
| `pblx8` | `boolean` | ```text 8xPBL mode. When this is set to true, the PBL value is multiplied eight times. Therefore, the DMA transfers the data in 8, 16, 32, 64, 128, and 256 beats depending on the PBL value. ``` |
| `ubl` | `boolean` | ```text AXI Undefined Burst Length. 1: The AXI master can perform burst transfers that are equal to or less than the maximum allowed burst length enabled. 0: The AXI master performs one of the following burst transfers: Burst transfers of fixed burst lengths as indicated by the BLEN256, BLEN128, BLEN64, BLEN32, BLEN16, BLEN8, or BLEN4 field. ``` |
| `blen4` | `boolean` | ```text AXI Burst Length 4. When this enabled and the mixed_burst is disabled, the AXI master can select a burst length of 4 on the AXI interface. When the mixed_burst enabled, enabling this field has no effect. ``` |
| `blen8` | `boolean` | ```text AXI Burst Length 8. When this enabled and the mixed_burst is disabled, the AXI master can select a burst length of 8 on the AXI interface. When the mixed_burst enabled, enabling this field has no effect. ``` |
| `blen16` | `boolean` | ```text AXI Burst Length 16. When this enabled and the mixed_burst is disabled, the AXI master can select a burst length of 16 on the AXI interface. When the mixed_burst enabled, enabling this field has no effect. ``` |
| `blen32` | `boolean` | ```text AXI Burst Length 32. When this enabled and the mixed_burst is disabled, the AXI master can select a burst length of 32 on the AXI interface. When the mixed_burst enabled, enabling this field has no effect. ``` |
| `blen64` | `boolean` | ```text AXI Burst Length 64. When this enabled and the mixed_burst is disabled, the AXI master can select a burst length of 64 on the AXI interface. When the mixed_burst enabled, enabling this field has no effect. ``` |
| `blen128` | `boolean` | ```text AXI Burst Length 128. When this enabled and the mixed_burst is disabled, the AXI master can select a burst length of 128 on the AXI interface. When the mixed_burst enabled, enabling this field has no effect. ``` |
| `blen256` | `boolean` | ```text AXI Burst Length 256. When this enabled and the mixed_burst is disabled, the AXI master can select a burst length of 256 on the AXI interface. When the mixed_burst enabled, enabling this field has no effect. ``` |
| `aal` | `boolean` | ```text Address-Aligned Beats. When this is enabled, the AXI master performs address-aligned burst transfers on Read and Write channels. ``` |
| `eame` | `boolean` | ```text Enhanced Address Mode Enable. DMA master enables the enhanced address mode (40-bit or 48-bit addressing mode). In this mode, the DMA engine uses either the 40-bit or 48-bit address, depending on the configuration. ``` |
| `dma-ch-mss` | `int` | ```text Maximum Segment Size. This field specifies the maximum segment size that must be used while segmenting the Transmit packet. This field is valid only if the TSE enabled. ```  Default value: `4096` |
| `dma-ch-tdrl` | `int` | ```text Transmit Descriptor Ring Length. This field sets the maximum number of Tx descriptors in the circular descriptor ring. The maximum number of descriptors is limited to 16384 descriptors. ```  Default value: `512` |
| `dma-ch-rdrl` | `int` | ```text Receive Descriptor Ring Length. This field sets the maximum number of Rx descriptors in the circular descriptor ring. The maximum number of descriptors is limited to 16384 descriptors. ```  Default value: `512` |
| `dma-ch-rbsz` | `int` | ```text Receive Buffer size. This field indicates the size of the Rx buffers specified in bytes allocated by the software to store the packets the Rx DMA transfers to the host memory. The maximum buffer size is limited to 16K bytes. The buffer size is applicable to payload buffers when split headers are enabled. ```  Default value: `16383` |
| `dma-ch-arbs` | `int` | ```text Alternate Receive Buffer Size Indicates size in bytes for Buffer 1 when ARBS is set to a non-zero value (when split header(SPH) feature is not enabled). When split header feature is enabled, ARBS indicates the buffer size for header data. The maximum alternate buffer is limited to 1016 or 1008-bytes depending on the data bus widths (64-bit or 128-bit respectively). When ARBS=0, Rx Buffer1 and Rx Buffer2 sizes are based on RBSZ field. Width of ARBS field is 7 or 6-bits depending on the data bus widths (64-bit or 128-bit respectively). ``` |
| `dma-ch-rxpbl` | `int` | ```text Receive Programmable Burst Length. These field indicate the maximum number of beats to be transferred in one DMA data transfer. ```  Default value: `32` |
| `dma-ch-txpbl` | `int` | ```text Transmit   Programmable Burst Length. These field indicate the maximum number of beats to be transferred in one DMA data transfer. ```  Default value: `32` |
| `dma-ch-sph` | `boolean` | ```text Header-Payload Split. When this field is set, the DMA splits the header and payload in the Receive path. The DMA writes the header to the Buffer Address1. The DMA writes the payload to the buffer to which the Buffer Address2 is pointing. The software must ensure that the header fits into the Receive buffers. If the header length exceeds the receive buffer size, the DMA does not split the header and payload. ``` |
| `dma-ch-edse` | `boolean` | ```text Enhanced Descriptor Enable. When this field is set, the corresponding channel uses enhanced Descriptors. ``` |
| `dma-ch-tse` | `boolean` | ```text TCP Segmentation Enabled. When this field is set, the DMA performs the TCP segmentation for packets in Channel. The TCP segmentation is done only for those packets for which the TSE is set in the Tx Normal descriptor. ``` |
| `dma-ch-osp` | `boolean` | ```text Operate on Second Packet. When this field is set, it instructs the DMA to process the second packet of the Transmit data even before closing the descriptor of the first packet. ``` |
| `mtl-raa` | `boolean` | ```text Receive Arbitration Algorithm. This field is used to select the arbitration algorithm for the Rx side. 0: Strict Priority (SP), 1: Weighted Strict Priority (WSP) ``` |
| `mtl-etsalg` | `int` | ```text ETS Algorithm. This field selects the type of ETS algorithm to be applied for traffic classes whose transmission selection algorithm (TSA) is set to ETS: 0: WRR algorithm 1: WFQ algorithm 2: DWRR algorithm ``` |
| `rxq-dyn-dma-en` | `int` | ```text Receive Queue Enabled for Dynamic DMA Channel Selection. Each bit position of this field maps to a queue. there are total 8 queues ```  Default value: `1` |
| `rxq-dma-ch-sel` | `uint8-array` | ```text Receive Queue Mapped to DMA Channel. this field does not have effect when rxQ-DynDma-En is enabled. range 0 - 7 ```  Default value: `[0, 1, 2, 3, 4, 5, 6, 7]` |
| `txq-size` | `uint8-array` | ```text This field indicates the size of the allocated Transmit queues in blocks of 256 bytes. = (txQ-size + 1) x 256 range: 0 - 7 ```  Default value: `[127]` |
| `map-queue-tc` | `uint8-array` | ```text Queue to Traffic Class Mapping. range 0 - 7 ```  Default value: `[0]` |
| `tx-threshold-ctrl` | `uint8-array` | ```text Transmit Threshold Control. These field control the threshold level of the MTL Tx Queue. Transmission starts when the packet size within the MTL Tx Queue is larger than the threshold. In addition, full packets with length less than the threshold are also transmitted. This field us used only when Transmit Store and Forward is disabled. range 0 - 7       0: 64       1: reserved       2: 96       3: 128       4: 192       5: 256       6: 384       7: 512 ```  Default value: `[0]` |
| `rx-threshold-ctrl` | `uint8-array` | ```text The received packet is transferred to the application or DMA when the packet size within the MTL Rx queue is larger than the threshold. In addition, full packets with length less than the threshold are automatically transferred. The value of 11 is not applicable if the size of the configured Rx Queue is 128 bytes. This field is valid only when the RSF bit is zero. This field is ignored when the RSF field is set to 1. range 0 - 3       0: 64       1: reserved       2: 96       3: 128 ```  Default value: `[0]` |
| `rxq-size` | `uint8-array` | ```text Receive Queue Size. This field indicates the size of the allocated Receive queues in blocks 256 bytes. = (rxQ-size + 1) x 256 Range: 0 - 127 , ```  Default value: `[127]` |
| `tx-store-fwrd-en` | `int` | ```text Transmit Store and Forward. When this field is set, the transmission starts when a full packet resides in the MTL Tx Queue. Each bit position of this field maps to a queue. there are total 8 queues ```  Default value: `255` |
| `hfc-en` | `int` | ```text Enable Hardware Flow Control. When this field is set, the flow control signal operation, based on the fill-level of Rx queue, is enabled. Each bit position of this field maps to a queue. there are total 8 queues ``` |
| `cs-error-pkt-drop-dis` | `int` | ```text Disable Dropping of TCP/IP Checksum Error Packets Each bit position of this field maps to a queue. there are total 8 queues ``` |
| `rx-store-fwrd-en` | `int` | ```text Receive Store and Forward. When this field is set, DWC_xgmac reads a packet from the Rx queue only after the complete packet has been written to it. Each bit position of this field maps to a queue. there are total 8 queues ```  Default value: `255` |
| `fep-en` | `int` | ```text Forward Error Packets.  When this bit is set, all packets except the runt error packets are forwarded to the application or DMA. Each bit position of this field maps to a queue. there are total 8 queues ``` |
| `fup-en` | `int` | ```text Forward Undersized Good Packets. When this field is set, the Rx queue forwards the undersized good packets. Each bit position of this field maps to a queue. there are total 8 queues ``` |
| `priorities-map-tc` | `array` | ```text Priorities Mapped to Traffic Class. This field determines if the transmit queues associated with the traffic class should be blocked from transmitting for the specified pause time when a PFC packet is received with priorities matching the priorities programmed in this field. range: 0 - 7 and max array size is 8 ex: <0,1,2,3,4,5,6,7> ```  Default value: `[0]` |
| `tx-sel-algorithm` | `uint8-array` | ```text Transmission Selection Algorithm. This field is used to assign a transmission selection algorithm for this traffic class. range: 0 -strict priority        1 - Credit based shaper        2 - Enhanced Transmission Selection ```  Default value: `[0]` |
| `jumbo-pkt-en` | `boolean` | ```text Jumbo Packet Enable. When this bit is set, the MAC allows jumbo packets of 9018 bytes (9022 bytes for VLAN tagged packets) without reporting a giant packet error in the Rx packet status ``` |
| `gaint-pkt-size-limit` | `int` | ```text Giant Packet Size Limit. If the received packet size is greater than the value programmed in this field in units of bytes, the MAC declares the received packet as Giant packet. The value programmed in this field must be greater than or equal to 1518 bytes. Any other programmed value is considered as 1518 bytes. ```  Default value: `9018` |
| `resets` | `phandle-array` | ```text Reset information ``` |
| `reset-names` | `string-array` | ```text Name of each reset ``` |
| `local-mac-address` | `uint8-array` | ```text Specifies the MAC address that was assigned to the network device ``` |
| `zephyr,random-mac-address` | `boolean` | ```text Use a random MAC address generated when the driver is initialized. Note that using this choice and rebooting a board may leave stale MAC address in peers' ARP caches and lead to issues and delays in communication.  (Use "ip neigh flush all" on Linux peers to clear ARP cache.)  It is driver specific how the OUI octets are handled.  If set we ignore any setting of the local-mac-address property. ``` |
| `phy-handle` | `phandle` | ```text Specifies a reference to a node representing a PHY device. ``` |
| `phy-connection-type` | `string` | ```text Specifies the interface connection type between ethernet MAC and PHY. ```  Legal values: `'mii'`, `'rmii'`, `'gmii'`, `'rgmii'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “snps,dwcxgmac” compatible.

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
