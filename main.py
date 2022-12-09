import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import subprocess

pipe = subprocess.Popen("pip3 install pygame",
 shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 
pipe = subprocess.Popen("pip3 install python-csv",
 shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


import pygame
import string


import csv
f = open(os.devnull, 'w')
sys.stdout = f
pygame.init()
font = pygame.font.SysFont('arial', 18)

NUMBERS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

LETTERS = string.ascii_lowercase

BLACK = (0,0,0)
WHITE = (255, 255, 255)

background_colour = (0, 0, 0)
 

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Openscorekeep')

screen.fill(background_colour)

pygame.display.flip()

header =  ["#", "Name", "2p", "2pa", "2p%", "3p", "3pa", "3p%", "ft", "fta", "ft%", "reb", "fouls", "steals", "assists", "pts"]

stat_names = ["2pm", "2pa", "2p%", "3pm", "3pa", "3p%", "ftm", "fta", "ft%", "reb", "fouls", "steals", "assists", "pts"]

game_log = []

input_text = ""

class Player:
    def __init__(self, number, name):
        self.number  = number
        self.name = name
        self.twpma = 0 #2pt makes
        self.twpmi = 0 #2pt miss
        self.thpma = 0 #3pt makes
        self.thpmi = 0 #3pt miss
        self.ftma = 0 #ft makes
        self.ftmi = 0 #ft miss
        self.fouls = 0 
        self.steals = 0
        self.assists = 0
        self.reb = 0
        
        self.pts = 0 #pts
        self.twpper = 0 #2pt %
        self.thpper = 0 #3pt %
        self.ftper = 0 #ft %
        
        self.stats = [
            self.twpma,
            self.twpmi,
            self.twpper, 
            self.thpma,
            self.thpmi,
            self.thpper,
            self.ftma,
            self.ftmi,
            self.ftper,
            self.reb,
            self.fouls,
            self.steals,
            self.assists,
            self.pts,
        ]
        
    def evaluate(self):
        print(self.twpma)
        self.pts = int(self.twpma*2 + self.thpma*3 + self.ftma)
        if (self.twpma+self.twpmi) != 0:
            self.twpper = round((100*self.twpma)/(self.twpma+self.twpmi), 2)
        else:
            self.twpper = 0
        if (self.thpma+self.thpmi) != 0:
            self.thpper = round((100*self.thpma)/(self.thpma+self.thpmi), 2)
        else:
            self.thpper = 0
        if (self.ftma+self.ftmi) != 0:
            self.ftper = round((100*self.ftma)/(self.ftma+self.ftmi), 2)
        else:
            self.ftper = 0
        self.stats = [
            self.twpma,
            self.twpmi,
            self.twpper, 
            self.thpma,
            self.thpmi,
            self.thpper,
            self.ftma,
            self.ftmi,
            self.ftper,
            self.reb,
            self.fouls,
            self.steals,
            self.assists,
            self.pts,
        ]
        

def take_input():
    global input_text, players, stat_names, game_log
    if input_text != "undo" and input_text != "save":
        game_log.append(input_text)
    print(game_log)
    text = input_text.split()
    
    print(text)
    if input_text == "save":
        save_file()
        return
    if input_text == "undo":
    
        #this is to undo the last action
        
        for each_player in players:
        
            text = game_log[len(game_log)-1].split()

            if int(text[0]) == each_player.number:
                
                if text[1] == "2pma":
                
                    each_player.twpma -= 1
                    
                elif text[1] == "2pmi":
                
                    each_player.twpmi -= 1
                
                elif text[1] == "3pma":
                
                    each_player.thpma -= 1
                    
                elif text[1] == "3pmi":
                
                    each_player.thpmi -= 1
                    
                elif text[1] == "ftma":
                
                    each_player.ftma -= 1
                    
                elif text[1] == "ftmi":
                
                    each_player.ftmi -= 1
                    
                elif text[1] == "foul":
                
                    each_player.fouls -= 1
                    
                elif text[1] == "reb":
                
                    each_player.reb -= 1
                    
                elif text[1] == "ast":
                
                    each_player.assists -= 1
                    
                elif text[1] == "steal":
                
                    each_player.steals -= 1
                each_player.evaluate()
                
                game_log.remove(game_log[len(game_log)-1])
                print(game_log)
                return
    
    for each_player in players:
    
        if int(text[0]) == each_player.number:
            
            if text[1] == "2pma":
            
                each_player.twpma += 1
                
            elif text[1] == "2pmi":
            
                each_player.twpmi += 1
            
            elif text[1] == "3pma":
            
                each_player.thpma += 1
                
            elif text[1] == "3pmi":
            
                each_player.thpmi += 1
                
            elif text[1] == "ftma":
            
                each_player.ftma += 1
                
            elif text[1] == "ftmi":
            
                each_player.ftmi += 1
                
            elif text[1] == "foul":
            
                print("foul")
            
                each_player.fouls += 1
                
            elif text[1] == "reb":
            
                each_player.reb += 1
                
            elif text[1] == "ast":
            
                each_player.assists += 1
                
            elif text[1] == "steal":
            
                each_player.steals += 1
            each_player.evaluate()
            
            return
    
def save_file():
    global players, header
    
    file_name = os.getcwd() + "\\game.csv"
    
    f = open("game.csv", "w", encoding="UTF8", newline="")
    
    writer = csv.writer(f)
    
    writer.writerow(header)
    
    for each in players:
    
        data = [each.number, each.name] + each.stats
    
        writer.writerow(data)
        
    f.close()
    
    
    
    

players = [
    Player(5, "Kincaid"),
    Player(6, "Frigaard"),
    Player(7, "O'Hagan"),
    Player(9, "Lo"),
    Player(10, "Lin"),
    Player(11, "Francois"),
    Player(12, "Tjandra"),
    Player(13, "Teodorescu"), 
    Player(14, "Guise"),
    Player(16, "Krishnatry"),
    Player(21, "Mehmi"),
    Player(22, "Kim")
]



def draw_table():
    global players, stat_names, input_text
    num_players = len(players)
    #first draw outline
    pygame.draw.line(screen, WHITE, (40, 20), (40, 60+30*num_players))
    pygame.draw.line(screen, WHITE, (40, 20), (1240, 20))
    pygame.draw.line(screen, WHITE, (1240, 20), (1240, 60+30*num_players))
    pygame.draw.line(screen, WHITE, (40, 60+30*num_players), (1240, 60+30*num_players))
    #draw the header line
    pygame.draw.line(screen, WHITE, (40, 60), (1240, 60))
    #draw the lines for the players
    for each_player in range(1, num_players):
        pygame.draw.line(screen, WHITE, (40, 60+30*each_player), (1240, 60+30*each_player))
    #from here draw the lines for the stats
    pygame.draw.line(screen, WHITE, (65, 20), (65, 60+30*num_players))#this is for the number
    pygame.draw.line(screen, WHITE, (190, 20), (190, 60+30*num_players)) #this if for name hence why its bigger
    for i in range(13): #this is for all the other stats
        pygame.draw.line(screen, WHITE, (265+75*i, 20), (265+75*i, 60+30*num_players))
    
    
    #from here we add the text
    text = font.render('#', True, WHITE)
    screen.blit(text, (45, 25))
    text = font.render('Name', True, WHITE)
    screen.blit(text, (70, 25))
    for each_stat in range(len(stat_names)):
        text = font.render(stat_names[each_stat], True, WHITE)
        screen.blit(text, (195+75*each_stat, 25))
    
    
    #from here we add the stats of each player
    for each_player in range(num_players):
        current_player = players[each_player]
        #this if for good coding practice
        
        text = font.render(str(current_player.number), True, WHITE)
        screen.blit(text, (45, 65+30*each_player))
        text = font.render(current_player.name, True, WHITE)
        screen.blit(text, (70, 65+30*each_player))
        
        for each_stat in range(len(stat_names)):
            text = font.render(str(current_player.stats[each_stat]), True, WHITE)
            screen.blit(text, (195+75*each_stat, 65+30*each_player))
        
        
    #from here we want to draw the input box
    pygame.draw.line(screen, WHITE, (40, 450), (40, 500))
    pygame.draw.line(screen, WHITE, (40, 450), (540, 450))
    pygame.draw.line(screen, WHITE, (540, 450), (540, 500))
    pygame.draw.line(screen, WHITE, (40, 500), (540, 500))
    #now write the text onto the screen
    text = font.render(input_text, True, WHITE)
    screen.blit(text, (45, 455))
    pygame.display.flip()
    



running = True

while running:
    screen.fill(BLACK)
    draw_table()
    
    for event in pygame.event.get():
     
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("entered")
                
                take_input()
                
                
                input_text = ""
            elif event.key in NUMBERS:
                input_text += str(NUMBERS.index(event.key))
                
            elif event.key == pygame.K_SPACE:
            
                input_text += " "
                
            elif event.key == pygame.K_BACKSPACE:
            
                input_text = input_text[:len(input_text)-1]
                
                print(len(input_text))
                
            else:
                try:
                    input_text += LETTERS[event.key-97]
                except:
                    pass
                    
                    