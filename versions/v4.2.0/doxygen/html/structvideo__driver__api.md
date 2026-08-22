---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvideo__driver__api.html
original_path: doxygen/html/structvideo__driver__api.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

`#include <[zephyr/drivers/video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1) | [set\_format](#a1859e3a1db99d97c38ea24f2f9cd00be) |
| [video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1) | [get\_format](#a8daefeec3cfc01de56f0168b32cdb640) |
| [video\_api\_set\_stream\_t](group__video__interface.md#gacda90bacb17a53e0bd11e5bfd37be57a) | [set\_stream](#adc08ef9eeeaac584c1b9ae5e6fb70c04) |
| [video\_api\_get\_caps\_t](group__video__interface.md#ga070cb5f5bf35b98e2e7dda3378114780) | [get\_caps](#a6ab4deb345d2138e63e0c6126eeb5078) |
| [video\_api\_enqueue\_t](group__video__interface.md#gae6849a22140b3507bab219b579bc3d40) | [enqueue](#a4762a3f103ca5999e3d3f790bb74af75) |
| [video\_api\_dequeue\_t](group__video__interface.md#ga4265087c8faf62bbc36e88c0587022a1) | [dequeue](#a96ba1bb4b76c7efc445b3071ef3a05ef) |
| [video\_api\_flush\_t](group__video__interface.md#ga990ba001531c7300a06ca02d64c31eaa) | [flush](#a963927cc38174c4703470df04ec73dc6) |
| [video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303) | [set\_ctrl](#a41cd20fbb013bdb6b28d79822733695c) |
| [video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303) | [get\_volatile\_ctrl](#af50329fd41db78f4c5a945f57a7c091e) |
| [video\_api\_set\_signal\_t](group__video__interface.md#gad5aacb1386785a3587d41844c7854f83) | [set\_signal](#a59dbaa93982c354c16d5de63c0d03ec2) |
| [video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88) | [set\_frmival](#ac4b155a56c07bd8f7ecff9ec75dd0792) |
| [video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88) | [get\_frmival](#abddf2db6034d10f76ac90ed5974df788) |
| [video\_api\_enum\_frmival\_t](group__video__interface.md#ga026c9a4531a125339e69b81f75343555) | [enum\_frmival](#a6481a76f3f4d33629bbebb29ef9e8726) |
| [video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a) | [set\_selection](#a800a2e8aaf59fc3fbd4bd2caaaf40f51) |
| [video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a) | [get\_selection](#a6ad8559ae0c2f6dc102e26e3714ded5d) |

## Field Documentation

## [◆ ](#a96ba1bb4b76c7efc445b3071ef3a05ef)dequeue

| [video\_api\_dequeue\_t](group__video__interface.md#ga4265087c8faf62bbc36e88c0587022a1) video\_driver\_api::dequeue |
| --- |

## [◆ ](#a4762a3f103ca5999e3d3f790bb74af75)enqueue

| [video\_api\_enqueue\_t](group__video__interface.md#gae6849a22140b3507bab219b579bc3d40) video\_driver\_api::enqueue |
| --- |

## [◆ ](#a6481a76f3f4d33629bbebb29ef9e8726)enum\_frmival

| [video\_api\_enum\_frmival\_t](group__video__interface.md#ga026c9a4531a125339e69b81f75343555) video\_driver\_api::enum\_frmival |
| --- |

## [◆ ](#a963927cc38174c4703470df04ec73dc6)flush

| [video\_api\_flush\_t](group__video__interface.md#ga990ba001531c7300a06ca02d64c31eaa) video\_driver\_api::flush |
| --- |

## [◆ ](#a6ab4deb345d2138e63e0c6126eeb5078)get\_caps

| [video\_api\_get\_caps\_t](group__video__interface.md#ga070cb5f5bf35b98e2e7dda3378114780) video\_driver\_api::get\_caps |
| --- |

## [◆ ](#a8daefeec3cfc01de56f0168b32cdb640)get\_format

| [video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1) video\_driver\_api::get\_format |
| --- |

## [◆ ](#abddf2db6034d10f76ac90ed5974df788)get\_frmival

| [video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88) video\_driver\_api::get\_frmival |
| --- |

## [◆ ](#a6ad8559ae0c2f6dc102e26e3714ded5d)get\_selection

| [video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a) video\_driver\_api::get\_selection |
| --- |

## [◆ ](#af50329fd41db78f4c5a945f57a7c091e)get\_volatile\_ctrl

| [video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303) video\_driver\_api::get\_volatile\_ctrl |
| --- |

## [◆ ](#a41cd20fbb013bdb6b28d79822733695c)set\_ctrl

| [video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303) video\_driver\_api::set\_ctrl |
| --- |

## [◆ ](#a1859e3a1db99d97c38ea24f2f9cd00be)set\_format

| [video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1) video\_driver\_api::set\_format |
| --- |

## [◆ ](#ac4b155a56c07bd8f7ecff9ec75dd0792)set\_frmival

| [video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88) video\_driver\_api::set\_frmival |
| --- |

## [◆ ](#a800a2e8aaf59fc3fbd4bd2caaaf40f51)set\_selection

| [video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a) video\_driver\_api::set\_selection |
| --- |

## [◆ ](#a59dbaa93982c354c16d5de63c0d03ec2)set\_signal

| [video\_api\_set\_signal\_t](group__video__interface.md#gad5aacb1386785a3587d41844c7854f83) video\_driver\_api::set\_signal |
| --- |

## [◆ ](#adc08ef9eeeaac584c1b9ae5e6fb70c04)set\_stream

| [video\_api\_set\_stream\_t](group__video__interface.md#gacda90bacb17a53e0bd11e5bfd37be57a) video\_driver\_api::set\_stream |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_driver\_api](structvideo__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
