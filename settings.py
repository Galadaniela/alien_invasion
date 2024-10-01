class Settings():
    def __init__(self):
     self.screen_width = 1200
     self.screen_height = 700
     self.color = (35, 49, 113)
     self.ship_limit =  3

     self.speedup_scale = 1.1

     self.score_scale = 1.5
    
    # Bullet settings
     self.bullet_width = 4
     self.bullet_height = 15
     self.bullet_color = 13, 13, 14 
     self.bullet_allowed = 5

     # Alien settings
     self.fleet_drop_speed = 10
    

     self.initialize_dynamic_settings()

    def  initialize_dynamic_settings(self):
      
      self.ship_speed_factor = 1.5
      self.bullet_speed = 3
      self.alien_speed = 1
      self.fleet_direction = 1
      # Puntos
      self.aliens_points = 50

    def increase_speed(self):
      self.ship_speed_factor *= self.speedup_scale
      self.bullet_speed *= self.speedup_scale
      self.alien_speed *= self.speedup_scale
      self.aliens_points += int(self.aliens_points  * self.score_scale)
      