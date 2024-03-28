import pygame, os
import settings as s
import world_object as wo


class Sprite(wo.WorldObject):
    """Represents a single sprite in a level."""

    def __init__(self, name, x, y):
        self.offset = x
        self.offset_y = y
        self.sprite = s.SPRITES[name]
        self.hit = False

        wo.WorldObject.__init__(self)

    def is_hooker(self):
        return "hooker" in self.sprite

    def is_speed_boost(self):
        return "speed_boost" in self.sprite

    def is_bonus(self):
        return "bonus" in self.sprite

    def path(self):
        sprite_name = self.sprite["path"]

        if self.is_hooker() and self.hit:
            sprite_name = sprite_name.replace(".", "_dead.")

        return pygame.image.load(os.path.join("lib", sprite_name))
