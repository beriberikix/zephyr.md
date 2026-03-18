---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__pcie__capabilities.html
original_path: doxygen/html/group__pcie__capabilities.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PCIe Capabilities

[Device Driver APIs](group__io__interfaces.md) » [PCIe Host Interface](group__pcie__host__interface.md)

| PCI & PCI Express Capabilities | |
| --- | --- |
| From PCI Code and ID Assignment Specification Revision 1.11 | |
| #define | [PCI\_CAP\_ID\_NULL](#ga890142bda671b3558cd881f4b91a43ab)   0x00U |
|  | Null Capability. |
| #define | [PCI\_CAP\_ID\_PM](#ga9379bf318dd400e1076fbd5f0e331adb)   0x01U |
|  | Power Management. |
| #define | [PCI\_CAP\_ID\_AGP](#gac68c228e23e701fd4040b89c42537eac)   0x02U |
|  | Accelerated Graphics Port. |
| #define | [PCI\_CAP\_ID\_VPD](#gaf419a56a517635f4d9f8a5c6f5fd9d08)   0x03U |
|  | Vital Product Data. |
| #define | [PCI\_CAP\_ID\_SLOTID](#ga6d286311dd9f54468f125fd367683f74)   0x04U |
|  | Slot Identification. |
| #define | [PCI\_CAP\_ID\_MSI](#gad19597699011d0e047083968d2e835bd)   0x05U |
|  | Message Signalled Interrupts. |
| #define | [PCI\_CAP\_ID\_CHSWP](#ga74356319083570ca7e5cf9a3eaaadd9b)   0x06U |
|  | CompactPCI HotSwap. |
| #define | [PCI\_CAP\_ID\_PCIX](#ga24709fe61430ca25fabe665d8b1efca0)   0x07U |
|  | PCI-X. |
| #define | [PCI\_CAP\_ID\_HT](#gad50ed1a81153a04fa19534823d0109c9)   0x08U |
|  | HyperTransport. |
| #define | [PCI\_CAP\_ID\_VNDR](#ga11b65631db23369276e062560f53b433)   0x09U |
|  | Vendor-Specific. |
| #define | [PCI\_CAP\_ID\_DBG](#ga5a37d779c6259232cd4ec7bc3d80bc83)   0x0AU |
|  | Debug port. |
| #define | [PCI\_CAP\_ID\_CCRC](#gad45dfbc6ea8d963703e243dacdee084f)   0x0BU |
|  | CompactPCI Central Resource Control. |
| #define | [PCI\_CAP\_ID\_SHPC](#gae538cdbc7eba80aac860f3340823f559)   0x0CU |
|  | PCI Standard Hot-Plug Controller. |
| #define | [PCI\_CAP\_ID\_SSVID](#ga8814c4f32748170e8b5f15dc2ade5dc5)   0x0DU |
|  | Bridge subsystem vendor/device ID. |
| #define | [PCI\_CAP\_ID\_AGP3](#gae351b2497f7231bfa2c08e97ba589cb7)   0x0EU |
|  | AGP 8x. |
| #define | [PCI\_CAP\_ID\_SECDEV](#ga20c7aadce06547a3ea37ce705ff0d289)   0x0FU |
|  | Secure Device. |
| #define | [PCI\_CAP\_ID\_EXP](#ga9b0efbb129a8600203135a64377beed0)   0x10U |
|  | PCI Express. |
| #define | [PCI\_CAP\_ID\_MSIX](#ga419307c3f83f3dca9aaa329de41dae63)   0x11U |
|  | MSI-X. |
| #define | [PCI\_CAP\_ID\_SATA](#ga437d2f840145a2aae97880ad3579ca7d)   0x12U |
|  | Serial ATA Data/Index Configuration. |
| #define | [PCI\_CAP\_ID\_AF](#ga7bf330224972c1a16cbafa907387b9ed)   0x13U |
|  | PCI Advanced Features. |
| #define | [PCI\_CAP\_ID\_EA](#ga591d30c052c32a4f3cbb510e8b052b62)   0x14U |
|  | PCI Enhanced Allocation. |
| #define | [PCI\_CAP\_ID\_FPB](#gad00f421c7bc8613ad7770ea2e0a5d8da)   0x14U |
|  | Flattening Portal Bridge. |

