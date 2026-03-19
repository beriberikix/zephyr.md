---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__devicetree-spi.html
original_path: doxygen/html/group__devicetree-spi.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree SPI API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_SPI\_HAS\_CS\_GPIOS](#gae8db0ce095bdd0066a845bc6a9bf329d)(spi) |
|  | Does a SPI controller node have chip select GPIOs configured? |
| #define | [DT\_SPI\_NUM\_CS\_GPIOS](#gafe2bddd961fe08672e131cfbd73eb466)(spi) |
|  | Number of chip select GPIOs in a SPI controller's cs-gpios property. |
| #define | [DT\_SPI\_DEV\_HAS\_CS\_GPIOS](#gad66b759d6aa4826f2c68a94e8708ad4f)(spi\_dev) |
|  | Does a SPI device have a chip select line configured? |
| #define | [DT\_SPI\_DEV\_CS\_GPIOS\_CTLR](#ga0eaad9de680b5ac7cd8950957560c199)(spi\_dev) |
|  | Get a SPI device's chip select GPIO controller's node identifier. |
| #define | [DT\_SPI\_DEV\_CS\_GPIOS\_PIN](#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)(spi\_dev) |
|  | Get a SPI device's chip select GPIO pin number. |
| #define | [DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS](#ga49fd9c174931b44584a7dbbc18f7c644)(spi\_dev) |
|  | Get a SPI device's chip select GPIO flags. |
| #define | [DT\_INST\_SPI\_DEV\_HAS\_CS\_GPIOS](#ga830f87f79c297c090a1929a288edc7ba)(inst) |
|  | Equivalent to [DT\_SPI\_DEV\_HAS\_CS\_GPIOS(DT\_DRV\_INST(inst))](#gad66b759d6aa4826f2c68a94e8708ad4f). |
| #define | [DT\_INST\_SPI\_DEV\_CS\_GPIOS\_CTLR](#ga0ffb7729cd90dc7bf4a1c33ead96a3d8)(inst) |
|  | Get GPIO controller node identifier for a SPI device instance This is equivalent to [DT\_SPI\_DEV\_CS\_GPIOS\_CTLR(DT\_DRV\_INST(inst))](#ga0eaad9de680b5ac7cd8950957560c199). |
| #define | [DT\_INST\_SPI\_DEV\_CS\_GPIOS\_PIN](#ga1ce1031b612257718fbab08139db44cf)(inst) |
|  | Equivalent to [DT\_SPI\_DEV\_CS\_GPIOS\_PIN(DT\_DRV\_INST(inst))](#ga8c1dd6a65c6f7fdf67291be1ed47fc9f). |
| #define | [DT\_INST\_SPI\_DEV\_CS\_GPIOS\_FLAGS](#ga6f42b7305ec5373ae14cad220a3196da)(inst) |
|  | [DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS(DT\_DRV\_INST(inst))](#ga49fd9c174931b44584a7dbbc18f7c644). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga0ffb7729cd90dc7bf4a1c33ead96a3d8)DT\_INST\_SPI\_DEV\_CS\_GPIOS\_CTLR

| #define DT\_INST\_SPI\_DEV\_CS\_GPIOS\_CTLR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_SPI\_DEV\_CS\_GPIOS\_CTLR](#ga0eaad9de680b5ac7cd8950957560c199)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

[DT\_SPI\_DEV\_CS\_GPIOS\_CTLR](#ga0eaad9de680b5ac7cd8950957560c199)

#define DT\_SPI\_DEV\_CS\_GPIOS\_CTLR(spi\_dev)

Get a SPI device's chip select GPIO controller's node identifier.

**Definition** spi.h:150

Get GPIO controller node identifier for a SPI device instance This is equivalent to [DT\_SPI\_DEV\_CS\_GPIOS\_CTLR(DT\_DRV\_INST(inst))](#ga0eaad9de680b5ac7cd8950957560c199).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   node identifier for instance's chip select GPIO controller

See also
:   [DT\_SPI\_DEV\_CS\_GPIOS\_CTLR()](#ga0eaad9de680b5ac7cd8950957560c199)

## [◆ ](#ga6f42b7305ec5373ae14cad220a3196da)DT\_INST\_SPI\_DEV\_CS\_GPIOS\_FLAGS

| #define DT\_INST\_SPI\_DEV\_CS\_GPIOS\_FLAGS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS](#ga49fd9c174931b44584a7dbbc18f7c644)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS](#ga49fd9c174931b44584a7dbbc18f7c644)

#define DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS(spi\_dev)

Get a SPI device's chip select GPIO flags.

**Definition** spi.h:211

[DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS(DT\_DRV\_INST(inst))](#ga49fd9c174931b44584a7dbbc18f7c644).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   flags value of the instance's chip select GPIO specifier, or zero if there is none

See also
:   [DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS()](#ga49fd9c174931b44584a7dbbc18f7c644)

## [◆ ](#ga1ce1031b612257718fbab08139db44cf)DT\_INST\_SPI\_DEV\_CS\_GPIOS\_PIN

| #define DT\_INST\_SPI\_DEV\_CS\_GPIOS\_PIN | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_SPI\_DEV\_CS\_GPIOS\_PIN](#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_SPI\_DEV\_CS\_GPIOS\_PIN](#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)

#define DT\_SPI\_DEV\_CS\_GPIOS\_PIN(spi\_dev)

Get a SPI device's chip select GPIO pin number.

**Definition** spi.h:183

Equivalent to [DT\_SPI\_DEV\_CS\_GPIOS\_PIN(DT\_DRV\_INST(inst))](#ga8c1dd6a65c6f7fdf67291be1ed47fc9f).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   pin number of the instance's chip select GPIO

See also
:   [DT\_SPI\_DEV\_CS\_GPIOS\_PIN()](#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)

## [◆ ](#ga830f87f79c297c090a1929a288edc7ba)DT\_INST\_SPI\_DEV\_HAS\_CS\_GPIOS

| #define DT\_INST\_SPI\_DEV\_HAS\_CS\_GPIOS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_SPI\_DEV\_HAS\_CS\_GPIOS](#gad66b759d6aa4826f2c68a94e8708ad4f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_SPI\_DEV\_HAS\_CS\_GPIOS](#gad66b759d6aa4826f2c68a94e8708ad4f)

#define DT\_SPI\_DEV\_HAS\_CS\_GPIOS(spi\_dev)

Does a SPI device have a chip select line configured?

**Definition** spi.h:117

Equivalent to [DT\_SPI\_DEV\_HAS\_CS\_GPIOS(DT\_DRV\_INST(inst))](#gad66b759d6aa4826f2c68a94e8708ad4f).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   1 if the instance's bus has a CS pin at index [DT\_INST\_REG\_ADDR(inst)](group__devicetree-inst.md#gafde8fa67b94ac959ba2e24b44b3386a7 "Get a DT_DRV_COMPAT's (only) register block address."), 0 otherwise

See also
:   [DT\_SPI\_DEV\_HAS\_CS\_GPIOS()](#gad66b759d6aa4826f2c68a94e8708ad4f)

## [◆ ](#ga0eaad9de680b5ac7cd8950957560c199)DT\_SPI\_DEV\_CS\_GPIOS\_CTLR

| #define DT\_SPI\_DEV\_CS\_GPIOS\_CTLR | ( |  | *spi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_GPIO\_CTLR\_BY\_IDX](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(spi\_dev), cs\_gpios, [DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(spi\_dev))

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3754

[DT\_GPIO\_CTLR\_BY\_IDX](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)

#define DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, idx)

Get the node identifier for the controller phandle from a gpio phandle-array property at an index.

**Definition** gpio.h:53

[DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)

#define DT\_REG\_ADDR\_RAW(node\_id)

Get a node's (only) register block raw address.

**Definition** devicetree.h:2400

Get a SPI device's chip select GPIO controller's node identifier.

Example devicetree fragment:

```
gpio1: gpio@... { ... };

gpio2: gpio@... { ... };

spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };

        b: spi-dev-b@1 {
                reg = <1>;
        };
};
```

Example usage:

```
DT_SPI_DEV_CS_GPIOS_CTLR(DT_NODELABEL(a)) // DT_NODELABEL(gpio1)
DT_SPI_DEV_CS_GPIOS_CTLR(DT_NODELABEL(b)) // DT_NODELABEL(gpio2)
```

Parameters
:   | spi\_dev | a SPI device node identifier |
    | --- | --- |

Returns
:   node identifier for spi\_dev's chip select GPIO controller

## [◆ ](#ga49fd9c174931b44584a7dbbc18f7c644)DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS

| #define DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS | ( |  | *spi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_GPIO\_FLAGS\_BY\_IDX](group__devicetree-gpio.md#ga672b2597b99194b8cbd42b3f3401d2b5)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(spi\_dev), cs\_gpios, [DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(spi\_dev))

[DT\_GPIO\_FLAGS\_BY\_IDX](group__devicetree-gpio.md#ga672b2597b99194b8cbd42b3f3401d2b5)

#define DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, idx)

Get a GPIO specifier's flags cell at an index.

**Definition** gpio.h:165

Get a SPI device's chip select GPIO flags.

Example devicetree fragment:

```
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };
};
```

Example usage:

```
DT_SPI_DEV_CS_GPIOS_FLAGS(DT_NODELABEL(a)) // GPIO_ACTIVE_LOW
```

If the GPIO specifier for spi\_dev's entry in its bus node's cs-gpios property has no flags cell, this expands to zero.

Parameters
:   | spi\_dev | a SPI device node identifier |
    | --- | --- |

Returns
:   flags value of spi\_dev's chip select GPIO specifier, or zero if there is none

## [◆ ](#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)DT\_SPI\_DEV\_CS\_GPIOS\_PIN

| #define DT\_SPI\_DEV\_CS\_GPIOS\_PIN | ( |  | *spi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_GPIO\_PIN\_BY\_IDX](group__devicetree-gpio.md#ga8f7d82567056266bab1603865f8b27af)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(spi\_dev), cs\_gpios, [DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(spi\_dev))

[DT\_GPIO\_PIN\_BY\_IDX](group__devicetree-gpio.md#ga8f7d82567056266bab1603865f8b27af)

#define DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, idx)

Get a GPIO specifier's pin cell at an index.

**Definition** gpio.h:109

Get a SPI device's chip select GPIO pin number.

It's an error if the GPIO specifier for spi\_dev's entry in its bus node's cs-gpios property has no pin cell.

Example devicetree fragment:

```
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };

        b: spi-dev-b@1 {
                reg = <1>;
        };
};
```

Example usage:

```
DT_SPI_DEV_CS_GPIOS_PIN(DT_NODELABEL(a)) // 10
DT_SPI_DEV_CS_GPIOS_PIN(DT_NODELABEL(b)) // 20
```

Parameters
:   | spi\_dev | a SPI device node identifier |
    | --- | --- |

Returns
:   pin number of spi\_dev's chip select GPIO

## [◆ ](#gad66b759d6aa4826f2c68a94e8708ad4f)DT\_SPI\_DEV\_HAS\_CS\_GPIOS

| #define DT\_SPI\_DEV\_HAS\_CS\_GPIOS | ( |  | *spi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_SPI\_HAS\_CS\_GPIOS](#gae8db0ce095bdd0066a845bc6a9bf329d)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(spi\_dev))

[DT\_SPI\_HAS\_CS\_GPIOS](#gae8db0ce095bdd0066a845bc6a9bf329d)

#define DT\_SPI\_HAS\_CS\_GPIOS(spi)

Does a SPI controller node have chip select GPIOs configured?

**Definition** spi.h:52

Does a SPI device have a chip select line configured?

Example devicetree fragment:

```
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };

        b: spi-dev-b@1 {
                reg = <1>;
        };
};

spi2: spi@... {
        compatible = "vnd,spi";
        c: spi-dev-c@0 {
                reg = <0>;
        };
};
```

Example usage:

```
DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(a)) // 1
DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(b)) // 1
DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(c)) // 0
```

Parameters
:   | spi\_dev | a SPI device node identifier |
    | --- | --- |

Returns
:   1 if spi\_dev's bus node [DT\_BUS(spi\_dev)](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc "Node's bus controller.") has a chip select pin at index [DT\_REG\_ADDR(spi\_dev)](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e "Get a node's (only) register block address."), 0 otherwise

## [◆ ](#gae8db0ce095bdd0066a845bc6a9bf329d)DT\_SPI\_HAS\_CS\_GPIOS

| #define DT\_SPI\_HAS\_CS\_GPIOS | ( |  | *spi* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(spi, cs\_gpios)

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3677

Does a SPI controller node have chip select GPIOs configured?

SPI bus controllers use the "cs-gpios" property for configuring chip select GPIOs. Its value is a phandle-array which specifies the chip select lines.

Example devicetree fragment:

```
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;
};

spi2: spi@... {
        compatible = "vnd,spi";
};
```

Example usage:

```
DT_SPI_HAS_CS_GPIOS(DT_NODELABEL(spi1)) // 1
DT_SPI_HAS_CS_GPIOS(DT_NODELABEL(spi2)) // 0
```

Parameters
:   | spi | a SPI bus controller node identifier |
    | --- | --- |

Returns
:   1 if "spi" has a cs-gpios property, 0 otherwise

## [◆ ](#gafe2bddd961fe08672e131cfbd73eb466)DT\_SPI\_NUM\_CS\_GPIOS

| #define DT\_SPI\_NUM\_CS\_GPIOS | ( |  | *spi* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](devicetree_2spi_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_SPI\_HAS\_CS\_GPIOS](#gae8db0ce095bdd0066a845bc6a9bf329d)(spi), \

([DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)(spi, cs\_gpios)), (0))

[DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)

#define DT\_PROP\_LEN(node\_id, prop)

Get a property's logical length.

**Definition** devicetree.h:779

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

Number of chip select GPIOs in a SPI controller's cs-gpios property.

Example devicetree fragment:

```
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;
};

spi2: spi@... {
        compatible = "vnd,spi";
};
```

Example usage:

```
DT_SPI_NUM_CS_GPIOS(DT_NODELABEL(spi1)) // 2
DT_SPI_NUM_CS_GPIOS(DT_NODELABEL(spi2)) // 0
```

Parameters
:   | spi | a SPI bus controller node identifier |
    | --- | --- |

Returns
:   Logical length of spi's cs-gpios property, or 0 if "spi" doesn't have a cs-gpios property

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
