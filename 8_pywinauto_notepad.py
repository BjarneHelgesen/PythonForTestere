import pywinauto

notepad = pywinauto.application.Application().start("notepad.exe")
window = notepad.window() 

window.Edit.type_keys("Hello, this is a test using pywinauto!", with_spaces=True)