def actCall(act, target, actor):
    if act.name == 'Talk':
        if currRoute == "Neutral":
            if actNum[0] == 0:
                actReturn = [[f"* Look, we're not looking for trouble.", actor.name], [f"* Can we settle this peacefully?", actor.name],
                             f"* But {target.name} refuse to hear {actor.name} out."]
            elif actNum[0] == 1:
                actReturn = [[f"* Please let us go.", actor.name], [f"* We aren't looking for a conflict right now.", actor.name],
                             f"* But {target.name} once again, refuse to hear {actor.name} out."]
            elif actNum[0] == 2:
                actReturn = [[f"* Surely we can work something out right?", actor.name], [f"* Let's just try to settle things.", actor.name],
                             f"* But {target.name} looked away."]
            else:
                actReturn = [[f"* I don't really know what to say now...", actor.name]]
            actNum[0] += 1
        elif currRoute == "Mercy":
            if actNum[1] == 0:
                actReturn = [f"* You try to reason peacefully.", f"* {target.name} simply ignores you."]
            elif actNum[1] == 1:
                actReturn = [f"* You told him how there is a better way.", f"* {target.name} refused to acknowledge."]
            elif actNum[1] == 2:
                actReturn = [f"* You try to reach to the good buried in him.", f"* ...", f"* But... nothing changed."]
            elif actNum[1] == 3:
                actReturn = [f"* You try to reach for words.", "* Nothing came out.", "* Yet...", "* You sense there might be a way..."]
            else:
                actReturn = [f"* End the talking, keep going."]
            actNum[1] += 1
        elif currRoute == "Fight":
            actReturn = [f"* You told him how the world is better off without him.", f"* {target.name} shook for a moment, but regain his composure."]
        elif currRoute == "Sadism":
            actReturn = [f"* You talk in peace, to trick him with talking.", f"* {target.name} sees through your facade."]
        
        return actReturn
actNum = [0, 0, 0, 0]
def onStart():
    setVar('useCustomDialogue', True)
    setVar('useExtraDialogue', False)
    setVar('useDodgeEquation', True)
    setVar('useDefensePercent', False)
    setVar('stuff', 'Skeleton-joke')
    setVar('speedBasedTurn', True)
    Opponent = getVar('opponentObj')
    theEnemy = getVar('opponent')
    theEnemy.clear()
    theEnemy.append(Opponent['Skeleton'])
    Player = getVar('playerObj')
    theAlly = getVar('party')
    theAlly.clear()
    theAlly.append(Player['Rany'])
    theAlly[0].skills[0].cost = 40
    theAlly[0].skills[0].baseNum = -80
    theAlly.append(Player['Rekety'])
    theAlly[0].skills.append(getVar('skillObj')['Guard Up'])
    theAlly[1].skills.append(getVar('skillObj')['Focus'])
    theAlly[1].skills.append(getVar('skillObj')['Power Slash'])
    theAlly[1].skills[0].cost = 30
    theAlly[1].skills[1].cost = 50
    for i in theAlly:
        i.level = 21
        i.levelUp(0)
        i.hpSet()
    addTurnDialogue('Clear')
    #addTurnDialogue(None, "A warrior block your path!", 0, None)
    #addTurnDialogue('Allerwave', "Try [orange]CANCEL[/orange] on the next dialogue!", 0, None)
    #addTurnDialogue('Allerwave', "E E E E E E E E E E E E E E E E E E E E E E  E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E ", 0, None)
    #addTurnDialogue('Allerwave', "Anyway, let's begin.", 0, None)
    #addTurnDialogue('Allerwave', "Note that this tutorial is not the final version.", 0, None)

game_state = "Ally Turn"
missCount = 0
subtractTurn = 0
fightDialogue = [
    ["You two have the biggest mistake of your life."],
    ["Deciding to step foot in [red]MY[/red] domain?"],
    ["Well guess what, you have dragged yourselves to your death."],
    ["Ah... I see.", "So your guys are [red]FIGHT[/red]ers huh?", "Don't worry...", "I have killed and been killed COUNTLESS times...", "I can handle it."],
    ["How rude of me, I have not introduced myself yet.", "They call me [black]'Skeleton joke'[/black].", "I know they gave me that name to mock me...", "But what other choice do I have?"],
    ["I can see you guys are more like me, being pure evil.", "I'm starting to wonder how much [red]Execution Points[/red] the two of you have gained..."],
    ["Are you guys dealing with your opponents with violence?", "Or with [#bb0000]Betrayal[/#bb0000] perhaps..?"],
    ["So many questions..", "Yet so much that stays untold..."],
    ["[shake]HOW MANY [red]HITS[/red] WILL IT TAKE FOR YOU TO DIE?!![/shake]"]
    ]

