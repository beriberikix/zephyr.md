---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/adi__max32__clock__control_8h.html
original_path: doxygen/html/adi__max32__clock__control_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adi\_max32\_clock\_control.h File Reference

`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`  
`#include <[zephyr/dt-bindings/clock/adi_max32_clock.h](adi__max32__clock_8h_source.md)>`  
`#include <wrap_max32_sys.h>`

[Go to the source code of this file.](adi__max32__clock__control_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [max32\_perclk](structmax32__perclk.md) |
|  | Driver structure definition. [More...](structmax32__perclk.md#details) |

| Macros | |
| --- | --- |
| #define | [ADI\_MAX32\_SYSCLK\_PRESCALER](#a41eab4d492a019700d1e1d4714932cd9)   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(gcr), sysclk\_prescaler, 1) |
|  | Get prescaler value if it defined. |
| #define | [ADI\_MAX32\_CLK\_IPO\_FREQ](#a31a7fbb2f0c1ce1f5b9899b49b6324ec)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ipo), clock\_frequency) |
| #define | [ADI\_MAX32\_CLK\_ERFO\_FREQ](#a56a549a210a78cb99f019f85fa15807b)   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_erfo), clock\_frequency, 0) |
| #define | [ADI\_MAX32\_CLK\_IBRO\_FREQ](#ae5e0473609734b17bcdd2ce6f4e7a63a)   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ibro), clock\_frequency, 0) |
| #define | [ADI\_MAX32\_CLK\_ISO\_FREQ](#ace96ad0d7564ad0fe326992257686820)   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_iso), clock\_frequency, 0) |
| #define | [ADI\_MAX32\_CLK\_INRO\_FREQ](#abb3947e441021737ca566e89fd56cb0c)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_inro), clock\_frequency) |
| #define | [ADI\_MAX32\_CLK\_ERTCO\_FREQ](#a664282617e29d44f951a48da1ac1ae9d)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ertco), clock\_frequency) |
| #define | [ADI\_MAX32\_CLK\_IPLL\_FREQ](#aa58ed1a1d381f11cd6410797449b17ba)   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ipll), clock\_frequency, 0) |
| #define | [ADI\_MAX32\_CLK\_EBO\_FREQ](#a47709e72b60d70e0d07576b8787118e0)   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ebo), clock\_frequency, 0) |
| #define | [ADI\_MAX32\_CLK\_EXTCLK\_FREQ](#a158271c4ced07ddeda9e677f7fd028c7)   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_extclk), clock\_frequency, 0) |
| #define | [DT\_GCR\_CLOCKS\_CTRL](#a1de5a43e10f129609662765dc2ebac24)   [DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(gcr)) |
| #define | [ADI\_MAX32\_SYSCLK\_SRC](#a21d5bba4fce8bf21105689ae8ea96216)   ADI\_MAX32\_CLK\_IPO |
| #define | [ADI\_MAX32\_SYSCLK\_FREQ](#ac82b515b2268a26b19b69972fc113e1c)   ([ADI\_MAX32\_CLK\_IPO\_FREQ](#a31a7fbb2f0c1ce1f5b9899b49b6324ec) / [ADI\_MAX32\_SYSCLK\_PRESCALER](#a41eab4d492a019700d1e1d4714932cd9)) |
| #define | [ADI\_MAX32\_PCLK\_FREQ](#a4e3ca6232db9220b60f17d1dca74627f)   ([ADI\_MAX32\_SYSCLK\_FREQ](#ac82b515b2268a26b19b69972fc113e1c) / 2) |
| #define | [ADI\_MAX32\_GET\_PRPH\_CLK\_FREQ](#abc5b92548642b17cb955d1f6b1949726)(clk\_src) |

## Macro Definition Documentation

## [◆ ](#a47709e72b60d70e0d07576b8787118e0)ADI\_MAX32\_CLK\_EBO\_FREQ

| #define ADI\_MAX32\_CLK\_EBO\_FREQ   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ebo), clock\_frequency, 0) |
| --- |

## [◆ ](#a56a549a210a78cb99f019f85fa15807b)ADI\_MAX32\_CLK\_ERFO\_FREQ

| #define ADI\_MAX32\_CLK\_ERFO\_FREQ   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_erfo), clock\_frequency, 0) |
| --- |

## [◆ ](#a664282617e29d44f951a48da1ac1ae9d)ADI\_MAX32\_CLK\_ERTCO\_FREQ

| #define ADI\_MAX32\_CLK\_ERTCO\_FREQ   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ertco), clock\_frequency) |
| --- |

## [◆ ](#a158271c4ced07ddeda9e677f7fd028c7)ADI\_MAX32\_CLK\_EXTCLK\_FREQ

| #define ADI\_MAX32\_CLK\_EXTCLK\_FREQ   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_extclk), clock\_frequency, 0) |
| --- |

## [◆ ](#ae5e0473609734b17bcdd2ce6f4e7a63a)ADI\_MAX32\_CLK\_IBRO\_FREQ

| #define ADI\_MAX32\_CLK\_IBRO\_FREQ   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ibro), clock\_frequency, 0) |
| --- |

## [◆ ](#abb3947e441021737ca566e89fd56cb0c)ADI\_MAX32\_CLK\_INRO\_FREQ

| #define ADI\_MAX32\_CLK\_INRO\_FREQ   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_inro), clock\_frequency) |
| --- |

## [◆ ](#aa58ed1a1d381f11cd6410797449b17ba)ADI\_MAX32\_CLK\_IPLL\_FREQ

| #define ADI\_MAX32\_CLK\_IPLL\_FREQ   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ipll), clock\_frequency, 0) |
| --- |

## [◆ ](#a31a7fbb2f0c1ce1f5b9899b49b6324ec)ADI\_MAX32\_CLK\_IPO\_FREQ

| #define ADI\_MAX32\_CLK\_IPO\_FREQ   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_ipo), clock\_frequency) |
| --- |

## [◆ ](#ace96ad0d7564ad0fe326992257686820)ADI\_MAX32\_CLK\_ISO\_FREQ

| #define ADI\_MAX32\_CLK\_ISO\_FREQ   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clk\_iso), clock\_frequency, 0) |
| --- |

## [◆ ](#abc5b92548642b17cb955d1f6b1949726)ADI\_MAX32\_GET\_PRPH\_CLK\_FREQ

| #define ADI\_MAX32\_GET\_PRPH\_CLK\_FREQ | ( |  | *clk\_src* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_PCLK](adi__max32__clock_8h.md#ad28575fff49c4cb3c4b8c4180cd387de) ? [ADI\_MAX32\_PCLK\_FREQ](#a4e3ca6232db9220b60f17d1dca74627f) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO](adi__max32__clock_8h.md#a0ec9e4fb6e4522325b7c26b1aa6ff4ae) ? [ADI\_MAX32\_CLK\_IBRO\_FREQ](#ae5e0473609734b17bcdd2ce6f4e7a63a) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_ERFO](adi__max32__clock_8h.md#af9ad74e5aff66314ef7ea4bcbd58a12f) ? [ADI\_MAX32\_CLK\_ERFO\_FREQ](#a56a549a210a78cb99f019f85fa15807b) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_ERTCO](adi__max32__clock_8h.md#ae22725273956cf339a7aa1ab99ec9d64) ? [ADI\_MAX32\_CLK\_ERTCO\_FREQ](#a664282617e29d44f951a48da1ac1ae9d) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_INRO](adi__max32__clock_8h.md#ad6039fb9117f11753b062ce70ab6086c) ? [ADI\_MAX32\_CLK\_INRO\_FREQ](#abb3947e441021737ca566e89fd56cb0c) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_ISO](adi__max32__clock_8h.md#a7cc83f5e0a532b4f59909167562042f0) ? [ADI\_MAX32\_CLK\_ISO\_FREQ](#ace96ad0d7564ad0fe326992257686820) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO\_DIV8](adi__max32__clock_8h.md#a79b4ec22a2ad744b20511fd72f00b88b) ? ([ADI\_MAX32\_CLK\_IBRO\_FREQ](#ae5e0473609734b17bcdd2ce6f4e7a63a) / 8) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_EXTCLK](adi__max32__clock_8h.md#a6bc3da20a61d735c15894c7cb7f6fb88) ? [ADI\_MAX32\_CLK\_EXTCLK\_FREQ](#a158271c4ced07ddeda9e677f7fd028c7) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_IPLL](adi__max32__clock_8h.md#abf12d2334614747738816c67aa32b4e6) ? [ADI\_MAX32\_CLK\_IPLL\_FREQ](#aa58ed1a1d381f11cd6410797449b17ba) \

: (clk\_src) == [ADI\_MAX32\_PRPH\_CLK\_SRC\_EBO](adi__max32__clock_8h.md#ada66413c52e2d3c1d166569fb9d52a84) ? [ADI\_MAX32\_CLK\_EBO\_FREQ](#a47709e72b60d70e0d07576b8787118e0) \

: 0)

[ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO](adi__max32__clock_8h.md#a0ec9e4fb6e4522325b7c26b1aa6ff4ae)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO

**Definition** adi\_max32\_clock.h:18

[ADI\_MAX32\_PRPH\_CLK\_SRC\_EXTCLK](adi__max32__clock_8h.md#a6bc3da20a61d735c15894c7cb7f6fb88)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_EXTCLK

**Definition** adi\_max32\_clock.h:17

[ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO\_DIV8](adi__max32__clock_8h.md#a79b4ec22a2ad744b20511fd72f00b88b)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO\_DIV8

**Definition** adi\_max32\_clock.h:23

[ADI\_MAX32\_PRPH\_CLK\_SRC\_ISO](adi__max32__clock_8h.md#a7cc83f5e0a532b4f59909167562042f0)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_ISO

**Definition** adi\_max32\_clock.h:22

[ADI\_MAX32\_PRPH\_CLK\_SRC\_IPLL](adi__max32__clock_8h.md#abf12d2334614747738816c67aa32b4e6)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_IPLL

**Definition** adi\_max32\_clock.h:24

[ADI\_MAX32\_PRPH\_CLK\_SRC\_PCLK](adi__max32__clock_8h.md#ad28575fff49c4cb3c4b8c4180cd387de)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_PCLK

Clock source for peripheral interfaces like UART, WDT...

**Definition** adi\_max32\_clock.h:16

[ADI\_MAX32\_PRPH\_CLK\_SRC\_INRO](adi__max32__clock_8h.md#ad6039fb9117f11753b062ce70ab6086c)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_INRO

**Definition** adi\_max32\_clock.h:21

[ADI\_MAX32\_PRPH\_CLK\_SRC\_EBO](adi__max32__clock_8h.md#ada66413c52e2d3c1d166569fb9d52a84)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_EBO

**Definition** adi\_max32\_clock.h:25

[ADI\_MAX32\_PRPH\_CLK\_SRC\_ERTCO](adi__max32__clock_8h.md#ae22725273956cf339a7aa1ab99ec9d64)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_ERTCO

**Definition** adi\_max32\_clock.h:20

[ADI\_MAX32\_PRPH\_CLK\_SRC\_ERFO](adi__max32__clock_8h.md#af9ad74e5aff66314ef7ea4bcbd58a12f)

#define ADI\_MAX32\_PRPH\_CLK\_SRC\_ERFO

**Definition** adi\_max32\_clock.h:19

[ADI\_MAX32\_CLK\_EXTCLK\_FREQ](#a158271c4ced07ddeda9e677f7fd028c7)

#define ADI\_MAX32\_CLK\_EXTCLK\_FREQ

**Definition** adi\_max32\_clock\_control.h:51

[ADI\_MAX32\_CLK\_EBO\_FREQ](#a47709e72b60d70e0d07576b8787118e0)

#define ADI\_MAX32\_CLK\_EBO\_FREQ

**Definition** adi\_max32\_clock\_control.h:49

[ADI\_MAX32\_PCLK\_FREQ](#a4e3ca6232db9220b60f17d1dca74627f)

#define ADI\_MAX32\_PCLK\_FREQ

**Definition** adi\_max32\_clock\_control.h:97

[ADI\_MAX32\_CLK\_ERFO\_FREQ](#a56a549a210a78cb99f019f85fa15807b)

#define ADI\_MAX32\_CLK\_ERFO\_FREQ

**Definition** adi\_max32\_clock\_control.h:43

[ADI\_MAX32\_CLK\_ERTCO\_FREQ](#a664282617e29d44f951a48da1ac1ae9d)

#define ADI\_MAX32\_CLK\_ERTCO\_FREQ

**Definition** adi\_max32\_clock\_control.h:47

[ADI\_MAX32\_CLK\_IPLL\_FREQ](#aa58ed1a1d381f11cd6410797449b17ba)

#define ADI\_MAX32\_CLK\_IPLL\_FREQ

**Definition** adi\_max32\_clock\_control.h:48

[ADI\_MAX32\_CLK\_INRO\_FREQ](#abb3947e441021737ca566e89fd56cb0c)

#define ADI\_MAX32\_CLK\_INRO\_FREQ

**Definition** adi\_max32\_clock\_control.h:46

[ADI\_MAX32\_CLK\_ISO\_FREQ](#ace96ad0d7564ad0fe326992257686820)

#define ADI\_MAX32\_CLK\_ISO\_FREQ

**Definition** adi\_max32\_clock\_control.h:45

[ADI\_MAX32\_CLK\_IBRO\_FREQ](#ae5e0473609734b17bcdd2ce6f4e7a63a)

#define ADI\_MAX32\_CLK\_IBRO\_FREQ

**Definition** adi\_max32\_clock\_control.h:44

## [◆ ](#a4e3ca6232db9220b60f17d1dca74627f)ADI\_MAX32\_PCLK\_FREQ

| #define ADI\_MAX32\_PCLK\_FREQ   ([ADI\_MAX32\_SYSCLK\_FREQ](#ac82b515b2268a26b19b69972fc113e1c) / 2) |
| --- |

## [◆ ](#ac82b515b2268a26b19b69972fc113e1c)ADI\_MAX32\_SYSCLK\_FREQ

| #define ADI\_MAX32\_SYSCLK\_FREQ   ([ADI\_MAX32\_CLK\_IPO\_FREQ](#a31a7fbb2f0c1ce1f5b9899b49b6324ec) / [ADI\_MAX32\_SYSCLK\_PRESCALER](#a41eab4d492a019700d1e1d4714932cd9)) |
| --- |

## [◆ ](#a41eab4d492a019700d1e1d4714932cd9)ADI\_MAX32\_SYSCLK\_PRESCALER

| #define ADI\_MAX32\_SYSCLK\_PRESCALER   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(gcr), sysclk\_prescaler, 1) |
| --- |

Get prescaler value if it defined.

## [◆ ](#a21d5bba4fce8bf21105689ae8ea96216)ADI\_MAX32\_SYSCLK\_SRC

| #define ADI\_MAX32\_SYSCLK\_SRC   ADI\_MAX32\_CLK\_IPO |
| --- |

## [◆ ](#a1de5a43e10f129609662765dc2ebac24)DT\_GCR\_CLOCKS\_CTRL

| #define DT\_GCR\_CLOCKS\_CTRL   [DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(gcr)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [adi\_max32\_clock\_control.h](adi__max32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