| PCI Express Extended Capabilities | |
| --- | --- |
| #define | [PCIE\_EXT\_CAP\_ID\_NULL](#ga2f6c4feb384e41711aa53545952e3cac)   0x0000U |
|  | Null Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_ERR](#ga224acf772427857ca1f5a0b155c30d63)   0x0001U |
|  | Advanced Error Reporting. |
| #define | [PCIE\_EXT\_CAP\_ID\_VC](#gaaa8d5de1c1925dea16e40b72fafa5b8f)   0x0002U |
|  | Virtual Channel when no MFVC. |
| #define | [PCIE\_EXT\_CAP\_ID\_DSN](#ga29a18f51cad5281e3f6a283d3c7acb49)   0x0003U |
|  | Device Serial Number. |
| #define | [PCIE\_EXT\_CAP\_ID\_PWR](#gadc91da3b61af0b0a047ec74860dc3201)   0x0004U |
|  | Power Budgeting. |
| #define | [PCIE\_EXT\_CAP\_ID\_RCLD](#ga46f3607fa47b26ef099f9bfdcdb0763f)   0x0005U |
|  | Root Complex Link Declaration. |
| #define | [PCIE\_EXT\_CAP\_ID\_RCILC](#ga973a2816ae68ab75d5b4118890fd4383)   0x0006U |
|  | Root Complex Internal Link Control. |
| #define | [PCIE\_EXT\_CAP\_ID\_RCEC](#ga78b98a43b8e6661d6745df19c8591f47)   0x0007U |
|  | Root Complex Event Collector Endpoint Association. |
| #define | [PCIE\_EXT\_CAP\_ID\_MFVC](#ga2cfa2f9212fb923c3811c0cdc769a877)   0x0008U |
|  | Multi-Function VC Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_MFVC\_VC](#ga7c2b491e1c994730afe08880dfb1b036)   0x0009U |
|  | Virtual Channel used with MFVC. |
| #define | [PCIE\_EXT\_CAP\_ID\_RCRB](#ga356973ae03fb0d33df4092a311818e9b)   0x000AU |
|  | Root Complex Register Block. |
| #define | [PCIE\_EXT\_CAP\_ID\_VNDR](#gac864550f144038d5bbdf5e556faa640e)   0x000BU |
|  | Vendor-Specific Extended Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_CAC](#gaff6494cd92013933dedbab2e2ae5c6b3)   0x000CU |
|  | Config Access Correlation - obsolete. |
| #define | [PCIE\_EXT\_CAP\_ID\_ACS](#ga6b63b04d182b916db526525b064ed285)   0x000DU |
|  | Access Control Services. |
| #define | [PCIE\_EXT\_CAP\_ID\_ARI](#gaf890e2f4f3873b60ac83df345ab0cd8f)   0x000EU |
|  | Alternate Routing-ID Interpretation. |
| #define | [PCIE\_EXT\_CAP\_ID\_ATS](#ga79a9cb071afc5cff9e699c232841623c)   0x000FU |
|  | Address Translation Services. |
| #define | [PCIE\_EXT\_CAP\_ID\_SRIOV](#gae8767a1dd6e203aa2ccd75d1fd05eb7d)   0x0010U |
|  | Single Root I/O Virtualization. |
| #define | [PCIE\_EXT\_CAP\_ID\_MRIOV](#gaa117a86f2691d8711fa6b70e196ead01)   0x0011U |
|  | Multi Root I/O Virtualization. |
| #define | [PCIE\_EXT\_CAP\_ID\_MCAST](#ga2810671833871608043e6e910d79dffd)   0x0012U |
|  | Multicast. |
| #define | [PCIE\_EXT\_CAP\_ID\_PRI](#ga37e0ac002e9742bb9177588d2dfa850b)   0x0013U |
|  | Page Request Interface. |
| #define | [PCIE\_EXT\_CAP\_ID\_AMD\_XXX](#gab8be630bf1dc810f2964e979ac46f77c)   0x0014U |
|  | Reserved for AMD. |
| #define | [PCIE\_EXT\_CAP\_ID\_REBAR](#gabae7e5d40435723e6d808c377753332a)   0x0015U |
|  | Resizable BAR. |
| #define | [PCIE\_EXT\_CAP\_ID\_DPA](#ga812c156b93d070a06d3a56b5785788fd)   0x0016U |
|  | Dynamic Power Allocation. |
| #define | [PCIE\_EXT\_CAP\_ID\_TPH](#ga558289987600691fce5574feb253b4cb)   0x0017U |
|  | TPH Requester. |
| #define | [PCIE\_EXT\_CAP\_ID\_LTR](#ga9545f09c97f2dd4f751767e6e54326ec)   0x0018U |
|  | Latency Tolerance Reporting. |
| #define | [PCIE\_EXT\_CAP\_ID\_SECPCI](#gacd1a90cce3892bacc40939a04b707d20)   0x0019U |
|  | Secondary PCIe Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_PMUX](#gaf6c41b4ad9e32c4420cb89cc5a0d51c2)   0x001AU |
|  | Protocol Multiplexing. |
| #define | [PCIE\_EXT\_CAP\_ID\_PASID](#ga0c3b5efb8d9fb69a8fdbb9ca147a3069)   0x001BU |
|  | Process Address Space ID. |
| #define | [PCIE\_EXT\_CAP\_ID\_DPC](#ga40f83a1c280acb8f3f3908d860874015)   0x001DU |
|  | DPC: Downstream Port Containment. |
| #define | [PCIE\_EXT\_CAP\_ID\_L1SS](#ga3006998c35d9c8f8e3d69716cda6def7)   0x001EU |
|  | L1 PM Substates. |
| #define | [PCIE\_EXT\_CAP\_ID\_PTM](#ga134d53764458500ea4ca58fe016f46fa)   0x001FU |
|  | Precision Time Measurement. |
| #define | [PCIE\_EXT\_CAP\_ID\_DVSEC](#gab1d94b05177a5064a78e4048eff473b1)   0x0023U |
|  | Designated Vendor-Specific Extended Capability. |
| #define | [PCIE\_EXT\_CAP\_ID\_DLF](#ga2e8324ea3b27a63e213252bed6c78ca6)   0x0025U |
|  | Data Link Feature. |
| #define | [PCIE\_EXT\_CAP\_ID\_PL\_16GT](#ga60203711f9fe698f3e7e138e0468645a)   0x0026U |
|  | Physical Layer 16.0 GT/s. |
| #define | [PCIE\_EXT\_CAP\_ID\_LMR](#ga56b3b2bd686b6b99c2ae34ae57228160)   0x0027U |
|  | Lane Margining at the Receiver. |
| #define | [PCIE\_EXT\_CAP\_ID\_HID](#ga0087a39c01053f83b3ac3bb3b057ac2a)   0x0028U |
|  | Hierarchy ID. |
| #define | [PCIE\_EXT\_CAP\_ID\_NPEM](#ga03dafb2eb5449f17dc18898ea319d729)   0x0029U |
|  | Native PCIe Enclosure Management. |
| #define | [PCIE\_EXT\_CAP\_ID\_PL\_32GT](#ga8a8768d04866a479114bcf276466501f)   0x002AU |
|  | Physical Layer 32.0 GT/s. |
| #define | [PCIE\_EXT\_CAP\_ID\_AP](#ga53e188f6e71f04012e7739e75a015398)   0x002BU |
|  | Alternate Protocol. |
| #define | [PCIE\_EXT\_CAP\_ID\_SFI](#ga0e173611874d25c0cd5bd62372542380)   0x002CU |
|  | System Firmware Intermediary. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga7bf330224972c1a16cbafa907387b9ed)PCI\_CAP\_ID\_AF

