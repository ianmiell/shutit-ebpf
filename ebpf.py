def do_ebpf(shutit_session):
	shutit_session.install('git')
	shutit_session.install('python')
	shutit_session.install('bpython')
	shutit_session.install('python-pip')
	shutit_session.install('bcc-lua')
	shutit_session.install('linux-tools-common')
	shutit_session.install('linux-tools-generic')
	shutit_session.install('linux-cloud-tools-generic')
	shutit_session.send('pip install --upgrade pip')
	shutit_session.send('pip install pyroute2')
	shutit_session.send('pip install future')
	shutit_session.send('pip install netaddr')
	shutit_session.send('''perf list 'net:*' ''')
	shutit_session.send('git clone https://github.com/iovisor/bcc')
	shutit_session.send('apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4052245BD4284CDD')
	shutit_session.send('echo "deb https://repo.iovisor.org/apt/xenial xenial main" | tee /etc/apt/sources.list.d/iovisor.list')
	shutit_session.send('apt-get update -y')
	shutit_session.send('apt-get install -y bcc-tools libbcc-examples linux-headers-$(uname -r)')
	shutit_session.send('PATH=/usr/share/bcc/examples/tracing:${PATH}')
	shutit_session.send('''echo 'PATH=/usr/share/bcc/examples/tracing:${PATH}' >> /root/.bashrc''')
	shutit_session.send('''echo 'PATH=/usr/share/bcc/tools:${PATH}' >> /root/.bashrc''')
	shutit_session.pause_point('see /usr/share/bcc/')

# /usr/share/bcc/examples/networking/http_filter
#root@ebpf1:/usr/share/bcc/examples/networking/http_filter# ./http-parse-simple.py -i enp0s3 &
#[1] 15717
#root@ebpf1:/usr/share/bcc/examples/networking/http_filter# binding socket to 'enp0s3'
#
#root@ebpf1:/usr/share/bcc/examples/networking/http_filter# curl google.com > /dev/null 2>&1
#GET / HTTP/1.1
#HTTP/1.1 301 Moved Permanently

# /usr/share/bcc/examples/lua
# /usr/share/bcc/examples/tracing
# /usr/share/bcc/man/man8 - tools doc'd?

# describes each one: /usr/share/bcc/tools/doc
# argdist          - Y - gets args to functions
# bashreadline     - bash commands across system
# biolatency       - TODO
# biosnoop       - TODO
# biotop       - TODO
# bitesize       - TODO
# bpflist       - TODO
# btrfsdist       - TODO
# btrfsslower       - TODO
# cachestat       - TODO
# cachetop       - TODO
# capable
# cobjnew       - TODO
# cpudist       - TODO
# cpuunclaimed       - TODO
# criticalstat       - TODO
# dbslower       - TODO
# dbstat       - TODO
# dcsnoop       - TODO
# dcstat       - TODO
# deadlock_detector - Y
# execsnoop       - TODO
# ext4dist       - TODO
# ext4slower       - TODO
# filelife       - TODO
# fileslower       - TODO
# filetop       - TODO
# funccount       - TODO
# funclatency       - TODO
# funcslower
# gethostlatency       - TODO
# hardirqs       - TODO
# inject       - TODO
# javacalls       - TODO
# javaflow       - TODO
# javagc       - TODO
# javaobjnew       - TODO
# javastat       - TODO
# javathreads
# killsnoop       - TODO
# llcstat       - TODO
# mdflush       - TODO
# memleak       - TODO
# mountsnoop       - TODO
# mysqld_qslower       - TODO
# nfsdist       - TODO
# nfsslower       - TODO
# nodegc       - Y
# nodestat     - Y
# offcputime   - Y
# offwaketime  - Y
# oomkill      - Y
# opensnoop    - Y
# perlcalls    - N
# perlflow     - N
# perlstat     - N
# phpcalls     - N
# phpflow      - N
# phpstat      - N
# pidpersec    - N
# profile      - Y
# pythoncalls  - N
# pythonflow   - N
# pythongc     - N
# pythonstat   - N
# reset-trace  - Y
# rubycalls    - N
# rubyflow     - N
# rubygc       - N
# rubyobjnew   - N
# rubystat     - N
# runqlat      - Y
# runqlen      - Y
# runqslower   - N
# slabratetop  - N
# softirqs     - N
# solisten     - N
# sslsniff     - Y
# stackcount   - Y
# statsnoop    - Y
# syncsnoop    - Y
# syscount     - Y
# tcpaccept    - Y
# tcpconnect   - Y
# tcpconnlat   - Y
# tcpdrop      - Y
# tcplife      - Y
# tcpretrans   - Y
# tcpstates    - Y
# tcpsubnet    - Y
# tcptop       - Y
# tcptracer    - Y
# tplist       - Y
# trace        - Y
# ttysnoop     - Y
# vfscount     - Y
# vfsstat      - Y
# wakeuptime   - Y
# xfsdist      - N
# xfsslower    - N
# zfsdist      - N
# zfsslower    - N
