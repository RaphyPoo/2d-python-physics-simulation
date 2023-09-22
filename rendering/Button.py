class Button():
    def __init__(self, x, y, width, height, text, color, screen, Render):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.screen = screen
        self.Render = Render
    
    def draw(self):
        Render.screen.blit(self.text, (self.x, self.y))