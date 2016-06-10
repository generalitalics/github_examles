# Пример класса

class Building:


    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
        # raise NotImplementedError

    def corners(self):
        dic = {}
        dic['south-east'] = [self.south, self.west + self.width_WE]
        dic['north-west'] = [self.south + self.width_NS, self.west]
        dic['north-east'] = [self.south + self.width_NS, self.west + self.width_WE]
        dic['south-west'] = [self.south, self.west]
        return dic
        #raise NotImplementedError
    
    def area(self):
        area = self.width_NS * self.width_WE
        return area
        #raise NotImplementedError
        
    def volume(self):
        volume = self.area() * self.height
        return volume
        #raise NotImplementedError
    #
    def __repr__(self):
        st = "Building({south}, {west}, {width_we}, {width_ns}, {height})"
        st2 = st.format(south=self.south, west=self.west, width_we=self.width_WE, width_ns=self.width_NS,
                        height=self.height)
        return st2
        #raise NotImplementedError

b = Building(1, 2, 2, 3)
print(b.corners())
print(b.area())
print(b.volume())
print(str(b))
