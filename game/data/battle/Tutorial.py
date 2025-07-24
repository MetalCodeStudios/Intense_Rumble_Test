def onStart():
    setVar('useCustomDialogue', True)
    setVar('useExtraDialogue', False)
    Opponent = getVar('opponentObj')
    theEnemy = getVar('opponent')
    theEnemy.clear()
    theEnemy.append(Opponent['Allerwave'])
    Player = getVar('playerObj')
    theAlly = getVar('party')
    theAlly.clear()
    theAlly.append(Player['Li Wei'])
    addTurnDialogue('Clear')
    addTurnDialogue('Allerwave', "Welcome to the tutorial! Press [green]CONFIRM[/green] to proceed!", 0, None)
    addTurnDialogue('Allerwave', "Try [orange]CANCEL[/orange] on the next dialogue!", 0, None)
    addTurnDialogue('Allerwave', "E E E E E E E E E E E E E E E E E E E E E E  E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E ", 0, None)
    addTurnDialogue('Allerwave', "Anyway, let's begin.", 0, None)
    addTurnDialogue('Allerwave', "Note that this tutorial is not the final version.", 0, None)

game_state = "keepMissing"
missCount = 0
subtractTurn = 0
def onUpdate():
    global game_state, missCount, subtractTurn
    if getVar('turn') == 1 or game_state == "keepMissing":
        setVar('actions', ['Fight'])
        setTurnText('Select the [red]FIGHT[/red] option and try attacking.', 'Allerwave')
        if getVar('party')[0].activity == 'chooseFightTarget':
            setTurnText('Now click [green]CONFIRM[/green] to attack!', 'Allerwave')
        if getVar('inFight') and getVar('turnAlly') and not getVar('allyTurn'):
            text = render_text("Press [green]CONFIRM[/green] to hit the Bar.", GREEN, 40, True, BLACK, 2)
            blitObj(hud, text, getVar('hudRect')[0], getVar('hudRect')[5]-50)

        if getVar('party')[0].activity == 'Attack_miss':
            missTurn = getVar('turn') + 1
            missCount = getVar('turn') - 1
            if missCount == 0:
                addTurnDialogue('Allerwave', "You... missed?", missTurn, None)
            elif missCount < 3:
                addTurnDialogue('Allerwave', "Again..?", missTurn, None)
            elif missCount < 5:
                addTurnDialogue('Allerwave', "Umm...", missTurn, None)
            elif missCount >= 5:
                addTurnDialogue('Allerwave', "...", missTurn, None)

            if missCount < 3:
                addTurnDialogue('Allerwave', "...", missTurn, None)
                addTurnDialogue('Allerwave', "Alright, so when you see a bar appear.", missTurn, None)
                addTurnDialogue('Allerwave', "Press [green]CONFIRM[/green] when the bar is at its closest to the center!", missTurn, None)
            elif missCount < 5:
                addTurnDialogue('Allerwave', "Just hit the bar by using [green]CONFIRM[/green].", missTurn, None)
            elif missCount == 5:
                addTurnDialogue('Allerwave', "I don't... even know at this point...", missTurn, None)
            elif missCount == 7:
                addTurnDialogue('Allerwave', "please just hit the bar already...", missTurn, None)
                addTurnDialogue('Allerwave', "i wanna move on to the next stage", missTurn, None)
            elif missCount == 9:
                addTurnDialogue('Allerwave', "[shake][#ff0000]AAAAAAAAAAAAAAAAAA[/#ff0000][/shake]", missTurn, None)
                addTurnDialogue('Allerwave', "Ok I'm fine now.", missTurn, None)
                addTurnDialogue('Allerwave', "But seriously though,", missTurn, None)
                addTurnDialogue('Allerwave', "[shake]PLEASE JUST HIT THE BAR!!!![/shake]", missTurn, None)
            elif missCount == 10:
                addTurnDialogue('Allerwave', "Are you trying to do a pacifist run or something?", missTurn, None)
                addTurnDialogue('Allerwave', "Because in this world.", missTurn, None)
                addTurnDialogue('Allerwave', "You can't even spare anyone, since they all wanna [red]FIGHT[/red].", missTurn, None)
                addTurnDialogue('Allerwave', "So please for goodness sake...", missTurn, None)
                addTurnDialogue('Allerwave', "[shake]HIT THE FRICKIN BAR![/shake]", missTurn, None)
            elif missCount == 11:
                addTurnDialogue('Allerwave', "My face may not show it right now.", missTurn, None)
                addTurnDialogue('Allerwave', "(Due to me being too lazy to code in emotions.)", missTurn, None)
                addTurnDialogue('Allerwave', "But I am in constant agony from this.", missTurn, None)
                addTurnDialogue('Allerwave', "Everytime you miss that singular bar, it fills me with irritation.", missTurn, None)
            elif missCount == 12:
                addTurnDialogue('Allerwave', "We have been standing here...", missTurn, None)
                addTurnDialogue('Allerwave', "FOR 14 FRICKIN TURNS!", missTurn, None)
                addTurnDialogue('Allerwave', "I may not have legs...", missTurn, None)
                addTurnDialogue('Allerwave', "[shake]BUT IT IS TIRING TO FLOAT IN ONE SPOT FOR SO LONG!!![/shake]", missTurn, None)
            elif missCount == 13:
                addTurnDialogue('Allerwave', "Look...", missTurn, None)
                addTurnDialogue('Allerwave', "I am trying my best to not lash out that much...", missTurn, None)
                addTurnDialogue('Allerwave', "Simply because hurling insults would mean I'll get cancelled.", missTurn, None)
                addTurnDialogue('Allerwave', "So please...", missTurn, None)
                addTurnDialogue('Allerwave', "[shake]HIT THE BAR!!!!!![/shake]", missTurn, None)
            elif missCount == 14:
                addTurnDialogue('Allerwave', "You know what. Let's just skip this stage", missTurn, None)
                addTurnDialogue('Allerwave', "I feel so tired and irritated right now...", missTurn, None)
                addTurnDialogue('Allerwave', "In fact...", missTurn, None)
                addTurnDialogue('Allerwave', "I'm too tired to explain [cyan]Actions[/cyan] in the [cyan]ACT[/cyan] menu.", missTurn, None)
                addTurnDialogue('Allerwave', "So you just try to figure out what to do while I rest for a while.", missTurn, None)
                game_state = "usingAct"
            else:
                game_state = "keepMissing"
            setVar('progressTurn', False)

        elif getVar('party')[0].activity == 'Attack_crit' or getVar('party')[0].activity == 'Attack_hit':
            setVar('progressTurn', False)
            game_state = "usingAct"
            nextTurn = getVar('turn') + 1
            if missCount < 3:
                addTurnDialogue('Allerwave', "You did it!", nextTurn, None)  
                addTurnDialogue('Allerwave', "Congratulation!", nextTurn, None)
                addTurnDialogue('Allerwave', "You have learnt how to [red]Attack[/red]!", nextTurn, None)
                addTurnDialogue('Allerwave', "Word of advice:", nextTurn, None)
                addTurnDialogue('Allerwave', "Aim for the [green]GREENEST[/green] area when hitting the bar!", nextTurn, None)
                addTurnDialogue('Allerwave', "You deal more damage that way!", nextTurn, None)

            elif missCount < 5:
                addTurnDialogue('Allerwave', "Yay! You manage to do it!", nextTurn, None)  
                addTurnDialogue('Allerwave', "Congratulation!", nextTurn, None)
                addTurnDialogue('Allerwave', "I hope you learnt how to [red]Attack[/red] now!", nextTurn, None)
                addTurnDialogue('Allerwave', "Here is some advice:", nextTurn, None)
                addTurnDialogue('Allerwave', "Aim for the [green]GREENEST[/green] area when hitting the bar!", nextTurn, None)
                addTurnDialogue('Allerwave', "You deal more damage that way!", nextTurn, None)

            elif missCount < 9:
                addTurnDialogue('Allerwave', "Finally! You done it!", nextTurn, None)  
                addTurnDialogue('Allerwave', "Congratulation!", nextTurn, None)
                addTurnDialogue('Allerwave', "You actually managed to [red]Attack[/red]!", nextTurn, None)
                addTurnDialogue('Allerwave', "Oh here is some helpful advice!", nextTurn, None)
                addTurnDialogue('Allerwave', "Aim for the [green]GREENEST[/green] area when hitting the bar!", nextTurn, None)
                addTurnDialogue('Allerwave', "You deal higher damage that way!", nextTurn, None)
            else:
                addTurnDialogue('Allerwave', "Thank goodness!", nextTurn, None)
                addTurnDialogue('Allerwave', "You done it!", nextTurn, None)
                addTurnDialogue('Allerwave', "Now let me just take a short rest...", nextTurn, None)
                for i in range(0, missCount-7):
                    addTurnDialogue('Allerwave', "...", nextTurn, None, doSpam=True)

            addTurnDialogue('Allerwave', "Now...", nextTurn, None)
            addTurnDialogue('Allerwave', "It's time for [cyan]ACT[/cyan].", nextTurn, None)
            addTurnDialogue('Allerwave', "The [cyan]ACT[/cyan] menu have several [cyan]Actions[/cyan] that a character can do.", nextTurn, None)
            addTurnDialogue('Allerwave', "The list of [cyan]Actions[/cyan] are...", nextTurn, None)
            addTurnDialogue('Allerwave', "[cyan]Check[/cyan]: Allows one to see a Target's stats and description.", nextTurn, None)
            addTurnDialogue('Allerwave', "[cyan]Defend[/cyan]: Increase the User's defense for one Cycle.", nextTurn, None)
            addTurnDialogue('Allerwave', "[cyan]Swap[/cyan]: Allows the User to swap position with a Target in their team.", nextTurn, None)
            addTurnDialogue('Allerwave', "[cyan]Heal[/cyan]: Heals the User's Health by a small amount.", nextTurn, None)
            addTurnDialogue('Allerwave', "Now that we got this cleared...", nextTurn, None)
            addTurnDialogue('Allerwave', "Let's try using [cyan]Actions[/cyan].", nextTurn, None)

    elif game_state == "usingAct":
        setVar('actions', ['Act'])
        #setVar('selectedAction', 0)
        setTurnText('Select the [cyan]ACT[/cyan] option and try doing an [cyan]Action[/cyan].', 'Allerwave')
        
        if getVar('party')[0].activity == 'Act_done':
            setVar('progressTurn', False)
            game_state = 'usingSkill'
            nextTurn = getVar('turn') + 1
            addTurnDialogue('Allerwave', "Awesome!", nextTurn, None)
            addTurnDialogue('Allerwave', "You managed to use an [cyan]Action[/cyan]!", nextTurn, None)

            addTurnDialogue('Allerwave', "Now, next thing we do are [blue]SKILLS[/blue].", nextTurn, None)
            addTurnDialogue('Allerwave', "Every [blue]Abilities[/blue] in the [blue]SKILLS[/blue] menu have one thing in common.", nextTurn, None)
            addTurnDialogue('Allerwave', "They all use [cyan]AP[/cyan].", nextTurn, None)
            addTurnDialogue('Allerwave', "[cyan]AP[/cyan] stands for [cyan]Act Points[/cyan], or [cyan]Ability Points[/cyan] if you prefer.", nextTurn, None)
            addTurnDialogue('Allerwave', "You earn [cyan]AP[/cyan] from doing [cyan]Actions[/cyan] or [red]Attacking[/red].", nextTurn, None)
            addTurnDialogue('Allerwave', "Here! I gave you an [blue]Ability[/blue]!", nextTurn, None)
            addTurnDialogue(None, "Li Wei gained [blue]Power Slash[/blue]!", nextTurn, None)
            if getVar('party')[0].skills == []:
                getVar('party')[0].skills.append(getVar('skillObj')['Power Slash'])

    elif game_state == "usingSkill":
        if getVar('allyTurn'):
            setVar('actions', ['Skills'])
        #setVar('selectedAction', 0)
        setTurnText('Select the [blue]SKILLS[/blue] option and try doing an [blue]Ability[/blue].', 'Allerwave')
        
        if getVar('party')[0].activity == 'Skill_done':
            setVar('progressTurn', False)
            game_state = 'usingItem'
            nextTurn = getVar('turn') + 1
            addTurnDialogue('Allerwave', "Ouch!", nextTurn, None)
            addTurnDialogue('Allerwave', "Wow.", nextTurn, None)
            addTurnDialogue('Allerwave', "That was a pretty strong slash!", nextTurn, None)
            addTurnDialogue('Allerwave', "Alright, now Ima just take your [blue]Ability[/blue] away.", nextTurn, None)
            getVar('party')[0].skills.clear()
            addTurnDialogue(None, "Allerwave took [blue]Power Slash[/blue] away!", nextTurn, None)

            addTurnDialogue('Allerwave', "Finally, we are using [green]ITEMS[/green]", nextTurn, None)
            addTurnDialogue('Allerwave', "It's pretty self explainatory.", nextTurn, None)
            addTurnDialogue('Allerwave', "Hmm...", nextTurn, None)
            addTurnDialogue('Allerwave', "Your [green]Health[/green] seems to be full.", nextTurn, None)
            addTurnDialogue('Allerwave', "Using an [green]Item[/green] in this stage seems to be...", nextTurn, None)
            addTurnDialogue('Allerwave', "wasteful...", nextTurn, None)
            addTurnDialogue('Allerwave', "So...", nextTurn, None)
            addTurnDialogue('Allerwave', "Now you are hurt!", nextTurn, None)
            addTurnDialogue('Allerwave', "Quick use an [green]Item[/green]!", nextTurn, None)
            #addTurnDialogue('Allerwave', "Anyway I will damage you so you can use an item.", nextTurn, None)
            
    elif game_state == "usingItem":
        turnDialogue = getVar('turnDialogue')
        turn = getVar('turn')
        if getVar('allyTurn'):
            setVar('actions', ['Items'])
        #setVar('selectedAction', 0)
        if getVar('party')[0].hp == getVar('party')[0].maxhp and isInDialogue(turn, 12):
            getVar('fightyLoop').append([getVar('party')[0], getVar('opponent')[0], getVar('party')[0].maxhp-1])
            
        setTurnText('You are hurt! \n* Use an [green]Item[/green] to heal up!', None)
        
        if getVar('party')[0].activity == 'Item_done':
            setVar('progressTurn', False)
            game_state = 'done'
            nextTurn = getVar('turn') + 1
            addTurnDialogue('Allerwave', "Yay! You healed up!", nextTurn, None)
            addTurnDialogue('Allerwave', "Anyway.", nextTurn, None)
            addTurnDialogue('Allerwave', "That's all the Battle Options.", nextTurn, None)
            addTurnDialogue('Allerwave', "So now...", nextTurn, None)
            addTurnDialogue('Allerwave', "It's time for the real deal!", nextTurn, None)
            addTurnDialogue('Allerwave', "Let's see how you face off some enemies!", nextTurn, None)
            addTurnDialogue('Allerwave', "But first, here's a brief recap of your stat.", nextTurn, None)
            addTurnDialogue('Allerwave', "[green]Health[/green]: It's a character's hit points.", nextTurn, None)
            addTurnDialogue('Allerwave', "If a character reach 0[green]HP[/green], they become [#bb0000]Down[/#bb0000].", nextTurn, None)
            addTurnDialogue('Allerwave', "If everyone in your team reach 0[green]HP[/green], you lose.", nextTurn, None)
            addTurnDialogue('Allerwave', "[red]Attack[/red]: It dictate how much strength a character have.", nextTurn, None)
            addTurnDialogue('Allerwave', "Higher [red]ATK[/red] means higher overall damage by a character.", nextTurn, None)
            addTurnDialogue('Allerwave', "[blue]Defense[/blue]: It dictate how much damage is reduced.", nextTurn, None)
            addTurnDialogue('Allerwave', "Higher [blue]DEF[/blue] means lower overall damage onto the character.", nextTurn, None)
            addTurnDialogue('Allerwave', "[yellow]Speed[/yellow]: It dictates a character's turn order and their chances of dodging an attack.", nextTurn, None)
            addTurnDialogue('Allerwave', "Higher [yellow]SPD[/yellow] means the character would likely go earlier, and have a higher dodging chance.", nextTurn, None)
            addTurnDialogue('Allerwave', "[purple]Productivity[/purple]: This is a new one. It dictates how much [cyan]AP[/cyan] a character can gain.", nextTurn, None)
            addTurnDialogue('Allerwave', "Higher [purple]PRD[/purple] means you gain more [cyan]AP[/cyan] from []Actions and Attacking.", nextTurn, None)
            addTurnDialogue('Allerwave', "[orange]Range[/orange]: Also a new one. It dictates how far a character can target.", nextTurn, None)
            addTurnDialogue('Allerwave', "Higher [orange]RGE[/orange] means a character can target further.", nextTurn, None)
            addTurnDialogue('Allerwave', "Welp. That's all the stats.", nextTurn, None)
            addTurnDialogue('Allerwave', "Anyway here are your teammates.", nextTurn, None)
            addTurnDialogue('Allerwave', "One is a Range, the other is a Support", nextTurn, None)
            addTurnDialogue('Allerwave', "And here are the enemies.", nextTurn, None)
            addTurnDialogue('Allerwave', "Practice fighting them and try to win.", nextTurn, None)
            addTurnDialogue('Allerwave', "And remember.", nextTurn, None)
            addTurnDialogue('Allerwave', "When attacking.", nextTurn, None)
            addTurnDialogue('Allerwave', "Aim for the [green]GREEN[/green], and hit the bar as close to it as possible!", nextTurn, None)
            addTurnDialogue('Allerwave', "Good luck, I shall disappear.", nextTurn, None)
            addTurnDialogue('Allerwave', "[shake]AAAAAAAAAAAA[/shake]", nextTurn, None)

    elif game_state == 'done':
        turn = getVar('turn')
        if isInDialogue(turn, 29):
            getVar('fightyLoop').append([getVar('opponent')[0], getVar('opponent')[0], 400])
            game_state = 'battleBegin'
            setVar('progressTurn', True)
            setTurnText('The mascot attacks!', None)
            subtractTurn = turn
        if len(getVar('party')) != 3 and isInDialogue(turn, 21):
            setVar('actions', ['Fight', 'Skills', 'Act', 'Items'])
            Players = getVar('playerObj')
            theParty = getVar('party')
            theParty.clear()
            theParty.append(Players['Rayson'])
            theParty.append(Players['Rany'])
            theParty.append(Players['Li Wei'])

        if len(getVar('opponent')) != 4 and isInDialogue(turn, 23):
            Opponent = getVar('opponentObj')
            theEnemy = getVar('opponent')
            #Opponent.clear()
            theEnemy.append(copy.deepcopy(Opponent['Mascot']))
            theEnemy[1].name = "Mascot A"
            theEnemy.append(copy.deepcopy(Opponent['Mascot']))
            theEnemy[2].name = "Mascot B"
            theEnemy.append(copy.deepcopy(Opponent['Mascot']))
            theEnemy[3].name = "Mascot C"
            for i in theEnemy:
                i.levelUp(0)
                i.hpSet()
            for i in getVar('party'):
                getVar('fightyLoop').append([i, i, -500])
    elif game_state == 'battleBegin':
        turn = getVar('turn') - subtractTurn
        if turn == 0:
            setTurnText('Li Wei is now supported by allies!', None)
        elif turn == 1:
            setTurnText('Rayson is calculating on what is the best outcome.', None)
        elif turn == 2:
            setTurnText('Rany feels like his healing magic could be useful in the future.', None)
        else:
            if getVar('party')[getVar('selectedAlly')].hp/getVar('party')[getVar('selectedAlly')].maxhp < 0.1:
                partyMember = getVar("party")[getVar('selectedAlly')].name
                setTurnText(f'[shake]{partyMember} is feeling very weak...[/shake]', None)
            else:
                if getVar('deadCount') == 1:
                    setTurnText('[shake]Tensions are rising[/shake].', None)
                elif getVar('deadCount') == 2:
                    partyMember = getVar("party")[getVar('selectedAlly')].name
                    setTurnText(f'{partyMember} stands [snake]alone[/snake]. \n* Why is the dialogue [snake]weird[/snake]?', None)
                else:
                    setTurnText('Not much more to [i]talk[/i] about.', None)

        if getVar('party')[getVar('selectedAlly')].activity == 'chooseFightTarget':
            partyMember = getVar("party")[getVar('selectedAlly')].name
            setTurnText(f'{partyMember} prepares to attack.', None)

        if getVar('win'):
            getVar('achievementObj')["Tutorial Complete!"].trigger()
            
            #[ Players['Rayson'], Players['Rany'], Players['Li Wei'] ])
            
            
            #addTurnDialogue('Allerwave', "Anyway I will damage you so you can use an item.", nextTurn, None)

