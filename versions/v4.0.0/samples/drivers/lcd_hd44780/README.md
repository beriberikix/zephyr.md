---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/lcd_hd44780/README.html
original_path: samples/drivers/lcd_hd44780/README.html
---

# HD44780 LCD controller

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/lcd_hd44780/README.rst/..)

## Overview

Display text strings on parallel interfacing HD44780 based
generic LCD controller using GPIO pins to interface with
Arduino Due (SAM3).

## Building and Running

This project can be built and executed on as follows:

```shell
west build -b arduino_due samples/drivers/lcd_hd44780
west flash
```

### Sample Output

```shell
LCD Init
Page 1: message
Page 2: message
Page 3: message
```

### Display output

```shell
********************
Arduino Due
yalpsiD DCL 4x02
********************
```

```shell
-------------------
Zephyr Rocks!
My super RTOS
-------------------
```

```shell
--------------------
--------HOME--------
I am home!
```

## See also

[GPIO Driver APIs](../../../doxygen/html/group__gpio__interface.md)