| #define PCI\_CAP\_ID\_AF   0x13U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

PCI Advanced Features.

## [◆ ](#gac68c228e23e701fd4040b89c42537eac)PCI\_CAP\_ID\_AGP

| #define PCI\_CAP\_ID\_AGP   0x02U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Accelerated Graphics Port.

## [◆ ](#gae351b2497f7231bfa2c08e97ba589cb7)PCI\_CAP\_ID\_AGP3

| #define PCI\_CAP\_ID\_AGP3   0x0EU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

AGP 8x.

## [◆ ](#gad45dfbc6ea8d963703e243dacdee084f)PCI\_CAP\_ID\_CCRC

| #define PCI\_CAP\_ID\_CCRC   0x0BU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

CompactPCI Central Resource Control.

## [◆ ](#ga74356319083570ca7e5cf9a3eaaadd9b)PCI\_CAP\_ID\_CHSWP

| #define PCI\_CAP\_ID\_CHSWP   0x06U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

CompactPCI HotSwap.

## [◆ ](#ga5a37d779c6259232cd4ec7bc3d80bc83)PCI\_CAP\_ID\_DBG

| #define PCI\_CAP\_ID\_DBG   0x0AU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Debug port.

## [◆ ](#ga591d30c052c32a4f3cbb510e8b052b62)PCI\_CAP\_ID\_EA

