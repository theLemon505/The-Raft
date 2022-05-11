import pygame as pg

from Source.Utils.time import Time
from Source.Io.display import Display
from os import system
from Source.System.resource_manager import ResourceManager
from Source.System.settings import Settings

def main():
    print("building the raft")

    system_settings = ResourceManager.read_settings()
    ResourceManager.write_settings(system_settings)
    print(Settings.max_threads)
    print(Settings.memory)
    print(Settings.detail)

    print("the raft is building")

    pg.init()
    display = Display(540, 400, "test")
    Time.delta_time = pg.time.Clock()


main()