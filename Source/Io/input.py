from abc import abstractmethod


import pygame as pg

class Keyboard:
    @abstractmethod
    def is_key_down(key_id):
        keys = pg.key.get_pressed()
        if keys[key_id]:
            return True
        
        return False

class Mouse:
    @abstractmethod
    def is_button_down(button_id):
        buttons = pg.mouse.get_pressed()
        if buttons[button_id]:
            return True
        
        return False