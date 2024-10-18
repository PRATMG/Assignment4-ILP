import os
import m5
from m5.objects import *

# Create the system
system = System()
system.clk_domain = SrcClockDomain(clock="1GHz", voltage_domain=VoltageDomain())
system.mem_mode = 'timing'  # Use timing mode for SE mode
system.mem_ranges = [AddrRange('512MB')]  # Define memory range

# Set up CPU as X86O3CPU with superscalar capabilities
system.cpu = X86O3CPU()

# Configure superscalar properties
system.cpu.numThreads = 1  # Single thread
system.cpu.fetchWidth = 4  # Fetch up to 4 instructions per cycle
system.cpu.decodeWidth = 4  # Decode up to 4 instructions per cycle
system.cpu.issueWidth = 4  # Issue up to 4 instructions per cycle
system.cpu.commitWidth = 4  # Commit up to 4 instructions per cycle
system.cpu.squashWidth = 4  # Squash up to 4 instructions per cycle

# Create memory bus and connect CPU
system.membus = SystemXBar()
system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports

# Set up interrupt controller for x86
system.cpu.createInterruptController()

# Connect the interrupt controller ports to the memory bus
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Create memory controller and connect to the bus
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# Connect the system port to the memory bus
system.system_port = system.membus.cpu_side_ports

# Path to the correct benchmark binary (update with your benchmark paths)
binary = "/Users/aanik_tmg/Downloads/gem5/tests/test-progs/hello/bin/x86/linux/hello"

# Check if binary exists
if not os.path.exists(binary):
    raise FileNotFoundError(f"The binary {binary} does not exist.")

# Set up the workload
system.workload = SEWorkload.init_compatible(binary)

# Create a process for the benchmark binary
process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

# Set up the root object and instantiate the simulation
root = Root(full_system=False, system=system)
m5.instantiate()

# Start the simulation
print(f"Starting simulation with benchmark: {binary}")
exit_event = m5.simulate()

# Print exit details
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")

# Gather and print statistics
print("\n--- Performance Metrics ---")

# Dump statistics to file (by default: m5out/stats.txt)
m5.stats.dump()

# Reset the stats for future runs
m5.stats.reset()

print("Statistics dumped to the default output file (m5out/stats.txt).")
