---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/develop/manifest/external/libmpix.html
original_path: develop/manifest/external/libmpix.html
---

# libmpix

## Introduction

The [libmpix](https://github.com/libmpix/libmpix) [[1]](#id2) project provides a library for working with image data on microcontrollers.
It supports pixel format conversion, debayer, blur, sharpen, color correction, resizing and more.

It pipelines multiple operations together, eliminating intermediate buffers.
This allows larger image resolutions to fit in constrained systems without compromising performance.

## Features

- Simple zero-copy, pipelined engine with low runtime overhead
- Reduces memory overhead (for example processes 1 MB of data with only 5 kB of RAM)
- POSIX support (Linux/BSD/MacOS) and Zephyr support

## Usage with Zephyr

To pull in libmpix as a Zephyr module, either add it as a West project in the `west.yaml`
file or pull it in by adding a submanifest (e.g. `zephyr/submanifests/libmpix.yaml`) file
with the following content and run **west update**:

```yaml
manifest:
  projects:
    - name: libmpix
      url: https://github.com/libmpix/libmpix.git
      revision: main
      path: modules/lib/libmpix
```

Refer to the `libmpix` headers for API details. A brief example is shown below.

```c
#include <mpix/image.h>

struct mpix_image img;

mpix_image_from_buf(&img, buf_in, sizeof(buf_in), MPIX_FORMAT_RGB24);
mpix_image_kernel(&img, MPIX_KERNEL_DENOISE, 5);
mpix_image_kernel(&img, MPIX_KERNEL_SHARPEN, 3);
mpix_image_convert(&img, MPIX_FORMAT_YUYV);
mpix_image_to_buf(&img, buf_out, sizeof(buf_out));

return img.err;
```

## References

[[1](#id3)]

[https://github.com/libmpix/libmpix](https://github.com/libmpix/libmpix)
