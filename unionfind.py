class UnionFind:
  def __init__(self, t=1, h=0, w=0):
    if t == 1:
      self.t = 1
      self.par = [-1]*h
      self.size = [1]*h
      self.len = h
    elif t == 2:
      self.t = 2
      self.par = [[-1 for i in range(h)] for j in range(w)]
      self.size = [[1]*h for i in range(w)]
      self.len = h
      self.width = w
    else:
      self.t = 0
      self.par = []
      self.size = []
      self.len = 0
      
  def __len__(self):
    return self.len
  
  def is_same(self, x, y):
    if self.t == 1:
      return self.root(x) == self.root(y)
    elif self.t == 2:
      rx = self.root(x)
      ry = self.root(y)
      return rx[0] == ry[0] and rx[1] == ry[1]
  
  def root(self, x):
    if self.t == 1:
      if self.par[x] == -1:
        return x
      else:
        tmp = self.root(self.par[x])
        self.par[x] = tmp
        return tmp
    elif self.t == 2:
      if self.par[x[0]][x[1]] == -1:
        return x[:]
      else:
        tmp = self.root(self.par[x[0]][x[1]])
        self.par[x[0]][x[1]] = tmp[:]
        return tmp[:]
      
  def unite(self, x, y):
    x, y = self.root(x), self.root(y)
    if self.t == 1:
      if x == y:
        return False
      else:
        if self.size[x] > self.size[y]:
          self.par[y] = x
          self.size[x] += self.size[y]
          return True
        else:
          self.par[x] = y
          self.size[y] += self.size[x]
          return True

    if self.t == 2:
      if x[0] == y[0] and x[1] == y[1]:
        return False

      else:
        if self.size[x[0]][x[1]] > self.size[y[0]][y[1]]:
          self.par[y[0]][y[1]] = [x[0], x[1]]
          self.size[x[0]][x[1]] += self.size[y[0]][y[1]]
          return True

        else:
          self.par[x[0]][x[1]] = [y[0], y[1]]
          self.size[y[0]][y[1]] += self.size[x[0]][x[1]]
          return True
  
  def size(self, x):
    if self.t == 1:
      return self.size[self.root(x)]

    if self.t == 2:
      rx = self.root(x)[:]
      return self.size[rx[0]][rx[1]]
