from copyreg import constructor
from enum import Enum
from hashlib import new
from os import stat

import psutil as ps
from .settings import Settings

class Cpus(Enum):
    Intel_i5 = 0
    Intel_i6 = 1
    Intel_i7 = 2
    Intel_i8 = 3
    Intel_i9 = 3

class Gpus(Enum):
    Old = 0
    GTX_1060 = 1
    GTX_1060ti = 2
    GTX_1070 = 3
    GTX_1070ti = 4
    GTX_1080 = 5
    GTX_1080ti = 6

class SystemSpecs:
    def __init__(self):
        self.dedicated_gpu = False
        self.graphics_device = Gpus.Old
        self.cpu = Cpus.Intel_i5
        self.memory = 2

    def __init__(self, dedicated_gpu, graphics_device, cpu, memory):
        self.dedicated_gpu = dedicated_gpu
        self.graphics_device = graphics_device
        self.cpu = cpu
        self.memory = memory

class ResourceManager:
    @staticmethod
    def read_settings():
        memory = 8
        cpu = Cpus.Intel_i5
        gpu = Gpus.GTX_1060
        return SystemSpecs(True, gpu, cpu, memory)

    @staticmethod
    def write_settings(system_specs : SystemSpecs):
        if system_specs.dedicated_gpu == True:
            if system_specs.graphics_device.value < Gpus.GTX_1060.value:
                Settings.detail = 1
            elif system_specs.graphics_device.value > Gpus.GTX_1060.value and system_specs.graphics_device < Gpus.GTX_1070.value:
                Settings.detail = 2
            elif system_specs.graphics_device.value > Gpus.GTX_1070.value and system_specs.graphics_device < Gpus.GTX_1080ti.value:
                Settings.detail = 3
            elif system_specs.graphics_device.value > Gpus.GTX_1080ti.value:
                Settings.detail = 4
        if system_specs.cpu.value < Cpus.Intel_i5.value:
            Settings.max_threads = 1
        elif system_specs.cpu.value > Cpus.Intel_i5.value and system_specs.cpu.value < Cpus.Intel_i7.value:
            Settings.max_threads = 3
        elif system_specs.cpu.value > Cpus.Intel_i7.value:
            Settings.max_threads = 6
        Settings.memory = system_specs.memory
