"""
*********************************************************************************************************
                            Welcome to the 2020 elections conspiracy game.
*********************************************************************************************************

The following game is scenario-based storyline mimicking potential outcomes of the upcoming 2020 elections.
The game contains 5 stages and  can be played in 16 different ways with 16 different outcomes.
This game is meant to be a fun game and it is therefore not to be taken seriously.
Do not hesitate to share with your friends and family!

Created by Quentin Adam (email: qadam2602@gmail.com)
Do not hesitate to contact me for any questions.

"""

# After start, choose between either of the following two variables
var2_1 = """
Trump is impeached and Hillary Clinton is running for presidency.
"""

var2_2 = """
Trump is not impeached and still running for presidency.
"""

# If step2_1 choose between either of the following two variables
var3_1 = """
Bernie Sanders is getting a lot of traction
from both businesses and the people
who see the need for reducing inequalities
in the country.
"""
var3_2 = """
Bernie Sanders complains about the elite and challenges the status quo.
Thus giving him a bad reputation.
"""
# Else step2_2, choose between either of the following two variables

var3_3 = """
Trump thanks Putin in a tweet for his help
in funding the propaganda media blitz to get 
him out of the impeachment claims.
"""
var3_4 = """
Trumps promises to unite the nation for
the first time ahead of the elections.
"""

# If step3_1 choose between either of the following two variables

var4_1 = """
The polls are looking great for Bernie ahead of the elections
as he is rallying in niche states and slowly
getting the public opinion in extremis.
"""
var4_2 = """
Bernies Sanders is caught smoking weed with his Vermont electorate.
This mistake negatively impacts his current polls.
"""

# elif step3_2
var4_3 = """
Hillary Clinton is pushing hard to get popular votes
while rallying in both the cities and rural areas.
"""
var4_4 = """
Elizabetyh Warren is slowly winning over Hillary in the polls.
The "Pocahontas" is having a lot of success among all Americans.
"""

# elif step3_3
var4_5 = """
Life goes on and nobody really pays attention to Trumps 
bad behavior as he hides behind "fake news".
"""
var4_6 = """
The country is shocked, strikes errupt across the country.
Fears of civil war are seriously considered.
"""

# else step3_4
var4_7 = """
Trump does not keep his promise of uniting the country.
He escalates the Trade War tensions. 
"""
var4_8 = """
Trump keeps his promise of uniting the country and pushing for more peace.
"""

