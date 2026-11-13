# Models

## realesr-general-x4v3.onnx

The small general-purpose model of [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) by Xintao Wang and others: it enlarges a picture four times and cleans it up. The photo booth uses it to make saved cut-outs sharper (see "Photo booth" in the main README).

- **Where it comes from:** the official weights `realesr-general-x4v3.pth`, release v0.2.5.0 of Real-ESRGAN.
- **What was done to it:** nothing but a change of file format. The network (SRVGGNetCompact: a convolution, then 32 pairs of PReLU and convolution, a last PReLU and convolution, a pixel shuffle by four, plus the input enlarged by nearest neighbour) was written out as ONNX (opset 13) with the weights unchanged, so that it runs in a browser with ONNX Runtime Web.
- **Licence:** BSD 3-Clause, Copyright (c) 2021, Xintao Wang. The full text is in `LICENSE-Real-ESRGAN.txt` next to this file.
- **Check:** the page only uses the file if its SHA-384 hash is `fynWnNZB1PjUlaYpM80JmLBwm9DHuhg08A6J7fMDUbtoVca46168enKecK9sGs2J` (base64).
