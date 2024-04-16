import time

invalid = "Invalid Input"


def parse_boolean(t,f):
  while True:
    boolean = input()
    if boolean == t:
        return True
    elif boolean == f:
        return False
    else:
        print(invalid)

timed = False

def main():
  if timed:
    start_time = time.time()
  print("Hello!")
  time.sleep(2)
  if timed:
    sec = str((time.time() - start_time) // 1)[1:]
    mins = sec // 60
    sec = (sec % 60)
    hours = mins // 60
    mins = mins % 60
    print("Time elapsed: {int(hours):02}:{int(mins):02}:{sec:02}")

print("...instructions")
print("Type 'start' to start the game and 'config' to change the settings.")

while True:
    command = input().casefold()
    if command == "start":
        main()
        break
    elif command == "config":
        print("Settings:")
        print("Speedrun Mode? (on/off)")
        timed = parse_boolean("on", "off")
        print("Type 'start' to start the game and 'config' to change the settings.");
        # other things like extras
    else:
        print(invalid)

print("The game ended.");