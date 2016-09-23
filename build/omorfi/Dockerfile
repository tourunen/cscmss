FROM cscmss/hfst

MAINTAINER Olli Tourunen <tourunen@csc.fi>

RUN dnf update -y &&\
    dnf groupinstall -y "C Development Tools and Libraries" &&\
    dnf groupinstall -y "Development Tools" &&\
    dnf install -y glibc-langpack-en python3 python3-devel time swig redhat-rpm-config &&\
    cd /tmp/ &&\
    git clone https://github.com/flammie/omorfi.git &&\
    cd /tmp/omorfi &&\
    ./autogen.sh &&\
    ./configure --enable-lemmatiser &&\
    make install &&\
    cd / &&\
    rm -rf /tmp/omorfi &&\
    dnf groupremove -y "C Development Tools and Libraries" &&\
    dnf groupremove -y "Development Tools" &&\
    dnf clean all
