class ToyRobot:
    face_position = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, x=None, y=None, f=None):
        if f not in ToyRobot.face_position:
            raise Exception('Invalid Face Position provided!')

        if x < 0 or x > 5:
            raise Exception('Invalid X')

        if y < 0 or y > 5:
            raise Exception('Invalid Y')

        self.x = x
        self.y = y
        self.f = f

    def toy_robot_movement(self): # toy robot movemeent
        try:
            if self.f.upper() in ['NORTH', 'SOUTH']:
                if self.y < 5:
                    self.y += 1

            elif self.f.upper() in ['EAST', 'WEST']:
                if self.x < 5:
                    self.x += 1

            else:
                raise Exception('Invalid direction provided!')
        except Exception as e:
            raise e

    def direction(self, direction): # toy robot direction
        try:
            if direction.upper() == 'RIGHT':
                if self.f == 'WEST':
                    self.f = 'NORTH'

                elif self.f == 'NORTH':
                    self.f = 'EAST'

                elif self.f == 'EAST':
                    self.f = 'SOUTH'

                elif self.f == 'SOUTH':
                    self.f = 'WEST'

            elif direction.upper() == 'LEFT':
                if self.f == 'WEST':
                    self.f = 'SOUTH'

                elif self.f == 'SOUTH':
                    self.f = 'EAST'

                elif self.f == 'EAST':
                    self.f = 'NORTH'

                elif self.f == 'NORTH':
                    self.f = 'WEST'

            else:
                raise Exception('Invalid direction provided!')
        except Exception as e:
            raise e

    def __str__(self):
        return str(self.x)+' '+str(self.y)+' '+self.f
