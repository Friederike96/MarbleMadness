from pygame import image

from game_state import GameState

game_state: GameState = GameState.GAME_OVER
current_level = 0

current_map: str = ''
current_map_short: str = ''
current_heightmap: str = ''
current_heightmap_short: str = ''

# marble = Actor('objects/marble', center=(300, 45))
# marbleh = Actor('objects/marble', center=(300, 60))
heightmap: image = None
marble = Actor('objects/marble', center=(310, 20))
marble.x = 350
marble.y = 350
marbleh = Actor('objects/marble', center=(310, 20))
marbleh.x = 350
marbleh.y = 50
marble.dir = marble.speed = 0
debug = False
timer = 30
score = 0
coinscore = 0
coin = Actor('objects/coingold')
coin.x = (150)
coin.y = (45)