| #define PCI\_CAP\_ID\_EA   0x14U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

PCI Enhanced Allocation.

## [◆ ](#ga9b0efbb129a8600203135a64377beed0)PCI\_CAP\_ID\_EXP

| #define PCI\_CAP\_ID\_EXP   0x10U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

PCI Express.

## [◆ ](#gad00f421c7bc8613ad7770ea2e0a5d8da)PCI\_CAP\_ID\_FPB

| #define PCI\_CAP\_ID\_FPB   0x14U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Flattening Portal Bridge.

## [◆ ](#gad50ed1a81153a04fa19534823d0109c9)PCI\_CAP\_ID\_HT

| #define PCI\_CAP\_ID\_HT   0x08U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

HyperTransport.

## [◆ ](#gad19597699011d0e047083968d2e835bd)PCI\_CAP\_ID\_MSI

| #define PCI\_CAP\_ID\_MSI   0x05U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Message Signalled Interrupts.

## [◆ ](#ga419307c3f83f3dca9aaa329de41dae63)PCI\_CAP\_ID\_MSIX

| #define PCI\_CAP\_ID\_MSIX   0x11U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

MSI-X.

## [◆ ](#ga890142bda671b3558cd881f4b91a43ab)PCI\_CAP\_ID\_NULL

| #define PCI\_CAP\_ID\_NULL   0x00U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Null Capability.

## [◆ ](#ga24709fe61430ca25fabe665d8b1efca0)PCI\_CAP\_ID\_PCIX

| #define PCI\_CAP\_ID\_PCIX   0x07U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

PCI-X.

## [◆ ](#ga9379bf318dd400e1076fbd5f0e331adb)PCI\_CAP\_ID\_PM

| #define PCI\_CAP\_ID\_PM   0x01U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Power Management.

## [◆ ](#ga437d2f840145a2aae97880ad3579ca7d)PCI\_CAP\_ID\_SATA

| #define PCI\_CAP\_ID\_SATA   0x12U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Serial ATA Data/Index Configuration.

## [◆ ](#ga20c7aadce06547a3ea37ce705ff0d289)PCI\_CAP\_ID\_SECDEV