var5_1 = """
Bernie Sanders wins the elections!!! Viva la Socialista
Inequalities are greatly reduced over time, well done!
"""
var5_2 = """
Bernie Sanders wins the elections!!! Viva la Socialista
However, the US economy falls apart and a new economic crisis is on its way!
"""
var5_3 = """
Hillary Clinton wins the elections! She is the first female President
of the USA. Well done! Positive change is on the way.
"""
var5_4 = """
Unfortunately Hillary Clinton has too many files against her.
Elizabeth Warren has been able to unite the country.
She is the first female President and probably the first to 
give more rights to the native Americans. Well done!
"""
var5_5 = """
Out of the blue, some dark files come up
about the Clinton's dark history. Hillary looses too many
votes to ELizabeth Warren.
Elizabeth Warren has been able to unite the country.
She is the first female President and probably the first to 
give more rights to the native Americans. Well done!
"""
var5_6 = """
Hillary Clinton wins the elections! She is the first female President
of the USA. Well done! Positive change is on the way.
"""
var5_7 = """
Hillary Clinton is about to win the elections. However, she decides
to surrender and let Joe Biden take the lead while she steps back as 
Vice-President. We were so close from getting the first female President of
the USA! Anyway, Biden does a great job at reuniting the country unlike
his predecessor.
"""
var5_8 = """
Out of the blue, a new candidate shows up and gets elected!!! Welcome Obama 
to the 2020 elections and back to his office. Yay, the whole country 
is in ecstasy.
:::::::::::::ccccc::::::;;,,,''',,,,,,,'''..............'',;;;;;;;;;;;;;;;,,,,,,;;;;:::::::::::::ccc::::::::::::::::::::::::::::::::;;;::;;;;;;;;;;;;;
:::::::::::ccccccc:cc:::;;,,,''',,,,'..                    ...',;;;;;;;;;;;;;;;;;;;;::::::::::::cccccccc:::::::::::::::::::::::::::::::::::::::::::::;
:::::::::::::ccccccccc::;;,,,''''...                           ...,;;;;;;;;;;;;;;;;;:::::ccc:::::ccccccccc::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::ccccccc::;;,,,,...                                  .',;;;;;;;;;;;;;;::::cccc::::::::ccccccc:::::::::::::::::::::::::;;:::;::::::::::::
::::::::::::::::ccccccc::;,,'.                                        .';;;;;;;;;;;;:::::::::::;::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;::::;;;;;;;
:::::::::::::::cccccccc::;,.                                            .,:;;;;;;;;;::::::::;;;;;;;;;;;;::;;;;;;;::::::::::;;;;;;;;;;;;;;;;:;;;;;;;;;;
::::::::::::::cccccccccc:,.  ..          ...   .................         .,;;:;;;;;::;;;;;;;;,,,,,,,;;;;;;;;;;;;;:::::::::::::::::::::::::::::::::::::
::::::::::::ccccccccccc:'     .     .. ......'',,;;::::::;;,''....        ..,;;;:::::;;;;;;;,,,,,,,,,,;;;;;;;;;;:::::ccccc::::::::::::::::::::::::::::
::::::::::::cccccccccc:.        .....,,;::;:llllllllccccc::;,,'....         .,:::::::;;;;;;,,,,,,,,,;;;;;;;;;;;:::cccccccccccccccccccccccccccccccccccc
:::::::::::cccccccccc:.      ..'';::cllllollooddooolllllllc::;,'....         .;::::::;;;;;;;;;;;;;;;;;;;;;;;;;:::ccccccccccccccccccccccccccccccccccccc
:::::::::::ccccccccc:'      ..';ccllllllooooddxxddddoooooolcc:;'....          ';:::::;;;;;;;;;;;;;;;;;;;;;;;;;:::ccccccccccccccccccccccccccccccccccccc
::::::::::cccccccccc;.     ..',:cccllooddxxxxxkkkkkxddoooollc:;,'...          .;::::::;;;;;;;;;;;:::::;;;;;;;;:::ccccccccccccccccccccccccccccccccccccc
cc::::::::cccccccccc;.    ...';::ccllodxkkkkkkkkkkkxxdoooolllc:;,'.....        ':::::::;;;;;;;;;::::::::;;;;;::::ccccccccccccccccccccccccccccccccccccc
::::::::::cccccccccc;.   ....',;::cllooddxxkkkkkkxxxxddoooolllc:,'......       .;:::::;;;;;;;;;;:;::::::;;;;;;:::ccccccccccccccccccccccccccccccccccccc
ccc:::::::cccccccccc;.   ....',;;:ccllooddxxxkkkkxxxxxxdddooolc::;,'.....      .;:::::;;;;;;;;;;;;;:::;;;;;;;;::::cccccccccccccccccccccccccccccccccccc
ccccccc:::cccccccccc:.   ....',,;;:clloodxxxkkkkkkkkxxkkxdollc:;;;,'...  .     .,,',::::;;;;;;;;;;;;;;;;;;;;;;::::cccccccccccccccccccccccccccccccccccc
cccccccccccccccccccc:.   ....',;;;:cclodxxkkkkkkkkkkxdddol:,'..          ...   ...  '::;;;;;;;;;;;;;;;;;;;;;;;:::ccccclccccccccccccccccccccccccccccccc
cccccccccccccclcccccc'  .....';::;:cloddxxxxddddoodddolc:'..    ...       ...  ......;;:;;;;;;;;;;;;;;;;::::::::cccccccccccc::::::::::::::::::::::::::
cccccccccccllllllcccc;.  ...';::;;;:looolc:;;,,,,;clool;..........       ..... ......,;:;;;;;;;;;;;;;::::::::::::ccccccccccc::::::::::::::::::::::::::
cccccccllllllllllllll:.   ..,;::;;;::,'...      ..;ldddc'.',',ll,....   ......  .....,;;;;;;;;;;;;;;::::::::::::::ccccccccccccc:::::::::::::::::::::::
ccccccllllllllllllllll,.   .,;;;;;,.....''... ...,:ldkxl;.,:ccc:;,,''.........  .,,..,::;;;;;;;;;;;;::::::::::::::ccccccccccccccccc:::::ccccccccc:cccc
ccccccccclllllllllllllc'.  .';;;;,....''...   .';:ccoddl:'.,:c::::;;;;;;,'..... .;:,.,::;;;;;;;;;;;;::::::::::::::ccccclllllllcccccccccccccccccccccccc
cccccccccccllllllllc;,::,.. .,;;;,,''....;;''',:clllloddc,',;ccc::::cccc;,..... .,:,.,::;;;;;;;;;;;;::::::::::::::ccccllllllllllcccccccccccccccccccccc
ccccccccccccclllllc;..,:clc'.',;;;;,''',::::ccloddooloodo:'.';cllcc:ccc:,'..... ....';:;:;;;;;;;;;;;::::::::::::::cccclllllllllccccccccccccccccccccccc
cccccccccccccllllllc;;cloloc'.,;::c:::cccclodddxxdollooddl;'.',coolc:::;,'..... ....,::::;;;;;;;;;;:::::::::::::::cccclllllllccccccccccllccccccccccccc
cccccccccccccllllllc::coxdc'''',;:clooooddddddxxxdlcloddddo:'',;codol::;'...... ....;:::;;;;;;;;::::::::::::::::::ccccllllllcccccccccccllcccccccllllll
llccccccccccclllllllclllooc;;;'',,;:loodddxxddxxxolclodxxdl;..'..,:lolc;,'.......,',::::;;;;;;:::::::::::::::::::::cccclllcccccccccccccllcclllllllllll
lccccccccccccclllllllllcldoddc,''',;:cllllodddxxdllol::cc:,. ....',;clc:,'......;c::::::;;;;;;:::::::::::::c:::::::cccccccccccccccccccllllllllllllllll
cccccccccccccccclllllllccdxxxl:,.',;::ccclloodxdol:,''','....'',;:c:;;;;,'......;c:::::;;;;;;;;::::::::::::cc:::::::ccccccccccccccccllllllllllllllllll
cccccccccccccccllllllllcclolll:;''',;::::clloddoodl::codl::cc:;;;;;;,...,,......;c:::::;;;;;;;;:::::::::ccccc::::::::cccccccccccccccllllllllllllllllll
ccccccccccccllllllllllllccccccll;''',;:;::cclollodddoollolcloc;;,''.....,;'.....:c:::::;;;;;;;;::::::cccccccc::::::::::cccccccccccclllllllllllllllllll
ccccccccccclllllllllllllccc:::cc;'''',;;;;:ccc:cooollcccc:;:;....    ...,:'.. .,:c:::::;;;;;;;;:::::cccccccccc::::::::::cccccccccllllllllllllllllllllc
ccccccccccclllllllllllllcc::;;,,,,''',,;;;;::;,:c::::;,'............''...'.   .;c:c::::;;;;;;;;::::ccccccccccc::::::::::cccccccccllllllllllllllllllllc
ccccccccccclllllllllllllcc::;,,,,,;,'',,;;,;:,,;,''......',,,,,''''',.. ..    ':c::::::;;;;;;;::::cccccccccccc::::::::::ccccccccclllllllllllllcclllccc
ccccccccccccllllllllllllcc::;,,,,,;;,''',,,,;::;;,;;;;;;:::;;,''''''....      .,::::::::;;;;;;:::cccclllllcccc::::::::::ccccclllllllllllllllcccccccccc
ccccccccccccllllllllllllcc:;;,,,,,,;;,'.''''';:;,;cclllc:;,''''''.......        .';::::;;;;;;:::cccclllllccccc::::::::::cccclllllllllllllllccccccccccc
cccccccccccccclllllllllccc:;;,,,,,;;;;,'......''',;;::::;;,,,''''',;,...       .'..';::;;;;;::::ccccllllcccccc:::::::::cccccccllllllllllllcccccccccccc
cccccccccccccccccllllllcc::;;,,,,,;;;;;,'.....''',;;;;;;;;;;::;;:::;'..       'cc'  .,;;;;;;::::cccccccccccccccc::::::cccccccccccccccccccccccccccccccc
ccccccccccccccccccclccccc::;;,,,,,;;;;;,,'.....''',;:ccclllcccccc:;'..       'ooc'    .,;;::::::ccccccccccccccccc::::ccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccc::;;,,,,,,;;;;;::'.......'';::ccllccc:;;,...      .;ddlc.      .';::::cccccccccccccccccc::::ccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccc::;,,,,,,,;;;;,lkc'''......'',,;;;;;,....        ;dxxdo:.        ..',::ccccccccccccccccc::::ccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccc::;,,,,,,,,;;,.:XOc;,,,'..............          .oOkddo,             ...',;:cccccccccccc:::::cccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccc::;,,,,',,,'.  ;0NKd:;;;,,''....    .          .cxkxxdc.                   ...',;:cccccc::::::cccccccccccccccccccccccccccc:::
ccccccccccccccccccccccccc::;;,,'...     ,0NWNkl:::;;;;,''..            .:xkkxxo'                           ..,;:ccc:::::cccccccccc::::::::::::::::::::
ccccccccccccccccccccccccc::,'..         'ONNWWKxl:;;;;;;,'.    ..   .':dkkkkxd:.                               ...'',,,;::ccc::cc:::::::::::::::::::::
ccccccccccccccccccccccccc;'.            'ONNNWWNOo:;;;;;;'....;dxc;:okO0Oxddxo'                                        ..',::::cc::::::::::::::::::::

"""
var5_9 = """
Elon Musk suddenly runs for Presidency and has a lot of traction.
His positive impact with both SpaceX and Tesla have given him a lot of
interest from younger generations.

Trump is not able to keep up with him.

Elon Musk becomes the new President of the USA!!!
"""
var5_10 = """
Trump is reelected and saves Syria from Erdogan. The electorate loves it.
His polls are better than ever and he is slowly taking back power 
over the chinese influence. You have done a great job for the USA!!!
"""
var5_11 = """
A new candidate comes back from the shadows and gets elected in extremis.

:::::::::::::ccccc::::::;;,,,''',,,,,,,'''..............'',;;;;;;;;;;;;;;;,,,,,,;;;;:::::::::::::ccc::::::::::::::::::::::::::::::::;;;::;;;;;;;;;;;;;
:::::::::::ccccccc:cc:::;;,,,''',,,,'..                    ...',;;;;;;;;;;;;;;;;;;;;::::::::::::cccccccc:::::::::::::::::::::::::::::::::::::::::::::;
:::::::::::::ccccccccc::;;,,,''''...                           ...,;;;;;;;;;;;;;;;;;:::::ccc:::::ccccccccc::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::ccccccc::;;,,,,...                                  .',;;;;;;;;;;;;;;::::cccc::::::::ccccccc:::::::::::::::::::::::::;;:::;::::::::::::
::::::::::::::::ccccccc::;,,'.                                        .';;;;;;;;;;;;:::::::::::;::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;::::;;;;;;;
:::::::::::::::cccccccc::;,.                                            .,:;;;;;;;;;::::::::;;;;;;;;;;;;::;;;;;;;::::::::::;;;;;;;;;;;;;;;;:;;;;;;;;;;
::::::::::::::cccccccccc:,.  ..          ...   .................         .,;;:;;;;;::;;;;;;;;,,,,,,,;;;;;;;;;;;;;:::::::::::::::::::::::::::::::::::::
::::::::::::ccccccccccc:'     .     .. ......'',,;;::::::;;,''....        ..,;;;:::::;;;;;;;,,,,,,,,,,;;;;;;;;;;:::::ccccc::::::::::::::::::::::::::::
::::::::::::cccccccccc:.        .....,,;::;:llllllllccccc::;,,'....         .,:::::::;;;;;;,,,,,,,,,;;;;;;;;;;;:::cccccccccccccccccccccccccccccccccccc
:::::::::::cccccccccc:.      ..'';::cllllollooddooolllllllc::;,'....         .;::::::;;;;;;;;;;;;;;;;;;;;;;;;;:::ccccccccccccccccccccccccccccccccccccc
:::::::::::ccccccccc:'      ..';ccllllllooooddxxddddoooooolcc:;'....          ';:::::;;;;;;;;;;;;;;;;;;;;;;;;;:::ccccccccccccccccccccccccccccccccccccc
::::::::::cccccccccc;.     ..',:cccllooddxxxxxkkkkkxddoooollc:;,'...          .;::::::;;;;;;;;;;;:::::;;;;;;;;:::ccccccccccccccccccccccccccccccccccccc
cc::::::::cccccccccc;.    ...';::ccllodxkkkkkkkkkkkxxdoooolllc:;,'.....        ':::::::;;;;;;;;;::::::::;;;;;::::ccccccccccccccccccccccccccccccccccccc
::::::::::cccccccccc;.   ....',;::cllooddxxkkkkkkxxxxddoooolllc:,'......       .;:::::;;;;;;;;;;:;::::::;;;;;;:::ccccccccccccccccccccccccccccccccccccc
ccc:::::::cccccccccc;.   ....',;;:ccllooddxxxkkkkxxxxxxdddooolc::;,'.....      .;:::::;;;;;;;;;;;;;:::;;;;;;;;::::cccccccccccccccccccccccccccccccccccc
ccccccc:::cccccccccc:.   ....',,;;:clloodxxxkkkkkkkkxxkkxdollc:;;;,'...  .     .,,',::::;;;;;;;;;;;;;;;;;;;;;;::::cccccccccccccccccccccccccccccccccccc
cccccccccccccccccccc:.   ....',;;;:cclodxxkkkkkkkkkkxdddol:,'..          ...   ...  '::;;;;;;;;;;;;;;;;;;;;;;;:::ccccclccccccccccccccccccccccccccccccc
cccccccccccccclcccccc'  .....';::;:cloddxxxxddddoodddolc:'..    ...       ...  ......;;:;;;;;;;;;;;;;;;;::::::::cccccccccccc::::::::::::::::::::::::::
cccccccccccllllllcccc;.  ...';::;;;:looolc:;;,,,,;clool;..........       ..... ......,;:;;;;;;;;;;;;;::::::::::::ccccccccccc::::::::::::::::::::::::::
cccccccllllllllllllll:.   ..,;::;;;::,'...      ..;ldddc'.',',ll,....   ......  .....,;;;;;;;;;;;;;;::::::::::::::ccccccccccccc:::::::::::::::::::::::
ccccccllllllllllllllll,.   .,;;;;;,.....''... ...,:ldkxl;.,:ccc:;,,''.........  .,,..,::;;;;;;;;;;;;::::::::::::::ccccccccccccccccc:::::ccccccccc:cccc
ccccccccclllllllllllllc'.  .';;;;,....''...   .';:ccoddl:'.,:c::::;;;;;;,'..... .;:,.,::;;;;;;;;;;;;::::::::::::::ccccclllllllcccccccccccccccccccccccc
cccccccccccllllllllc;,::,.. .,;;;,,''....;;''',:clllloddc,',;ccc::::cccc;,..... .,:,.,::;;;;;;;;;;;;::::::::::::::ccccllllllllllcccccccccccccccccccccc
ccccccccccccclllllc;..,:clc'.',;;;;,''',::::ccloddooloodo:'.';cllcc:ccc:,'..... ....';:;:;;;;;;;;;;;::::::::::::::cccclllllllllccccccccccccccccccccccc
cccccccccccccllllllc;;cloloc'.,;::c:::cccclodddxxdollooddl;'.',coolc:::;,'..... ....,::::;;;;;;;;;;:::::::::::::::cccclllllllccccccccccllccccccccccccc
cccccccccccccllllllc::coxdc'''',;:clooooddddddxxxdlcloddddo:'',;codol::;'...... ....;:::;;;;;;;;::::::::::::::::::ccccllllllcccccccccccllcccccccllllll
llccccccccccclllllllclllooc;;;'',,;:loodddxxddxxxolclodxxdl;..'..,:lolc;,'.......,',::::;;;;;;:::::::::::::::::::::cccclllcccccccccccccllcclllllllllll
lccccccccccccclllllllllcldoddc,''',;:cllllodddxxdllol::cc:,. ....',;clc:,'......;c::::::;;;;;;:::::::::::::c:::::::cccccccccccccccccccllllllllllllllll
cccccccccccccccclllllllccdxxxl:,.',;::ccclloodxdol:,''','....'',;:c:;;;;,'......;c:::::;;;;;;;;::::::::::::cc:::::::ccccccccccccccccllllllllllllllllll
cccccccccccccccllllllllcclolll:;''',;::::clloddoodl::codl::cc:;;;;;;,...,,......;c:::::;;;;;;;;:::::::::ccccc::::::::cccccccccccccccllllllllllllllllll
ccccccccccccllllllllllllccccccll;''',;:;::cclollodddoollolcloc;;,''.....,;'.....:c:::::;;;;;;;;::::::cccccccc::::::::::cccccccccccclllllllllllllllllll
ccccccccccclllllllllllllccc:::cc;'''',;;;;:ccc:cooollcccc:;:;....    ...,:'.. .,:c:::::;;;;;;;;:::::cccccccccc::::::::::cccccccccllllllllllllllllllllc
ccccccccccclllllllllllllcc::;;,,,,''',,;;;;::;,:c::::;,'............''...'.   .;c:c::::;;;;;;;;::::ccccccccccc::::::::::cccccccccllllllllllllllllllllc
ccccccccccclllllllllllllcc::;,,,,,;,'',,;;,;:,,;,''......',,,,,''''',.. ..    ':c::::::;;;;;;;::::cccccccccccc::::::::::ccccccccclllllllllllllcclllccc
ccccccccccccllllllllllllcc::;,,,,,;;,''',,,,;::;;,;;;;;;:::;;,''''''....      .,::::::::;;;;;;:::cccclllllcccc::::::::::ccccclllllllllllllllcccccccccc
ccccccccccccllllllllllllcc:;;,,,,,,;;,'.''''';:;,;cclllc:;,''''''.......        .';::::;;;;;;:::cccclllllccccc::::::::::cccclllllllllllllllccccccccccc
cccccccccccccclllllllllccc:;;,,,,,;;;;,'......''',;;::::;;,,,''''',;,...       .'..';::;;;;;::::ccccllllcccccc:::::::::cccccccllllllllllllcccccccccccc
cccccccccccccccccllllllcc::;;,,,,,;;;;;,'.....''',;;;;;;;;;;::;;:::;'..       'cc'  .,;;;;;;::::cccccccccccccccc::::::cccccccccccccccccccccccccccccccc
ccccccccccccccccccclccccc::;;,,,,,;;;;;,,'.....''',;:ccclllcccccc:;'..       'ooc'    .,;;::::::ccccccccccccccccc::::ccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccc::;;,,,,,,;;;;;::'.......'';::ccllccc:;;,...      .;ddlc.      .';::::cccccccccccccccccc::::ccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccc::;,,,,,,,;;;;,lkc'''......'',,;;;;;,....        ;dxxdo:.        ..',::ccccccccccccccccc::::ccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccc::;,,,,,,,,;;,.:XOc;,,,'..............          .oOkddo,             ...',;:cccccccccccc:::::cccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccc::;,,,,',,,'.  ;0NKd:;;;,,''....    .          .cxkxxdc.                   ...',;:cccccc::::::cccccccccccccccccccccccccccc:::
ccccccccccccccccccccccccc::;;,,'...     ,0NWNkl:::;;;;,''..            .:xkkxxo'                           ..,;:ccc:::::cccccccccc::::::::::::::::::::
ccccccccccccccccccccccccc::,'..         'ONNWWKxl:;;;;;;,'.    ..   .':dkkkkxd:.                               ...'',,,;::ccc::cc:::::::::::::::::::::
ccccccccccccccccccccccccc;'.            'ONNNWWNOo:;;;;;;'....;dxc;:okO0Oxddxo'                                        ..',::::cc::::::::::::::::::::

"""
var5_12 = """
Trump gets elected anyway because he has done a good job
at "Making America Great Again". He is now "Keeping America Great".

Well done, you have been able to keep the status quo
and prevent any unexpected events from happening!!
"""
var5_13 = """
Trump stays in power. He is reelected.
The global tensions are at their peak and a nuclear exchange is expected
between China and the US. The country is about to implode.

You have failed to your mission.
Unless your mission was to implode the country...
"""
var5_14 = """
Trump is reelected and decides to bomb North Korea. The strategic bombing
has killed the government officials without touching civilians.
North Koreans are now free from the former dictatorship.

Well done! You are a warrior and a keeper of democracy.
"""
var5_15 = """

Trump is reelected and slowly moving his speeches toward 
peace talks between the USA and China.

Well done! You have seen in the current president an ability
to play multiple hats when the people ask for it.
"""
var5_16 = """
Trump keeps his promise of uniting the country.
However as soon as he is elected he decides that
"to keep America Great" he will need to fight Danish
people over Greenland. As he does so, Europe breaks ties 
with the US, as well as China.

The whole world is now against the US because of Trump.
"""


