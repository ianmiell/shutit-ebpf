def run(shutit_sessions, machines):
	print('machines:')
	print(machines)
	term = shutit_sessions['machinewilted1']
	# bcc tools are different from bpf - they use a language front end to libbcc and libbpf
	term.send('apt install -y bpftrace bpfcc-tools python3-bpfcc bcc')
	# For bpftool
	term.send('apt install -y linux-tools-5.4.0-89-generic')
	term.send('bpftool')
	term.send('bpftool prog help')
	# The perf subcommand shows BPF programs attached via perf_event_open(), which is the norm for BCC and bpftrace programs on Linux 4.17 and later.
	term.send('bpftool perf')
	# The prog show subcommand lists all programs (not just those that are perf_event_open() based):
	term.send('bpftool prog show')
	# Each BPF program can be printed ('dumped') via its ID. The xlated mode prints the BPF instructions translated to assembly. Here is program 234, the bpftrace block I/O done program:
	id = term.send_and_get_output(r"""bpftool prog show | head -1 | awk '{print $1}' | sed 's/\(.*\):/\1/g'""")
	term.send('bpftool prog dump xlated id ' + id)
	term.pause_point('GO')
