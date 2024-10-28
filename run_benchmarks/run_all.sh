#!/bin/bash

echo "Running integer benchmark..."
/Users/aanik_tmg/Downloads/gem5/build/X86/gem5.opt --outdir=m5out/integer /Users/aanik_tmg/Downloads/gem5/configs/test1/run_benchmarks/run_integer.py

echo "Running floating-point benchmark..."
/Users/aanik_tmg/Downloads/gem5/build/X86/gem5.opt --outdir=m5out/floating /Users/aanik_tmg/Downloads/gem5/configs/test1/run_benchmarks/run_floating_point.py

echo "Running memory benchmark..."
/Users/aanik_tmg/Downloads/gem5/build/X86/gem5.opt --outdir=m5out/memory /Users/aanik_tmg/Downloads/gem5/configs/test1/run_benchmarks/run_memory.py

echo "All benchmarks completed."
