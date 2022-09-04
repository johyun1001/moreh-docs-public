# Update History

## v22.8.0
- Supported the relaxed fp32 mode that performs fp32 matrix multiplications in bfloat16 (torch.moreh.options.allow_relaxed_fp32)
- The DataParallel compiler pass will be safely bypassed if it fails to parallelize the source graph, instead of raising an exception.

## v22.8.1
- Shorten the communication latency between an application process and a worker process.
- Supported PyTorch DP/DDP functions.
- Improved floating-point arithmetic accuracy for fp16 matrix multiplications.

## v22.8.2
- Corrected the behavior of pytorch_sample.py bundled in the HAC VM image
- Supported software update on VMs not containing the moreh-switch-model command

## v22.8.3
- Hotfix for heartbeat thread issues