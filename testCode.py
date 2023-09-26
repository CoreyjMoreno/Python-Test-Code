def intersects(self,minx, miny, maxx, maxy):
     if ((minx < self.minx and maxx < self.minx) or
         (miny < self.miny and maxy < self.miny) or
         (minx < self.maxx and maxx > self.maxx) or
         (miny > self.maxy and maxy > self.maxy)):
            return False
     return True
