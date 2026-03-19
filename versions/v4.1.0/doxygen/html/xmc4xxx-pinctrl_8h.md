---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xmc4xxx-pinctrl_8h.html
original_path: doxygen/html/xmc4xxx-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xmc4xxx-pinctrl.h File Reference

[Go to the source code of this file.](xmc4xxx-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [XMC4XXX\_PORT\_POS](#aab30618ebe31012b3bf6a72d55f9335c)   0 |
| #define | [XMC4XXX\_PORT\_MASK](#a99aa017fa346da406fca137d0c42c1e4)   0xf |
| #define | [XMC4XXX\_PIN\_POS](#a511179d787ebfbb7f37a92326d4a8984)   4 |
| #define | [XMC4XXX\_PIN\_MASK](#a693fe19f7d6073121d89c4bd6dbff99b)   0xf |
| #define | [XMC4XXX\_ALT\_POS](#a532151552d5ea717d093deb4c9c9d233)   8 |
| #define | [XMC4XXX\_ALT\_MASK](#aba9bea82a961c304cb90a7c24527d531)   0xf |
| #define | [XMC4XXX\_PULL\_DOWN\_POS](#ac6ec7a70bdaae2909baea4f179327871)   12 |
| #define | [XMC4XXX\_PULL\_DOWN\_MASK](#ac202c2ad9b97865b1d7f9d282c9a7d10)   0x1 |
| #define | [XMC4XXX\_PULL\_UP\_POS](#a87e81f7624a28d5fea5ad3a2074329a0)   13 |
| #define | [XMC4XXX\_PULL\_UP\_MASK](#ac165407103a525da4919fee7c4dc22c9)   0x1 |
| #define | [XMC4XXX\_PUSH\_PULL\_POS](#a9f50c28d310a0cc771b979e731c05060)   14 |
| #define | [XMC4XXX\_PUSH\_PULL\_MASK](#a308fe5c756b2058b2eec25d9e95d439a)   0x1 |
| #define | [XMC4XXX\_OPEN\_DRAIN\_POS](#ad8da22497d5f36d3cd56477506eca3b5)   15 |
| #define | [XMC4XXX\_OPEN\_DRAIN\_MASK](#a4dbdbb0b4fe95db634c55b7840a08a47)   0x1 |
| #define | [XMC4XXX\_OUT\_HIGH\_POS](#ada9fafd51a6d8e7e6b4f2b05bf2d3dd0)   16 |
| #define | [XMC4XXX\_OUT\_HIGH\_MASK](#a58396a809d6950afd8b5cc6fd4193589)   0x1 |
| #define | [XMC4XXX\_OUT\_LOW\_POS](#abbac18ae6e6d52b33db5b352ca323e11)   17 |
| #define | [XMC4XXX\_OUT\_LOW\_MASK](#af8c9d1c2e5664ff59538c08b4ed8fa8b)   0x1 |
| #define | [XMC4XXX\_INV\_INPUT\_POS](#a2da9db848ad0c85751747df0f3948f97)   18 |
| #define | [XMC4XXX\_INV\_INPUT\_MASK](#aab423e91fbddbe908d9393447ff943f0)   0x1 |
| #define | [XMC4XXX\_DRIVE\_POS](#ac8284e39124ff71b5335e46e56fb8000)   19 |
| #define | [XMC4XXX\_DRIVE\_MASK](#aa6829bced6bf9f7908e31fb3c9205f93)   0x7 |
| #define | [XMC4XXX\_HWCTRL\_POS](#a80e80262f3abb20055891211ee43201a)   22 |
| #define | [XMC4XXX\_HWCTRL\_MASK](#a0fc560c059b8fabf8e811e81783f5e2a)   0x3 |
| #define | [XMC4XXX\_PINMUX\_SET](#a30211ecff4f4b6b3f02386ae55d1cb8d)(port, pin, alt\_fun) |
| #define | [XMC4XXX\_PINMUX\_GET\_PORT](#ae0748e6dbb9ca36ad0ab40e3a53daea2)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_PIN](#a3d889d7f75a6b88b252cb13f3004ea6a)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_ALT](#afdad7ccafbdee5a2b1d512f0e280abfe)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_PULL\_DOWN](#a56ebba3de971f70ad47005cf0a5246c1)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_PULL\_UP](#ac28a73b740da97d7d0008ab0af577a92)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_PUSH\_PULL](#a376e85562e0dc5a1ea2c9f3b8eaeeb9e)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_OPEN\_DRAIN](#a57626f3b88704a87ed5f9bfba44c8daf)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_OUT\_HIGH](#a1de2bc4e89167d9a0399edf63078d928)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_OUT\_LOW](#abbeef6122d273c9f074fb1cc5456febf)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_INV\_INPUT](#a43ce0d809351bef0989f0330073f9453)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_DRIVE](#a11bd50351e3aabed088cc4158474edc3)(mx) |
| #define | [XMC4XXX\_PINMUX\_GET\_HWCTRL](#a33694b664b4212d95cc18659173675c0)(mx) |

## Macro Definition Documentation

## [◆ ](#aba9bea82a961c304cb90a7c24527d531)XMC4XXX\_ALT\_MASK

| #define XMC4XXX\_ALT\_MASK   0xf |
| --- |

## [◆ ](#a532151552d5ea717d093deb4c9c9d233)XMC4XXX\_ALT\_POS

| #define XMC4XXX\_ALT\_POS   8 |
| --- |

## [◆ ](#aa6829bced6bf9f7908e31fb3c9205f93)XMC4XXX\_DRIVE\_MASK

| #define XMC4XXX\_DRIVE\_MASK   0x7 |
| --- |

## [◆ ](#ac8284e39124ff71b5335e46e56fb8000)XMC4XXX\_DRIVE\_POS

| #define XMC4XXX\_DRIVE\_POS   19 |
| --- |

## [◆ ](#a0fc560c059b8fabf8e811e81783f5e2a)XMC4XXX\_HWCTRL\_MASK

| #define XMC4XXX\_HWCTRL\_MASK   0x3 |
| --- |

## [◆ ](#a80e80262f3abb20055891211ee43201a)XMC4XXX\_HWCTRL\_POS

| #define XMC4XXX\_HWCTRL\_POS   22 |
| --- |

## [◆ ](#aab423e91fbddbe908d9393447ff943f0)XMC4XXX\_INV\_INPUT\_MASK

| #define XMC4XXX\_INV\_INPUT\_MASK   0x1 |
| --- |

## [◆ ](#a2da9db848ad0c85751747df0f3948f97)XMC4XXX\_INV\_INPUT\_POS

| #define XMC4XXX\_INV\_INPUT\_POS   18 |
| --- |

## [◆ ](#a4dbdbb0b4fe95db634c55b7840a08a47)XMC4XXX\_OPEN\_DRAIN\_MASK

| #define XMC4XXX\_OPEN\_DRAIN\_MASK   0x1 |
| --- |

## [◆ ](#ad8da22497d5f36d3cd56477506eca3b5)XMC4XXX\_OPEN\_DRAIN\_POS

| #define XMC4XXX\_OPEN\_DRAIN\_POS   15 |
| --- |

## [◆ ](#a58396a809d6950afd8b5cc6fd4193589)XMC4XXX\_OUT\_HIGH\_MASK

| #define XMC4XXX\_OUT\_HIGH\_MASK   0x1 |
| --- |

## [◆ ](#ada9fafd51a6d8e7e6b4f2b05bf2d3dd0)XMC4XXX\_OUT\_HIGH\_POS

| #define XMC4XXX\_OUT\_HIGH\_POS   16 |
| --- |

## [◆ ](#af8c9d1c2e5664ff59538c08b4ed8fa8b)XMC4XXX\_OUT\_LOW\_MASK

| #define XMC4XXX\_OUT\_LOW\_MASK   0x1 |
| --- |

## [◆ ](#abbac18ae6e6d52b33db5b352ca323e11)XMC4XXX\_OUT\_LOW\_POS

| #define XMC4XXX\_OUT\_LOW\_POS   17 |
| --- |

## [◆ ](#a693fe19f7d6073121d89c4bd6dbff99b)XMC4XXX\_PIN\_MASK

| #define XMC4XXX\_PIN\_MASK   0xf |
| --- |

## [◆ ](#a511179d787ebfbb7f37a92326d4a8984)XMC4XXX\_PIN\_POS

| #define XMC4XXX\_PIN\_POS   4 |
| --- |

## [◆ ](#afdad7ccafbdee5a2b1d512f0e280abfe)XMC4XXX\_PINMUX\_GET\_ALT

| #define XMC4XXX\_PINMUX\_GET\_ALT | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_ALT\_POS](#a532151552d5ea717d093deb4c9c9d233)) & [XMC4XXX\_ALT\_MASK](#aba9bea82a961c304cb90a7c24527d531))

[XMC4XXX\_ALT\_POS](#a532151552d5ea717d093deb4c9c9d233)

#define XMC4XXX\_ALT\_POS

**Definition** xmc4xxx-pinctrl.h:18

[XMC4XXX\_ALT\_MASK](#aba9bea82a961c304cb90a7c24527d531)

#define XMC4XXX\_ALT\_MASK

**Definition** xmc4xxx-pinctrl.h:19

## [◆ ](#a11bd50351e3aabed088cc4158474edc3)XMC4XXX\_PINMUX\_GET\_DRIVE

| #define XMC4XXX\_PINMUX\_GET\_DRIVE | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_DRIVE\_POS](#ac8284e39124ff71b5335e46e56fb8000)) & [XMC4XXX\_DRIVE\_MASK](#aa6829bced6bf9f7908e31fb3c9205f93))

[XMC4XXX\_DRIVE\_MASK](#aa6829bced6bf9f7908e31fb3c9205f93)

#define XMC4XXX\_DRIVE\_MASK

**Definition** xmc4xxx-pinctrl.h:43

[XMC4XXX\_DRIVE\_POS](#ac8284e39124ff71b5335e46e56fb8000)

#define XMC4XXX\_DRIVE\_POS

**Definition** xmc4xxx-pinctrl.h:42

## [◆ ](#a33694b664b4212d95cc18659173675c0)XMC4XXX\_PINMUX\_GET\_HWCTRL

| #define XMC4XXX\_PINMUX\_GET\_HWCTRL | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_HWCTRL\_POS](#a80e80262f3abb20055891211ee43201a)) & [XMC4XXX\_HWCTRL\_MASK](#a0fc560c059b8fabf8e811e81783f5e2a))

[XMC4XXX\_HWCTRL\_MASK](#a0fc560c059b8fabf8e811e81783f5e2a)

#define XMC4XXX\_HWCTRL\_MASK

**Definition** xmc4xxx-pinctrl.h:46

[XMC4XXX\_HWCTRL\_POS](#a80e80262f3abb20055891211ee43201a)

#define XMC4XXX\_HWCTRL\_POS

**Definition** xmc4xxx-pinctrl.h:45

## [◆ ](#a43ce0d809351bef0989f0330073f9453)XMC4XXX\_PINMUX\_GET\_INV\_INPUT

| #define XMC4XXX\_PINMUX\_GET\_INV\_INPUT | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_INV\_INPUT\_POS](#a2da9db848ad0c85751747df0f3948f97)) & [XMC4XXX\_INV\_INPUT\_MASK](#aab423e91fbddbe908d9393447ff943f0))

[XMC4XXX\_INV\_INPUT\_POS](#a2da9db848ad0c85751747df0f3948f97)

#define XMC4XXX\_INV\_INPUT\_POS

**Definition** xmc4xxx-pinctrl.h:39

[XMC4XXX\_INV\_INPUT\_MASK](#aab423e91fbddbe908d9393447ff943f0)

#define XMC4XXX\_INV\_INPUT\_MASK

**Definition** xmc4xxx-pinctrl.h:40

## [◆ ](#a57626f3b88704a87ed5f9bfba44c8daf)XMC4XXX\_PINMUX\_GET\_OPEN\_DRAIN

| #define XMC4XXX\_PINMUX\_GET\_OPEN\_DRAIN | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_OPEN\_DRAIN\_POS](#ad8da22497d5f36d3cd56477506eca3b5)) & [XMC4XXX\_OPEN\_DRAIN\_MASK](#a4dbdbb0b4fe95db634c55b7840a08a47))

[XMC4XXX\_OPEN\_DRAIN\_MASK](#a4dbdbb0b4fe95db634c55b7840a08a47)

#define XMC4XXX\_OPEN\_DRAIN\_MASK

**Definition** xmc4xxx-pinctrl.h:31

[XMC4XXX\_OPEN\_DRAIN\_POS](#ad8da22497d5f36d3cd56477506eca3b5)

#define XMC4XXX\_OPEN\_DRAIN\_POS

**Definition** xmc4xxx-pinctrl.h:30

## [◆ ](#a1de2bc4e89167d9a0399edf63078d928)XMC4XXX\_PINMUX\_GET\_OUT\_HIGH

| #define XMC4XXX\_PINMUX\_GET\_OUT\_HIGH | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_OUT\_HIGH\_POS](#ada9fafd51a6d8e7e6b4f2b05bf2d3dd0)) & [XMC4XXX\_OUT\_HIGH\_MASK](#a58396a809d6950afd8b5cc6fd4193589))

[XMC4XXX\_OUT\_HIGH\_MASK](#a58396a809d6950afd8b5cc6fd4193589)

#define XMC4XXX\_OUT\_HIGH\_MASK

**Definition** xmc4xxx-pinctrl.h:34

[XMC4XXX\_OUT\_HIGH\_POS](#ada9fafd51a6d8e7e6b4f2b05bf2d3dd0)

#define XMC4XXX\_OUT\_HIGH\_POS

**Definition** xmc4xxx-pinctrl.h:33

## [◆ ](#abbeef6122d273c9f074fb1cc5456febf)XMC4XXX\_PINMUX\_GET\_OUT\_LOW

| #define XMC4XXX\_PINMUX\_GET\_OUT\_LOW | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_OUT\_LOW\_POS](#abbac18ae6e6d52b33db5b352ca323e11)) & [XMC4XXX\_OUT\_LOW\_MASK](#af8c9d1c2e5664ff59538c08b4ed8fa8b))

[XMC4XXX\_OUT\_LOW\_POS](#abbac18ae6e6d52b33db5b352ca323e11)

#define XMC4XXX\_OUT\_LOW\_POS

**Definition** xmc4xxx-pinctrl.h:36

[XMC4XXX\_OUT\_LOW\_MASK](#af8c9d1c2e5664ff59538c08b4ed8fa8b)

#define XMC4XXX\_OUT\_LOW\_MASK

**Definition** xmc4xxx-pinctrl.h:37

## [◆ ](#a3d889d7f75a6b88b252cb13f3004ea6a)XMC4XXX\_PINMUX\_GET\_PIN

| #define XMC4XXX\_PINMUX\_GET\_PIN | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_PIN\_POS](#a511179d787ebfbb7f37a92326d4a8984)) & [XMC4XXX\_PIN\_MASK](#a693fe19f7d6073121d89c4bd6dbff99b))

[XMC4XXX\_PIN\_POS](#a511179d787ebfbb7f37a92326d4a8984)

#define XMC4XXX\_PIN\_POS

**Definition** xmc4xxx-pinctrl.h:15

[XMC4XXX\_PIN\_MASK](#a693fe19f7d6073121d89c4bd6dbff99b)

#define XMC4XXX\_PIN\_MASK

**Definition** xmc4xxx-pinctrl.h:16

## [◆ ](#ae0748e6dbb9ca36ad0ab40e3a53daea2)XMC4XXX\_PINMUX\_GET\_PORT

| #define XMC4XXX\_PINMUX\_GET\_PORT | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_PORT\_POS](#aab30618ebe31012b3bf6a72d55f9335c)) & [XMC4XXX\_PORT\_MASK](#a99aa017fa346da406fca137d0c42c1e4))

[XMC4XXX\_PORT\_MASK](#a99aa017fa346da406fca137d0c42c1e4)

#define XMC4XXX\_PORT\_MASK

**Definition** xmc4xxx-pinctrl.h:13

[XMC4XXX\_PORT\_POS](#aab30618ebe31012b3bf6a72d55f9335c)

#define XMC4XXX\_PORT\_POS

**Definition** xmc4xxx-pinctrl.h:12

## [◆ ](#a56ebba3de971f70ad47005cf0a5246c1)XMC4XXX\_PINMUX\_GET\_PULL\_DOWN

| #define XMC4XXX\_PINMUX\_GET\_PULL\_DOWN | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_PULL\_DOWN\_POS](#ac6ec7a70bdaae2909baea4f179327871)) & [XMC4XXX\_PULL\_DOWN\_MASK](#ac202c2ad9b97865b1d7f9d282c9a7d10))

[XMC4XXX\_PULL\_DOWN\_MASK](#ac202c2ad9b97865b1d7f9d282c9a7d10)

#define XMC4XXX\_PULL\_DOWN\_MASK

**Definition** xmc4xxx-pinctrl.h:22

[XMC4XXX\_PULL\_DOWN\_POS](#ac6ec7a70bdaae2909baea4f179327871)

#define XMC4XXX\_PULL\_DOWN\_POS

**Definition** xmc4xxx-pinctrl.h:21

## [◆ ](#ac28a73b740da97d7d0008ab0af577a92)XMC4XXX\_PINMUX\_GET\_PULL\_UP

| #define XMC4XXX\_PINMUX\_GET\_PULL\_UP | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_PULL\_UP\_POS](#a87e81f7624a28d5fea5ad3a2074329a0)) & [XMC4XXX\_PULL\_UP\_MASK](#ac165407103a525da4919fee7c4dc22c9))

[XMC4XXX\_PULL\_UP\_POS](#a87e81f7624a28d5fea5ad3a2074329a0)

#define XMC4XXX\_PULL\_UP\_POS

**Definition** xmc4xxx-pinctrl.h:24

[XMC4XXX\_PULL\_UP\_MASK](#ac165407103a525da4919fee7c4dc22c9)

#define XMC4XXX\_PULL\_UP\_MASK

**Definition** xmc4xxx-pinctrl.h:25

## [◆ ](#a376e85562e0dc5a1ea2c9f3b8eaeeb9e)XMC4XXX\_PINMUX\_GET\_PUSH\_PULL

| #define XMC4XXX\_PINMUX\_GET\_PUSH\_PULL | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_PUSH\_PULL\_POS](#a9f50c28d310a0cc771b979e731c05060)) & [XMC4XXX\_PUSH\_PULL\_MASK](#a308fe5c756b2058b2eec25d9e95d439a))

[XMC4XXX\_PUSH\_PULL\_MASK](#a308fe5c756b2058b2eec25d9e95d439a)

#define XMC4XXX\_PUSH\_PULL\_MASK

**Definition** xmc4xxx-pinctrl.h:28

[XMC4XXX\_PUSH\_PULL\_POS](#a9f50c28d310a0cc771b979e731c05060)

#define XMC4XXX\_PUSH\_PULL\_POS

**Definition** xmc4xxx-pinctrl.h:27

## [◆ ](#a30211ecff4f4b6b3f02386ae55d1cb8d)XMC4XXX\_PINMUX\_SET

| #define XMC4XXX\_PINMUX\_SET | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *alt\_fun* ) |

**Value:**

((port) << [XMC4XXX\_PORT\_POS](#aab30618ebe31012b3bf6a72d55f9335c) | (pin) << [XMC4XXX\_PIN\_POS](#a511179d787ebfbb7f37a92326d4a8984) | (alt\_fun) << [XMC4XXX\_ALT\_POS](#a532151552d5ea717d093deb4c9c9d233))

## [◆ ](#a99aa017fa346da406fca137d0c42c1e4)XMC4XXX\_PORT\_MASK

| #define XMC4XXX\_PORT\_MASK   0xf |
| --- |

## [◆ ](#aab30618ebe31012b3bf6a72d55f9335c)XMC4XXX\_PORT\_POS

| #define XMC4XXX\_PORT\_POS   0 |
| --- |

## [◆ ](#ac202c2ad9b97865b1d7f9d282c9a7d10)XMC4XXX\_PULL\_DOWN\_MASK

| #define XMC4XXX\_PULL\_DOWN\_MASK   0x1 |
| --- |

## [◆ ](#ac6ec7a70bdaae2909baea4f179327871)XMC4XXX\_PULL\_DOWN\_POS

| #define XMC4XXX\_PULL\_DOWN\_POS   12 |
| --- |

## [◆ ](#ac165407103a525da4919fee7c4dc22c9)XMC4XXX\_PULL\_UP\_MASK

| #define XMC4XXX\_PULL\_UP\_MASK   0x1 |
| --- |

## [◆ ](#a87e81f7624a28d5fea5ad3a2074329a0)XMC4XXX\_PULL\_UP\_POS

| #define XMC4XXX\_PULL\_UP\_POS   13 |
| --- |

## [◆ ](#a308fe5c756b2058b2eec25d9e95d439a)XMC4XXX\_PUSH\_PULL\_MASK

| #define XMC4XXX\_PUSH\_PULL\_MASK   0x1 |
| --- |

## [◆ ](#a9f50c28d310a0cc771b979e731c05060)XMC4XXX\_PUSH\_PULL\_POS

| #define XMC4XXX\_PUSH\_PULL\_POS   14 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [xmc4xxx-pinctrl.h](xmc4xxx-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
