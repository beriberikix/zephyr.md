---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/g1120b0mipi/doc/index.html
original_path: boards/shields/g1120b0mipi/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# G1120B0MIPI MIPI Display

## Overview

The G1120B0MIPI is a 1.2 inch circular AMOLED display, 390x390 pixels, with a
1-lane MIPI interface. This display connects to the i.MX RT595 Evaluation Kit.

More information about the shield can be found
at the [G1120B0MIPI product page](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/1-2-wearable-display-g1120b0mipi:G1120B0MIPI) [[1]](#id1).

This display uses a 40 pin FPC interface, which is available on many
NXP EVKs.

### Pins Assignment of the G1120B0MIPI MIPI Display

| FPC Connector Pin | Function |
| --- | --- |
| 1 | LED backlight cathode |
| 21 | Controller reset |
| 22 | Controller LPTE |
| 26 | Touch ctrl I2C SDA |
| 27 | Touch ctrl I2C SCL |
| 28 | Touch ctrl reset |
| 29 | Touch ctrl interrupt |
| 32 | LCD power enable |
| 34 | Backlight power enable |

## Requirements

This shield can only be used with a board which provides a configuration
for the 40 pin FPC interface

## Programming

Set `-DSHIELD=g1120b0mipi` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b mimxrt595_evk_cm33 samples/drivers/display -- -DSHIELD=g1120b0mipi
```

## References

[[1](#id2)]

[https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/1-2-wearable-display-g1120b0mipi:G1120B0MIPI](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/1-2-wearable-display-g1120b0mipi:G1120B0MIPI)
