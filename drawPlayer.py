import drawPlayer
import gameBoard
import colFont
import UnitStats
import pygame

import nothing
RedUnit = UnitStats.BasicUnit(100,0,0,0,True,0,0,False,0,0,0,0,0)
BlueUnit = UnitStats.BasicUnit(100,0,0,0,True,0,0,False,0,0,0,0,0)
def RedPlayer():
    redName = colFont.arial21.render('Red', True, colFont.red)
    redUnitLife = colFont.arial21.render('Life: '+str(RedUnit.life),True,colFont.red)
    redUnitAttack = colFont.arial21.render('Attack: ' + str(RedUnit.attack), True, colFont.red)
    redUnitDefense = colFont.arial21.render('Defense: ' + str(RedUnit.defend), True, colFont.red)
    redUnitInitiative = colFont.arial21.render('Initiative: ' + str(RedUnit.initiative), True,colFont.red)
    redWin = colFont.arial21.render('Red Win: '+str(RedUnit.totwin), True, (255, 0, 0))
    redLoss = colFont.arial21.render('Red Loss: '+str(RedUnit.totloss), True, (255, 0, 0))
    redBigWin = colFont.arial42.render ('', True, (255, 0, 0))
    AttTotal = colFont.arial21.render("Total Attack: "+str(drawPlayer.RedUnit.totalAttack), True, colFont.green)
    Offense = colFont.arial21.render("Offensive", True, colFont.red)
    Defense = colFont.arial21.render("Defensive", True, colFont.blue)
    if RedUnit.initWin == 1:
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (25, 105, 155, 18), 0)
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (330, 50, 115, 20), 0)
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (690, 50, 118, 20), 0)

        gameBoard.screen.blit(AttTotal, (305, 115))
        gameBoard.screen.blit(Offense, (330, 50))
        gameBoard.screen.blit(Defense, (690,50))
    if RedUnit.attacker==1:
        totalAttack = colFont.arial21.render('Red Unit Total Attack= ' + str(RedUnit.tempRoll) + "+" + str(RedUnit.attack) + '=' + str(RedUnit.totalAttack), True,colFont.red)
        totalDefense = colFont.arial21.render('Blue Unit Total Defense: ' + str(BlueUnit.tempRoll) + "+" + str(BlueUnit.defend) + '=' + str(BlueUnit.totalDefense),True, colFont.blue)
        gameBoard.screen.blit(totalAttack, (400, 200))
        gameBoard.screen.blit(totalDefense, (400, 230))
        if RedUnit.hits ==1:
            dispHits = colFont.arial21.render('Red Unit hits for: ' + str(RedUnit.damage), True, colFont.red)
            gameBoard.screen.blit(dispHits, (400, 260))
        elif RedUnit.hits==2:
            dispHits = colFont.arial21.render('Red Unit Misses', True, colFont.red)
            gameBoard.screen.blit(dispHits, (400, 260))


    gameBoard.screen.blit(redName, (25, 25))
    gameBoard.screen.blit(redUnitLife, (25, 45))
    gameBoard.screen.blit(redUnitAttack, (25, 65))
    gameBoard.screen.blit(redUnitDefense, (25, 85))
    gameBoard.screen.blit(redUnitInitiative, (25, 105))
    gameBoard.screen.blit(redWin, (330, 75))
    gameBoard.screen.blit(redLoss, (25, 125))
    gameBoard.screen.blit(redBigWin, (525, 145))



def BluePlayer():
    blueName = colFont.arial21.render('Blue', True, colFont.blue)
    blueUnitLife = colFont.arial21.render('Life: ' + str(BlueUnit.life), True, colFont.blue)
    blueUnitAttack = colFont.arial21.render('Attack: ' + str(BlueUnit.attack), True, colFont.blue)
    blueUnitDefense = colFont.arial21.render('Defense: ' + str(BlueUnit.defend), True, colFont.blue)
    blueUnitInitiative = colFont.arial21.render('Initiative: ' + str(BlueUnit.initiative), True, colFont.blue)
    blueWin = colFont.arial21.render('Blue wins: '+str(BlueUnit.totwin), True, colFont.blue)
    blueLoss = colFont.arial21.render('Blue Loss: '+str(BlueUnit.totloss), True, colFont.blue)
    blueBigWin = colFont.arial42.render('', True, (255, 0, 0))
    AttTotal = colFont.arial21.render("Total Attack: " + str(drawPlayer.BlueUnit.totalAttack), True, colFont.green)
    Offense = colFont.arial21.render("Offensive", True, colFont.blue)
    Defense = colFont.arial21.render("Defensive", True, colFont.red)
    if BlueUnit.initWin == 1:
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (1030, 105, 155, 18), 0)
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (330, 50, 115, 20), 0)
        pygame.draw.rect(gameBoard.screen, (255, 255, 255), (690, 50, 118, 20), 0)
        gameBoard.screen.blit(AttTotal, (305, 115))
        gameBoard.screen.blit(Defense, (330, 50))
        gameBoard.screen.blit(Offense, (690, 50))

    if BlueUnit.attacker==1:
        totalAttack = colFont.arial21.render('Blue Unit Total Attack= ' + str(BlueUnit.tempRoll) + "+" + str(BlueUnit.attack) + '=' + str(BlueUnit.totalAttack), True,colFont.blue)
        totalDefense = colFont.arial21.render('Red Unit Total Defense: ' + str(RedUnit.tempRoll) + "+" + str(RedUnit.defend) + '=' + str(RedUnit.totalDefense),True, colFont.red)
        gameBoard.screen.blit(totalAttack, (400, 200))
        gameBoard.screen.blit(totalDefense, (400, 230))
        if BlueUnit.hits ==1:
            dispHits = colFont.arial21.render('Blue Unit hits for: ' + str(BlueUnit.damage), True, colFont.blue)
            gameBoard.screen.blit(dispHits, (400, 260))
        elif BlueUnit.hits==2:
            dispHits = colFont.arial21.render('Blue Unit Misses', True, colFont.blue)
            gameBoard.screen.blit(dispHits, (400, 260))

    gameBoard.screen.blit(blueName, (1050, 25))
    gameBoard.screen.blit(blueUnitLife, (1030, 45))
    gameBoard.screen.blit(blueUnitAttack, (1030, 65))
    gameBoard.screen.blit(blueUnitDefense, (1030, 85))
    gameBoard.screen.blit(blueUnitInitiative, (1030, 105))
    gameBoard.screen.blit(blueWin, (670, 75))
    gameBoard.screen.blit(blueLoss, (1030, 125))
    gameBoard.screen.blit(blueBigWin, (815, 145))
