#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019, Benjamin Weps
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Authors:
# - 2019 Benjamin Weps

# This is the compiler setup script for the gcc provided by SiFive.
# Don't get confused about the riscv64 prefix, the compiler supports both
# 32 and 64 bit targets (the processor width its part of the ISA definition)

from SCons.Script import *

def generate(env, **kw):
    env['PROGSUFFIX'] = '.elf'
    env['ARCHITECTURE'] = 'riscv64'
    env.SetDefault(OS='unknown')

    env.SetDefault(COMPILERPREFIX='riscv64-unknown-elf-')
    env.SetDefault(RISCV_ISA="rv32imac")
    env.SetDefault(RISCV_ABI="ilp32")

    env.SetDefault(CCFLAGS_target=[
        '-march=$RISCV_ISA',
        "-mabi=$RISCV_ABI",])
    env.SetDefault(CCFLAGS_debug=['-gdwarf-2'])
    env.SetDefault(CCFLAGS_optimize=[
        '-Os',
        '-ffunction-sections',
        '-fdata-sections', ])
    env.SetDefault(CCFLAGS_other=[
        '-finline-limit=10000',
        '-funsigned-char',
        '-funsigned-bitfields',
        '-fno-split-wide-types',
        '-fno-move-loop-invariants',
        '-fno-tree-loop-optimize',
        '-fno-unwind-tables',
        '-fshort-wchar',        # Required when using newlib.nano
        ])

    env.SetDefault(CXXFLAGS_target=[
        "-march=$RISCV_ISA",
        "-mabi=$RISCV_ABI"])
    env.SetDefault(CXXFLAGS_other=[
        '-fno-threadsafe-statics',
        '-fuse-cxa-atexit',])
    env.SetDefault(CXXFLAGS_language=[
        '-std=c++17',
        '-fno-exceptions',
        '-fno-rtti',])

    env.SetDefault(ASFLAGS_target=[
        "-march=$RISCV_ISA"
        ])

    env.SetDefault(LINKFLAGS_target=[
        "-march=$RISCV_ISA",
        "-mabi=$RISCV_ABI",
        ])
    env.SetDefault(LINKFLAGS_optimize=['--gc-sections', ])
    env.SetDefault(LINKFLAGS_other=[
        "-Wl,--fatal-warnings",
        # "-Wl,-Map=project.map,--cref",
        ])

    env.Tool('settings_gcc_default_internal')


def exists(env):
    return env.Detect('gcc')
