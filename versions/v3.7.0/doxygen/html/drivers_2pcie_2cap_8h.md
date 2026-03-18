---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2pcie_2cap_8h.html
original_path: doxygen/html/drivers_2pcie_2cap_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cap.h File Reference

PCIe Capabilities.
[More...](#details)

[Go to the source code of this file.](drivers_2pcie_2cap_8h_source.md)

| Macros | |
| --- | --- |
| PCI & PCI Express Capabilities | |
| From PCI Code and ID Assignment Specification Revision 1.11 | |
| #define | [PCI\_CAP\_ID\_NULL](group__pcie__capabilities.md#ga890142bda671b3558cd881f4b91a43ab)   0x00U |
|  | Null Capability. |
| #define | [PCI\_CAP\_ID\_PM](group__pcie__capabilities.md#ga9379bf318dd400e1076fbd5f0e331adb)   0x01U |
|  | Power Management. |
| #define | [PCI\_CAP\_ID\_AGP](group__pcie__capabilities.md#gac68c228e23e701fd4040b89c42537eac)   0x02U |
|  | Accelerated Graphics Port. |
| #define | [PCI\_CAP\_ID\_VPD](group__pcie__capabilities.md#gaf419a56a517635f4d9f8a5c6f5fd9d08)   0x03U |
|  | Vital Product Data. |
| #define | [PCI\_CAP\_ID\_SLOTID](group__pcie__capabilities.md#ga6d286311dd9f54468f125fd367683f74)   0x04U |
|  | Slot Identification. |
| #define | [PCI\_CAP\_ID\_MSI](group__pcie__capabilities.md#gad19597699011d0e047083968d2e835bd)   0x05U |
|  | Message Signalled Interrupts. |
| #define | [PCI\_CAP\_ID\_CHSWP](group__pcie__capabilities.md#ga74356319083570ca7e5cf9a3eaaadd9b)   0x06U |
|  | CompactPCI HotSwap. |
| #define | [PCI\_CAP\_ID\_PCIX](group__pcie__capabilities.md#ga24709fe61430ca25fabe665d8b1efca0)   0x07U |
|  | PCI-X. |
| #define | [PCI\_CAP\_ID\_HT](group__pcie__capabilities.md#gad50ed1a81153a04fa19534823d0109c9)   0x08U |
|  | HyperTransport. |
| #define | [PCI\_CAP\_ID\_VNDR](group__pcie__capabilities.md#ga11b65631db23369276e062560f53b433)   0x09U |
|  | Vendor-Specific. |
| #define | [PCI\_CAP\_ID\_DBG](group__pcie__capabilities.md#ga5a37d779c6259232cd4ec7bc3d80bc83)   0x0AU |
|  | Debug port. |
| #define | [PCI\_CAP\_ID\_CCRC](group__pcie__capabilities.md#gad45dfbc6ea8d963703e243dacdee084f)   0x0BU |
|  | CompactPCI Central Resource Control. |
| #define | [PCI\_CAP\_ID\_SHPC](group__pcie__capabilities.md#gae538cdbc7eba80aac860f3340823f559)   0x0CU |
|  | PCI Standard Hot-Plug Controller. |
| #define | [PCI\_CAP\_ID\_SSVID](group__pcie__capabilities.md#ga8814c4f32748170e8b5f15dc2ade5dc5)   0x0DU |
|  | Bridge subsystem vendor/device ID. |
| #define | [PCI\_CAP\_ID\_AGP3](group__pcie__capabilities.md#gae351b2497f7231bfa2c08e97ba589cb7)   0x0EU |
|  | AGP 8x. |
| #define | [PCI\_CAP\_ID\_SECDEV](group__pcie__capabilities.md#ga20c7aadce06547a3ea37ce705ff0d289)   0x0FU |
|  | Secure Device. |
| #define | [PCI\_CAP\_ID\_EXP](group__pcie__capabilities.md#ga9b0efbb129a8600203135a64377beed0)   0x10U |
|  | PCI Express. |
| #define | [PCI\_CAP\_ID\_MSIX](group__pcie__capabilities.md#ga419307c3f83f3dca9aaa329de41dae63)   0x11U |
|  | MSI-X. |
| #define | [PCI\_CAP\_ID\_SATA](group__pcie__capabilities.md#ga437d2f840145a2aae97880ad3579ca7d)   0x12U |
|  | Serial ATA Data/Index Configuration. |
| #define | [PCI\_CAP\_ID\_AF](group__pcie__capabilities.md#ga7bf330224972c1a16cbafa907387b9ed)   0x13U |
|  | PCI Advanced Features. |
| #define | [PCI\_CAP\_ID\_EA](group__pcie__capabilities.md#ga591d30c052c32a4f3cbb510e8b052b62)   0x14U |
|  | PCI Enhanced Allocation. |
| #define | [PCI\_CAP\_ID\_FPB](group__pcie__capabilities.md#gad00f421c7bc8613ad7770ea2e0a5d8da)   0x14U |
|  | Flattening Portal Bridge. |
| PCI Express Extended Capabilities | |
| #define | [PCIE\_EXT\_CAP\_ID\_NULL](group__pcie__capabilities.md#ga2f6c4feb384e41711aa53545952e3cac)   0x0000U |
|  | Null Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_ERR](group__pcie__capabilities.md#ga224acf772427857ca1f5a0b155c30d63)   0x0001U |
|  | Advanced Error Reporting. |
| #define | [PCIE\_EXT\_CAP\_ID\_VC](group__pcie__capabilities.md#gaaa8d5de1c1925dea16e40b72fafa5b8f)   0x0002U |
|  | Virtual Channel when no MFVC. |
| #define | [PCIE\_EXT\_CAP\_ID\_DSN](group__pcie__capabilities.md#ga29a18f51cad5281e3f6a283d3c7acb49)   0x0003U |
|  | Device Serial Number. |
| #define | [PCIE\_EXT\_CAP\_ID\_PWR](group__pcie__capabilities.md#gadc91da3b61af0b0a047ec74860dc3201)   0x0004U |
|  | Power Budgeting. |
| #define | [PCIE\_EXT\_CAP\_ID\_RCLD](group__pcie__capabilities.md#ga46f3607fa47b26ef099f9bfdcdb0763f)   0x0005U |
|  | Root Complex Link Declaration. |
| #define | [PCIE\_EXT\_CAP\_ID\_RCILC](group__pcie__capabilities.md#ga973a2816ae68ab75d5b4118890fd4383)   0x0006U |
|  | Root Complex Internal Link Control. |
| #define | [PCIE\_EXT\_CAP\_ID\_RCEC](group__pcie__capabilities.md#ga78b98a43b8e6661d6745df19c8591f47)   0x0007U |
|  | Root Complex Event Collector Endpoint Association. |
| #define | [PCIE\_EXT\_CAP\_ID\_MFVC](group__pcie__capabilities.md#ga2cfa2f9212fb923c3811c0cdc769a877)   0x0008U |
|  | Multi-Function VC Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_MFVC\_VC](group__pcie__capabilities.md#ga7c2b491e1c994730afe08880dfb1b036)   0x0009U |
|  | Virtual Channel used with MFVC. |
| #define | [PCIE\_EXT\_CAP\_ID\_RCRB](group__pcie__capabilities.md#ga356973ae03fb0d33df4092a311818e9b)   0x000AU |
|  | Root Complex Register Block. |
| #define | [PCIE\_EXT\_CAP\_ID\_VNDR](group__pcie__capabilities.md#gac864550f144038d5bbdf5e556faa640e)   0x000BU |
|  | Vendor-Specific Extended Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_CAC](group__pcie__capabilities.md#gaff6494cd92013933dedbab2e2ae5c6b3)   0x000CU |
|  | Config Access Correlation - obsolete. |
| #define | [PCIE\_EXT\_CAP\_ID\_ACS](group__pcie__capabilities.md#ga6b63b04d182b916db526525b064ed285)   0x000DU |
|  | Access Control Services. |
| #define | [PCIE\_EXT\_CAP\_ID\_ARI](group__pcie__capabilities.md#gaf890e2f4f3873b60ac83df345ab0cd8f)   0x000EU |
|  | Alternate Routing-ID Interpretation. |
| #define | [PCIE\_EXT\_CAP\_ID\_ATS](group__pcie__capabilities.md#ga79a9cb071afc5cff9e699c232841623c)   0x000FU |
|  | Address Translation Services. |
| #define | [PCIE\_EXT\_CAP\_ID\_SRIOV](group__pcie__capabilities.md#gae8767a1dd6e203aa2ccd75d1fd05eb7d)   0x0010U |
|  | Single Root I/O Virtualization. |
| #define | [PCIE\_EXT\_CAP\_ID\_MRIOV](group__pcie__capabilities.md#gaa117a86f2691d8711fa6b70e196ead01)   0x0011U |
|  | Multi Root I/O Virtualization. |
| #define | [PCIE\_EXT\_CAP\_ID\_MCAST](group__pcie__capabilities.md#ga2810671833871608043e6e910d79dffd)   0x0012U |
|  | Multicast. |
| #define | [PCIE\_EXT\_CAP\_ID\_PRI](group__pcie__capabilities.md#ga37e0ac002e9742bb9177588d2dfa850b)   0x0013U |
|  | Page Request Interface. |
| #define | [PCIE\_EXT\_CAP\_ID\_AMD\_XXX](group__pcie__capabilities.md#gab8be630bf1dc810f2964e979ac46f77c)   0x0014U |
|  | Reserved for AMD. |
| #define | [PCIE\_EXT\_CAP\_ID\_REBAR](group__pcie__capabilities.md#gabae7e5d40435723e6d808c377753332a)   0x0015U |
|  | Resizable BAR. |
| #define | [PCIE\_EXT\_CAP\_ID\_DPA](group__pcie__capabilities.md#ga812c156b93d070a06d3a56b5785788fd)   0x0016U |
|  | Dynamic Power Allocation. |
| #define | [PCIE\_EXT\_CAP\_ID\_TPH](group__pcie__capabilities.md#ga558289987600691fce5574feb253b4cb)   0x0017U |
|  | TPH Requester. |
| #define | [PCIE\_EXT\_CAP\_ID\_LTR](group__pcie__capabilities.md#ga9545f09c97f2dd4f751767e6e54326ec)   0x0018U |
|  | Latency Tolerance Reporting. |
| #define | [PCIE\_EXT\_CAP\_ID\_SECPCI](group__pcie__capabilities.md#gacd1a90cce3892bacc40939a04b707d20)   0x0019U |
|  | Secondary PCIe Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_PMUX](group__pcie__capabilities.md#gaf6c41b4ad9e32c4420cb89cc5a0d51c2)   0x001AU |
|  | Protocol Multiplexing. |
| #define | [PCIE\_EXT\_CAP\_ID\_PASID](group__pcie__capabilities.md#ga0c3b5efb8d9fb69a8fdbb9ca147a3069)   0x001BU |
|  | Process Address Space ID. |
| #define | [PCIE\_EXT\_CAP\_ID\_DPC](group__pcie__capabilities.md#ga40f83a1c280acb8f3f3908d860874015)   0x001DU |
|  | DPC: Downstream Port Containment. |
| #define | [PCIE\_EXT\_CAP\_ID\_L1SS](group__pcie__capabilities.md#ga3006998c35d9c8f8e3d69716cda6def7)   0x001EU |
|  | L1 PM Substates. |
| #define | [PCIE\_EXT\_CAP\_ID\_PTM](group__pcie__capabilities.md#ga134d53764458500ea4ca58fe016f46fa)   0x001FU |
|  | Precision Time Measurement. |
| #define | [PCIE\_EXT\_CAP\_ID\_DVSEC](group__pcie__capabilities.md#gab1d94b05177a5064a78e4048eff473b1)   0x0023U |
|  | Designated Vendor-Specific Extended Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_DLF](group__pcie__capabilities.md#ga2e8324ea3b27a63e213252bed6c78ca6)   0x0025U |
|  | Data Link Feature. |
| #define | [PCIE\_EXT\_CAP\_ID\_PL\_16GT](group__pcie__capabilities.md#ga60203711f9fe698f3e7e138e0468645a)   0x0026U |
|  | Physical Layer 16.0 GT/s. |
| #define | [PCIE\_EXT\_CAP\_ID\_LMR](group__pcie__capabilities.md#ga56b3b2bd686b6b99c2ae34ae57228160)   0x0027U |
|  | Lane Margining at the Receiver. |
| #define | [PCIE\_EXT\_CAP\_ID\_HID](group__pcie__capabilities.md#ga0087a39c01053f83b3ac3bb3b057ac2a)   0x0028U |
|  | Hierarchy ID. |
| #define | [PCIE\_EXT\_CAP\_ID\_NPEM](group__pcie__capabilities.md#ga03dafb2eb5449f17dc18898ea319d729)   0x0029U |
|  | Native PCIe Enclosure Management. |
| #define | [PCIE\_EXT\_CAP\_ID\_PL\_32GT](group__pcie__capabilities.md#ga8a8768d04866a479114bcf276466501f)   0x002AU |
|  | Physical Layer 32.0 GT/s. |
| #define | [PCIE\_EXT\_CAP\_ID\_AP](group__pcie__capabilities.md#ga53e188f6e71f04012e7739e75a015398)   0x002BU |
|  | Alternate Protocol. |
| #define | [PCIE\_EXT\_CAP\_ID\_SFI](group__pcie__capabilities.md#ga0e173611874d25c0cd5bd62372542380)   0x002CU |
|  | System Firmware Intermediary. |

## Detailed Description

PCIe Capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [cap.h](drivers_2pcie_2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
