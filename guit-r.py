#!/usr/bin/python

import simpleaudio as sa, sys

# Tunings
standard = ['E2', 'A2', 'D3', 'G3', 'B3', 'E4']
drop_d = ['D2', 'A2', 'D3', 'G3', 'B3', 'E4']
drop_c = ['C2', 'G2', 'C3', 'F3', 'A3', 'D4']

fd = os.path.dirname(__file__)

def play(note):
    n = sa.WaveObject.from_wave_file(f'{fd}/notes/{note}.wav')
    play_obj = n.play()
    play_obj.wait_done()

def tune(tuning):
    for t in tuning:
        print('\n', t, end='\n')
        if t != tuning[-1]:
            choice = input('[P]lay, [N]ext\n >')
        else:
            choice = input('[P]lay, [Q]uit\n >')
        if choice == 'P' or choice == 'p':
            play(t)
            while True:
                if t != tuning[-1]:
                    choice = input('[R]eplay, [N]ext\n >')
                    if choice == 'R' or choice == 'r':
                        play(t)
                    else:
                        break
                else:
                    choice = input('[R]eplay, [Q]uit\n >')
                    if choice == 'R' or choice == 'r':
                        play(t)
                    else:
                        break
    print("Goodbye! Have fun!")

def main():
    print("\nChoose your tuning:\n\n[1] Standard (EADGBE)\n[2] Drop D (DADGBE) \n[3] Drop C (CGCFAD)\n\nor [Q]uit")
    while True:
        pick = input(' > ')
        if '1' in pick:
            tune(standard)
            break
        elif '2' in pick:
            tune(drop_d)
            break
        elif '3' in pick:
            tune(drop_c)
            break
        elif 'Q' in pick:
            print("See ya!")
            sys.exit()
        else:
            print("You have to choose a tuning! Try again")
            continue

if __name__ == "__main__":
    main()
