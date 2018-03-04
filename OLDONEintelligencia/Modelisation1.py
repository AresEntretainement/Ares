from index import ControllerRobot


robot = ControllerRobot('Main')
print(robot.Robot['MoteurSparBar'].PWM)
robot.do(
    [
        robot.useModule('UltrasonGaucheTorse','mesureForce',10,0,[1]),
        robot.useModule('MoteurSparBar','turnSpeed',10,1,[2])
    ]
)





