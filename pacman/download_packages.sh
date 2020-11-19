#!/bin/bash

ARCH="armv7l"
MIRROR="http://arch.mirror.far.fi/"

wget "${MIRROR}/community/os/${ARCH}/community.db"
wget "${MIRROR}/core/os/${ARCH}/core.db"
wget "${MIRROR}/extra/os/${ARCH}/extra.db"
wget "${MIRROR}/multilib/os/${ARCH}/multilib.db"