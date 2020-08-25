import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import math

class main:
    path = "C:\\Users\\" + os.getlogin() + "\\Desktop\\gcodeSIM\\"
    name = "code3.gcode"
    coords = []
    layers = []
    x = []
    y = []
    z = []
    currentz = '0.2'
    def check(self, array):
        for line in array:
            if 'G1' in line:
                start = line.find('X')
                end = line.find('E')
                line = line[start:end]
                line = line.replace('X', '')
                line = line.replace('Y', '')
                self.coords.append(line + str(self.currentz))
            elif 'G0' in line:
                if 'Z' in line:
                    start = line.find('Z')
                    end = line.find('\n')
                    line = line[start:end].replace('Z', '')
                    self.layers.append(line)
                    self.currentz = line

    def main(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        print(self.path + self.name)
        with open(self.path + self.name, "r") as f:
            self.check(f.readlines())
            f.close

        for instruction in self.coords:
            try:
                self.z.append(float(instruction.split(' ')[2]))
                self.y.append(float(instruction.split(' ')[1]))
                self.x.append(float(instruction.split(' ')[0]))
                
                
            except Exception:
                pass
        print('Print layers: ' + str(len(self.layers)))
        print('Instruction lenght: ' + str(len(self.coords)))
        Axes3D.scatter3D(ax, self.x, self.y, self.z, c=self.z, cmap="viridis")
        plt.show()

if __name__ == "__main__":
    m = main()
    m.main()