---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/dsp/index.html
original_path: services/dsp/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Digital Signal Processing (DSP)

The DSP API provides an architecture agnostic way for signal processing.
Currently, the API will work on any architecture but will likely not be
optimized. The status of the various architectures can be found below:

| Architecture | Status |
| --- | --- |
| ARC | Optimized |
| ARM | Optimized |
| ARM64 | Optimized |
| MIPS | Unoptimized |
| NIOS2 | Unoptimized |
| POSIX | Unoptimized |
| RISCV | Unoptimized |
| RISCV64 | Unoptimized |
| SPARC | Unoptimized |
| X86 | Unoptimized |
| XTENSA | Unoptimized |

## [Using zDSP](#id1)

zDSP provides various backend options which are selected automatically for the
application. By default, including the CMSIS module will enable all
architectures to use the zDSP APIs. This can be done by setting:

```text
CONFIG_CMSIS_DSP=y
```

If your application requires some additional customization, it’s possible to
enable [`CONFIG_DSP_BACKEND_CUSTOM`](../../kconfig.md#CONFIG_DSP_BACKEND_CUSTOM "CONFIG_DSP_BACKEND_CUSTOM") which means that the
application is responsible for providing the implementation of the zDSP
library.

## [Optimizing for your architecture](#id2)

If your architecture is showing as `Unoptimized`, it’s possible to add a new
zDSP backend to better support it. To do that, a new Kconfig option should be
added to `subsys/dsp/Kconfig` along with the required dependencies and the
`default` set for `DSP_BACKEND` Kconfig choice.

Next, the implementation should be added at `subsys/dsp/<backend>/` and
linked in at `subsys/dsp/CMakeLists.txt`. To add architecture-specific attributes,
its corresponding Kconfig option should be added to `subsys/dsp/Kconfig` and use
them to update `DSP_DATA` and `DSP_STATIC_DATA` in `include/zephyr/dsp/dsp.h`.

## [API Reference](#id3)

*group* math\_dsp
:   DSP Interface.

    Typedefs

    typedef int8\_t q7\_t
    :   8-bit fractional data type in 1.7 format.

    typedef int16\_t q15\_t
    :   16-bit fractional data type in 1.15 format.

    typedef int32\_t q31\_t
    :   32-bit fractional data type in 1.31 format.

    typedef int64\_t q63\_t
    :   64-bit fractional data type in 1.63 format.

    typedef \_\_fp16 float16\_t
    :   16-bit floating point type definition.

    typedef float float32\_t
    :   32-bit floating-point type definition.

    typedef double float64\_t
    :   64-bit floating-point type definition.
