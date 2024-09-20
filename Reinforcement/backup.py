import tkinter as tk
from collections import namedtuple

class Node:
    def __init__(self, canvas, focus,radius=10, node=None):
        self.canvas = canvas
        self.focus = focus
        self.node = node
        canvas.create_oval(focus.x - radius, focus.y - radius, focus.x + radius, focus.y + radius, fill='blue')

    def ConnectNode(self):
        if(self.node == None):
            print("No node attached")
            return
        elif(type(self.node) == Node):
            self.canvas.create_line(self.focus.x,self.focus.y,self.node.focus.x,self.node.focus.y,fill='blue',width=2)
        elif(type(self.node) == list):
            for node in self.node:
                self.canvas.create_line(self.focus.x,self.focus.y,node.focus.x,node.focus.y,fill='blue',width=2)
        else:
            print("Bad Inputs to Node")
            return 1
    def Activate(self):
        pass


Point = namedtuple('Point', ['x', 'y'])

class NeuronLayer:
    def __init__(self,canvas, n_nodes, XPos, canvas_height, PrevLayer: 'NeuronLayer' = None):
        self.nodes = []
        self.canvas = canvas
        self.canvas_height = canvas_height
        self.YPositions = self.GenerateIndexs(n_nodes)
        self.XPos = XPos
        self.PrevLayer = PrevLayer
        if self.PrevLayer:
            for YCords in self.YPositions:
                self.nodes.append(Node(self.canvas, focus=Point(x=self.XPos, y=YCords), node=PrevLayer.nodes))
        else:
            for YCords in self.YPositions:
                self.nodes.append(Node(self.canvas, focus=Point(x=self.XPos, y=YCords)))

    def GenerateIndexs(self, nPoints):
        nPtList = []
        separation = self.canvas_height // (nPoints + 1)
        index = 0
        for counter in range(nPoints):
            index += separation
            nPtList.append(index)
        return nPtList
    
    def NodeAttachments(self):
        for node in self.nodes:
            node.ConnectNode()


class NNVisualizer():
    
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("NNVisualizer")

        #Dimensions of the Canvas
        self.canvas_width = 800
        self.canvas_height = 600
        
       #Create a canvas widget
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        #How many Nodes in each layer
        n_Pt_1_Layer = 11
        n_Pt_2_Layer = 16

        #Creating X Positions
        Layer1XIdx = 200
        Layer2XIdx = 400
        

        #Create Layers
        Layer1 = NeuronLayer(canvas=self.canvas, n_nodes=n_Pt_1_Layer,XPos=Layer1XIdx, canvas_height=self.canvas_height)
        Layer2 = NeuronLayer(canvas=self.canvas, n_nodes=n_Pt_2_Layer,XPos=Layer2XIdx, canvas_height=self.canvas_height, PrevLayer=Layer1)
        Layer2.NodeAttachments()


        #First Layer Generation of Nodes
        

        #Connect First Layer to Second
        
        
    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()



myNN = NNVisualizer()
myNN.run()


