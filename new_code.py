import random


class match:

    def play(self):
        ball = -1
        page = -1
        while True:
            print()
            runs = self.score[self.bat][1]
            wick = self.score[self.bat][2]
            who = self.score[self.bat][0]
            target = self.score[not self.bat][1] + 1

            currScore = ""
            currScore += who + ": " + str(runs) + "/" + str(wick)
            print(currScore)

            over = str(int((self.played - self.played % 6) / 6)) + "." + str(self.played % 6) + " overs"
            print(over)
            print()

            if self.isSecInn:
                print("Target: " + str(target))
                print()

            if ball != -1:
                print("Page: " + str(page))
                if ball:
                    print(str(ball) + " runs scored.")
                else:
                    print("OUT!")
                print()

            result = ["You lose. Better luck next time!", "You win!!"]

            if self.isSecInn:
                if runs >= target:
                    print(result[self.bat])

                    input("Press ENTER to exit...")
                    break
                else:
                    if wick == self.wickets or self.played == self.balls:
                        if runs == target - 1:
                            print("It's a tie!")
                        else:
                            print(result[not self.bat])

                        input("Press ENTER to exit...")
                        break

            else:
                if wick == self.wickets or self.played == self.balls:
                    self.isSecInn = True
                    self.played = 0
                    self.bat = not self.bat
                    ball = -1
                    page = -1
                    input("1st innings ends. Press ENTER to play 2nd innings...")
                    continue

            ch = input("Type n + ENTER to flip book, or press ENTER to quit game: ")

            if ch == "n":
                page = random.randint(1, 100)
                ball = page % 10

                if ball:
                    if ball > 6:
                        ball -= 6
                    self.score[self.bat][1] += ball
                else:
                    self.score[self.bat][2] += 1

                self.played += 1
            else:
                break

    def __init__(self, pages, overs, wickets, bat):
        self.pages = pages
        self.balls = overs * 6
        self.wickets = wickets
        self.bat = bat
        self.score = {True: ["User", 0, 0], False: ["CPU", 0, 0]}
        self.played = 0
        self.isSecInn = False

        self.play()


test = match(100, 5, 3, True)