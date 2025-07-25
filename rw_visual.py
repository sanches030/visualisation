import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:                                 
  rw = RandomWalk(50_000)
  rw.fill_walk()

  plt.style.use('classic')
  fig, ax = plt.subplots()
  point_numbers = range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
             cmap=plt.cm.Blues, edgecolors='none', s=2)
  plt.show()

  keep_running = input("Згенерувати нове блукання? (y/n): ")
  if keep_running == 'n':
    break