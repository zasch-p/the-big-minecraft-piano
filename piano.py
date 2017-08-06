from pythonosc import osc_message_builder
from pythonosc import udp_client
from mcpi.minecraft import Minecraft
from time import sleep

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
mc = Minecraft.create()

player_x, player_y, player_z  = mc.player.getTilePos()

def bulldozer(x, y, z):
    mc.setBlocks(x - 30, y - 3, z - 30, x + 30, y + 20, z + 30, 0)

def black_key(x, y, z):
      mc.setBlocks(x, y - 1, z, x + 1, y - 1, z + 8, 49)
def white_key(x, y, z):
      mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44, 7)
