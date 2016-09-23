FROM fedora

MAINTAINER Olli Tourunen <tourunen@csc.fi>

ENV LANG=en_US.UTF-8

RUN dnf update -y &&\
    dnf groupinstall -y "C Development Tools and Libraries" &&\
    dnf groupinstall -y "Development Tools" &&\
    dnf install -y glibc-langpack-en python3 python3-devel time swig redhat-rpm-config &&\
    cd /tmp/ &&\
    git clone https://github.com/hfst/hfst.git &&\
    cd /tmp/hfst &&\
    ./autogen.sh &&\
    ./configure --enable-proc &&\
    make install &&\
    cd /tmp/hfst/python &&\
    python3 setup.py build &&\
    python3 setup.py install &&\
    cd /tmp &&\
    rm -rf /tmp/hfst/ &&\
    dnf groupremove -y "C Development Tools and Libraries" &&\
    dnf groupremove -y "Development Tools" &&\
    dnf clean all

RUN echo  "/usr/local/lib" > /etc/ld.so.conf.d/usr_local_lib.conf && ldconfig
