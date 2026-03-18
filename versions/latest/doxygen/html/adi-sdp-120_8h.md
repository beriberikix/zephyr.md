---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/adi-sdp-120_8h.html
original_path: doxygen/html/adi-sdp-120_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adi-sdp-120.h File Reference

Copyright (c) 2024 Analog Devices Inc.
[More...](#details)

[Go to the source code of this file.](adi-sdp-120_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(n) |
|  | IO[n] signal on a SDP-120 GPIO nexus node following. |
| #define | [SDP\_120\_SPI\_D2](#aee741ae2a6bc2581ac2c4bb32a56aef7)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(33) /\* SPI\_D2 \*/ |
| #define | [SDP\_120\_SPI\_D3](#a9ed3217c827aa9f2262fa5bd77fbf11b)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(34) /\* SPI\_D3 \*/ |
| #define | [SDP\_120\_SERIAL\_INT](#a8e2bc0d10b7bff636da4f83b78f5aabc)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(35) /\* SERIAL\_INT \*/ |
| #define | [SDP\_120\_SPI\_SEL\_B\_N](#ad0630139116e6af22329af773a5dfc58)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(37) /\* SPI\_SEL\_B\_N \*/ |
| #define | [SDP\_120\_SPI\_SEL\_C\_N](#acc00b195bf35cdea02ae02824c46a8bc)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(38) /\* SPI\_SEL\_C\_N \*/ |
| #define | [SDP\_120\_SPI\_SS\_N](#a7bd3994cd8d15c7abc8f4c8c2cd0c935)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(39) /\* SPI\_SS\_N \*/ |
| #define | [SDP\_120\_GPIO0](#add120c01738682c1bafb3e0709af107b)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(43) /\* GPIO0 \*/ |
| #define | [SDP\_120\_GPIO2](#a0ac1ea00a661fd760dbbe6d3d95e5cdb)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(44) /\* GPIO2 \*/ |
| #define | [SDP\_120\_GPIO4](#ac6d9aadae724e4423475da16b04e2531)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(45) /\* GPIO4 \*/ |
| #define | [SDP\_120\_GPIO6](#a1a1f15052ff7cf0a1b39f9aee922dc83)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(47) /\* GPIO6 \*/ |
| #define | [SDP\_120\_TMR\_A](#a17e46db1c2848751cbff6cdc4f013bf5)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(48) /\* TMR\_A \*/ |
| #define | [SDP\_120\_UART\_RX](#a7ef869f19822b0866dd5cc8cf15d77b6)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(59) /\* UART2\_RX \*/ |
| #define | [SDP\_120\_UART\_TX](#a816693d1532b48588f91fee54e78fd43)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(62) /\* UART2\_TX \*/ |
| #define | [SDP\_120\_TMR\_D](#afe0bd2dd3b90e13d8973f087a2ccba6d)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(72) /\* TMR\_D \*/ |
| #define | [SDP\_120\_TMR\_B](#ae6861bfd6c1903f6cef4e20dde2c8307)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(73) /\* TMR\_B \*/ |
| #define | [SDP\_120\_GPIO7](#aff11d960caef06059ad60cd0bc9d9649)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(74) /\* GPIO7 \*/ |
| #define | [SDP\_120\_GPIO5](#a9b25021cd21089ffe45f447b3327f7e5)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(76) /\* GPIO5 \*/ |
| #define | [SDP\_120\_GPIO3](#a64dfbef1a64613dc18241199c3cfd1c2)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(77) /\* GPIO3 \*/ |
| #define | [SDP\_120\_GPIO1](#a70d8426587c4497729eea1c9e201a53e)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(78) /\* GPIO1 \*/ |
| #define | [SDP\_120\_SCL\_0](#ac43d3d5c6b9d35677821ef0184027577)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(79) /\* SCL\_0 \*/ |
| #define | [SDP\_120\_SDA\_0](#a34cdc1330a64c8980a40052f380b3a25)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(80) /\* SDA\_0 \*/ |
| #define | [SDP\_120\_SPI\_CLK](#ad13ae79930628584fb9eef6ee00f7103)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(82) /\* SPI\_CLK \*/ |
| #define | [SDP\_120\_SPI\_MISO](#a5c9a67e842262480a257f1e771f3bac4)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(83) /\* SPI\_MISO \*/ |
| #define | [SDP\_120\_SPI\_MOSI](#ac45042556abbcb2b70738bb06a2f6f17)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(84) /\* SPI\_MOSI \*/ |
| #define | [SDP\_120\_SPI\_SEL\_A\_N](#ae25f3acec680970f67ae1cdf57df9adb)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(85) /\* SPI\_SEL\_A\_N \*/ |
| #define | [SDP\_120\_SPI\_SPORT\_TSCLK](#aa7d9c2aacf247c057d9dd36a7fd37610)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(87) /\* SPORT\_TSCLK \*/ |
| #define | [SDP\_120\_SPI\_SPORT\_DT0](#ae07a46b852400aca6408948f54ccd6d3)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(88) /\* SPORT\_DT0 \*/ |
| #define | [SDP\_120\_SPI\_SPORT\_TFS](#aabc39d3cacfb51a0b5f6db48947750e2)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(89) /\* SPORT\_TFS \*/ |
| #define | [SDP\_120\_SPI\_SPORT\_RFS](#a19b87a9e7e924aad756e70df72b0a2f9)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(90) /\* SPORT\_RFS \*/ |
| #define | [SDP\_120\_SPI\_SPORT\_DR0](#a6346b80db55747c4ad2e10051616b168)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(91) /\* SPORT\_DR0 \*/ |
| #define | [SDP\_120\_SPI\_SPORT\_RSCLK](#a5f06bebd3dcaf01c3eefc6ffc9a2c3cf)   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(92) /\* SPORT\_RSCLK \*/ |

## Detailed Description

Copyright (c) 2024 Analog Devices Inc.

Copyright (c) 2024 Baylibre, SAS

SPDX-License-Identifier: Apache-2.0

SDP-120 GPIO index definitions

Defines meant to be used in conjunction with the "adi,sdp-120" ADI SDP-120 mapping.

Example usage:

&spi1 {

cs-gpios = <&sdp\_120 SDP\_120\_SPI\_SS\_N GPIO\_ACTIVE\_LOW>;

example\_device: example-dev@0 {

compatible = "vnd,spi-device";

reg = <0>;

};

};

## Macro Definition Documentation

## [◆ ](#add120c01738682c1bafb3e0709af107b)SDP\_120\_GPIO0

| #define SDP\_120\_GPIO0   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(43) /\* GPIO0 \*/ |
| --- |

## [◆ ](#a70d8426587c4497729eea1c9e201a53e)SDP\_120\_GPIO1

| #define SDP\_120\_GPIO1   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(78) /\* GPIO1 \*/ |
| --- |

## [◆ ](#a0ac1ea00a661fd760dbbe6d3d95e5cdb)SDP\_120\_GPIO2

| #define SDP\_120\_GPIO2   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(44) /\* GPIO2 \*/ |
| --- |

## [◆ ](#a64dfbef1a64613dc18241199c3cfd1c2)SDP\_120\_GPIO3

| #define SDP\_120\_GPIO3   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(77) /\* GPIO3 \*/ |
| --- |

## [◆ ](#ac6d9aadae724e4423475da16b04e2531)SDP\_120\_GPIO4

| #define SDP\_120\_GPIO4   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(45) /\* GPIO4 \*/ |
| --- |

## [◆ ](#a9b25021cd21089ffe45f447b3327f7e5)SDP\_120\_GPIO5

| #define SDP\_120\_GPIO5   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(76) /\* GPIO5 \*/ |
| --- |

## [◆ ](#a1a1f15052ff7cf0a1b39f9aee922dc83)SDP\_120\_GPIO6

| #define SDP\_120\_GPIO6   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(47) /\* GPIO6 \*/ |
| --- |

## [◆ ](#aff11d960caef06059ad60cd0bc9d9649)SDP\_120\_GPIO7

| #define SDP\_120\_GPIO7   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(74) /\* GPIO7 \*/ |
| --- |

## [◆ ](#a92ae0ab5dc11a6de9fe4436c497b6174)SDP\_120\_IO

| #define SDP\_120\_IO | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(n-1)

IO[n] signal on a SDP-120 GPIO nexus node following.

## [◆ ](#ac43d3d5c6b9d35677821ef0184027577)SDP\_120\_SCL\_0

| #define SDP\_120\_SCL\_0   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(79) /\* SCL\_0 \*/ |
| --- |

## [◆ ](#a34cdc1330a64c8980a40052f380b3a25)SDP\_120\_SDA\_0

| #define SDP\_120\_SDA\_0   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(80) /\* SDA\_0 \*/ |
| --- |

## [◆ ](#a8e2bc0d10b7bff636da4f83b78f5aabc)SDP\_120\_SERIAL\_INT

| #define SDP\_120\_SERIAL\_INT   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(35) /\* SERIAL\_INT \*/ |
| --- |

## [◆ ](#ad13ae79930628584fb9eef6ee00f7103)SDP\_120\_SPI\_CLK

| #define SDP\_120\_SPI\_CLK   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(82) /\* SPI\_CLK \*/ |
| --- |

## [◆ ](#aee741ae2a6bc2581ac2c4bb32a56aef7)SDP\_120\_SPI\_D2

| #define SDP\_120\_SPI\_D2   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(33) /\* SPI\_D2 \*/ |
| --- |

## [◆ ](#a9ed3217c827aa9f2262fa5bd77fbf11b)SDP\_120\_SPI\_D3

| #define SDP\_120\_SPI\_D3   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(34) /\* SPI\_D3 \*/ |
| --- |

## [◆ ](#a5c9a67e842262480a257f1e771f3bac4)SDP\_120\_SPI\_MISO

| #define SDP\_120\_SPI\_MISO   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(83) /\* SPI\_MISO \*/ |
| --- |

## [◆ ](#ac45042556abbcb2b70738bb06a2f6f17)SDP\_120\_SPI\_MOSI

| #define SDP\_120\_SPI\_MOSI   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(84) /\* SPI\_MOSI \*/ |
| --- |

## [◆ ](#ae25f3acec680970f67ae1cdf57df9adb)SDP\_120\_SPI\_SEL\_A\_N

| #define SDP\_120\_SPI\_SEL\_A\_N   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(85) /\* SPI\_SEL\_A\_N \*/ |
| --- |

## [◆ ](#ad0630139116e6af22329af773a5dfc58)SDP\_120\_SPI\_SEL\_B\_N

| #define SDP\_120\_SPI\_SEL\_B\_N   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(37) /\* SPI\_SEL\_B\_N \*/ |
| --- |

## [◆ ](#acc00b195bf35cdea02ae02824c46a8bc)SDP\_120\_SPI\_SEL\_C\_N

| #define SDP\_120\_SPI\_SEL\_C\_N   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(38) /\* SPI\_SEL\_C\_N \*/ |
| --- |

## [◆ ](#a6346b80db55747c4ad2e10051616b168)SDP\_120\_SPI\_SPORT\_DR0

| #define SDP\_120\_SPI\_SPORT\_DR0   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(91) /\* SPORT\_DR0 \*/ |
| --- |

## [◆ ](#ae07a46b852400aca6408948f54ccd6d3)SDP\_120\_SPI\_SPORT\_DT0

| #define SDP\_120\_SPI\_SPORT\_DT0   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(88) /\* SPORT\_DT0 \*/ |
| --- |

## [◆ ](#a19b87a9e7e924aad756e70df72b0a2f9)SDP\_120\_SPI\_SPORT\_RFS

| #define SDP\_120\_SPI\_SPORT\_RFS   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(90) /\* SPORT\_RFS \*/ |
| --- |

## [◆ ](#a5f06bebd3dcaf01c3eefc6ffc9a2c3cf)SDP\_120\_SPI\_SPORT\_RSCLK

| #define SDP\_120\_SPI\_SPORT\_RSCLK   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(92) /\* SPORT\_RSCLK \*/ |
| --- |

## [◆ ](#aabc39d3cacfb51a0b5f6db48947750e2)SDP\_120\_SPI\_SPORT\_TFS

| #define SDP\_120\_SPI\_SPORT\_TFS   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(89) /\* SPORT\_TFS \*/ |
| --- |

## [◆ ](#aa7d9c2aacf247c057d9dd36a7fd37610)SDP\_120\_SPI\_SPORT\_TSCLK

| #define SDP\_120\_SPI\_SPORT\_TSCLK   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(87) /\* SPORT\_TSCLK \*/ |
| --- |

## [◆ ](#a7bd3994cd8d15c7abc8f4c8c2cd0c935)SDP\_120\_SPI\_SS\_N

| #define SDP\_120\_SPI\_SS\_N   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(39) /\* SPI\_SS\_N \*/ |
| --- |

## [◆ ](#a17e46db1c2848751cbff6cdc4f013bf5)SDP\_120\_TMR\_A

| #define SDP\_120\_TMR\_A   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(48) /\* TMR\_A \*/ |
| --- |

## [◆ ](#ae6861bfd6c1903f6cef4e20dde2c8307)SDP\_120\_TMR\_B

| #define SDP\_120\_TMR\_B   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(73) /\* TMR\_B \*/ |
| --- |

## [◆ ](#afe0bd2dd3b90e13d8973f087a2ccba6d)SDP\_120\_TMR\_D

| #define SDP\_120\_TMR\_D   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(72) /\* TMR\_D \*/ |
| --- |

## [◆ ](#a7ef869f19822b0866dd5cc8cf15d77b6)SDP\_120\_UART\_RX

| #define SDP\_120\_UART\_RX   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(59) /\* UART2\_RX \*/ |
| --- |

## [◆ ](#a816693d1532b48588f91fee54e78fd43)SDP\_120\_UART\_TX

| #define SDP\_120\_UART\_TX   [SDP\_120\_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)(62) /\* UART2\_TX \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [adi-sdp-120.h](adi-sdp-120_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