| #define PCI\_CAP\_ID\_SECDEV   0x0FU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Secure Device.

## [◆ ](#gae538cdbc7eba80aac860f3340823f559)PCI\_CAP\_ID\_SHPC

| #define PCI\_CAP\_ID\_SHPC   0x0CU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

PCI Standard Hot-Plug Controller.

## [◆ ](#ga6d286311dd9f54468f125fd367683f74)PCI\_CAP\_ID\_SLOTID

| #define PCI\_CAP\_ID\_SLOTID   0x04U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Slot Identification.

## [◆ ](#ga8814c4f32748170e8b5f15dc2ade5dc5)PCI\_CAP\_ID\_SSVID

| #define PCI\_CAP\_ID\_SSVID   0x0DU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Bridge subsystem vendor/device ID.

## [◆ ](#ga11b65631db23369276e062560f53b433)PCI\_CAP\_ID\_VNDR

| #define PCI\_CAP\_ID\_VNDR   0x09U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Vendor-Specific.

## [◆ ](#gaf419a56a517635f4d9f8a5c6f5fd9d08)PCI\_CAP\_ID\_VPD

| #define PCI\_CAP\_ID\_VPD   0x03U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Vital Product Data.

## [◆ ](#ga6b63b04d182b916db526525b064ed285)PCIE\_EXT\_CAP\_ID\_ACS

| #define PCIE\_EXT\_CAP\_ID\_ACS   0x000DU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Access Control Services.

## [◆ ](#gab8be630bf1dc810f2964e979ac46f77c)PCIE\_EXT\_CAP\_ID\_AMD\_XXX

| #define PCIE\_EXT\_CAP\_ID\_AMD\_XXX   0x0014U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Reserved for AMD.

## [◆ ](#ga53e188f6e71f04012e7739e75a015398)PCIE\_EXT\_CAP\_ID\_AP

| #define PCIE\_EXT\_CAP\_ID\_AP   0x002BU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Alternate Protocol.

## [◆ ](#gaf890e2f4f3873b60ac83df345ab0cd8f)PCIE\_EXT\_CAP\_ID\_ARI

| #define PCIE\_EXT\_CAP\_ID\_ARI   0x000EU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Alternate Routing-ID Interpretation.

## [◆ ](#ga79a9cb071afc5cff9e699c232841623c)PCIE\_EXT\_CAP\_ID\_ATS

| #define PCIE\_EXT\_CAP\_ID\_ATS   0x000FU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Address Translation Services.

## [◆ ](#gaff6494cd92013933dedbab2e2ae5c6b3)PCIE\_EXT\_CAP\_ID\_CAC

| #define PCIE\_EXT\_CAP\_ID\_CAC   0x000CU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Config Access Correlation - obsolete.

## [◆ ](#ga2e8324ea3b27a63e213252bed6c78ca6)PCIE\_EXT\_CAP\_ID\_DLF

| #define PCIE\_EXT\_CAP\_ID\_DLF   0x0025U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Data Link Feature.

## [◆ ](#ga812c156b93d070a06d3a56b5785788fd)PCIE\_EXT\_CAP\_ID\_DPA

| #define PCIE\_EXT\_CAP\_ID\_DPA   0x0016U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Dynamic Power Allocation.

## [◆ ](#ga40f83a1c280acb8f3f3908d860874015)PCIE\_EXT\_CAP\_ID\_DPC

| #define PCIE\_EXT\_CAP\_ID\_DPC   0x001DU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

DPC: Downstream Port Containment.

## [◆ ](#ga29a18f51cad5281e3f6a283d3c7acb49)PCIE\_EXT\_CAP\_ID\_DSN

| #define PCIE\_EXT\_CAP\_ID\_DSN   0x0003U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Device Serial Number.

## [◆ ](#gab1d94b05177a5064a78e4048eff473b1)PCIE\_EXT\_CAP\_ID\_DVSEC

