import logging
import sportsreference
import numpy
from matplotlib import pyplot

logging.basicConfig(
    filename='Final-log' + '.log',
    format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

user = input("Please select Premier League or Bundeliga: ")

if user == "Bundesliga":
    from sportsreference.fb.team import Team

    Dortmund = Team('add600ae')
    BMunich = Team('9133b975')
    Leipzig = Team('acbb6a5b')
    Monchengladbach = Team('cbefe26c')
    Leverkusen = Team('c7a9f859')
    Schalke = Team('c539e393')
    Wolfsburg = Team('a1393014')
    Freiburg = Team('b4de690d')
    Hoffenheim = Team('033ea6b8')
    Koln = Team('bc357bf7')
    UnionBerlin = Team('7a41008f')
    Frankfurt = Team('f0ac8ee6')
    Augsburg = Team('0cdc4311')
    Mainz = Team('a224b06a')
    Dusseldorf = Team('b1278397')
    Bremen = Team('7adbf480')
    Paderborn = Team('d9f93f02')
    HBerlin = Team('2818f8bc')

    Bundesliga = [Dortmund, BMunich, Leipzig, Monchengladbach, Leverkusen, Schalke,
                  Wolfsburg, Freiburg, Hoffenheim, Koln, UnionBerlin, Frankfurt,
                  Augsburg, Mainz, Dusseldorf, Bremen, Paderborn, HBerlin]

    for team in Bundesliga:

        if team.position == None:
            Bundesliga.remove(team)
            logging.error("{}'s data could not be retrieved".format(team.name))
        else:
            logging.info("{}'s data was successfully retrieved".format(team.name))
    Bundesliga.sort(key=lambda team: team.position)
    print("Here are today's Bundesliga standings: ")
    print("{:<9} {:<20} {:<8} {:<8}".format("Position", "Name", "Points", "W-L-D"))
    plotList = []
    for team in Bundesliga:
        try:
            print("{:<9} {:<20} {:<8} {:<8}".format(team.position, team.name, team.points, team.record))
            plotList.insert(team.position, team.points)
            pyplot.title("Bundesliga Position vs Points")
            pyplot.xlabel("Position")
            pyplot.ylabel("Points")
            pyplot.plot(plotList)
            pyplot.savefig(fname="BundesligaPlot.png", format="png")
            pyplot.show()
        except:
            print("Plot could not be printed!")

    print("\n")

    user = input("If you'd like to learn more about a team, just type in a name from the list above"
                 " or type exit to exit the program: ")
    while user != "exit":
        teamFound = False
        for team in Bundesliga:
            if user == team.name:
                teamFound = True
                print("Manager: {}".format(team.manager))
                print("Players:")
                for player in team.roster:
                    print(player.name)
                user = input("If you'd like to learn about another team, type in their name"
                             " if not, type exit: ")
        if teamFound == False:
            user = input("That wasn't a name you could pick! Please try again: ")

if user == "Premier League":
    from sportsreference.fb.team import Team

    Liverpool = Team('e87167c6')
    ManCity = Team('9ce68f8a')
    Leicester = Team('a2d435b3')
    Chelsea = Team('a6a4e67d')
    ManUtd = Team('19538871')
    Wolverhampton = Team('8cec06e1')
    Sheffield = Team('1df6b87e')
    Tottenham = Team('361ca564')
    Arsenal = Team('411b1108')
    Burnley = Team('943e8050')
    CrystalPalace = Team('47c64c55')
    Everton = Team('c4989550')
    Newcastle = Team('b2b47a98')
    Southampton = Team('33c895d4')
    Brighton = Team('d07537b9')
    WestHam = Team('52d65cea')
    Watford = Team('2abfe087')
    Bournemouth = Team('c5b06e34')
    AstonVilla = Team('8602292d')
    Norwich = Team('1c781004')

    Prem = [Liverpool, ManCity, Leicester, Chelsea, ManUtd, Wolverhampton,
            Sheffield, Tottenham, Arsenal, Burnley, CrystalPalace, Everton,
            Newcastle, Southampton, Brighton, WestHam, Watford, Bournemouth,
            AstonVilla, Norwich]

    for team in Prem:
        if team.position == None:
            Prem.remove(team)
            logging.error("{}'s data could not be retrieved".format(team.name))
        else:
            logging.info("{}'s data was successfully retrieved".format(team.name))
    Prem.sort(key=lambda team: team.position)
    print("Here are today's Premier League standings: ")
    print("{:<9} {:<28} {:<8} {:<8}".format("Position", "Name", "Points", "W-L-D"))
    plotList = []
    for team in Prem:
        try:
            print("{:<9} {:<28} {:<8} {:<8}".format(team.position, team.name, team.points, team.record))
            plotList.insert(team.position, team.points)
            pyplot.title("Premier League Position vs Points")
            pyplot.xlabel("Position")
            pyplot.ylabel("Points")
            pyplot.plot(plotList)
            pyplot.savefig(fname="PremPlot.png", format="png")
            pyplot.show()
        except:
            print("Plot could not be printed!")

    print("\n")

    user = input("If you'd like to learn more about a team, just type in a name from the list above"
                 " or type exit to exit the program: ")
    while user != "exit":
        teamFound = False
        for team in Prem:
            if user == team.name:
                teamFound = True
                print("Manager: {}".format(team.manager))
                print("Players:")
                for player in team.roster:
                    print(player.name)
                user = input("If you'd like to learn about another team, type in their name"
                             " if not, type exit: ")
        if teamFound == False:
            user = input("That wasn't a name you could pick! Please try again: ")
