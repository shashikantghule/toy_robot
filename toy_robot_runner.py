from toy_robot_position import ToyRobot
import sys


class ToyRobotRunner:

    @staticmethod
    def toy_robot_runner(): # robot runner
        global toy_instance
        try:
            print('PLACE x,y,f | MOVE | LEFT | RIGHT | REPORT | quit: for quit')
            input_parameters = input(':')
            if 'PLACE' in input_parameters:
                position = input_parameters.replace('PLACE', '').replace(' ', '').split(',')
                x = int(position[0])
                y = int(position[1])
                f = position[2]

                if len(position) == 3 and f in ToyRobot.face_position:
                    toy_instance = ToyRobot(x, y, f)
                    print(toy_instance)
                else:
                    print('ERROR: INVALID PARAMETERS FOR PLACE OPTION!')

            elif input_parameters.upper() == 'MOVE':
                if toy_instance:
                    toy_instance.toy_robot_movement()
                else:
                    print('ERROR: PLACE ROBOT FIRST!')

            elif input_parameters.upper() == 'LEFT':
                if toy_instance:
                    toy_instance.direction('LEFT')
                else:
                    print('ERROR: PLACE ROBOT FIRST!')

            elif input_parameters.upper() == 'RIGHT':
                if toy_instance:
                    toy_instance.direction('RIGHT')
                else:
                    print('ERROR: PLACE ROBOT FIRST!')

            elif input_parameters.upper() == 'REPORT':
                if toy_instance:
                    print(toy_instance)
                else:
                    print('ERROR: PLACE ROBOT FIRST!')

            elif input_parameters.upper() == 'QUIT':
                print('GOOD BYE!')
                sys.exit(0)

        except Exception as e:
            print('ERROR :', e)
        ToyRobotRunner.toy_robot_runner()


def main():
    ToyRobotRunner.toy_robot_runner()


if __name__ == "__main__":
    main()




