class SleighScenario:
    def __init__(self, totalSpeed, santaKgStatus, injuredList, houseNumber=30000):
        self.checkInhuredList(injuredList)
        self.checkSantaKgStatus(santaKgStatus, totalSpeed)
        self.santaKgStatus = santaKgStatus
        self.checkHouseNumber(houseNumber)

    def checkSantaKgStatus(self, santaKgStatus, totalSpeed):
        if santaKgStatus == "+":
            self.totalSpeed = totalSpeed - ((totalSpeed / 100) * 20)
        elif santaKgStatus == "-":
            self.totalSpeed = totalSpeed + ((totalSpeed / 100) * 20)
        elif santaKgStatus == 0 or santaKgStatus == "0":
            self.totalSpeed = totalSpeed
        else:
            raise SyntaxError('Santa KG Status HAS NO MEANNING\n')

    def checkHouseNumber(self, houseNumber):
        if int(houseNumber) >= 30000:
            self.houseNumber = houseNumber
        elif int(houseNumber) < 30000:
            raise SyntaxError('THE NUMBER OF CHILDREN DOES NOT DECREASE !!!\n')
        else:
            raise SyntaxError('POPULATION MUST BE AN INTEGER!\n')

    def checkInhuredList(self, injuredList):
        if len(injuredList) == 8:
            raise SyntaxError('ALL REINDEERS CANNOT BE INJURED!\n')
        else:
            self.injuredList = injuredList

    def __str__(self):
        spentTime = int(self.houseNumber) / int(self.totalSpeed)
        result = 360 - spentTime

        if len(self.injuredList) == 0:
            print("Nobody was injured and there was no delay due to injury.\n")
        else:
            print(self.injuredList)
            print("There was a delay because these Reindeers were injured.\n")

        if self.santaKgStatus == "0":
            print("Santa Claus kept his weight and there was no delay due to this.\n")
        elif self.santaKgStatus == "+":
            print("Santa Claus gained weight and there was delay due to this. "
                  "Our speed has decreased by 20%.\n")
        elif self.santaKgStatus == "_":
            print("Santa Claus lost weight and therefore gifts were distributed faster. "
                  "Our speed increased by 20%.\n")
        else:
            pass

        if self.houseNumber == 30000:
            print("The pandemic did not affect the number of children"
                  " and therefore we did not distribute any more gifts.\n")
        else:
            print("The pandemic caused an increase in the number of children, "
                  "so we distributed more gifts.\n")

        if result == 0:
            return "As a result:\n" \
                   "The day was almost dawn when we put in the last gift. " \
                   "So it was 06:00 am.\n"
        elif result > 0:
            return "As a result:\n" \
                   "We came home {} minutes early.\n" \
                   "If more gifts were needed, we could " \
                   "distribute {} more gifts during this time.\n".format(result, result * self.totalSpeed)
        elif result < 0:
            return "As a result:\n" \
                   "We were not able to deliver all the gifts and we were {} minutes late.\n" \
                   "Unfortunately, {} gifts were not given.".format(result * (-1),
                                                                    result * (-1) * self.totalSpeed)
        else:
            pass