| #define PCIE\_EXT\_CAP\_ID\_DVSEC   0x0023U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Designated Vendor-Specific Extended Capability.

## [◆ ](#ga224acf772427857ca1f5a0b155c30d63)PCIE\_EXT\_CAP\_ID\_ERR

| #define PCIE\_EXT\_CAP\_ID\_ERR   0x0001U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Advanced Error Reporting.

## [◆ ](#ga0087a39c01053f83b3ac3bb3b057ac2a)PCIE\_EXT\_CAP\_ID\_HID

| #define PCIE\_EXT\_CAP\_ID\_HID   0x0028U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Hierarchy ID.

## [◆ ](#ga3006998c35d9c8f8e3d69716cda6def7)PCIE\_EXT\_CAP\_ID\_L1SS

| #define PCIE\_EXT\_CAP\_ID\_L1SS   0x001EU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

L1 PM Substates.

## [◆ ](#ga56b3b2bd686b6b99c2ae34ae57228160)PCIE\_EXT\_CAP\_ID\_LMR

| #define PCIE\_EXT\_CAP\_ID\_LMR   0x0027U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Lane Margining at the Receiver.

## [◆ ](#ga9545f09c97f2dd4f751767e6e54326ec)PCIE\_EXT\_CAP\_ID\_LTR

| #define PCIE\_EXT\_CAP\_ID\_LTR   0x0018U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Latency Tolerance Reporting.

## [◆ ](#ga2810671833871608043e6e910d79dffd)PCIE\_EXT\_CAP\_ID\_MCAST

| #define PCIE\_EXT\_CAP\_ID\_MCAST   0x0012U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Multicast.

## [◆ ](#ga2cfa2f9212fb923c3811c0cdc769a877)PCIE\_EXT\_CAP\_ID\_MFVC

| #define PCIE\_EXT\_CAP\_ID\_MFVC   0x0008U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Multi-Function VC Capability.

## [◆ ](#ga7c2b491e1c994730afe08880dfb1b036)PCIE\_EXT\_CAP\_ID\_MFVC\_VC

| #define PCIE\_EXT\_CAP\_ID\_MFVC\_VC   0x0009U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Virtual Channel used with MFVC.

## [◆ ](#gaa117a86f2691d8711fa6b70e196ead01)PCIE\_EXT\_CAP\_ID\_MRIOV

| #define PCIE\_EXT\_CAP\_ID\_MRIOV   0x0011U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Multi Root I/O Virtualization.

## [◆ ](#ga03dafb2eb5449f17dc18898ea319d729)PCIE\_EXT\_CAP\_ID\_NPEM

| #define PCIE\_EXT\_CAP\_ID\_NPEM   0x0029U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Native PCIe Enclosure Management.

## [◆ ](#ga2f6c4feb384e41711aa53545952e3cac)PCIE\_EXT\_CAP\_ID\_NULL

| #define PCIE\_EXT\_CAP\_ID\_NULL   0x0000U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Null Capability.

## [◆ ](#ga0c3b5efb8d9fb69a8fdbb9ca147a3069)PCIE\_EXT\_CAP\_ID\_PASID

| #define PCIE\_EXT\_CAP\_ID\_PASID   0x001BU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Process Address Space ID.

## [◆ ](#ga60203711f9fe698f3e7e138e0468645a)PCIE\_EXT\_CAP\_ID\_PL\_16GT

| #define PCIE\_EXT\_CAP\_ID\_PL\_16GT   0x0026U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Physical Layer 16.0 GT/s.

## [◆ ](#ga8a8768d04866a479114bcf276466501f)PCIE\_EXT\_CAP\_ID\_PL\_32GT

| #define PCIE\_EXT\_CAP\_ID\_PL\_32GT   0x002AU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Physical Layer 32.0 GT/s.