mercyDialogue = [
    ["You two have the biggest mistake of your life."],
    ["Deciding to step foot in [red]MY[/red] domain?"],
    ["Well guess what, you have dragged yourselves to your death."],
    ["The death [cyan]YOU[/cyan] can't escape, no matter what you do..."],
    ["How rude of me, I have not introduced myself yet.", "They call me [black]'Skeleton joke'[/black].", "I know they gave me that name to mock me...", "But what other choice do I have?"],
    ["I used to be pure... just like you guys..."],
    ["I don't really know much about my past life...", "Because I have been driven insane in this hellhole."],
    ["I can only remember me like this...", "Then I started to feel worried about myself..."],
    ["There is a [blue]Man[/blue] that's holding all the cards.", "[blue]He's[/blue] responsible for all the mess that happened in the first place.", "[blue]He[/blue] keeps me here and use me like a [blue]puppet[/blue]."],
    ["That [blue]Man[/blue] is dangerous.", "If [blue]he[/blue] spots you.", "You will be done for."],
    ["I am doing you guys a favour!", "Trust me!", "You don't wanna end up like me!!", "Don't you understand?", "No one has made it out unspotted.", "The [blue]Man[/blue] is always watching us from above!!"],
    ["Now, do me a favour...", "...and just stay still..."],
    ["..."]
    ]

abortDialogue = [
    ["Sparing me? After you [red]FIGHT[/red]?"],
    ["Talking? You're just wasting your time.", "I already see your true nature..."],
    ["Wasting your time again Talking huh?", "You really are a fool."],
    ["Don't bother."],
    ["Checking my stats, how pathetic."],
    ["You're wasting your time."],
    ["So you dare to [red]Attack[/red]...", "Heh...", "I was correct about you all..."]
    ]

mercySpare = [
    ["Sparing me...", "You know that is futile."],
    ["..."],
    ]

mercyTalk = [
    ["You can't Talk your way out this time."],
    ["Why do this again?"],
    ["..."]
    ]

actCheck = [
    ["You really wanna spend your time checking?"],
    ["..."]
    ]

splashText_Neutral = ["You are faced with the enemy.",
                      "The environment feels tense.",
                      "[red]Fight[/red] or [cyan]Act[/cyan]. The outcome may differ.",
                      "Maybe he has a reason for his cruelty.",
                      "Maybe he is irredeemable like many.",
                      "..."
                      ]

splashTextNum = 0

splashText_Fight = ["Get rid of the warrior.",
                    "You sense evil emanating from him.",
                    "The world is better without him",
                    "He must [#bb0000]die[/#bb0000].",
                    "Don't try to negotiate, he won't listen.",
                    "Kill him for the good of the world."]

splashText_Mercy = ["You sense something tragic.",
                    "Listening might be key.",
                    "He is corrupted, but not irredeemable.",
                    "Negotiation may be useless. Listening might help.",
                    "Don't try to [red]attack[/red], it may trigger him."]

splashText_Betrayal = ["[red]Fighting[/red] at his weakest.",
                       "Cruelty pulse through your veins.",
                       "Mercy is just a guise.",
                       "Provocation.",
                       "You smiled."]

splashText_Attack = ["Prepare to [red]Fight[/red].",
                     "Prepare to [red]kill[/red].",
                     "You feel like you should not be doing this.",
                     "Strike the foe with glee."]

splashText_Down = ["One of your ally is down.",
                   "An ally is down... useless",
                   "An ally is down, keep persisting.",
                   "The pain of your ally. It fills you with [i]pleasure[/i]."
                   ]

splashText_Final_Mercy = ["Go Purify"]
currRoute = 'Neutral'
dialogueTurn = -1

