from pyniryo2 import *
import os
import sys
sys.path.append(os.getcwd() + "/task1")
#import core as c          # planning core

from importlib import reload
import threading


class BlockStacker:
    
    def __init__(self, robot=None, event_variable=None):
        self.robot_actual = True
        if not robot:
            try:
            
                self.robot = NiryoRobot("169.254.200.201") # Assuming ethernet!
            except Exception as e:
                print("Couldn't connect to robot")
                self.robot_actual = False #Mock
                self.robot = None
        else:
            self.robot = robot
            
        self.event = event_variable

    
    def end(self):
        self.robot.end()
      
    def move(self, l_from, l_to):
        # switch to move-pose
	    self.robot.arm.move_joints(l_to)
	
    def carry(self, b, l_from, l_to):
        self.robot.arm.move_joints(l_to)
    
    def floor(self, b, l):
        self.robot.tool.open_gripper()
        
    def stack(self, b1, l1, b2, l2):
        #print("Stacking " + b1 + " on " + b2 + "...")
        self.robot.tool.open_gripper()
        
    def grasp_on_floor(self, b, l):
        self.grasp(b, l, None)
          
    def grasp(self, b, l1, l2):
        #print("Grasping " + b + "...")
        self.robot.tool.close_gripper()
		
    def drop(self, l):
        self.robot.tool.open_gripper()

    def execute(self, plan):
        print("%%%%%%%%%%%%%% Plan Execution: %%%%%%%%%%%%%")

        a1 = [0.5845812043582548, -0.498940318815149, -0.561317863564226, 0.01083051910499222, -0.5170441791072538, -0.012179192713292153]
        b1 = [1.0396374095722325, -0.5034851561873422, -0.5673776467271503, 0.12894703977218658, -0.5170441791072538, -0.012179192713292153]
        c1 = [1.4779524166010805, -0.4504620535117546, -0.5673776467271503, -0.0014413271980928677, -0.5170441791072538, -0.012179192713292153]
                
        a2 = a1.copy()
        a2[1] = -0.3641101434400832
        a2[2] = -0.5355637851217977
        a2[4] = -0.6351606997744481
        b2 = b1.copy()
        b2[1] = -0.3641101434400832
        b2[2] = -0.5355637851217977
        b2[4] = -0.6351606997744481
        c2 = c1.copy()
        c2[1] = -0.3641101434400832
        c2[2] = -0.5355637851217977
        c2[4] = -0.6351606997744481

        a3 = a2.copy()
        a3[1] = -0.2883628539035292
        a3[2] = -0.4779958450740167
        a3[4] = -0.8499180100784383
        b3 = b2.copy()
        b3[1] = -0.2883628539035292
        b3[2] = -0.4779958450740167
        b3[4] = -0.8499180100784383
        c3 = c2.copy()
        c3[1] = -0.2883628539035292
        c3[2] = -0.4779958450740167
        c3[4] = -0.8499180100784383

        a4 = a3.copy()
        a4[1] = 0.04189532847584576
        a4[2] = -0.406793392909656
        a4[4] = -1.1720539755344226
        b4 = b3.copy()
        b4[1] = 0.04189532847584576
        b4[2] = -0.406793392909656
        b4[4] = -1.1720539755344226
        c4 = c3.copy()
        c4[1] = 0.04189532847584576
        c4[2] = -0.406793392909656
        c4[4] = -1.1720539755344226
        
        block1 = "block1"
        block2 = "block2"
        block3 = "block3"
        # Align initials (move block too).        
        #self.move(None, l2) # not sure I want this...
        #self.floor(None, None)
        
        for action in plan.actions:
            
            
            if self.robot_actual:
                print("executing " + str(action))
                exec("self." + str(action))
            else:
                print('exec("self.' + str(action) + '")')
        print("Goal reached.")
        print("%%%%%%%%%%%%%% End Plan Execution: %%%%%%%%%%%%%")	
		
		 
    def start(self):
        p = c.PlanningProblem(None)
        plan = p.solve()
        #print(plan)
        self.execute(plan)