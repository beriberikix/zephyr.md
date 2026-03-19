---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usbd__hid_8h_source.html
original_path: doxygen/html/usbd__hid_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_hid.h

[Go to the documentation of this file.](usbd__hid_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_USBD\_HID\_CLASS\_DEVICE\_H\_

13#define ZEPHYR\_INCLUDE\_USBD\_HID\_CLASS\_DEVICE\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/usb/class/hid.h](hid_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

31

32/\*

33 \* HID Device overview:

34 \*

35 \* +---------------------+

36 \* | |

37 \* | |

38 \* | HID Device |

39 \* | User "top half" |

40 \* | of the device that +-------+

41 \* | deals with input | |

42 \* | sampling | |

43 \* | | |

44 \* | | |

45 \* | ------------------- | |

46 \* | | |

47 \* | HID Device user | |

48 \* | callbacks | |

49 \* | handlers | |

50 \* +---------------------+ |

51 \* ^ | HID Device Driver API:

52 \* | |

53 \* set\_protocol() | | hid\_device\_register()

54 \* get\_report() | | hid\_device\_submit\_report(

55 \* .... | | ...

56 \* v |

57 \* +---------------------+ |

58 \* | | |

59 \* | HID Device | |

60 \* | "bottom half" |<------+

61 \* | USB HID class |

62 \* | implementation |

63 \* | |

64 \* | |

65 \* +---------------------+

66 \* ^

67 \* v

68 \* +--------------------+

69 \* | |

70 \* | USB Device |

71 \* | Support |

72 \* | |

73 \* +--------------------+

74 \*/

75

79enum {

[ 80](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd) [HID\_REPORT\_TYPE\_INPUT](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd) = 1,

[ 81](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3) [HID\_REPORT\_TYPE\_OUTPUT](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3),

[ 82](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea) [HID\_REPORT\_TYPE\_FEATURE](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea),

83};

84

[ 96](structhid__device__ops.md)struct [hid\_device\_ops](structhid__device__ops.md) {

[ 104](structhid__device__ops.md#a8d96a142b963dd257b2dbb64df82181d) void (\*[iface\_ready](structhid__device__ops.md#a8d96a142b963dd257b2dbb64df82181d))(const struct [device](structdevice.md) \*dev, const bool ready);

105

[ 116](structhid__device__ops.md#aff034989bee801c143384464eb6a5a9d) int (\*[get\_report](structhid__device__ops.md#aff034989bee801c143384464eb6a5a9d))(const struct [device](structdevice.md) \*dev,

117 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

118 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf);

119

[ 128](structhid__device__ops.md#add555b9782b763d5b411909d07d952b8) int (\*[set\_report](structhid__device__ops.md#add555b9782b763d5b411909d07d952b8))(const struct [device](structdevice.md) \*dev,

129 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

130 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf);

131

[ 140](structhid__device__ops.md#a48e03408d693d4d9d9dacf6513a36828) void (\*[set\_idle](structhid__device__ops.md#a48e03408d693d4d9d9dacf6513a36828))(const struct [device](structdevice.md) \*dev,

141 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) duration);

142

[ 148](structhid__device__ops.md#afd8c16e1256945bc15c70439051deb26) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[get\_idle](structhid__device__ops.md#afd8c16e1256945bc15c70439051deb26))(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id);

149

[ 154](structhid__device__ops.md#ae9290b806b57c9595fad3ec0a65fdca2) void (\*[set\_protocol](structhid__device__ops.md#ae9290b806b57c9595fad3ec0a65fdca2))(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto);

155

[ 162](structhid__device__ops.md#ae60e82dd991f18d28da1a035ae6b257c) void (\*[input\_report\_done](structhid__device__ops.md#ae60e82dd991f18d28da1a035ae6b257c))(const struct [device](structdevice.md) \*dev);

163

[ 171](structhid__device__ops.md#ac58785fc2a44be7c46e0c950fc09f0ac) void (\*[output\_report](structhid__device__ops.md#ac58785fc2a44be7c46e0c950fc09f0ac))(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len,

172 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf);

[ 179](structhid__device__ops.md#a0043b6bf005785274de2b65f341cb588) void (\*[sof](structhid__device__ops.md#a0043b6bf005785274de2b65f341cb588))(const struct [device](structdevice.md) \*dev);

180};

181

[ 193](group__usbd__hid__device.md#gabb4502a7c3ab5d2400c039549577f4d0)int [hid\_device\_register](group__usbd__hid__device.md#gabb4502a7c3ab5d2400c039549577f4d0)(const struct [device](structdevice.md) \*dev,

194 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const rdesc, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rsize,

195 const struct [hid\_device\_ops](structhid__device__ops.md) \*const ops);

196

[ 211](group__usbd__hid__device.md#ga547f99b1089a4d65a297faa5d6e8edd8)int [hid\_device\_submit\_report](group__usbd__hid__device.md#ga547f99b1089a4d65a297faa5d6e8edd8)(const struct [device](structdevice.md) \*dev,

212 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const report);

213

217

218#ifdef \_\_cplusplus

219}

220#endif

221

222#endif /\* ZEPHYR\_INCLUDE\_USBD\_HID\_CLASS\_DEVICE\_H\_ \*/

[device.h](device_8h.md)

[hid\_device\_submit\_report](group__usbd__hid__device.md#ga547f99b1089a4d65a297faa5d6e8edd8)

int hid\_device\_submit\_report(const struct device \*dev, const uint16\_t size, const uint8\_t \*const report)

Submit new input report.

[hid\_device\_register](group__usbd__hid__device.md#gabb4502a7c3ab5d2400c039549577f4d0)

int hid\_device\_register(const struct device \*dev, const uint8\_t \*const rdesc, const uint16\_t rsize, const struct hid\_device\_ops \*const ops)

Register HID device report descriptor and user callbacks.

[HID\_REPORT\_TYPE\_INPUT](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd)

@ HID\_REPORT\_TYPE\_INPUT

**Definition** usbd\_hid.h:80

[HID\_REPORT\_TYPE\_OUTPUT](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3)

@ HID\_REPORT\_TYPE\_OUTPUT

**Definition** usbd\_hid.h:81

[HID\_REPORT\_TYPE\_FEATURE](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea)

@ HID\_REPORT\_TYPE\_FEATURE

**Definition** usbd\_hid.h:82

[hid.h](hid_8h.md)

USB Human Interface Device (HID) common definitions header.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[hid\_device\_ops](structhid__device__ops.md)

HID device user callbacks.

**Definition** usbd\_hid.h:96

[hid\_device\_ops::sof](structhid__device__ops.md#a0043b6bf005785274de2b65f341cb588)

void(\* sof)(const struct device \*dev)

Optional Start of Frame (SoF) event callback.

**Definition** usbd\_hid.h:179

[hid\_device\_ops::set\_idle](structhid__device__ops.md#a48e03408d693d4d9d9dacf6513a36828)

void(\* set\_idle)(const struct device \*dev, const uint8\_t id, const uint32\_t duration)

Notification to limit input report frequency.

**Definition** usbd\_hid.h:140

[hid\_device\_ops::iface\_ready](structhid__device__ops.md#a8d96a142b963dd257b2dbb64df82181d)

void(\* iface\_ready)(const struct device \*dev, const bool ready)

The interface ready callback is called with the ready argument set to true when the corresponding int...

**Definition** usbd\_hid.h:104

[hid\_device\_ops::output\_report](structhid__device__ops.md#ac58785fc2a44be7c46e0c950fc09f0ac)

void(\* output\_report)(const struct device \*dev, const uint16\_t len, const uint8\_t \*const buf)

New output report callback.

**Definition** usbd\_hid.h:171

[hid\_device\_ops::set\_report](structhid__device__ops.md#add555b9782b763d5b411909d07d952b8)

int(\* set\_report)(const struct device \*dev, const uint8\_t type, const uint8\_t id, const uint16\_t len, const uint8\_t \*const buf)

This callback is called for the HID Set Report request to set a feature, input, or output report,...

**Definition** usbd\_hid.h:128

[hid\_device\_ops::input\_report\_done](structhid__device__ops.md#ae60e82dd991f18d28da1a035ae6b257c)

void(\* input\_report\_done)(const struct device \*dev)

Notification that input report submitted with hid\_device\_submit\_report() has been sent.

**Definition** usbd\_hid.h:162

[hid\_device\_ops::set\_protocol](structhid__device__ops.md#ae9290b806b57c9595fad3ec0a65fdca2)

void(\* set\_protocol)(const struct device \*dev, const uint8\_t proto)

Notification that the host has changed the protocol from Boot Protocol(0) to Report Protocol(1) or vi...

**Definition** usbd\_hid.h:154

[hid\_device\_ops::get\_idle](structhid__device__ops.md#afd8c16e1256945bc15c70439051deb26)

uint32\_t(\* get\_idle)(const struct device \*dev, const uint8\_t id)

If a report ID is used in the report descriptor, the device must implement this callback and return t...

**Definition** usbd\_hid.h:148

[hid\_device\_ops::get\_report](structhid__device__ops.md#aff034989bee801c143384464eb6a5a9d)

int(\* get\_report)(const struct device \*dev, const uint8\_t type, const uint8\_t id, const uint16\_t len, uint8\_t \*const buf)

This callback is called for the HID Get Report request to get a feature, input, or output report,...

**Definition** usbd\_hid.h:116

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_hid.h](usbd__hid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