def hsv(h=0, s=1.0, v=1.0):
    """
    Convert HSV (Hue in degrees) to RGB (0–255 format).
    Hue: 0–360 degrees
    Saturation and Value: 0.0–1.0
    """
    if not (0 <= h <= 360):
        raise ValueError("Hue must be between 0 and 360 degrees")
    if not (0.0 <= s <= 1.0):
        raise ValueError("Saturation must be between 0.0 and 1.0")
    if not (0.0 <= v <= 1.0):
        raise ValueError("Value must be between 0.0 and 1.0")

    # Normalize hue to 0.0–1.0 for colorsys
    h_normalized = h / 360.0

    r, g, b = colorsys.hsv_to_rgb(h_normalized, s, v)
    return (int(r * 255), int(g * 255), int(b * 255))


hey = loadMenu
def loadMenu():
    hey(hsv(0, 1, (math.sin(frame/25)+1)/2), (0, 0, 0, 0))

    centerX = hudRect[0]
    centerY = hudRect[1]
    hudLength = hudRect[2]
    hudHeight = hudRect[3]
    hudX = hudRect[4]
    hudY = hudRect[5]
    thickness = hudRect[6]
    #drawRect(hud, borderColor, (hudX, hudY, hudLength, hudHeight)) # The HPBG one
    #for i in range(1, 5):
        #drawRect(hud, (0, 0, 0, i*255/5), (hudX + thickness, hudY + thickness + (i-5)*20, hudLength - (2*thickness), hudHeight - (2*thickness) - (i-5)*10)) # The MAX HP one
def onUpdate():
    backGroundScreen.surface.set_alpha(100)
    global game_state, missCount, subtractTurn, splashTextNum, dialogueTurn, currRoute
    #return False
    backGroundScreen.fill((0, 0, 0, 255))
    hud.camera_rotation = math.sin(frame/15)
    #hud.camera_zoom = (math.sin(frame/15)+2)/2.3
    if 1==0:
        backGroundScreen.camera_rotation = 3*math.sin(frame/20)
        backGroundScreen.camera_zoom = (abs(math.cos(frame/10))+1.5)
    for i in range(0, 11):
        drawRect(backGroundScreen.surface, (min(i*10, 255), min(i*10, 255), min(i*10, 255)) ,(0, 0+i*40+20*math.sin(frame/20+i), width, height-i*80+10*math.cos(frame/20+i)))
    if getVar('allyTurn') == True:
        game_state = 'Ally Turn'
    if getVar('enemyTurn') == True and not game_state == 'Not Enemy Turn':
        game_state = 'Enemy Turn'
    #if getVar('enemyTurn') == False:
        #game_state = 'Not Enemy Turn'

    if game_state == 'Ally Turn':
        currSplashText = splashText_Neutral
        if currRoute == 'Mercy':
            currSplashText = splashText_Mercy
        elif currRoute == 'Sadism':
            currSplashText = splashText_Betrayal
        elif currRoute == 'Fight':
            currSplashText = splashText_Fight
        setTurnText(currSplashText[splashTextNum], None)
        #game_state = 'done'
        if getVar('allyTurn') == False:
            splashTextNum += 1
            if splashTextNum == len(currSplashText):
                splashTextNum = len(currSplashText) - 1
            game_state = 'Not Ally Turn'
    if game_state == 'Enemy Turn':
        turnCount = getVar('turn')
        dialogueTurn += 1
        currDialogue = fightDialogue
        if currRoute == 'Mercy':
            currDialogue = mercyDialogue
        if len(currDialogue) > dialogueTurn:
            for i in currDialogue[dialogueTurn]:
                addTurnDialogue(None, i, turnCount, None)
        game_state = 'Not Enemy Turn'
    if dialogueTurn == 2 and game_state == 'Not Ally Turn':
        currRoute = 'Mercy'
        splashTextNum = 0
        for i in getVar('party'):
            if i.activity == 'Attack_crit' or i.activity == 'Attack_hit' or i.activity == 'Attack_blocked':
                currRoute = 'Fight'
                break
    elif dialogueTurn > 2:
        for i in getVar('party'):
            if i.activity == 'Attack_crit' or i.activity == 'Attack_hit' or i.activity == 'Attack_blocked':
                if currRoute == 'Mercy':
                    currRoute = 'Sadism'
                    splashTextNum = 0
                    for j in abortDialogue[6]:
                        dialogueTurn = 4
                        addTurnDialogue(None, j, getVar('turn') + 1, None)
        
        

    #for i in range
