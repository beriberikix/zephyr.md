---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/qdec/README.html
original_path: samples/sensor/qdec/README.html
---

# Quadrature Decoder Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/qdec/README.rst/..)

## Overview

This sample reads the value of the counter which has been configured in
quadrature decoder mode.

It requires:

- an external mechanical encoder
- pin to be properly configured in the device tree

## Building and Running

In order to run this sample you need to:

- enable the quadrature decoder device in your board’s DT file or board overlay
- add a new alias property named `qdec0` and make it point to the decoder
  device you just enabled

For example, here’s how the overlay file of an STM32F401 board looks like when
using decoder from TIM3 through pins PA6 and PA7:

```dts
/ {
    aliases {
        qdec0 = &qdec;
    };
};

&timers3 {
    status = "okay";

    qdec: qdec {
        status = "okay";
        pinctrl-0 = <&tim3_ch1_pa6 &tim3_ch2_pa7>;
        pinctrl-names = "default";
        st,input-polarity-inverted;
        st,input-filter-level = <FDIV32_N8>;
        st,counts-per-revolution = <16>;
    };
};
```

### Sample Output

Once the MCU is started it prints the counter value every second on the
console

```shell
Quadrature decoder sensor test
Position = 0 degrees
Position = 15 degrees
Position = 30 degrees
...
```

Of course the read value changes once the user manually rotates the mechanical
encoder.

Note

The reported increment/decrement can be larger/smaller than the one shown
in the above example. This depends on the mechanical encoder being used and
`st,counts-per-revolution` value.

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
