import win32api
import win32gui
import win32con
import time
import ctypes

def click1(x,y): #第一种
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,111,110)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,110,110)

#def click2(x,y): #第二种 
#    ctypes.windll.user32.SetCursorPos(x,y) 
#    ctypes.windll.user32.mouse_event(2,0,0,0,0) 
#    ctypes.windll.user32.mouse_event(4,0,0,0,0)

#def click_it(pos): #第三种 
#    handle= win32gui.WindowFromPoint(pos) 
#    client_pos =win32gui.ScreenToClient(handle,pos) 
#    tmp=win32api.MAKELONG(client_pos[0],client_pos[1]) 
#    win32gui.SendMessage(handle, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0) 
#    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,tmp) 
#    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,tmp)
