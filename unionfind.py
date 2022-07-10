class UnionFind:
  """
  Attributes
  ----------
  t: int
    1次元配列か2次元配列かを選択する
  par: List[int] or List[List[int]]
    どのグループに属するかを保存する
  size: int
    そのノードが属するグループのサイズを保存する
  len: int
    横の長さ(1次元方向の長さ)
  height: int
    縦の長さ(2次元方向の長さ)
  """
  def __init__(self, t=1, w=0, h=0):
    """
    Parameter
    ---------
    t: int
      1次元配列か二次元配列かを選択する
    w: int
      1次元方向の長さ
    h: int
      2次元方向の長さ
    """
    if t == 1:
      self.t = 1
      self.par = [-1]*w
      self.size = [1]*w
      self.len = w
    elif t == 2:
      self.t = 2
      self.par = [[-1 for i in range(w)] for j in range(h)]
      self.size = [[1]*w for i in range(h)]
      self.len = w
      self.height = h
    else:
      """
      3次元以上は未実装
      """
      self.t = 0
      self.par = []
      self.size = []
      self.len = 0
      
  def __len__(self):
    return self.len
  
  def is_same(self, x, y):
    """
    xとyが同じグループに属するかを判定する
    
    Parameter
    ---------
    x: int or List[int]
      ノード1の位置
    y: int or List[int]
      ノード2の位置
    """
    if self.t == 1:
      return self.root(x) == self.root(y)
    elif self.t == 2:
      rx = self.root(x)
      ry = self.root(y)
      return rx[0] == ry[0] and rx[1] == ry[1]
  
  def root(self, x):
    """
    xの親要素の位置を取得する
    
    Parameter
    ---------
    x: int or List[int]
      ノードの位置
    """
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
    """
    xとyを合体
    
    Parameter
    ---------
    x: int or List[int]
      ノード1の位置
    y: int or List[int]
      ノード2の位置
    """
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
    """
    xの属するグループの大きさを取得
    
    Parameter
    ---------
    x: int or List[int]
      ノードの位置
    """
    if self.t == 1:
      return self.size[self.root(x)]

    if self.t == 2:
      rx = self.root(x)[:]
      return self.size[rx[0]][rx[1]]
