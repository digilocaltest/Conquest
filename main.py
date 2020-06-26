import pygame, math, random

class GameObject():
  # Basic game object, all pieces have these properties
  def __init__(self, population, size, team):
      self.population = population
      self.size = size
      self.team = team
      self.image = self.make_object_surface()
      self.rect = self.image.get_rect()

  def make_object_surface(self): # returns a surface that is a squiare of the size and color of the team
    surface = pygame.Surface((self.size, self.size))
    surface.fill(303030)
    self.colour = teams_colours[self.team]
    pygame.draw.rect(surface, self.colour, (3, 3, self.size-6, self.size -6))
    return surface

  def draw(self): # Update playing_area with self image and population 
    top_lef_corner = self.x, self.y
    playing_area.blit(self.image, top_lef_corner)
    text = font.render(str(self.population), True, BLACK)
    playing_area.blit(text, (int(top_lef_corner[0] + 2), int(top_lef_corner[1] + self.size/4)))

# RGB COLORS
GREY, BLACK = (150, 150, 150), (0,0,0)
RED, YELLOW = (255,50,50), (255,255,50)
GREEN, BLUE = (50,50,255), (50,255,50)

teams_colours = [GREY, RED, YELLOW, GREEN, BLUE]

class Building(GameObject):
  # Builds tambien tiene una fila y una columna posicion
  # El estado debe ser True si estan en una nueva Base
  def __init__(self, column, row, population, team, status):
    super().__init__(population, 30, team)
    # Columns = unit x values
    # rows = uniut y values
    
    self.column = column
    self.row = row
    self.x = (self.column * 40) + 10
    self.y = (self.row * 40) + 10
    self.capacity = 100
    self.neutral = status
    

# lo que hace esta funcion es recibir el numero de columna y el numero de fila y multiplicarlo por 40 + 10 para colocarlo de forma grafica en el eje de cordenadas x/y

# Setting un our Play Screen

pygame.init()
playing_area = pygame.display.set_mode((690,690))
pygame.display.set_caption('Conquest')
font = pygame.font.SysFont('arial', 14)
clock = pygame.time.Clock()
timer = 0 
random.seed()

game_squares = []

for column in range(0,17):
  # Añadimos una lista vacia a cada columna para luego agregarle las filas
  game_squares.append([])
  for row in range(0,17):
    # Añadimos los objetos en su posicion final utilizando la posicion de la columna y la fila como "x" y "y"
    #print("Column: ", column, "row: ", row)
    game_squares[column].append(Building(column, row, 20, 1, False))

# Ahora necesitamos que python funcione el Bucle para que pinte, Primero pintamos en fondo. Porque? Porque vamos por capas! y si pintamos el fondo al final no tiene sentido. Despues pintamos nuestros edificios. Con otro Loop

while True:
  playing_area.fill(GREY)
  for row in game_squares:
    for piece in row:
      # Comprobamos si lo que hay es un edificion
      if isinstance(piece, Building):
        piece.draw()
  pygame.display.update()
  clock.tick(60)



# Problemas, Necesitamos transformar x and y to Int en la funcion Blit
















