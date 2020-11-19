#!/bin/bash

ARCH="armv7l"
MIRROR="dk.mirror.archlinuxarm.org"


wget "${MIRROR}/armv7h/community/community.db"
wget "${MIRROR}/armv7h/core/core.db"
wget "${MIRROR}/armv7h/extra/extra.db"
wget "${MIRROR}/armv7h/alarm/alarm.db"
wget "${MIRROR}/armv7h/aur/aur.db"