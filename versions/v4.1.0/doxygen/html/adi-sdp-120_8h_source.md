---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/adi-sdp-120_8h_source.html
original_path: doxygen/html/adi-sdp-120_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adi-sdp-120.h

[Go to the documentation of this file.](adi-sdp-120_8h.md)

1

26

27#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ADI\_SDP\_120\_H\_

28#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ADI\_SDP\_120\_H\_

29

30/\* GPIO \*/

31

35

[ 36](adi-sdp-120_8h.md#a92ae0ab5dc11a6de9fe4436c497b6174)#define SDP\_120\_IO(n) (n-1)

37

38/\* SPI \*/

[ 39](adi-sdp-120_8h.md#aee741ae2a6bc2581ac2c4bb32a56aef7)#define SDP\_120\_SPI\_D2 SDP\_120\_IO(33) /\* SPI\_D2 \*/

[ 40](adi-sdp-120_8h.md#a9ed3217c827aa9f2262fa5bd77fbf11b)#define SDP\_120\_SPI\_D3 SDP\_120\_IO(34) /\* SPI\_D3 \*/

[ 41](adi-sdp-120_8h.md#a8e2bc0d10b7bff636da4f83b78f5aabc)#define SDP\_120\_SERIAL\_INT SDP\_120\_IO(35) /\* SERIAL\_INT \*/

[ 42](adi-sdp-120_8h.md#ad0630139116e6af22329af773a5dfc58)#define SDP\_120\_SPI\_SEL\_B\_N SDP\_120\_IO(37) /\* SPI\_SEL\_B\_N \*/

[ 43](adi-sdp-120_8h.md#acc00b195bf35cdea02ae02824c46a8bc)#define SDP\_120\_SPI\_SEL\_C\_N SDP\_120\_IO(38) /\* SPI\_SEL\_C\_N \*/

[ 44](adi-sdp-120_8h.md#a7bd3994cd8d15c7abc8f4c8c2cd0c935)#define SDP\_120\_SPI\_SS\_N SDP\_120\_IO(39) /\* SPI\_SS\_N \*/

45

46/\* GPIO \*/

[ 47](adi-sdp-120_8h.md#add120c01738682c1bafb3e0709af107b)#define SDP\_120\_GPIO0 SDP\_120\_IO(43) /\* GPIO0 \*/

[ 48](adi-sdp-120_8h.md#a0ac1ea00a661fd760dbbe6d3d95e5cdb)#define SDP\_120\_GPIO2 SDP\_120\_IO(44) /\* GPIO2 \*/

[ 49](adi-sdp-120_8h.md#ac6d9aadae724e4423475da16b04e2531)#define SDP\_120\_GPIO4 SDP\_120\_IO(45) /\* GPIO4 \*/

[ 50](adi-sdp-120_8h.md#a1a1f15052ff7cf0a1b39f9aee922dc83)#define SDP\_120\_GPIO6 SDP\_120\_IO(47) /\* GPIO6 \*/

51

52/\* TMR \*/

[ 53](adi-sdp-120_8h.md#a17e46db1c2848751cbff6cdc4f013bf5)#define SDP\_120\_TMR\_A SDP\_120\_IO(48) /\* TMR\_A \*/

54

55/\* USART \*/

[ 56](adi-sdp-120_8h.md#a7ef869f19822b0866dd5cc8cf15d77b6)#define SDP\_120\_UART\_RX SDP\_120\_IO(59) /\* UART2\_RX \*/

[ 57](adi-sdp-120_8h.md#a816693d1532b48588f91fee54e78fd43)#define SDP\_120\_UART\_TX SDP\_120\_IO(62) /\* UART2\_TX \*/

58

59/\* TMR \*/

[ 60](adi-sdp-120_8h.md#afe0bd2dd3b90e13d8973f087a2ccba6d)#define SDP\_120\_TMR\_D SDP\_120\_IO(72) /\* TMR\_D \*/

[ 61](adi-sdp-120_8h.md#ae6861bfd6c1903f6cef4e20dde2c8307)#define SDP\_120\_TMR\_B SDP\_120\_IO(73) /\* TMR\_B \*/

62

63/\* GPIO \*/

[ 64](adi-sdp-120_8h.md#aff11d960caef06059ad60cd0bc9d9649)#define SDP\_120\_GPIO7 SDP\_120\_IO(74) /\* GPIO7 \*/

[ 65](adi-sdp-120_8h.md#a9b25021cd21089ffe45f447b3327f7e5)#define SDP\_120\_GPIO5 SDP\_120\_IO(76) /\* GPIO5 \*/

[ 66](adi-sdp-120_8h.md#a64dfbef1a64613dc18241199c3cfd1c2)#define SDP\_120\_GPIO3 SDP\_120\_IO(77) /\* GPIO3 \*/

[ 67](adi-sdp-120_8h.md#a70d8426587c4497729eea1c9e201a53e)#define SDP\_120\_GPIO1 SDP\_120\_IO(78) /\* GPIO1 \*/

68

69/\* I2C \*/

[ 70](adi-sdp-120_8h.md#ac43d3d5c6b9d35677821ef0184027577)#define SDP\_120\_SCL\_0 SDP\_120\_IO(79) /\* SCL\_0 \*/

[ 71](adi-sdp-120_8h.md#a34cdc1330a64c8980a40052f380b3a25)#define SDP\_120\_SDA\_0 SDP\_120\_IO(80) /\* SDA\_0 \*/

72

73/\* SPI \*/

[ 74](adi-sdp-120_8h.md#ad13ae79930628584fb9eef6ee00f7103)#define SDP\_120\_SPI\_CLK SDP\_120\_IO(82) /\* SPI\_CLK \*/

[ 75](adi-sdp-120_8h.md#a5c9a67e842262480a257f1e771f3bac4)#define SDP\_120\_SPI\_MISO SDP\_120\_IO(83) /\* SPI\_MISO \*/

[ 76](adi-sdp-120_8h.md#ac45042556abbcb2b70738bb06a2f6f17)#define SDP\_120\_SPI\_MOSI SDP\_120\_IO(84) /\* SPI\_MOSI \*/

[ 77](adi-sdp-120_8h.md#ae25f3acec680970f67ae1cdf57df9adb)#define SDP\_120\_SPI\_SEL\_A\_N SDP\_120\_IO(85) /\* SPI\_SEL\_A\_N \*/

78

79/\* SPORT - no driver yet \*/

[ 80](adi-sdp-120_8h.md#aa7d9c2aacf247c057d9dd36a7fd37610)#define SDP\_120\_SPI\_SPORT\_TSCLK SDP\_120\_IO(87) /\* SPORT\_TSCLK \*/

[ 81](adi-sdp-120_8h.md#ae07a46b852400aca6408948f54ccd6d3)#define SDP\_120\_SPI\_SPORT\_DT0 SDP\_120\_IO(88) /\* SPORT\_DT0 \*/

[ 82](adi-sdp-120_8h.md#aabc39d3cacfb51a0b5f6db48947750e2)#define SDP\_120\_SPI\_SPORT\_TFS SDP\_120\_IO(89) /\* SPORT\_TFS \*/

[ 83](adi-sdp-120_8h.md#a19b87a9e7e924aad756e70df72b0a2f9)#define SDP\_120\_SPI\_SPORT\_RFS SDP\_120\_IO(90) /\* SPORT\_RFS \*/

[ 84](adi-sdp-120_8h.md#a6346b80db55747c4ad2e10051616b168)#define SDP\_120\_SPI\_SPORT\_DR0 SDP\_120\_IO(91) /\* SPORT\_DR0 \*/

[ 85](adi-sdp-120_8h.md#a5f06bebd3dcaf01c3eefc6ffc9a2c3cf)#define SDP\_120\_SPI\_SPORT\_RSCLK SDP\_120\_IO(92) /\* SPORT\_RSCLK \*/

86

87#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ADI\_SDP\_120\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [adi-sdp-120.h](adi-sdp-120_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
