using Plots
pyplot()

ak = (k) -> 2/(k^2 * pi^2) * (1 - cos(k * pi))

ts = 1:10

p = plot(ts, ak)
display(p)



