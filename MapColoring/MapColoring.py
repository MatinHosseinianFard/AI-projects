import time
from Countries import Australia, Sweden


class MapColoring:
    def __init__(self, nodes, numberOfColors, countryName) -> None:
        self.nodes = nodes
        self.numberOfColors = numberOfColors
        self.countryName = countryName
        self.visited = []

    def printSolution(self):
        print(f"Solution Exists: Following are the assigned colors for {self.countryName} ")
        for i, j in self.nodes.items():
            key = list(colors)[j['color']-1]
            val = list(colors.values())[j['color']-1]
            print(val + i, colors['RESET'])

    def remValCalculator(self, node, color):
        affectedCities = []
        for city in self.nodes[node]['neighbours']:
            if city not in self.visited:
                if color in self.nodes[city]['rem_val']:
                    self.nodes[city]['rem_val'].remove(color)
                    affectedCities.append([city, color])
        return affectedCities
    
    def getNodeWithMRVDegree(self):
        # Find the MRV value of the nodes that have the lowest MRV among the nodes that are not visited
        minCount = len(self.nodes[min({key: value for (key, value) in self.nodes.items(
        ) if key not in self.visited}, key=lambda v: len(self.nodes[v]['rem_val']))]['rem_val'])

        # Finding the node that has the highest degree among the nodes with the lowest MRV value and return it
        selectedNode = max({key: value for (key, value) in self.nodes.items() if key not in self.visited and len(
            value['rem_val']) == minCount}, key=lambda v: len(self.nodes[v]['neighbours']))
        return selectedNode

    def getColorsWithLCV(self, selectedNode):
        # Counting the number of constraints each color creates
        lis = []
        for value in self.nodes[selectedNode]['rem_val']:
            count = 0
            for key in self.nodes[selectedNode]['neighbours']:
                if key not in self.visited:
                    if value in self.nodes[key]['rem_val']:
                        count += 1
            lis.append([value, count])

        # Sort and return colors according to the constraints they create
        lis.sort(key=lambda item: item[1])
        orderedColors = [item[0] for item in lis]
        return orderedColors

    def solve(self, i):

        # if current index reached end then print solution and return
        if (i == len(self.nodes)):
            self.printSolution()
            return True

        # Node selection based on MRV & Degree heuristic
        selectedNode = self.getNodeWithMRVDegree()

        # Sort color assignment based on LCV heuristic
        orderedColors = self.getColorsWithLCV(selectedNode)

        for color in orderedColors:
            # Assign one of the colors in the domain to this node
            self.nodes[selectedNode]['color'] = color

            # Removing the color of the node from the remaining colors of the neighboring nodes and gives affected nodes
            affectedCities = self.remValCalculator(selectedNode, color)

            # Add selected node to visited
            self.visited.append(selectedNode)

            # Go to another node for color assignment
            if (self.solve(i + 1)):
                return True

            # If it fails, return to the state before assigning this color
            self.nodes[selectedNode]['color'] = 0
            self.nodes[selectedNode]['rem_val'] = orderedColors
            self.visited.remove(selectedNode)
            
            # Return the values taken from the neighbors of the selected node  
            for city in affectedCities:
                self.nodes[city[0]]['rem_val'].append(city[1])

        return False


if __name__ == '__main__':

    colors = {'RED': '\033[31m', 'GREEN': '\033[32m',
              'BLUE': '\033[34m', 'YELLOW': '\033[33m', 'RESET': '\033[0m'}

    start_time = time.time()
    test1 = MapColoring(Australia, numberOfColors=3, countryName="Australia")
    if not test1.solve(0):
        print("Solution Does Not Exists")
    print("Execution Time: ", time.time() - start_time, "s")
    
    print()
    
    start_time = time.time()
    test2 = MapColoring(Sweden, numberOfColors=4, countryName="Sweden")
    if not test2.solve(0):
        print("Solution Does Not Exists")
    print("Execution Time: ", time.time() - start_time, "s")
