# Update History

## v22.8.3
- Hotfix for heartbeat thread issues

## v22.8.2
- Corrected the behavior of pytorch_sample.py bundled in the HAC VM image
- Supported software update on VMs not containing the moreh-switch-model command

## v22.8.1
- Shorten the communication latency between an application process and a worker process.
- Supported PyTorch DP/DDP functions.
- Improved floating-point arithmetic accuracy for fp16 matrix multiplications.

## v22.8.0
- Supported the relaxed fp32 mode that performs fp32 matrix multiplications in bfloat16 (torch.moreh.options.allow_relaxed_fp32)
- The DataParallel compiler pass will be safely bypassed if it fails to parallelize the source graph, instead of raising an exception.

## v22.7.2
- Supported fallback to an NVIDIA GPU for unsupported operations
- Ensured Tensile GEMM kernels are not crashed for narrow-shaped tensors

## v22.7.1
- Fixed a precision issue in the SELU activation function
- Removed an unnecessary error message

## v22.7.0
- Bug fixes for KT HAC reference models

## v22.6.1
- Improved PyTorch portability

## v0.10.1
- The DeviceUsage API returns min/max/average percentages

## v0.10.0
- Introduced the graph executor running on GPU nodes to reduce inter-node packets
    - A user process can offload an entire computational graph instead of individual operations
- Improved PyTorch API portability and performance
- Supported AMD gfx908/gfx90a architectures (incl. MI100 and MI250 GPUs) and utilized their matrix core instructions

## v0.9.10
- Fixed `torch.jit.trace` to work
- DeviceUsageInfo API support that does not specify a token
- Corrected inplaceness check in the IR constructor

## v0.9.9
- Fixed the parallelization scheme of `unique()`
- Correctly handled variable-length operations with outermost size smaller than # of GPUs
- Resolved a potential GPU memory object leak in the storage allocator

## v0.9.8
- Supported `show usage` command in `moreh_smclient`

## v0.9.7
- Fixed a bug in torch.nn.functional.binary_cross_entropy_with_logits
- Fixed a message parsing error between frontend and worker

## v0.9.6
- Fixed a bug in torch.meshgrid

## v0.9.5
- Fixed some bugs in the PyTorch driver

## v0.9.4
- Fixed a bug of `Tensor.__getitem__()`

## v0.9.3
- Resolved a potential memory access fault in Convolution3d
- Fixed a bug in the memory allocator

## v0.9.2
- Fixed a GPU memory allocation issue

## v0.9.1
- Improved performance of grouped convolutions
- Fixed to connect to multiple moreh_workers at the correct timing
- Improved PyTorch portability

## v0.9.0
- Improved performance of some frequently used operations
- Improved PyTorch portability

## v0.8.3
- Supported backward computation of evaluation-mode batchnorm and dropout

## v0.8.2
- Supported boolean arithmetic operations
- Supported `normal`_, `pairwise_distance`, and `triplet_margin_with_distance_loss`

## v0.8.1
- Fixed a bug in the BatchNorm layer
- Fixed `torch.Tensor.type_as()` to correctly move data between devices
- Other bug fixes in SDAManager