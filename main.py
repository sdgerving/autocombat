import Combat
import pygame
import UnitStats
import Initiative
import gameBoard
import drawPlayer
import colFont
import Mouse
#import testes

pygame.init()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if Initiative.initiative.gameState == 0:
            Initiative.rollInitiative()
        elif Initiative.initiative.gameState  == 1:
            Combat.rollAction()
        elif Initiative.initiative.gameState==1:
            Initiative.rerollInit()

        gameBoard.drawGameBoard()
        Mouse.MousePos()
        drawPlayer.RedPlayer()
        drawPlayer.BluePlayer()
        pygame.display.flip()

pygame.quit()