def start():
    """ This function takes no argument and is called to begin the game"""
    while True:
        try:
            name = str(input("Please enter your name here to get started: "))
            print('Enter your password to continue')
            print("Hint: the password is the year of the 2020 elections") 
            count = 0
            while count < 3:
                username = name
                password = input('Enter password: ')
                if password == "2020" and username == name:
                    print('Access granted')
                    input('<Press any key to continue>\n')
                    print(f"""Hi {name}, You are accessing an NSA Confidential File.
This file will enable you to decide on
the outcomes of the 2020 elections!\n""")
                    break
                else:
                    print('Access denied. Try again.')
                    count += 1
            break
        except ValueError:
            print(f"Oops! {name} is not a valid name.  Try again...")
            start()
    if count == 3:
        jail()
    else:
        step1()


def step1():
    print("Press 1 to start.")
    print("Press 2 to stop.")

    choice = input("<Waiting for your input> ")
    if choice == '1':
        step_2()  # This moves us into step_2

    elif choice == '2':
        jail()  # This stops the process

    else:
        print("Invalid entry. Please try again.\n")
        start()  # Brings us back to the beginning of step_0 to try again


def step_2():
    print("Let's decide on Trump's destiny!\n")
    input('<Press any key to continue>\n')

    print("Press 1 if you want Trump impeached.")
    print("Press 2 if you do not want Trump impeached.")
    print("Press 3 to stop the conspiracy")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step2_1()  # This moves us into step2_1

    if choice == '2':
        step2_2()  # This moves us into step2_2

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step_2()  # Brings us back to the beginning of current step to try again


