import pyautogui as pyg


#clicks

def leftClick():
	pyg.click()

def rightClick():
	pyg.click(button = 'right')

def leftClickHold():
	pyg.mouseDown()

def leftClickRelease():
	pyg.mouseUp()

#movement

def interact(self):
	pyg.press('f')

def aimRel(self, x, y, dur = 0):
	#moves cursor to position relative to where cursor is currently
	pyg.moveRel(x, y, duration = dur)

def aimTo(self, x, y, dur = 0):
	#moves cursor to a position on the screen with top left corner as (0, 0)
	pyg.moveTo(x, y, duration = dur)

def Ndown(self):
	pyg.keyDown('up')

def Nup(self):
	pyg.keyUp('up')

def Edown(self):
	pyg.keyDown('right')

def Eup(self):
	pyg.keyUp('right')

def Sdown(self):
	pyg.keyDown('down')

def Sup(self):
	pyg.keyUp('down')
	
def Wdown(self):
	pyg.keyDown('left')

def Wup(self):
	pyg.keyUp('left')

def NEdown(self):
	pyg.keyDown('up')
	pyg.keyDown('right')

def NEup(self):
	pyg.keyUp('up')
	pyg.keyUp('right')

def NWdown(self):
	pyg.keyDown('up')
	pyg.keyDown('left')

def NWup(self):
	pyg.keyUp('up')
	pyg.keyUp('left')

def SEdown(self):
	pyg.keyDown('down')
	pyg.keyDown('right')

def SEup(self):
	pyg.keyUp('down')
	pyg.keyUp('right')

def SWdown(self):
	pyg.keyDown('down')
	pyg.keyDown('left')

def SWup(self):
	pyg.keyUp('down')
	pyg.keyUp('left')

#Combat

def weapon1(self):
	pyg.press('1')

def weapon2(self):
	pyg.press('2')

def fists(self):
	pyg.press('3')

def grenade(self):
	pyg.press('4')

def lastWeapon(self):
	pyg.press('q')

def reload(self):
	pyg.press('r')

def switchSlots(self):
	pyg.press('t')

#Meds

def bandage(self):
	pyg.press('7')

def medkit(self):
	pyg.press('8')

def soda(self):
	pyg.press('9')

def pills(self):
	pyg.press('0')

#navigation

def map(self):
	pyg.press('m')

def minimap(self):
	pyg.press('v')

#emotes
dur = .2

def emote1(self):
	pyg.mouseDown(button = 'right')
	pyg.moveRel(0, -40, duration = dur)
	pyg.mouseUp(button = 'right')

def emote2(self):
	pyg.mouseDown(button = 'right')
	pyg.moveRel(40, 0, duration = dur)
	pyg.mouseUp(button = 'right')

def emote3(self):
	pyg.mouseDown(button = 'right')
	pyg.moveRel(0, 40, duration = dur)
	pyg.mouseUp(button = 'right')

def emote4(self):
	pyg.mouseDown(button = 'right')
	pyg.moveRel(-40, 0, duration = dur)
	pyg.mouseUp(button = 'right')

def warnping(self):
	pyg.keyDown('c')
	pyg.mouseDown(button = 'right')
	pyg.moveRel(0, -40, duration = dur)
	pyg.mouseUp(button = 'right')
	pyg.keyUp('c')

def gotoping(self):
	pyg.keyDown('c')
	pyg.mouseDown(button = 'right')
	pyg.moveRel(40, 0, duration = dur)
	pyg.mouseUp(button = 'right')
	pyg.mouseUp('c')

def giftping(self):
	pyg.keyDown('c')
	pyg.mouseDown(button = 'right')
	pyg.moveRel(0, 40, duration = dur)
	pyg.mouseUp(button = 'right')
	pyg.keyUp('c')

def healping(self):
	pyg.keyDown('c')
	pyg.mouseDown(button = 'right')
	pyg.moveRel(-36.955, 15.307, duration = dur)
	pyg.mouseUp(button = 'right')
	pyg.keyUp('c')

def ammoping(self):
	pyg.keyDown('c')
	pyg.mouseDown(button = 'right')
	pyg.moveRel(-36.955, -15.307, duration = dur)
	pyg.mouseUp(button = 'right')
	pyg.keyUp('c')

