---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/console.html
original_path: services/console.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Console

Related code samples

[Console echo](../samples/subsys/console/echo/README.md#console_echo "Echo an input character back to the output using the Console API.")
:   Echo an input character back to the output using the Console API.

*group* Console API
:   Console API.

    Functions

    int console\_init(void)
    :   Initialize console device.

        This function should be called once to initialize pull-style access to console via [console\_getchar()](#group__console__api_1ga2ba36eb1081cd0b98aa43216ccd6fbd5) function and buffered output using [console\_putchar()](#group__console__api_1ga7bd842f1cda6c8218cb1d41420e4de49) function. This function supersedes, and incompatible with, callback (push-style) console handling (via console\_input\_fn callback, etc.).

        Returns:
        :   0 on success, error code (<0) otherwise

    ssize\_t console\_read(void \*dummy, void \*buf, size\_t size)
    :   Read data from console.

        Parameters:
        :   - **Functions** (Dummy L2/driver Support) – ignored, present to follow read() prototype
            - **buf** – buffer to read data to
            - **size** – maximum number of bytes to read

        Returns:
        :   >0, number of actually read bytes (can be less than size param) =0, in case of EOF <0, in case of error (e.g. -EAGAIN if timeout expired). errno variable is also set.

    ssize\_t console\_write(void \*dummy, const void \*buf, size\_t size)
    :   Write data to console.

        Parameters:
        :   - **Functions** (Dummy L2/driver Support) – ignored, present to follow write() prototype
            - **buf** – buffer to write data to
            - **size** – maximum number of bytes to write

        Returns:
        :   =>0, number of actually written bytes (can be less than size param) <0, in case of error (e.g. -EAGAIN if timeout expired). errno variable is also set.

    int console\_getchar(void)
    :   Get next char from console input buffer.

        Return next input character from console. If no characters available, this function will block. This function is similar to ANSI C getchar() function and is intended to ease porting of existing software. Before this function can be used, [console\_init()](#group__console__api_1ga0bf949437e32d17992435003cf8b46b5) should be called once. This function is incompatible with native Zephyr callback-based console input processing, shell subsystem, or [console\_getline()](#group__console__api_1ga3454f5b84d38d46a6c2bbf7fd6baa815).

        Returns:
        :   0-255: a character read, including control characters. <0: error occurred.

    int console\_putchar(char c)
    :   Output a char to console (buffered).

        Puts a character into console output buffer. It will be sent to a console asynchronously, e.g. using an IRQ handler.

        Returns:
        :   <0 on error, otherwise 0.

    void console\_getline\_init(void)
    :   Initialize [console\_getline()](#group__console__api_1ga3454f5b84d38d46a6c2bbf7fd6baa815) call.

        This function should be called once to initialize pull-style access to console via [console\_getline()](#group__console__api_1ga3454f5b84d38d46a6c2bbf7fd6baa815) function. This function supersedes, and incompatible with, callback (push-style) console handling (via console\_input\_fn callback, etc.).

    char \*console\_getline(void)
    :   Get next line from console input buffer.

        Return next input line from console. Until full line is available, this function will block. This function is similar to ANSI C gets() function (except a line is returned in system-owned buffer, and system takes care of the buffer overflow checks) and is intended to ease porting of existing software. Before this function can be used, [console\_getline\_init()](#group__console__api_1gacd13267df8567c63f2285ce0e1cbbc20) should be called once. This function is incompatible with native Zephyr callback-based console input processing, shell subsystem, or [console\_getchar()](#group__console__api_1ga2ba36eb1081cd0b98aa43216ccd6fbd5).

        Returns:
        :   A pointer to a line read, not including EOL character(s). A line resides in a system-owned buffer, so an application should finish any processing of this line immediately after [console\_getline()](#group__console__api_1ga3454f5b84d38d46a6c2bbf7fd6baa815) call, or the buffer can be reused.
