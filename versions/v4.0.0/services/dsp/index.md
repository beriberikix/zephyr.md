---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/dsp/index.html
original_path: services/dsp/index.html
---

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

[DSP Interface](../../doxygen/html/group__math__dsp.md)
