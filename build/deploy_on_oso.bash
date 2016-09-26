#!/usr/bin/env bash

set -e -x

oc new-build https://github.com/tourunen/cscmss.git --context-dir build/hfst --name hfst
sleep 15
oc logs -f bc/hfst

oc new-build https://github.com/tourunen/cscmss.git --context-dir build/omorfi --name omorfi
sleep 15
oc logs -f bc/omorfi

oc new-app https://github.com/tourunen/cscmss.git --context-dir build/omorfi-mss --name omorfi-mss
oc logs -f bc/omorfi-mss

oc expose service omorfi-mss --hostname omorfi-mss.dac-oso.csc.fi
