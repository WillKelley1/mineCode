from minecraft import *
from time import sleep

# Connect to Minecraft
mc = Minecraft.create()

# Define a function to mine blocks in a straight line
def mine_line(length):
    for i in range(length):
        mc.setBlock(mc.player.getTilePos().x + i, mc.player.getTilePos().y, mc.player.getTilePos().z, AIR)
        sleep(0.1)

# Mine a tunnel of length 10
mine_line(10)
