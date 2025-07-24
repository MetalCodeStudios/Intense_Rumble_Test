def actCall(act, target, actor):
    actReturn = None
    if act.name == 'Talk':
        actReturn = ["* You tried striking a conversation.", f"* {target.name} does not seems to be interested."]

        #return actReturn
    if act.name == "Sparing":
        actReturn = [["* ...", actor.name], f"* {actor.name} looked at you in expectation."]
        
    return actReturn
actNum = [0, 0, 0, 0]
def onStart():
    setVar('useCustomDialogue', False)
    setVar('useExtraDialogue', True)
    setVar('useDodgeEquation', False)
    setVar('useDefensePercent', True)
    setVar('stuff', 'ZephyrMusic')
    setVar('speedBasedTurn', True)
    setVar('allowWin', False)
    #turnDialogue.clear()
    #addTurnDialogue(None, "You are now testing Endless Mode.", 0, None)
    #addTurnDialogue('Allerwave', "Try [orange]CANCEL[/orange] on the next dialogue!", 0, None)
    #addTurnDialogue('Allerwave', "E E E E E E E E E E E E E E E E E E E E E E  E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E ", 0, None)
    #addTurnDialogue('Allerwave', "Anyway, let's begin.", 0, None)
    #addTurnDialogue('Allerwave', "Note that this tutorial is not the final version.", 0, None)

game_state = "Ally Turn"
missCount = 0
subtractTurn = 0

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
destroyed = False

def buildEnemyList(validEnemy, desired_length):
    validEnemy = copy.deepcopy(validEnemy)
    random.shuffle(validEnemy)
    if desired_length > len(validEnemy):
        raise ValueError("Requested list length exceeds number of unique valid enemies.")

    selected_enemies = []               # The grand list we’re building
    used_enemies = set()               # Track used enemies by identity (we’ll use id or name)

    for index in range(desired_length):
        # First, filter out enemies that haven't been used AND whose range is greater than current index
        eligible = [
            enemy for enemy in validEnemy
            if enemy.name not in used_enemies and enemy.range > index
        ]

        if not eligible:
            print(f"No eligible enemy found for position {index}. Aborting with partial list.")
            break

        # Sort eligible enemies by how close their range is to the current index
        eligible.sort(key=lambda enemy: enemy.range - index)

        # Prioritize the closest match (i.e., range just barely greater than index)
        # To keep it spicy, we can randomly pick from the top 3 closest matches, if there are that many
        top_choices = eligible[:3] if len(eligible) >= 3 else eligible
        chosen = random.choice(top_choices)

        selected_enemies.append(chosen)
        used_enemies.add(chosen.name)

        #print(f"Position {index}: Added {chosen}")

    return selected_enemies

backUp = copy.deepcopy(getVar("validEnemy"))
wave = 1
destroyed = False
circleThing = []
for i in range(0, 35):
    circleThing.append([(0, 0), random.randint(0, 255)])
#circleThing = [[(0, 0), 255]]*50
def onUpdate():
    #backGroundScreen.surface.set_alpha(100)
    global game_state, missCount, subtractTurn, wave, destroyed
    if intenseMode and not destroyed:
        destroyed = True
        destroyAction("Act")
        ally = party[0]
        for i in party:
            if i.hp > 0:
                ally = i
                break
        turnDialogue.clear()
        addTurnDialogue("Allerwave", "No more actions lol.", turn, None)
        addTurnDialogue(ally.name, "BRO WHY YOU TAKE MY ACTION???", turn, None)
        addTurnDialogue("Allerwave", "Why not?", turn, None)
        addTurnDialogue("Allerwave", "Plus, you all fricking invade into this realm that I was still working on.", turn, None)
        addTurnDialogue("Allerwave", "So I say it's a fair trade-off.", turn, None)
        addTurnDialogue(ally.name, "Don't you think The Creator guy would be pissed?", turn, None)
        addTurnDialogue("Allerwave", "Funni non canon moment.", turn, None)
        addTurnDialogue("Allerwave", "Nah that guy is probably blending about 2763 blueberries.", turn, None)
        addTurnDialogue("Allerwave", "And he is probably getting brokenfingers from having to deal with mewing Whatsapp Blueberry sigma gyatt ohio rizzfull brainrot.", turn, None)
        addTurnDialogue(ally.name, "...", turn, None)
    #return False
    backGroundScreen.fill((0, 0, 0, 255))
                #print(i[0])
    hud.camera_rotation = math.sin(frame/15)
    cyclePlayText = render_text(f'WAVE {str(wave)}', WHITE, 40, True, BLACK, 3)
    blitObj(hud, cyclePlayText, width/2, 50)
    #hud.camera_zoom = (math.sin(frame/15)+2)/2.3
    for i in range(0, 11):
        drawRect(backGroundScreen.surface, (min(i*10, 255), 0, 0) ,(0, 0+i*40+20*math.sin(frame/20+i), width, height-i*80+10*math.cos(frame/20+i)))
    if intenseMode:
        #setVar('allowWin', True)
        for i in circleThing:
            i[1] += 1.5
            #print(i[0], True)
            x, y = i[0][0], i[0][1]
            x += 25*math.sin(i[1]/20)
            y -= i[1]
            #print(y, 7*i[0], i[0][1])
            
            drawCircle(screen, (255, 255, 255, max(255 - i[1], 0)), (x, y), 10 + math.sin(i[1]/20))
            
            if i[1] >= 255:
                #print(True, y, x, height)
                i[1] = 0
                i[0] = (random.randint(0, width), abs(height))
    if getVar("win"):
        setVar("whichTurn", False)
    if getVar("win") == True and getVar("fightyLoop") == []:
        setVar("win", False)
        allEnemy = backUp#getVar("opponentObj")
        theEnemy = getVar("opponent")
        theEnemy.clear()
        #enemySprite.clear()
        for i in party:
            if i.hp > 0:    
                fightyLoop.append([i, i, int(-0.6*i.maxhp)])
        for num, ally in enumerate(party):
            enemySprite[num].pos[0] = width + 200
            x = opponentCoords[num][0]
            y = opponentCoords[num][1]
            enemySprite[num].tweenClear('all')
            #enemySprite[num].tweenPos((x, y), 'easeOut', 1, True)
            enemyShakeBool[num] = False
        wave += 1
        newEnemy = buildEnemyList(allEnemy, len(party))
        for i in newEnemy:
            theEnemy.append(i)

def onEnd():
    global loadMenu
    loadMenu = hey
    backGroundScreen.surface.set_alpha(255)
    hud.camera_rotation = 0
        
        

    #for i in range
