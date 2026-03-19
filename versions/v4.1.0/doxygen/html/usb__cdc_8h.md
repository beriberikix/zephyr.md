---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usb__cdc_8h.html
original_path: doxygen/html/usb__cdc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_cdc.h File Reference

USB Communications Device Class (CDC) public header.
[More...](#details)

[Go to the source code of this file.](usb__cdc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [cdc\_header\_descriptor](structcdc__header__descriptor.md) |
|  | Header Functional Descriptor. [More...](structcdc__header__descriptor.md#details) |
| struct | [cdc\_union\_descriptor](structcdc__union__descriptor.md) |
|  | Union Interface Functional Descriptor. [More...](structcdc__union__descriptor.md#details) |
| struct | [cdc\_cm\_descriptor](structcdc__cm__descriptor.md) |
|  | Call Management Functional Descriptor. [More...](structcdc__cm__descriptor.md#details) |
| struct | [cdc\_acm\_descriptor](structcdc__acm__descriptor.md) |
|  | Abstract Control Management Functional Descriptor. [More...](structcdc__acm__descriptor.md#details) |
| struct | [cdc\_acm\_line\_coding](structcdc__acm__line__coding.md) |
|  | Data structure for GET\_LINE\_CODING / SET\_LINE\_CODING class requests. [More...](structcdc__acm__line__coding.md#details) |
| struct | [cdc\_acm\_notification](structcdc__acm__notification.md) |
|  | Data structure for the notification about SerialState. [More...](structcdc__acm__notification.md#details) |
| struct | [cdc\_ecm\_descriptor](structcdc__ecm__descriptor.md) |
|  | Ethernet Networking Functional Descriptor. [More...](structcdc__ecm__descriptor.md#details) |
| struct | [cdc\_ncm\_descriptor](structcdc__ncm__descriptor.md) |
|  | Ethernet Network Control Model (NCM) Descriptor. [More...](structcdc__ncm__descriptor.md#details) |

| Macros | |
| --- | --- |
| #define | [CDC\_SRN\_1\_20](#a2d44425b0b0c5e525885c5764348ec54)   0x0120 |
|  | CDC Specification release number in BCD format. |
| #define | [ACM\_SUBCLASS](#a01b7a28004a035df52334b64308e4b22)   0x02 |
|  | Communications Class Subclass Codes. |
| #define | [ECM\_SUBCLASS](#a39f776a70d5139575ed84be1a9faee5d)   0x06 |
| #define | [EEM\_SUBCLASS](#a73503e51ff8700620866be15a8d7ab43)   0x0c |
| #define | [NCM\_SUBCLASS](#af4edeebbc1d4fb6f3a727083a36e731e)   0x0d |
| #define | [AT\_CMD\_V250\_PROTOCOL](#aaf98d38c2b9c859cf86e281bb67f27b0)   0x01 |
|  | Communications Class Protocol Codes. |
| #define | [EEM\_PROTOCOL](#ab4f22c3c42b5a4efe7735bafebc1cb9b)   0x07 |
| #define | [ACM\_VENDOR\_PROTOCOL](#a20396bb325a1e947b2e4b0017a134082)   0xFF |
| #define | [NCM\_DATA\_PROTOCOL](#a6577856e991bddc829d93af0ea527ef6)   0x01 |
| #define | [DATA\_INTERFACE\_CLASS](#ae4044b943c9e54cb7a64c8c35acaf8bc)   0x0A |
|  | Data Class Interface Codes. |
| #define | [HEADER\_FUNC\_DESC](#a008b7d343c5a1876a78c885f7a496b66)   0x00 |
|  | bDescriptor SubType for Communications Class Functional Descriptors |
| #define | [CALL\_MANAGEMENT\_FUNC\_DESC](#a60552aa9506dc2c6dede5146c5251aaf)   0x01 |
| #define | [ACM\_FUNC\_DESC](#a057b9de28602442b66a8c3a7befd62a7)   0x02 |
| #define | [UNION\_FUNC\_DESC](#aab7f21ab95fc5916f758e66087caef25)   0x06 |
| #define | [ETHERNET\_FUNC\_DESC](#a22b2b55d7ab3cdd4206df07cddcc44e9)   0x0F |
| #define | [ETHERNET\_FUNC\_DESC\_NCM](#ad788a76ba44ab5d02c699b110856e18e)   0x1a |
| #define | [CDC\_SEND\_ENC\_CMD](#a926f6444745d1cdc991d97e4f1d265ad)   0x00 |
|  | PSTN Subclass Specific Requests for ACM devices. |
| #define | [CDC\_GET\_ENC\_RSP](#ac9008f0dc0d4fc7141de9dd12352caa8)   0x01 |
| #define | [SET\_LINE\_CODING](#a91a9c047339a1a5918b6a923af6d1af6)   0x20 |
| #define | [GET\_LINE\_CODING](#a6698d8d2ca56fafdc943aec2cede1daf)   0x21 |
| #define | [SET\_CONTROL\_LINE\_STATE](#a437869c339749d5d011060cd5676659e)   0x22 |
| #define | [USB\_CDC\_NETWORK\_CONNECTION](#a7e9384e6a613e38c543d7eba05f64c07)   0x00 |
|  | PSTN Subclass Class-Specific Notification Codes. |
| #define | [USB\_CDC\_RESPONSE\_AVAILABLE](#a970045b850b0195b5a4a2913d5a0b918)   0x01 |
| #define | [USB\_CDC\_AUX\_JACK\_HOOK\_STATE](#afdeb5f862a52b953653b9ab567979cec)   0x08 |
| #define | [USB\_CDC\_RING\_DETECT](#a52452ce9272b97203fece115b5005aff)   0x09 |
| #define | [USB\_CDC\_SERIAL\_STATE](#ac167f480370c73b830281d98ad5899b1)   0x20 |
| #define | [USB\_CDC\_CALL\_STATE\_CHANGE](#a6bb6650664f82fd25330af0357e5831e)   0x28 |
| #define | [USB\_CDC\_LINE\_STATE\_CHANGE](#ac63891d7c3321f7f4eb297f87c0978f6)   0x23 |
| #define | [USB\_CDC\_SERIAL\_STATE\_OVERRUN](#a504f682d66f714730f35d282ce0b9177)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | PSTN UART State Bitmap Values. |
| #define | [USB\_CDC\_SERIAL\_STATE\_PARITY](#a1ff82c5d551211d2298128bd84eeb60a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [USB\_CDC\_SERIAL\_STATE\_FRAMING](#a59f5f1ebab838621cdc67668541432ca)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [USB\_CDC\_SERIAL\_STATE\_RINGSIGNAL](#a60f22cb2ae47789875e2542063899876)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [USB\_CDC\_SERIAL\_STATE\_BREAK](#a15f3c90969106ecdf3b1cdf258cad5df)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [USB\_CDC\_SERIAL\_STATE\_TXCARRIER](#ab96b4f63f2de0ef913862878bce1029f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [USB\_CDC\_SERIAL\_STATE\_RXCARRIER](#ad720be9e3738bcba7e37dc9392c3b6e8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [SET\_CONTROL\_LINE\_STATE\_RTS](#a00788c95fb39c2636d7d5a427282399f)   0x02 |
|  | Control Signal Bitmap Values for SetControlLineState. |
| #define | [SET\_CONTROL\_LINE\_STATE\_DTR](#a07623c40153f936c863627a3dc30da7a)   0x01 |
| #define | [USB\_CDC\_LINE\_CTRL\_BAUD\_RATE](#a89554d686630d67d642e228b7ee0dc2c)   [UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) |
|  | Enhance enum [uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0 "Line control signals.") with CDC specific values. |
| #define | [USB\_CDC\_LINE\_CTRL\_DCD](#a7e6b9bb33debc489b7ac7e0fb0e94947)   [UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) |
| #define | [USB\_CDC\_LINE\_CTRL\_DSR](#a6876caf1b77477e259bb391216309799)   [UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) |
| #define | [USB\_CDC\_LINE\_CTRL\_BREAK](#a716d9aaf772e1fa3f8b555077048ecbb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [USB\_CDC\_LINE\_CTRL\_RING\_SIGNAL](#a8ec9b8c619c567cc174c0473dda5a5fd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [USB\_CDC\_LINE\_CTRL\_FRAMING](#a263186a0a64d9a8e7e9e97a54b951bdf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [USB\_CDC\_LINE\_CTRL\_PARITY](#ae2779672a5b5ab49a2ed7240e463f9e8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [USB\_CDC\_LINE\_CTRL\_OVER\_RUN](#a8bf1722f98bf48394605efddf6be1295)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [SERIAL\_STATE\_OVER\_RUN](#ae38825267009563e0aa82a58a7fc4fd2)   0x40 |
|  | UART State Bitmap Values. |
| #define | [SERIAL\_STATE\_PARITY](#a738f180df5795376763ff233fb8aa68d)   0x20 |
| #define | [SERIAL\_STATE\_FRAMING](#aacd68fe3a081441ee684bf2ef6312bec)   0x10 |
| #define | [SERIAL\_STATE\_RING\_SIGNAL](#a935c772da45984e8d796396146413037)   0x08 |
| #define | [SERIAL\_STATE\_BREAK](#aa66ab791abfcf7ef5a37758c1b33138a)   0x04 |
| #define | [SERIAL\_STATE\_TX\_CARRIER](#a22cd80b90c53ff44a4c1de08310ba3c2)   0x02 |
| #define | [SERIAL\_STATE\_RX\_CARRIER](#a9677c612766f3e788ad2960a17ad0791)   0x01 |
| #define | [USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1](#a8a06b3413e1c665f13ba4895c220d608)   0 |
|  | PSTN Subclass Line Coding Values. |
| #define | [USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1\_5](#a4159f50590d647510a6a1f38875e012e)   1 |
| #define | [USB\_CDC\_LINE\_CODING\_STOP\_BITS\_2](#a7e7fc73b4490a694aa982b4862782157)   2 |
| #define | [USB\_CDC\_LINE\_CODING\_PARITY\_NO](#a549181d2cc92c42b4db8c3c34927d97f)   0 |
| #define | [USB\_CDC\_LINE\_CODING\_PARITY\_ODD](#a44d808ad4f27ecf3502b9c14da2aa9b9)   1 |
| #define | [USB\_CDC\_LINE\_CODING\_PARITY\_EVEN](#a327b5f99ab7e5cfc99d7592d1f9c1c25)   2 |
| #define | [USB\_CDC\_LINE\_CODING\_PARITY\_MARK](#a490d381698ce91db4ab8bb24dd70820a)   3 |
| #define | [USB\_CDC\_LINE\_CODING\_PARITY\_SPACE](#a5aa1b5cf30cb4020442131f66170fec6)   4 |
| #define | [USB\_CDC\_LINE\_CODING\_DATA\_BITS\_5](#a327c495a9930b3e5519f0a9c7cd9ed18)   5 |
| #define | [USB\_CDC\_LINE\_CODING\_DATA\_BITS\_6](#a231932add6d9ceef4f5332a0db1b9f55)   6 |
| #define | [USB\_CDC\_LINE\_CODING\_DATA\_BITS\_7](#a6a276593bc4587671df5e6da8cce5ebb)   7 |
| #define | [USB\_CDC\_LINE\_CODING\_DATA\_BITS\_8](#a64e296aec72bbd8f9bdc1aefa5aab654)   8 |
| #define | [SET\_ETHERNET\_MULTICAST\_FILTERS](#a4dce35ee8cf2337bab3c90081200a9f6)   0x40 |
|  | Class-Specific Request Codes for Ethernet subclass. |
| #define | [SET\_ETHERNET\_PM\_FILTER](#a1506deda422ee354040b0feeb09ad4b6)   0x41 |
| #define | [GET\_ETHERNET\_PM\_FILTER](#a53ea6ae0e1fe8a88350740fd594507fd)   0x42 |
| #define | [SET\_ETHERNET\_PACKET\_FILTER](#adae019242224bbbc9d0f853da3733f1c)   0x43 |
| #define | [GET\_ETHERNET\_STATISTIC](#a7dffeba1576d6660fb930eabc5c515b7)   0x44 |
| #define | [GET\_NTB\_PARAMETERS](#a44e5dd539b8b41ccc9c61dd95ee4fb2e)   0x80 |
|  | Class-Specific Request Codes for NCM subclass. |
| #define | [GET\_NET\_ADDRESS](#a58701f26151379cd5dd8b7a7350dcda5)   0x81 |
| #define | [SET\_NET\_ADDRESS](#a2d8525d02e54ec44143a7732a15ad5b0)   0x82 |
| #define | [GET\_NTB\_FORMAT](#a2ba9ad377b20364fc811ec6d5bb74995)   0x83 |
| #define | [SET\_NTB\_FORMAT](#a9c48d4f5685678b1429ba90f7c0a7d9b)   0x84 |
| #define | [GET\_NTB\_INPUT\_SIZE](#ae5ab2b5f3c10b1fc42d5873f8e8082c0)   0x85 |
| #define | [SET\_NTB\_INPUT\_SIZE](#a485fd89a465fb5ad82c09a686ba3bc1b)   0x86 |
| #define | [GET\_MAX\_DATAGRAM\_SIZE](#aca024f2e7bb9f99d3376753589fa7c3f)   0x87 |
| #define | [SET\_MAX\_DATAGRAM\_SIZE](#a4d224c04ec87088b4494f43c59c59b86)   0x88 |
| #define | [GET\_CRC\_MODE](#a9dd7dad1bd3421f42a67f280826d464b)   0x89 |
| #define | [SET\_CRC\_MODE](#a634a3403221f33ae8506481b38840c2c)   0x8A |
| #define | [PACKET\_TYPE\_MULTICAST](#a4abfd25c9ca3e70c5b33b89ee9456087)   0x10 |
|  | Ethernet Packet Filter Bitmap. |
| #define | [PACKET\_TYPE\_BROADCAST](#a3143cff5f7275d394f259c3b83e54e4b)   0x08 |
| #define | [PACKET\_TYPE\_DIRECTED](#a5a2d0aa22741a4a48b976cddc6f57f98)   0x04 |
| #define | [PACKET\_TYPE\_ALL\_MULTICAST](#aac32de24c40e08d0d32d3db264fa964a)   0x02 |
| #define | [PACKET\_TYPE\_PROMISCUOUS](#a7be4d4e65526efb94ea1ef71da62f835)   0x01 |

## Detailed Description

USB Communications Device Class (CDC) public header.

Header follows the Class Definitions for Communications Devices Specification (CDC120-20101103-track.pdf), PSTN Devices Specification (PSTN120.pdf) and Ethernet Control Model Devices Specification (ECM120.pdf). Header is limited to ACM and ECM Subclasses.

## Macro Definition Documentation

## [◆ ](#a057b9de28602442b66a8c3a7befd62a7)ACM\_FUNC\_DESC

| #define ACM\_FUNC\_DESC   0x02 |
| --- |

## [◆ ](#a01b7a28004a035df52334b64308e4b22)ACM\_SUBCLASS

| #define ACM\_SUBCLASS   0x02 |
| --- |

Communications Class Subclass Codes.

## [◆ ](#a20396bb325a1e947b2e4b0017a134082)ACM\_VENDOR\_PROTOCOL

| #define ACM\_VENDOR\_PROTOCOL   0xFF |
| --- |

## [◆ ](#aaf98d38c2b9c859cf86e281bb67f27b0)AT\_CMD\_V250\_PROTOCOL

| #define AT\_CMD\_V250\_PROTOCOL   0x01 |
| --- |

Communications Class Protocol Codes.

## [◆ ](#a60552aa9506dc2c6dede5146c5251aaf)CALL\_MANAGEMENT\_FUNC\_DESC

| #define CALL\_MANAGEMENT\_FUNC\_DESC   0x01 |
| --- |

## [◆ ](#ac9008f0dc0d4fc7141de9dd12352caa8)CDC\_GET\_ENC\_RSP

| #define CDC\_GET\_ENC\_RSP   0x01 |
| --- |

## [◆ ](#a926f6444745d1cdc991d97e4f1d265ad)CDC\_SEND\_ENC\_CMD

| #define CDC\_SEND\_ENC\_CMD   0x00 |
| --- |

PSTN Subclass Specific Requests for ACM devices.

Note
:   PSTN120.pdf, 6.3, Table 13

## [◆ ](#a2d44425b0b0c5e525885c5764348ec54)CDC\_SRN\_1\_20

| #define CDC\_SRN\_1\_20   0x0120 |
| --- |

CDC Specification release number in BCD format.

## [◆ ](#ae4044b943c9e54cb7a64c8c35acaf8bc)DATA\_INTERFACE\_CLASS

| #define DATA\_INTERFACE\_CLASS   0x0A |
| --- |

Data Class Interface Codes.

Note
:   CDC120-20101103-track.pdf, 4.5, Table 6

## [◆ ](#a39f776a70d5139575ed84be1a9faee5d)ECM\_SUBCLASS

| #define ECM\_SUBCLASS   0x06 |
| --- |

## [◆ ](#ab4f22c3c42b5a4efe7735bafebc1cb9b)EEM\_PROTOCOL

| #define EEM\_PROTOCOL   0x07 |
| --- |

## [◆ ](#a73503e51ff8700620866be15a8d7ab43)EEM\_SUBCLASS

| #define EEM\_SUBCLASS   0x0c |
| --- |

## [◆ ](#a22b2b55d7ab3cdd4206df07cddcc44e9)ETHERNET\_FUNC\_DESC

| #define ETHERNET\_FUNC\_DESC   0x0F |
| --- |

## [◆ ](#ad788a76ba44ab5d02c699b110856e18e)ETHERNET\_FUNC\_DESC\_NCM

| #define ETHERNET\_FUNC\_DESC\_NCM   0x1a |
| --- |

## [◆ ](#a9dd7dad1bd3421f42a67f280826d464b)GET\_CRC\_MODE

| #define GET\_CRC\_MODE   0x89 |
| --- |

## [◆ ](#a53ea6ae0e1fe8a88350740fd594507fd)GET\_ETHERNET\_PM\_FILTER

| #define GET\_ETHERNET\_PM\_FILTER   0x42 |
| --- |

## [◆ ](#a7dffeba1576d6660fb930eabc5c515b7)GET\_ETHERNET\_STATISTIC

| #define GET\_ETHERNET\_STATISTIC   0x44 |
| --- |

## [◆ ](#a6698d8d2ca56fafdc943aec2cede1daf)GET\_LINE\_CODING

| #define GET\_LINE\_CODING   0x21 |
| --- |

## [◆ ](#aca024f2e7bb9f99d3376753589fa7c3f)GET\_MAX\_DATAGRAM\_SIZE

| #define GET\_MAX\_DATAGRAM\_SIZE   0x87 |
| --- |

## [◆ ](#a58701f26151379cd5dd8b7a7350dcda5)GET\_NET\_ADDRESS

| #define GET\_NET\_ADDRESS   0x81 |
| --- |

## [◆ ](#a2ba9ad377b20364fc811ec6d5bb74995)GET\_NTB\_FORMAT

| #define GET\_NTB\_FORMAT   0x83 |
| --- |

## [◆ ](#ae5ab2b5f3c10b1fc42d5873f8e8082c0)GET\_NTB\_INPUT\_SIZE

| #define GET\_NTB\_INPUT\_SIZE   0x85 |
| --- |

## [◆ ](#a44e5dd539b8b41ccc9c61dd95ee4fb2e)GET\_NTB\_PARAMETERS

| #define GET\_NTB\_PARAMETERS   0x80 |
| --- |

Class-Specific Request Codes for NCM subclass.

Note
:   NCM100.pdf, 6.2, Table 6-2

## [◆ ](#a008b7d343c5a1876a78c885f7a496b66)HEADER\_FUNC\_DESC

| #define HEADER\_FUNC\_DESC   0x00 |
| --- |

bDescriptor SubType for Communications Class Functional Descriptors

Note
:   CDC120-20101103-track.pdf, 5.2.3, Table 13

## [◆ ](#a6577856e991bddc829d93af0ea527ef6)NCM\_DATA\_PROTOCOL

| #define NCM\_DATA\_PROTOCOL   0x01 |
| --- |

## [◆ ](#af4edeebbc1d4fb6f3a727083a36e731e)NCM\_SUBCLASS

| #define NCM\_SUBCLASS   0x0d |
| --- |

## [◆ ](#aac32de24c40e08d0d32d3db264fa964a)PACKET\_TYPE\_ALL\_MULTICAST

| #define PACKET\_TYPE\_ALL\_MULTICAST   0x02 |
| --- |

## [◆ ](#a3143cff5f7275d394f259c3b83e54e4b)PACKET\_TYPE\_BROADCAST

| #define PACKET\_TYPE\_BROADCAST   0x08 |
| --- |

## [◆ ](#a5a2d0aa22741a4a48b976cddc6f57f98)PACKET\_TYPE\_DIRECTED

| #define PACKET\_TYPE\_DIRECTED   0x04 |
| --- |

## [◆ ](#a4abfd25c9ca3e70c5b33b89ee9456087)PACKET\_TYPE\_MULTICAST

| #define PACKET\_TYPE\_MULTICAST   0x10 |
| --- |

Ethernet Packet Filter Bitmap.

## [◆ ](#a7be4d4e65526efb94ea1ef71da62f835)PACKET\_TYPE\_PROMISCUOUS

| #define PACKET\_TYPE\_PROMISCUOUS   0x01 |
| --- |

## [◆ ](#aa66ab791abfcf7ef5a37758c1b33138a)SERIAL\_STATE\_BREAK

| #define SERIAL\_STATE\_BREAK   0x04 |
| --- |

## [◆ ](#aacd68fe3a081441ee684bf2ef6312bec)SERIAL\_STATE\_FRAMING

| #define SERIAL\_STATE\_FRAMING   0x10 |
| --- |

## [◆ ](#ae38825267009563e0aa82a58a7fc4fd2)SERIAL\_STATE\_OVER\_RUN

| #define SERIAL\_STATE\_OVER\_RUN   0x40 |
| --- |

UART State Bitmap Values.

## [◆ ](#a738f180df5795376763ff233fb8aa68d)SERIAL\_STATE\_PARITY

| #define SERIAL\_STATE\_PARITY   0x20 |
| --- |

## [◆ ](#a935c772da45984e8d796396146413037)SERIAL\_STATE\_RING\_SIGNAL

| #define SERIAL\_STATE\_RING\_SIGNAL   0x08 |
| --- |

## [◆ ](#a9677c612766f3e788ad2960a17ad0791)SERIAL\_STATE\_RX\_CARRIER

| #define SERIAL\_STATE\_RX\_CARRIER   0x01 |
| --- |

## [◆ ](#a22cd80b90c53ff44a4c1de08310ba3c2)SERIAL\_STATE\_TX\_CARRIER

| #define SERIAL\_STATE\_TX\_CARRIER   0x02 |
| --- |

## [◆ ](#a437869c339749d5d011060cd5676659e)SET\_CONTROL\_LINE\_STATE

| #define SET\_CONTROL\_LINE\_STATE   0x22 |
| --- |

## [◆ ](#a07623c40153f936c863627a3dc30da7a)SET\_CONTROL\_LINE\_STATE\_DTR

| #define SET\_CONTROL\_LINE\_STATE\_DTR   0x01 |
| --- |

## [◆ ](#a00788c95fb39c2636d7d5a427282399f)SET\_CONTROL\_LINE\_STATE\_RTS

| #define SET\_CONTROL\_LINE\_STATE\_RTS   0x02 |
| --- |

Control Signal Bitmap Values for SetControlLineState.

## [◆ ](#a634a3403221f33ae8506481b38840c2c)SET\_CRC\_MODE

| #define SET\_CRC\_MODE   0x8A |
| --- |

## [◆ ](#a4dce35ee8cf2337bab3c90081200a9f6)SET\_ETHERNET\_MULTICAST\_FILTERS

| #define SET\_ETHERNET\_MULTICAST\_FILTERS   0x40 |
| --- |

Class-Specific Request Codes for Ethernet subclass.

Note
:   ECM120.pdf, 6.2, Table 6

## [◆ ](#adae019242224bbbc9d0f853da3733f1c)SET\_ETHERNET\_PACKET\_FILTER

| #define SET\_ETHERNET\_PACKET\_FILTER   0x43 |
| --- |

## [◆ ](#a1506deda422ee354040b0feeb09ad4b6)SET\_ETHERNET\_PM\_FILTER

| #define SET\_ETHERNET\_PM\_FILTER   0x41 |
| --- |

## [◆ ](#a91a9c047339a1a5918b6a923af6d1af6)SET\_LINE\_CODING

| #define SET\_LINE\_CODING   0x20 |
| --- |

## [◆ ](#a4d224c04ec87088b4494f43c59c59b86)SET\_MAX\_DATAGRAM\_SIZE

| #define SET\_MAX\_DATAGRAM\_SIZE   0x88 |
| --- |

## [◆ ](#a2d8525d02e54ec44143a7732a15ad5b0)SET\_NET\_ADDRESS

| #define SET\_NET\_ADDRESS   0x82 |
| --- |

## [◆ ](#a9c48d4f5685678b1429ba90f7c0a7d9b)SET\_NTB\_FORMAT

| #define SET\_NTB\_FORMAT   0x84 |
| --- |

## [◆ ](#a485fd89a465fb5ad82c09a686ba3bc1b)SET\_NTB\_INPUT\_SIZE

| #define SET\_NTB\_INPUT\_SIZE   0x86 |
| --- |

## [◆ ](#aab7f21ab95fc5916f758e66087caef25)UNION\_FUNC\_DESC

| #define UNION\_FUNC\_DESC   0x06 |
| --- |

## [◆ ](#afdeb5f862a52b953653b9ab567979cec)USB\_CDC\_AUX\_JACK\_HOOK\_STATE

| #define USB\_CDC\_AUX\_JACK\_HOOK\_STATE   0x08 |
| --- |

## [◆ ](#a6bb6650664f82fd25330af0357e5831e)USB\_CDC\_CALL\_STATE\_CHANGE

| #define USB\_CDC\_CALL\_STATE\_CHANGE   0x28 |
| --- |

## [◆ ](#a327c495a9930b3e5519f0a9c7cd9ed18)USB\_CDC\_LINE\_CODING\_DATA\_BITS\_5

| #define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_5   5 |
| --- |

## [◆ ](#a231932add6d9ceef4f5332a0db1b9f55)USB\_CDC\_LINE\_CODING\_DATA\_BITS\_6

| #define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_6   6 |
| --- |

## [◆ ](#a6a276593bc4587671df5e6da8cce5ebb)USB\_CDC\_LINE\_CODING\_DATA\_BITS\_7

| #define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_7   7 |
| --- |

## [◆ ](#a64e296aec72bbd8f9bdc1aefa5aab654)USB\_CDC\_LINE\_CODING\_DATA\_BITS\_8

| #define USB\_CDC\_LINE\_CODING\_DATA\_BITS\_8   8 |
| --- |

## [◆ ](#a327b5f99ab7e5cfc99d7592d1f9c1c25)USB\_CDC\_LINE\_CODING\_PARITY\_EVEN

| #define USB\_CDC\_LINE\_CODING\_PARITY\_EVEN   2 |
| --- |

## [◆ ](#a490d381698ce91db4ab8bb24dd70820a)USB\_CDC\_LINE\_CODING\_PARITY\_MARK

| #define USB\_CDC\_LINE\_CODING\_PARITY\_MARK   3 |
| --- |

## [◆ ](#a549181d2cc92c42b4db8c3c34927d97f)USB\_CDC\_LINE\_CODING\_PARITY\_NO

| #define USB\_CDC\_LINE\_CODING\_PARITY\_NO   0 |
| --- |

## [◆ ](#a44d808ad4f27ecf3502b9c14da2aa9b9)USB\_CDC\_LINE\_CODING\_PARITY\_ODD

| #define USB\_CDC\_LINE\_CODING\_PARITY\_ODD   1 |
| --- |

## [◆ ](#a5aa1b5cf30cb4020442131f66170fec6)USB\_CDC\_LINE\_CODING\_PARITY\_SPACE

| #define USB\_CDC\_LINE\_CODING\_PARITY\_SPACE   4 |
| --- |

## [◆ ](#a8a06b3413e1c665f13ba4895c220d608)USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1

| #define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1   0 |
| --- |

PSTN Subclass Line Coding Values.

Note
:   PSTN120.pdf, 6.3.11, Table 17

## [◆ ](#a4159f50590d647510a6a1f38875e012e)USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1\_5

| #define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_1\_5   1 |
| --- |

## [◆ ](#a7e7fc73b4490a694aa982b4862782157)USB\_CDC\_LINE\_CODING\_STOP\_BITS\_2

| #define USB\_CDC\_LINE\_CODING\_STOP\_BITS\_2   2 |
| --- |

## [◆ ](#a89554d686630d67d642e228b7ee0dc2c)USB\_CDC\_LINE\_CTRL\_BAUD\_RATE

| #define USB\_CDC\_LINE\_CTRL\_BAUD\_RATE   [UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) |
| --- |

Enhance enum [uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0 "Line control signals.") with CDC specific values.

## [◆ ](#a716d9aaf772e1fa3f8b555077048ecbb)USB\_CDC\_LINE\_CTRL\_BREAK

| #define USB\_CDC\_LINE\_CTRL\_BREAK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a7e6b9bb33debc489b7ac7e0fb0e94947)USB\_CDC\_LINE\_CTRL\_DCD

| #define USB\_CDC\_LINE\_CTRL\_DCD   [UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) |
| --- |

## [◆ ](#a6876caf1b77477e259bb391216309799)USB\_CDC\_LINE\_CTRL\_DSR

| #define USB\_CDC\_LINE\_CTRL\_DSR   [UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) |
| --- |

## [◆ ](#a263186a0a64d9a8e7e9e97a54b951bdf)USB\_CDC\_LINE\_CTRL\_FRAMING

| #define USB\_CDC\_LINE\_CTRL\_FRAMING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a8bf1722f98bf48394605efddf6be1295)USB\_CDC\_LINE\_CTRL\_OVER\_RUN

| #define USB\_CDC\_LINE\_CTRL\_OVER\_RUN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#ae2779672a5b5ab49a2ed7240e463f9e8)USB\_CDC\_LINE\_CTRL\_PARITY

| #define USB\_CDC\_LINE\_CTRL\_PARITY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a8ec9b8c619c567cc174c0473dda5a5fd)USB\_CDC\_LINE\_CTRL\_RING\_SIGNAL

| #define USB\_CDC\_LINE\_CTRL\_RING\_SIGNAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#ac63891d7c3321f7f4eb297f87c0978f6)USB\_CDC\_LINE\_STATE\_CHANGE

| #define USB\_CDC\_LINE\_STATE\_CHANGE   0x23 |
| --- |

## [◆ ](#a7e9384e6a613e38c543d7eba05f64c07)USB\_CDC\_NETWORK\_CONNECTION

| #define USB\_CDC\_NETWORK\_CONNECTION   0x00 |
| --- |

PSTN Subclass Class-Specific Notification Codes.

Note
:   PSTN120.pdf, 6.5, Table 30

## [◆ ](#a970045b850b0195b5a4a2913d5a0b918)USB\_CDC\_RESPONSE\_AVAILABLE

| #define USB\_CDC\_RESPONSE\_AVAILABLE   0x01 |
| --- |

## [◆ ](#a52452ce9272b97203fece115b5005aff)USB\_CDC\_RING\_DETECT

| #define USB\_CDC\_RING\_DETECT   0x09 |
| --- |

## [◆ ](#ac167f480370c73b830281d98ad5899b1)USB\_CDC\_SERIAL\_STATE

| #define USB\_CDC\_SERIAL\_STATE   0x20 |
| --- |

## [◆ ](#a15f3c90969106ecdf3b1cdf258cad5df)USB\_CDC\_SERIAL\_STATE\_BREAK

| #define USB\_CDC\_SERIAL\_STATE\_BREAK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a59f5f1ebab838621cdc67668541432ca)USB\_CDC\_SERIAL\_STATE\_FRAMING

| #define USB\_CDC\_SERIAL\_STATE\_FRAMING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a504f682d66f714730f35d282ce0b9177)USB\_CDC\_SERIAL\_STATE\_OVERRUN

| #define USB\_CDC\_SERIAL\_STATE\_OVERRUN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

PSTN UART State Bitmap Values.

Note
:   PSTN120.pdf, 6.5.4, Table 31

## [◆ ](#a1ff82c5d551211d2298128bd84eeb60a)USB\_CDC\_SERIAL\_STATE\_PARITY

| #define USB\_CDC\_SERIAL\_STATE\_PARITY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a60f22cb2ae47789875e2542063899876)USB\_CDC\_SERIAL\_STATE\_RINGSIGNAL

| #define USB\_CDC\_SERIAL\_STATE\_RINGSIGNAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#ad720be9e3738bcba7e37dc9392c3b6e8)USB\_CDC\_SERIAL\_STATE\_RXCARRIER

| #define USB\_CDC\_SERIAL\_STATE\_RXCARRIER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ab96b4f63f2de0ef913862878bce1029f)USB\_CDC\_SERIAL\_STATE\_TXCARRIER

| #define USB\_CDC\_SERIAL\_STATE\_TXCARRIER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_cdc.h](usb__cdc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
