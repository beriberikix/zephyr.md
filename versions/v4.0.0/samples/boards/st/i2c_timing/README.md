---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/st/i2c_timing/README.html
original_path: samples/boards/st/i2c_timing/README.html
---

# I2C V2 timings

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/i2c_timing/README.rst/..)

## Overview

This sample simply demonstrate the **get\_config** API of the stm32 I2C driver.
The I2C peripheral configuration is checked regarding the I2C bitrate which can be:

> - <I2C\_BITRATE\_FAST\_STANDARD>
> - <I2C\_BITRATE\_FAST>
> - <I2C\_BITRATE\_FAST\_PLUS>

In case of the I2C V2, the I2C peripheral of the STM32 microcontrollers have
a TIMING register to write in order to generate the correct I2C clock signal.
This value depends on the peripheral clock input and the I2C speed.
The calculation of that TIMING value can be given by the [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html) application
**or** by the present sample.

Because the code sequence to calculate the I2C V2 TIMING value is heavy,
it is not advised to enable it in production binary.
By enabling CONFIG\_I2C\_STM32\_V2\_TIMING flag, this sample allows to
retrieve timing register configuration for the defined `clock-frequency`.
User can then configure timing in his application by adapting the following dts
snippet with the output of this sample:

> ```c
> &i2c {
>     timings = <160000000 I2C_BITRATE_STANDARD  0xB0C03E40>,
>                 <160000000 I2C_BITRATE_FAST  0xC041090F>,
>                 <160000000 I2C_BITRATE_FAST_PLUS  0x6021050A>;
> }
> ```

## Building and Running

In order to run this sample, make sure to

- enable `i2c` node in your board DT file.
- enable the CONFIG\_I2C\_STM32\_V2\_TIMING=y in the board **conf** file
- alias the **i2c-0** to your `i2c` node of the board **overlay** file

> ```shell
> west build -b b_u585i_iot02a samples/boards/st/i2c_timing
> ```

### Sample Output

When setting the b\_u585i\_iot02a.overlay to

> ```c
> / {
>     aliases {
>      i2c-0 = &i2c2;
>   };
> };
> &i2c2 {
>     /delete-property/ clock-frequency;
>     clock-frequency = <I2C_BITRATE_FAST>;
> };
> ```

The sample gives the corresponding TIMING value to report to the Device Tree:

```shell
I2C timing value, report to the DTS :
timings = <160000000 I2C_BITRATE_FAST  0xC041090F>;

I2C config : I2C_BITRATE_FAST
```

## See also

[I2C Interface](../../../../doxygen/html/group__i2c__interface.md)
