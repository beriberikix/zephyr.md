---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/lcd_hd44780/README.html
original_path: samples/drivers/lcd_hd44780/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# HD44780 LCD controller

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
