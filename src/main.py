import pyautogui
from pynput import mouse, keyboard
import sys;
import pygame;
from pygame.locals import *

switch_options = {"kill":"]", "draw":"z"}

kill_switch_key = "]"

width,height = pyautogui.size()

can_draw = False
left_held = False
left_released = False
global xInitial, yInitial, xReleased, yReleased
global pygameInfo, pygameScreen
current_keys = set()

def on_press(key):
      global can_draw
      current_keys.add(key)
      if (keyboard.Key.ctrl_l in current_keys or keyboard.Key.ctrl_r in current_keys):
            try:
                  if key.char.lower() == switch_options["kill"]:
                        print("Kill switch pressed! Exiting...")
                        mouse_listener.stop()
                        keyboard_listener.stop()
                        sys.exit()
                  elif key.char.lower() == switch_options["draw"]:
                        print("i can draw")
                        can_draw = True
            
            except AttributeError:
                  pass

def on_click(x,y,button, pressed):
      global left_held, xInitial,yInitial, left_released, yReleased, xReleased, can_draw, pygameScreen
      if can_draw:
            print('starting to draw')
            if button == mouse.Button.left:
                  if pressed:
                        left_held = True
                        left_released = False
                        xInitial = x
                        yInitial = y
                  else: 
                        left_held = False
                        left_released = True
                        xReleased = x
                        yReleased = y
                        can_draw = False
                        draw_rect(xInitial, yInitial, xReleased, yReleased, pygameScreen, (0,0,0))
            
# x1 and y1 are the top left of the box and x2,y2 are the bottom right           
def draw_rect(x1,y1,x2,y2, screen, rect_color):
      widtRectangle = x2 -x1
      heightRectangle = y2 - y1
      rect = pygame.Rect(x1,y1,widtRectangle, heightRectangle)
      pygame.draw.rect(screen,rect_color, rect, 2)

def pygame_init():
      info = pygame.display.Info()
      screen = pygame.display.set_mode((width,height), pygame.NOFRAME | pygame.SCALED)
      pygame.display.set_caption("rectangle drawer")
      return info,screen


# print(pyautogui.position())

def main():
      global pygameInfo, pygameScreen
      pygame.init()
      pygameInfo,pygameScreen = pygame_init();
      mouse_listener = mouse.Listener(on_click=on_click)
      mouse_listener.start()

      keyboard_listener = keyboard.Listener(on_press=on_press)
      keyboard_listener.start()

      mouse_listener.join()
      keyboard_listener.join()

main()