## [◆ ](#gaf6c41b4ad9e32c4420cb89cc5a0d51c2)PCIE\_EXT\_CAP\_ID\_PMUX

| #define PCIE\_EXT\_CAP\_ID\_PMUX   0x001AU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Protocol Multiplexing.

## [◆ ](#ga37e0ac002e9742bb9177588d2dfa850b)PCIE\_EXT\_CAP\_ID\_PRI

| #define PCIE\_EXT\_CAP\_ID\_PRI   0x0013U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Page Request Interface.

## [◆ ](#ga134d53764458500ea4ca58fe016f46fa)PCIE\_EXT\_CAP\_ID\_PTM

| #define PCIE\_EXT\_CAP\_ID\_PTM   0x001FU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Precision Time Measurement.

## [◆ ](#gadc91da3b61af0b0a047ec74860dc3201)PCIE\_EXT\_CAP\_ID\_PWR

| #define PCIE\_EXT\_CAP\_ID\_PWR   0x0004U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Power Budgeting.

## [◆ ](#ga78b98a43b8e6661d6745df19c8591f47)PCIE\_EXT\_CAP\_ID\_RCEC

| #define PCIE\_EXT\_CAP\_ID\_RCEC   0x0007U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Root Complex Event Collector Endpoint Association.

## [◆ ](#ga973a2816ae68ab75d5b4118890fd4383)PCIE\_EXT\_CAP\_ID\_RCILC

| #define PCIE\_EXT\_CAP\_ID\_RCILC   0x0006U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Root Complex Internal Link Control.

## [◆ ](#ga46f3607fa47b26ef099f9bfdcdb0763f)PCIE\_EXT\_CAP\_ID\_RCLD

| #define PCIE\_EXT\_CAP\_ID\_RCLD   0x0005U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Root Complex Link Declaration.

## [◆ ](#ga356973ae03fb0d33df4092a311818e9b)PCIE\_EXT\_CAP\_ID\_RCRB

| #define PCIE\_EXT\_CAP\_ID\_RCRB   0x000AU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Root Complex Register Block.

## [◆ ](#gabae7e5d40435723e6d808c377753332a)PCIE\_EXT\_CAP\_ID\_REBAR

| #define PCIE\_EXT\_CAP\_ID\_REBAR   0x0015U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Resizable BAR.

## [◆ ](#gacd1a90cce3892bacc40939a04b707d20)PCIE\_EXT\_CAP\_ID\_SECPCI

| #define PCIE\_EXT\_CAP\_ID\_SECPCI   0x0019U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Secondary PCIe Capability.

## [◆ ](#ga0e173611874d25c0cd5bd62372542380)PCIE\_EXT\_CAP\_ID\_SFI

| #define PCIE\_EXT\_CAP\_ID\_SFI   0x002CU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

System Firmware Intermediary.

## [◆ ](#gae8767a1dd6e203aa2ccd75d1fd05eb7d)PCIE\_EXT\_CAP\_ID\_SRIOV

| #define PCIE\_EXT\_CAP\_ID\_SRIOV   0x0010U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Single Root I/O Virtualization.

## [◆ ](#ga558289987600691fce5574feb253b4cb)PCIE\_EXT\_CAP\_ID\_TPH

| #define PCIE\_EXT\_CAP\_ID\_TPH   0x0017U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

TPH Requester.

## [◆ ](#gaaa8d5de1c1925dea16e40b72fafa5b8f)PCIE\_EXT\_CAP\_ID\_VC

| #define PCIE\_EXT\_CAP\_ID\_VC   0x0002U |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Virtual Channel when no MFVC.

## [◆ ](#gac864550f144038d5bbdf5e556faa640e)PCIE\_EXT\_CAP\_ID\_VNDR

| #define PCIE\_EXT\_CAP\_ID\_VNDR   0x000BU |
| --- |

`#include <[cap.h](drivers_2pcie_2cap_8h.md)>`

Vendor-Specific Extended Capability.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