def step2_1():
    print("Great choice!\n")
    input('<Press any key to continue>\n')

    print(f"Press 1 if you like Bernie Sanders.")
    print(f"Press 2 if you would like an alternative to Bernie.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step3_1()  # This moves us into step3 choice 1

    if choice == '2':
        step3_2()  # This moves us into step3 choice 2

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step2_1()  # Brings us back to beginning of current step to try again


def step2_2():
    print("Good choice!\n")
    input('<Press any key to continue>\n')

    print("Press 1 if you trust Trump.")
    print("Press 2 if you do not trust Trump.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step3_3()  # This moves us into step_2

    if choice == '2':
        step3_4()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step2_2()  # Brings us back to beginning of current step to try again


def step3_1():
    input('<Press any key to continue>\n')

    print("Press 1 to help Bernie be a better candidate.")
    print("Press 2 to see how he will compare to his female counter parts.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step4_1()  # This moves us into step_2

    if choice == '2':
        step4_2()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step3_1()  # Brings us back to beginning of current step to try again


def step3_2():
    input('<Press any key to continue>\n')

    print("Press 1 to push Hillary Clinton up in the polls.")
    print("Press 2 if you think she needs to prove herself next to other running candidates.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step4_3()  # This moves us into step_2

    if choice == '2':
        step4_4()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step3_2()  # Brings us back to beginning of current step to try again


def step3_3():
    input('<Press any key to continue>\n')

    print("Press 1 if you like Trump's tweets.")
    print("Press 2 if you are shocked by some or all of his tweets.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step4_5()  # This moves us into step_2

    if choice == '2':
        step4_6()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step3_3()  # Brings us back to beginning of current step to try again


def step3_4():
    input('<Press any key to continue>\n')

    print("Press 1 to test Trumps promises to the People.")
    print("Press 2 if you think that he keeps his words.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step4_7()  # This moves us into step_2

    if choice == '2':
        step4_8()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step3_4()  # Brings us back to beginning of current step to try again


def step4_1():
    input('<Press any key to continue>\n')

    print("Press 1 if you think Bernie will be a good President.")
    print("Press 2 if you think that his socialist views are not good for the future of the US .")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step5_1()  # This moves us into step_2

    if choice == '2':
        step5_2()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step4_1()  # Brings us back to beginning of current step to try again


def step4_2():
    input('<Press any key to continue>\n')

    print("Press 1 if you would love to see another female than Hillary Clinton President.")
    print("Press 2 if you think that Hillary Clinton is better than Bernie and any other female candidate.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step5_3()  # This moves us into step_2

    if choice == '2':
        step5_4()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step4_2()  # Brings us back to beginning of current step to try again


def step4_3():
    input('<Press any key to continue>\n')

    print("Press 1 if you want to vote for Hillary Clinton.")
    print("Press 2 if you do not want a female in power but still like Hillary.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step5_5()  # This moves us into step_2

    if choice == '2':
        step5_6()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step4_3()  # Brings us back to beginning of current step to try again


def step4_4():
    input('<Press any key to continue>\n')

    print("Press 1 if you think that Hillary Clinton did her time and should retire.")
    print("Press 2 if you think that a surprise candidate would be better!")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step5_7()  # This moves us into step_2

    if choice == '2':
        step5_8()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step4_4()  # Brings us back to beginning of current step to try again


def step4_5():
    input('<Press any key to continue>\n')

    print("Press 1 if you prefer Elon Musk and his tweets.")
    print("Press 2 if you think that Trump should go to war as much as he tweets.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step5_9()  # This moves us into step_2

    if choice == '2':
        step5_10()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step4_5()  # Brings us back to beginning of current step to try again


def step4_6():
    input('<Press any key to continue>\n')

    print("Press 1 if you are outraged by Trump's tweets and want Obama back.")
    print("Press 2 if you would still vote for Trump after his shocking tweets.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step5_11()  # This moves us into step_2

    if choice == '2':
        step5_12()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step4_6()  # Brings us back to beginning of current step to try again


def step4_7():
    input('<Press any key to continue>\n')

    print("Press 1 if you are benefiting from the Trade War .")
    print("Press 2 if you think that North Korea should respect democracy and that the US should step in.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step5_13()  # This moves us into step_2

    if choice == '2':
        step5_14()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step4_7()  # Brings us back to beginning of current step to try again


def step4_8():
    input('<Press any key to continue>\n')

    print("Press 1 to push Trump to look for peace in world (might not happen).")
    print("Press 2 to let Trump do exactly what he is planning to do.")
    print("Press 3 to stop the conspiracy.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        step5_15()  # This moves us into step_2

    if choice == '2':
        step5_16()  # This moves us into stepN+1_n

    elif choice == '3':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step4_8()  # Brings us back to beginning of current step to try again


def step5_1():
    input('<Press any key to continue>\n')

    print(f"{var2_1}{var3_1}{var4_1}{var5_1}")

    input('<Press any key to continue>\n')

    step_end()


def step5_2():
    input('<Press any key to continue>\n')

    print(f"{var2_1}{var3_1}{var4_1}{var5_2}")

    input('<Press any key to continue>\n')

    step_end()


def step5_3():
    input('<Press any key to continue>\n')

    print(f"{var2_1}{var3_1}{var4_2}{var5_3}")

    input('<Press any key to continue>\n')

    step_end()


def step5_4():
    input('<Press any key to continue>\n')

    print(f"{var2_1}{var3_1}{var4_2}{var5_4}")

    input('<Press any key to continue>\n')

    step_end()


def step5_5():
    input('<Press any key to continue>\n')

    print(f"{var2_1}{var3_2}{var4_3}{var5_5}")

    input('<Press any key to continue>\n')

    step_end()


def step5_6():
    input('<Press any key to continue>\n')

    print(f"{var2_1}{var3_2}{var4_3}{var5_6}")

    step_end()


def step5_7():
    input('<Press any key to continue>\n')

    print(f"{var2_1}{var3_2}{var4_4}{var5_7}")

    input('<Press any key to continue>\n')

    step_end()


def step5_8():
    input('<Press any key to continue>\n')

    print(f"{var2_1}{var3_2}{var4_4}{var5_8}")

    input('<Press any key to continue>\n')

    step_end()


def step5_9():
    input('<Press any key to continue>\n')

    print(f"{var2_2}{var3_3}{var4_5}{var5_9}")

    input('<Press any key to continue>\n')

    step_end()


def step5_10():
    input('<Press any key to continue>\n')

    print(f"{var2_2}{var3_3}{var4_5}{var5_10}")

    input('<Press any key to continue>\n')

    step_end()


def step5_11():
    input('<Press any key to continue>\n')

    print(f"{var2_2}{var3_3}{var4_6}{var5_11}")

    input('<Press any key to continue>\n')

    step_end()


def step5_12():
    input('<Press any key to continue>\n')

    print(f"{var2_2}{var3_3}{var4_6}{var5_12}")

    input('<Press any key to continue>\n')

    step_end()


def step5_13():
    input('<Press any key to continue>\n')

    print(f"{var2_2}{var3_4}{var4_7}{var5_13}")

    input('<Press any key to continue>\n')

    jail()


def step5_14():
    input('<Press any key to continue>\n')

    print(f"{var2_2}{var3_4}{var4_8}{var5_14}")

    input('<Press any key to continue>\n')

    step_end()


def step5_15():
    input('<Press any key to continue>\n')

    print(f"{var2_2}{var3_4}{var4_7}{var5_15}")

    input('<Press any key to continue>\n')

    step_end()


def step5_16():
    input('<Press any key to continue>\n')

    print(f"{var2_2}{var3_4}{var4_8}{var5_16}")

    input('<Press any key to continue>\n')

    step_end()


def jail():
    print("""
    You are on trial for your unlawful behavior.
    You've been found guilty for accessing confidential NSA documents
    and will spend the rest of your life into jail
    for playing on people's lives with your conspiracy theories!
    """)
    # declaring an object to contain the number of counts
    count = 20

    # looping while count is greater than zero
    while count > 0:
        count = count - 1
        input("<Press any key as mamy times as you can to escape to Russia>\n")

    # Out of Russia!
    print("Yay! You are out of the country and on your way to Russia!")

    step_end()

def step_end():

    print(
        """
        *******************************************************************************************
        Scroll down
        *******************************************************************************************
    
      / ____|         | | |  _ \| |                           
     | |  __  ___   __| | | |_) | | ___  ___ ___              
     | | |_ |/ _ \ / _` | |  _ <| |/ _ \/ __/ __|             
     | |__| | (_) | (_| | | |_) | |  __/\__ \__ \             
      \_____|\___/ \__,_| |____/|_|\___||___/___/ _           
     | | | |          | |  | |     (_) |         | |          
     | |_| |__   ___  | |  | |_ __  _| |_ ___  __| |          
     | __| '_ \ / _ \ | |  | | '_ \| | __/ _ \/ _` |          
     | |_| | | |  __/ | |__| | | | | | ||  __/ (_| |          
      \__|_| |_|\___| _\____/|_| |_|_|\__\___|\__,_|          
      / ____| |      | |                                      
     | (___ | |_ __ _| |_ ___  ___                            
      \___ \| __/ _` | __/ _ \/ __|                           
      ____) | || (_| | ||  __/\__ \                           
     |_____/ \__\__,_|\__\___||___/            _              
            / _|     /\                       (_)             
       ___ | |_     /  \   _ __ ___   ___ _ __ _  ___ __ _    
      / _ \|  _|   / /\ \ | '_ ` _ \ / _ \ '__| |/ __/ _` |   
     | (_) | |    / ____ \| | | | | |  __/ |  | | (_| (_| |_  
      \___/|_|   /_/    \_\_| |_| |_|\___|_|  |_|\___\__,_( ) 
     | | | |                                              |/  
     | |_| |__   ___                                          
     | __| '_ \ / _ \                                         
     | |_| | | |  __/                                         
      \__|_| |_|\___|                                         
         | |                                                  
       __| | ___ _ __ ___   ___   ___ _ __ __ _  ___ _   _    
      / _` |/ _ \ '_ ` _ \ / _ \ / __| '__/ _` |/ __| | | |   
     | (_| |  __/ | | | | | (_) | (__| | | (_| | (__| |_| |   
      \__,_|\___|_| |_| |_|\___/ \___|_|  \__,_|\___|\__, |   
                     | | | | | |                      __/ |   
       __ _ _ __   __| | | |_| |__   ___             |___/    
      / _` | '_ \ / _` | | __| '_ \ / _ \                     
     | (_| | | | | (_| | | |_| | | |  __/                     
      \__,_|_| |_|\__,_|  \__|_| |_|\___|   ___               
                           |__ \ / _ \__ \ / _ \              
      _ __   _____      __    ) | | | | ) | | | |             
     | '_ \ / _ \ \ /\ / /   / /| | | |/ /| | | |             
     | | | |  __/\ V  V /   / /_| |_| / /_| |_| |             
     |_|_|_|\___| \_/\_/  _|____|\___/____|\___/ _            
     |  __ \             (_)   | |          | | | |           
     | |__) | __ ___  ___ _  __| | ___ _ __ | |_| |           
     |  ___/ '__/ _ \/ __| |/ _` |/ _ \ '_ \| __| |           
     | |   | | |  __/\__ \ | (_| |  __/ | | | |_|_|           
     |_|   |_|  \___||___/_|\__,_|\___|_| |_|\__(_)
    
        *******************************************************************************************
        PS: if you have not yet found the Easter egg
        you will need to play again.
    
        HINT : Impeach Trump and keep choosing
        the second option!
        *******************************************************************************************
    
        """)
    print("Press 1 to restart the game.")
    print("Press 2 to stop escape to Russia before getting caught by the FBI.")

    choice = input("<Waiting for your input> ")

    if choice == '1':
        start()  # This moves us to the start

    elif choice == '2':
        jail()  # This moves us to jail

    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')

        step_end()


start()
