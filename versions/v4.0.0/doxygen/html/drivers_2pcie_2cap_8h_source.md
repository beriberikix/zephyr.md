---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2pcie_2cap_8h_source.html
original_path: doxygen/html/drivers_2pcie_2cap_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cap.h

[Go to the documentation of this file.](drivers_2pcie_2cap_8h.md)

1/\*

2 \* Copyright (c) 2021 BayLibre, SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_CAP\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_CAP\_H\_

8

16

[ 23](group__pcie__capabilities.md#ga890142bda671b3558cd881f4b91a43ab)#define PCI\_CAP\_ID\_NULL 0x00U

[ 24](group__pcie__capabilities.md#ga9379bf318dd400e1076fbd5f0e331adb)#define PCI\_CAP\_ID\_PM 0x01U

[ 25](group__pcie__capabilities.md#gac68c228e23e701fd4040b89c42537eac)#define PCI\_CAP\_ID\_AGP 0x02U

[ 26](group__pcie__capabilities.md#gaf419a56a517635f4d9f8a5c6f5fd9d08)#define PCI\_CAP\_ID\_VPD 0x03U

[ 27](group__pcie__capabilities.md#ga6d286311dd9f54468f125fd367683f74)#define PCI\_CAP\_ID\_SLOTID 0x04U

[ 28](group__pcie__capabilities.md#gad19597699011d0e047083968d2e835bd)#define PCI\_CAP\_ID\_MSI 0x05U

[ 29](group__pcie__capabilities.md#ga74356319083570ca7e5cf9a3eaaadd9b)#define PCI\_CAP\_ID\_CHSWP 0x06U

[ 30](group__pcie__capabilities.md#ga24709fe61430ca25fabe665d8b1efca0)#define PCI\_CAP\_ID\_PCIX 0x07U

[ 31](group__pcie__capabilities.md#gad50ed1a81153a04fa19534823d0109c9)#define PCI\_CAP\_ID\_HT 0x08U

[ 32](group__pcie__capabilities.md#ga11b65631db23369276e062560f53b433)#define PCI\_CAP\_ID\_VNDR 0x09U

[ 33](group__pcie__capabilities.md#ga5a37d779c6259232cd4ec7bc3d80bc83)#define PCI\_CAP\_ID\_DBG 0x0AU

[ 34](group__pcie__capabilities.md#gad45dfbc6ea8d963703e243dacdee084f)#define PCI\_CAP\_ID\_CCRC 0x0BU

[ 35](group__pcie__capabilities.md#gae538cdbc7eba80aac860f3340823f559)#define PCI\_CAP\_ID\_SHPC 0x0CU

[ 36](group__pcie__capabilities.md#ga8814c4f32748170e8b5f15dc2ade5dc5)#define PCI\_CAP\_ID\_SSVID 0x0DU

[ 37](group__pcie__capabilities.md#gae351b2497f7231bfa2c08e97ba589cb7)#define PCI\_CAP\_ID\_AGP3 0x0EU

[ 38](group__pcie__capabilities.md#ga20c7aadce06547a3ea37ce705ff0d289)#define PCI\_CAP\_ID\_SECDEV 0x0FU

[ 39](group__pcie__capabilities.md#ga9b0efbb129a8600203135a64377beed0)#define PCI\_CAP\_ID\_EXP 0x10U

[ 40](group__pcie__capabilities.md#ga419307c3f83f3dca9aaa329de41dae63)#define PCI\_CAP\_ID\_MSIX 0x11U

[ 41](group__pcie__capabilities.md#ga437d2f840145a2aae97880ad3579ca7d)#define PCI\_CAP\_ID\_SATA 0x12U

[ 42](group__pcie__capabilities.md#ga7bf330224972c1a16cbafa907387b9ed)#define PCI\_CAP\_ID\_AF 0x13U

[ 43](group__pcie__capabilities.md#ga591d30c052c32a4f3cbb510e8b052b62)#define PCI\_CAP\_ID\_EA 0x14U

[ 44](group__pcie__capabilities.md#gad00f421c7bc8613ad7770ea2e0a5d8da)#define PCI\_CAP\_ID\_FPB 0x14U

48

53

[ 54](group__pcie__capabilities.md#ga2f6c4feb384e41711aa53545952e3cac)#define PCIE\_EXT\_CAP\_ID\_NULL 0x0000U

[ 55](group__pcie__capabilities.md#ga224acf772427857ca1f5a0b155c30d63)#define PCIE\_EXT\_CAP\_ID\_ERR 0x0001U

[ 56](group__pcie__capabilities.md#gaaa8d5de1c1925dea16e40b72fafa5b8f)#define PCIE\_EXT\_CAP\_ID\_VC 0x0002U

[ 57](group__pcie__capabilities.md#ga29a18f51cad5281e3f6a283d3c7acb49)#define PCIE\_EXT\_CAP\_ID\_DSN 0x0003U

[ 58](group__pcie__capabilities.md#gadc91da3b61af0b0a047ec74860dc3201)#define PCIE\_EXT\_CAP\_ID\_PWR 0x0004U

[ 59](group__pcie__capabilities.md#ga46f3607fa47b26ef099f9bfdcdb0763f)#define PCIE\_EXT\_CAP\_ID\_RCLD 0x0005U

[ 60](group__pcie__capabilities.md#ga973a2816ae68ab75d5b4118890fd4383)#define PCIE\_EXT\_CAP\_ID\_RCILC 0x0006U

[ 61](group__pcie__capabilities.md#ga78b98a43b8e6661d6745df19c8591f47)#define PCIE\_EXT\_CAP\_ID\_RCEC 0x0007U

[ 62](group__pcie__capabilities.md#ga2cfa2f9212fb923c3811c0cdc769a877)#define PCIE\_EXT\_CAP\_ID\_MFVC 0x0008U

[ 63](group__pcie__capabilities.md#ga7c2b491e1c994730afe08880dfb1b036)#define PCIE\_EXT\_CAP\_ID\_MFVC\_VC 0x0009U

[ 64](group__pcie__capabilities.md#ga356973ae03fb0d33df4092a311818e9b)#define PCIE\_EXT\_CAP\_ID\_RCRB 0x000AU

[ 65](group__pcie__capabilities.md#gac864550f144038d5bbdf5e556faa640e)#define PCIE\_EXT\_CAP\_ID\_VNDR 0x000BU

[ 66](group__pcie__capabilities.md#gaff6494cd92013933dedbab2e2ae5c6b3)#define PCIE\_EXT\_CAP\_ID\_CAC 0x000CU

[ 67](group__pcie__capabilities.md#ga6b63b04d182b916db526525b064ed285)#define PCIE\_EXT\_CAP\_ID\_ACS 0x000DU

[ 68](group__pcie__capabilities.md#gaf890e2f4f3873b60ac83df345ab0cd8f)#define PCIE\_EXT\_CAP\_ID\_ARI 0x000EU

[ 69](group__pcie__capabilities.md#ga79a9cb071afc5cff9e699c232841623c)#define PCIE\_EXT\_CAP\_ID\_ATS 0x000FU

[ 70](group__pcie__capabilities.md#gae8767a1dd6e203aa2ccd75d1fd05eb7d)#define PCIE\_EXT\_CAP\_ID\_SRIOV 0x0010U

[ 71](group__pcie__capabilities.md#gaa117a86f2691d8711fa6b70e196ead01)#define PCIE\_EXT\_CAP\_ID\_MRIOV 0x0011U

[ 72](group__pcie__capabilities.md#ga2810671833871608043e6e910d79dffd)#define PCIE\_EXT\_CAP\_ID\_MCAST 0x0012U

[ 73](group__pcie__capabilities.md#ga37e0ac002e9742bb9177588d2dfa850b)#define PCIE\_EXT\_CAP\_ID\_PRI 0x0013U

[ 74](group__pcie__capabilities.md#gab8be630bf1dc810f2964e979ac46f77c)#define PCIE\_EXT\_CAP\_ID\_AMD\_XXX 0x0014U

[ 75](group__pcie__capabilities.md#gabae7e5d40435723e6d808c377753332a)#define PCIE\_EXT\_CAP\_ID\_REBAR 0x0015U

[ 76](group__pcie__capabilities.md#ga812c156b93d070a06d3a56b5785788fd)#define PCIE\_EXT\_CAP\_ID\_DPA 0x0016U

[ 77](group__pcie__capabilities.md#ga558289987600691fce5574feb253b4cb)#define PCIE\_EXT\_CAP\_ID\_TPH 0x0017U

[ 78](group__pcie__capabilities.md#ga9545f09c97f2dd4f751767e6e54326ec)#define PCIE\_EXT\_CAP\_ID\_LTR 0x0018U

[ 79](group__pcie__capabilities.md#gacd1a90cce3892bacc40939a04b707d20)#define PCIE\_EXT\_CAP\_ID\_SECPCI 0x0019U

[ 80](group__pcie__capabilities.md#gaf6c41b4ad9e32c4420cb89cc5a0d51c2)#define PCIE\_EXT\_CAP\_ID\_PMUX 0x001AU

[ 81](group__pcie__capabilities.md#ga0c3b5efb8d9fb69a8fdbb9ca147a3069)#define PCIE\_EXT\_CAP\_ID\_PASID 0x001BU

[ 82](group__pcie__capabilities.md#ga40f83a1c280acb8f3f3908d860874015)#define PCIE\_EXT\_CAP\_ID\_DPC 0x001DU

[ 83](group__pcie__capabilities.md#ga3006998c35d9c8f8e3d69716cda6def7)#define PCIE\_EXT\_CAP\_ID\_L1SS 0x001EU

[ 84](group__pcie__capabilities.md#ga134d53764458500ea4ca58fe016f46fa)#define PCIE\_EXT\_CAP\_ID\_PTM 0x001FU

[ 85](group__pcie__capabilities.md#gab1d94b05177a5064a78e4048eff473b1)#define PCIE\_EXT\_CAP\_ID\_DVSEC 0x0023U

[ 86](group__pcie__capabilities.md#ga2e8324ea3b27a63e213252bed6c78ca6)#define PCIE\_EXT\_CAP\_ID\_DLF 0x0025U

[ 87](group__pcie__capabilities.md#ga60203711f9fe698f3e7e138e0468645a)#define PCIE\_EXT\_CAP\_ID\_PL\_16GT 0x0026U

[ 88](group__pcie__capabilities.md#ga56b3b2bd686b6b99c2ae34ae57228160)#define PCIE\_EXT\_CAP\_ID\_LMR 0x0027U

[ 89](group__pcie__capabilities.md#ga0087a39c01053f83b3ac3bb3b057ac2a)#define PCIE\_EXT\_CAP\_ID\_HID 0x0028U

[ 90](group__pcie__capabilities.md#ga03dafb2eb5449f17dc18898ea319d729)#define PCIE\_EXT\_CAP\_ID\_NPEM 0x0029U

[ 91](group__pcie__capabilities.md#ga8a8768d04866a479114bcf276466501f)#define PCIE\_EXT\_CAP\_ID\_PL\_32GT 0x002AU

[ 92](group__pcie__capabilities.md#ga53e188f6e71f04012e7739e75a015398)#define PCIE\_EXT\_CAP\_ID\_AP 0x002BU

[ 93](group__pcie__capabilities.md#ga0e173611874d25c0cd5bd62372542380)#define PCIE\_EXT\_CAP\_ID\_SFI 0x002CU

97

101

102#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_CAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [cap.h](drivers_2pcie_2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
