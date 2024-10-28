import os
import m5
from m5.objects import *

# Path to the memory benchmark binary
memory_benchmark = "/Users/aanik_tmg/Downloads/gem5/configs/test1/benchmarks/memory_benchmark"

# Set up the system
system = System()
system.clk_domain = SrcClockDomain(clock="1GHz", voltage_domain=VoltageDomain())
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# Set up CPU as X86O3CPU with superscalar capabilities
system.cpu = X86O3CPU()
system.cpu.numThreads = 1
system.cpu.fetchWidth = 4
system.cpu.decodeWidth = 4
system.cpu.issueWidth = 4
system.cpu.commitWidth = 4
system.cpu.squashWidth = 4

# Memory and bus setup
system.membus = SystemXBar()
system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports
system.system_port = system.membus.cpu_side_ports

# Set up the workload
system.workload = SEWorkload.init_compatible(memory_benchmark)
process = Process()
process.cmd = [memory_benchmark]
system.cpu.workload = process
system.cpu.createThreads()

# Root and simulation instantiation
root = Root(full_system=False, system=system)
m5.instantiate()

print("Starting memory benchmark...")
exit_event = m5.simulate(1_000_000_000)  # Set a tick limit to avoid indefinite execution
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")

# Dump statistics
m5.stats.dump()
m5.stats.reset()
