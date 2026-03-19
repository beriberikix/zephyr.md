---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.html
original_path: doxygen/html/structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a40980265955d4d58a9b5407ff845fde4) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_handle](#a4f8fe99c2392c06125ba94e61aed0e6c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_config\_supported](#ab09a466b2a9a0be5f5021f1da0d7393a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_consecutive\_procedures\_supported](#ac73a8bf5425c80739e84cb30ce94f3e7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_antennas\_supported](#adcf35e055d04775c444fa28655b95337) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_antenna\_paths\_supported](#a50ad0408019dce16685215c6a1b6d0ef) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [roles\_supported](#a99f9f7b08de6b41e88cea10ba0ca6010) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [modes\_supported](#ab7a35b1093ece7ae9cc5def4a3e473b2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtt\_capability](#ace95740224b31c127f5e13550cb5a23a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtt\_aa\_only\_n](#a843968ec69106d076596e110407d8a1a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtt\_sounding\_n](#a7f796e2eda8d3c7eae556932e37cd93d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtt\_random\_payload\_n](#a3f275ad58ca745347172ad0b89faf2c4) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [nadm\_sounding\_capability](#adebb5328c7baeaa786bc185fec432e40) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [nadm\_random\_capability](#a7af3067f319be094af31512d4ee5101e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cs\_sync\_phys\_supported](#a1f303dc3aa8a23fccde27a2d2f64d732) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [subfeatures\_supported](#ac83543c17606e401d919fce841a12c6c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [t\_ip1\_times\_supported](#ad330adf1ae5b9b84756d36801a4cf289) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [t\_ip2\_times\_supported](#a0a1d9dcdf184e49349e86980da2e4bed) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [t\_fcs\_times\_supported](#a44869fd19ae813830e38f6e4b88dbb1d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [t\_pm\_times\_supported](#afef9f37784d75f54521793f07b5baece) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_sw\_time\_supported](#a21a322fc8efd0c410dda78e2652d506d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_snr\_capability](#ae3d06bce4df7a2ca07c5d6dd01124743) |

## Field Documentation

## [◆ ](#a4f8fe99c2392c06125ba94e61aed0e6c)conn\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::conn\_handle |
| --- |

## [◆ ](#a1f303dc3aa8a23fccde27a2d2f64d732)cs\_sync\_phys\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::cs\_sync\_phys\_supported |
| --- |

## [◆ ](#a50ad0408019dce16685215c6a1b6d0ef)max\_antenna\_paths\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::max\_antenna\_paths\_supported |
| --- |

## [◆ ](#ac73a8bf5425c80739e84cb30ce94f3e7)max\_consecutive\_procedures\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::max\_consecutive\_procedures\_supported |
| --- |

## [◆ ](#ab7a35b1093ece7ae9cc5def4a3e473b2)modes\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::modes\_supported |
| --- |

## [◆ ](#a7af3067f319be094af31512d4ee5101e)nadm\_random\_capability

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::nadm\_random\_capability |
| --- |

## [◆ ](#adebb5328c7baeaa786bc185fec432e40)nadm\_sounding\_capability

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::nadm\_sounding\_capability |
| --- |

## [◆ ](#adcf35e055d04775c444fa28655b95337)num\_antennas\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::num\_antennas\_supported |
| --- |

## [◆ ](#ab09a466b2a9a0be5f5021f1da0d7393a)num\_config\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::num\_config\_supported |
| --- |

## [◆ ](#a99f9f7b08de6b41e88cea10ba0ca6010)roles\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::roles\_supported |
| --- |

## [◆ ](#a843968ec69106d076596e110407d8a1a)rtt\_aa\_only\_n

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::rtt\_aa\_only\_n |
| --- |

## [◆ ](#ace95740224b31c127f5e13550cb5a23a)rtt\_capability

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::rtt\_capability |
| --- |

## [◆ ](#a3f275ad58ca745347172ad0b89faf2c4)rtt\_random\_payload\_n

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::rtt\_random\_payload\_n |
| --- |

## [◆ ](#a7f796e2eda8d3c7eae556932e37cd93d)rtt\_sounding\_n

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::rtt\_sounding\_n |
| --- |

## [◆ ](#a40980265955d4d58a9b5407ff845fde4)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::status |
| --- |

## [◆ ](#ac83543c17606e401d919fce841a12c6c)subfeatures\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::subfeatures\_supported |
| --- |

## [◆ ](#a44869fd19ae813830e38f6e4b88dbb1d)t\_fcs\_times\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_fcs\_times\_supported |
| --- |

## [◆ ](#ad330adf1ae5b9b84756d36801a4cf289)t\_ip1\_times\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_ip1\_times\_supported |
| --- |

## [◆ ](#a0a1d9dcdf184e49349e86980da2e4bed)t\_ip2\_times\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_ip2\_times\_supported |
| --- |

## [◆ ](#afef9f37784d75f54521793f07b5baece)t\_pm\_times\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_pm\_times\_supported |
| --- |

## [◆ ](#a21a322fc8efd0c410dda78e2652d506d)t\_sw\_time\_supported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_sw\_time\_supported |
| --- |

## [◆ ](#ae3d06bce4df7a2ca07c5d6dd01124743)tx\_snr\_capability

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::tx\_snr\_capability |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
