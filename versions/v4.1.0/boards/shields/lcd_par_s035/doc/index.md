---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/lcd_par_s035/doc/index.html
original_path: boards/shields/lcd_par_s035/doc/index.html
---

# NXP LCD\_PAR\_S035 TFT LCD Module

## Overview

The LCD-PAR-S035 is a 3.5” 480x320 IPS TFT LCD module with wide viewing angle
and 5-point capacitive touch functionality. The LCD module can be controlled
through either SPI or parallel (8/16bit) 8080/6800.
More information about the shield can be found
at the [LCD-PAR-S035 product page](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/3-5-480x320-ips-tft-lcd-module:LCD-PAR-S035) [[1]](#id1).

## Requirements

This shield can only be used with FRDM-X evaluation kits with a parallel LCD
connector or a PMOD connector. Currently only the parallel LCD connector is
enabled.

## Programming

Set `--shield lcd_par_s035_8080` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 --shield lcd_par_s035_8080 samples/drivers/display
```

## References

[[1](#id2)]

[https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/3-5-480x320-ips-tft-lcd-module:LCD-PAR-S035](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/3-5-480x320-ips-tft-lcd-module:LCD-PAR-S035)
