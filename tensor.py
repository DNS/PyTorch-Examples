https://docs.pytorch.org/docs/stable/tensors.html

     

Python API

    torch
        Tensors
        Generators
        Random sampling
        Serialization
        Parallelism
        Locally disabling gradient computation
        Math operations
        Utilities
        Symbolic Numbers
        Export Path
        Optimizations
        Operator Tags
    torch.nn
        Parameter
        UninitializedParameter
        UninitializedBuffer
        Containers
        Convolution Layers
        Pooling layers
        Padding Layers
        Non-linear Activations (weighted sum, nonlinearity)
        Non-linear Activations (other)
        Normalization Layers
        Recurrent Layers
        Transformer Layers
        Linear Layers
        Dropout Layers
        Sparse Layers
        Distance Functions
        Loss Functions
        Vision Layers
        Shuffle Layers
        DataParallel Layers (multi-GPU, distributed)
        Utilities
        Quantized Functions
        Lazy Modules Initialization
    torch.nn.functional
        Convolution functions
        Pooling functions
        Attention Mechanisms
        Non-linear activation functions
        Linear functions
        Dropout functions
        Sparse functions
        Distance functions
        Loss functions
        Vision functions
        DataParallel functions (multi-GPU, distributed)
    torch.Tensor
        Data types
        Initializing and basic operations
        Tensor class reference
    Tensor Attributes
        torch.dtype
        torch.device
        torch.layout
        torch.memory_format
    Tensor Views
    torch.amp
        Autocasting
        Gradient Scaling
        Autocast Op Reference
    torch.autograd
        torch.autograd.backward
        torch.autograd.grad
        Forward-mode Automatic Differentiation
        Functional higher level API
        Locally disabling gradient computation
        Default gradient layouts
        In-place operations on Tensors
        Variable (deprecated)
        Tensor autograd functions
        Function
        Context method mixins
        Numerical gradient checking
        Profiler
        Anomaly detection
        Autograd graph
    torch.library
    torch.cpu
        torch.cpu.current_stream
        torch.cpu.is_available
        torch.cpu.synchronize
        torch.cpu.stream
        torch.cpu.device_count
        StreamContext
        Streams and events
    torch.cuda
        StreamContext
        torch.cuda.can_device_access_peer
        torch.cuda.current_blas_handle
        torch.cuda.current_device
        torch.cuda.current_stream
        torch.cuda.default_stream
        device
        torch.cuda.device_count
        device_of
        torch.cuda.get_arch_list
        torch.cuda.get_device_capability
        torch.cuda.get_device_name
        torch.cuda.get_device_properties
        torch.cuda.get_gencode_flags
        torch.cuda.get_sync_debug_mode
        torch.cuda.init
        torch.cuda.ipc_collect
        torch.cuda.is_available
        torch.cuda.is_initialized
        torch.cuda.memory_usage
        torch.cuda.set_device
        torch.cuda.set_stream
        torch.cuda.set_sync_debug_mode
        torch.cuda.stream
        torch.cuda.synchronize
        torch.cuda.utilization
        torch.cuda.temperature
        torch.cuda.power_draw
        torch.cuda.clock_rate
        torch.cuda.OutOfMemoryError
        Random Number Generator
        Communication collectives
        Streams and events
        Graphs (beta)
        Memory management
        NVIDIA Tools Extension (NVTX)
        Jiterator (beta)
        Stream Sanitizer (prototype)
    Understanding CUDA Memory Usage
    Generating a Snapshot
    Using the visualizer
        Active Memory Timeline
        Allocator State History
    Snapshot API Reference
    torch.mps
        torch.mps.synchronize
        torch.mps.get_rng_state
        torch.mps.set_rng_state
        torch.mps.manual_seed
        torch.mps.seed
        torch.mps.empty_cache
        torch.mps.set_per_process_memory_fraction
        torch.mps.current_allocated_memory
        torch.mps.driver_allocated_memory
        MPS Profiler
        MPS Event
    torch.backends
        torch.backends.cpu
        torch.backends.cuda
        torch.backends.cudnn
        torch.backends.mps
        torch.backends.mkl
        torch.backends.mkldnn
        torch.backends.openmp
        torch.backends.opt_einsum
        torch.backends.xeon
    torch.export
        Overview
        Exporting a PyTorch Model
        Limitations of torch.export
        Read More
        API Reference
    torch.distributed
        Backends
        Basics
        Initialization
        Post-Initialization
        Distributed Key-Value Store
        Groups
        Point-to-point communication
        Synchronous and asynchronous collective operations
        Collective functions
        Profiling Collective Communication
        Multi-GPU collective functions
        Third-party backends
        Launch utility
        Spawn utility
        Debugging torch.distributed applications
        Logging
    torch.distributed.algorithms.join
    torch.distributed.elastic
        Get Started
        Documentation
    torch.distributed.fsdp
    torch.distributed.optim
    torch.distributed.tensor.parallel
    torch.distributed.checkpoint
    torch.distributions
        Score function
        Pathwise derivative
        Distribution
        ExponentialFamily
        Bernoulli
        Beta
        Binomial
        Categorical
        Cauchy
        Chi2
        ContinuousBernoulli
        Dirichlet
        Exponential
        FisherSnedecor
        Gamma
        Geometric
        Gumbel
        HalfCauchy
        HalfNormal
        Independent
        Kumaraswamy
        LKJCholesky
        Laplace
        LogNormal
        LowRankMultivariateNormal
        MixtureSameFamily
        Multinomial
        MultivariateNormal
        NegativeBinomial
        Normal
        OneHotCategorical
        Pareto
        Poisson
        RelaxedBernoulli
        LogitRelaxedBernoulli
        RelaxedOneHotCategorical
        StudentT
        TransformedDistribution
        Uniform
        VonMises
        Weibull
        Wishart
        KL Divergence
        Transforms
        Constraints
        Constraint Registry
    torch.compiler
        Read More
    torch.fft
        Fast Fourier Transforms
        Helper Functions
    torch.func
        What are composable function transforms?
        Why composable function transforms?
        Read More
    torch.futures
    torch.fx
        Overview
        Writing Transformations
        Debugging
        Limitations of Symbolic Tracing
        API Reference
    torch.hub
        Publishing models
        Loading models from Hub
    torch.jit
        TorchScript Language Reference
        Creating TorchScript Code
        Mixing Tracing and Scripting
        TorchScript Language
        Built-in Functions and Modules
        Debugging
        Frequently Asked Questions
        Known Issues
        Appendix
    torch.linalg
        Matrix Properties
        Decompositions
        Solvers
        Inverses
        Matrix Functions
        Matrix Products
        Tensor Operations
        Misc
        Experimental Functions
    torch.monitor
        API Reference
    torch.signal
        torch.signal.windows
    torch.special
        Functions
    torch.overrides
        Functions
    torch.package
        Tutorials
        How do I…
        Explanation
        API Reference
    torch.profiler
        Overview
        API Reference
        Intel Instrumentation and Tracing Technology APIs
    torch.nn.init
    torch.onnx
        Overview
        TorchDynamo-based ONNX Exporter
        TorchScript-based ONNX Exporter
        Contributing / Developing
    torch.optim
        How to use an optimizer
        Base class
        Algorithms
        How to adjust learning rate
        Weight Averaging (SWA and EMA)
    Complex Numbers
        Creating Complex Tensors
        Transition from the old representation
        Accessing real and imag
        Angle and abs
        Linear Algebra
        Serialization
        Autograd
    DDP Communication Hooks
        How to Use a Communication Hook?
        What Does a Communication Hook Operate On?
        Default Communication Hooks
        PowerSGD Communication Hook
        Debugging Communication Hooks
        Checkpointing of Communication Hooks
        Acknowledgements
    Pipeline Parallelism
        Model Parallelism using multiple GPUs
        Pipelined Execution
        Pipe APIs in PyTorch
        Tutorials
        Acknowledgements
    Quantization
        Introduction to Quantization
        Quantization API Summary
        Quantization Stack
        Quantization Support Matrix
        Quantization API Reference
        Quantization Backend Configuration
        Quantization Accuracy Debugging
        Quantization Customizations
        Best Practices
        Frequently Asked Questions
        Common Errors
    Distributed RPC Framework
        Basics
        RPC
        RRef
        RemoteModule
        Distributed Autograd Framework
        Distributed Optimizer
        Design Notes
        Tutorials
    torch.random
    torch.masked
        Introduction
        Supported Operators
    torch.nested
        Introduction
        Construction
        size
        unbind
        Nested tensor constructor and conversion functions
        Supported operations
    torch.sparse
        Why and when to use sparsity
        Functionality overview
        Operator overview
        Sparse Semi-Structured Tensors
        Sparse COO tensors
        Sparse Compressed Tensors
        Supported operations
    torch.Storage
    torch.testing
    torch.utils
        torch.utils.rename_privateuse1_backend
        torch.utils.generate_methods_for_privateuse1_backend
        torch.utils.get_cpp_backtrace
        torch.utils.set_module
    torch.utils.benchmark
    torch.utils.bottleneck
    torch.utils.checkpoint
    torch.utils.cpp_extension
    torch.utils.data
        Dataset Types
        Data Loading Order and Sampler
        Loading Batched and Non-Batched Data
        Single- and Multi-process Data Loading
        Memory Pinning
    torch.utils.jit
    torch.utils.dlpack
    torch.utils.mobile_optimizer
    torch.utils.model_zoo
    torch.utils.tensorboard
    Type Info
        torch.finfo
        torch.iinfo
    Named Tensors
        Creating named tensors
        Named dimensions
        Name propagation semantics
        Explicit alignment by names
        Manipulating dimensions
        Autograd support
        Currently supported operations and subsystems
        Named tensor API reference
    Named Tensors operator coverage
        Keeps input names
        Removes dimensions
        Unifies names from inputs
        Permutes dimensions
        Contracts away dims
        Factory functions
        out function and in-place variants
    torch.__config__
    torch._logging
        torch._logging.set_logs

Libraries

    torchaudio
    TorchData
    TorchRec
    TorchServe
    torchtext
    torchvision
    PyTorch on XLA Devices





