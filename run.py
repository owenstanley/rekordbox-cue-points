from pynput.keyboard import Key, Controller, Events, KeyCode
import time

# setting up the keyboard controller
kb = Controller()

def set_cue_points(num_songs):
    # sets the number of bars the program run through for each track
    max_bars = 96

    # for every bar until the maximum
    for i in range(0,max_bars * num_songs + 1):
        
        # if the current bar is a multiple of 16 or is the 8th bar of the track
        # set a cue
        # TODO - change logic of this to make it easy for users to customise
        # TODO make this look nicer?
        if i % 16 == 0 or (i-8) % max_bars == 0:
            kb.press('c')
            time.sleep(0.1)
            kb.release('c')
            time.sleep(0.5)
            kb.press('m')
            time.sleep(0.1)
            kb.release('m')
            time.sleep(0.5)
        
        # if the current bar is the last of a track (up to the maximum)
        # move to the next track and set a cue
        # TODO make this look nicer?
        if i % max_bars == 0 and i !=0:
            kb.press(Key.ctrl)
            kb.press(Key.down)
            time.sleep(0.1)
            kb.release(Key.ctrl)
            kb.release(Key.down)
            time.sleep(0.5)
            kb.press('a')
            kb.release('a')
            time.sleep(0.5)
            kb.press('c')
            kb.release('c')
            time.sleep(0.5)
            kb.press('m')
            kb.release('m')
            time.sleep(0.5)
        
        # move to the next bar
        kb.press(Key.right)

        time.sleep(0.1)

# main function for the program
def run():
    # getting number of songs
    num_songs = int(input("Welcome. How many songs do you need to automate?\n"))
    print("While in rekordbox, press f1 to start.")
    # The event listener will be running in this block
    with Events() as events:
        for event in events:
            if event.key == Key.esc:
                # if esc is pressed, stop listening
                break
            elif event.key == Key.f1:
                # if f1 is pressed, start automation
                set_cue_points(num_songs)
                break



if __name__ == '__main__':
    run()
