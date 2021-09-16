
set.seed(12345)

N1 <- 25
N2 <- 30
N3 <- 40

x = c(0.03 + 0.21 * runif(N1),
      0.10 + 0.20 * runif(N2),
      0.60 + 0.24 * runif(N3))
         
y = c(0.10 + 0.25 * runif(N1),
      0.65 + 0.28 * runif(N2),
      0.20 + 0.30 * runif(N3))
     
z = c(rep(0, N1), rep(1, N2), rep(2, N3))
     
df <- data.frame(x=x, y=y, z=z)
      


### Grafica   
plot(s$x, s$y, col = 'white', bg = 'black', xlim=c(0,1), ylim=c(0,1), ylab='',  xlab='', axes=FALSE,)
box(col="gray")

axis(1, col="gray", col.axis="gray", cex.axis=0.6)
axis(2, col="gray", col.axis="gray", cex.axis=0.6)



## puntos fuera de la muestra
x = c(0.06, 0.42, 0.60, 0.36) 
y = c(0.50, 0.76, 0.10, 0.49)


df$dist1 = sqrt((df$x - x[1])^2 + (df$y - y[1])^2)
df$dist2 = sqrt((df$x - x[2])^2 + (df$y - y[2])^2)
df$dist3 = sqrt((df$x - x[3])^2 + (df$y - y[3])^2)
df$dist4 = sqrt((df$x - x[4])^2 + (df$y - y[4])^2)

n1 = order(df$dist1)
n2 = order(df$dist2)
n3 = order(df$dist3)
n4 = order(df$dist4)


## rayos
for(index in 1:8)
{
	lines(c(x[1], df$x[n1[index]]), c(y[1], df$y[n1[index]]), col = 'gray')
	lines(c(x[2], df$x[n2[index]]), c(y[2], df$y[n2[index]]), col = 'gray')
	lines(c(x[3], df$x[n3[index]]), c(y[3], df$y[n3[index]]), col = 'gray')
	lines(c(x[4], df$x[n4[index]]), c(y[4], df$y[n4[index]]), col = 'gray')
	
}

## puntos
s = subset(df, z == 0); points(s$x, s$y, col='blue',  bg = 'white', lwd = 2, pch = 19, cex = 0.5)
s = subset(df, z == 1); points(s$x, s$y, col='red',   bg = 'white', lwd = 2, pch = 19, cex = 0.5)
s = subset(df, z == 2); points(s$x, s$y, col='green', bg = 'white', lwd = 2, pch = 19, cex = 0.5)

points(x[1], y[1], col='black', bg = 'blue', lwd=2, pch=22, cex=1.5)
points(x[2], y[2], col='black', bg = 'red', lwd=2, pch=22, cex=1.5)
points(x[3], y[3], col='black', bg = 'green', lwd=2, pch=22, cex=1.5)
points(x[4], y[4], col='black', bg = 'red', lwd=2, pch=22, cex=1.5)



