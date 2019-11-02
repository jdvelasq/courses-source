
set.seed(12345)

## cantidad de puntos por cluster
N1 <- 20
N2 <- 20
N3 <- 20

## datos aleatorios 
x = c(0.03 + 0.21 * runif(N1),
      0.10 + 0.20 * runif(N2),
      0.60 + 0.24 * runif(N3))
         
y = c(0.10 + 0.25 * runif(N1),
      0.65 + 0.28 * runif(N2),
      0.20 + 0.30 * runif(N3))

## cluster
z = c(rep(0, N1), rep(0, N2), rep(0, N3))
     
df <- data.frame(x=x, y=y)


##
## Grafica 1
##   Puntos sin agrupar
##
par(pty="s")
jpeg(filename = "agrupamiento-1.jpg",
     width = 500, height = 500, units = "px", pointsize = 12,
     quality = 100,
     bg = "white")
  
plot(s$x, s$y, col = 'white', bg = 'black', 
     xlim=c(0,1), ylim=c(0,1), ylab='',  xlab='', axes=FALSE)
box(col="darkgray")
axis(1, col="black", col.axis="black", cex.axis=0.9)
axis(2, col="black", col.axis="black", cex.axis=0.9)

points(df$x, df$y, col='black', bg = 'black', lwd=1, pch=21, cex=0.9)

dev.off()



##
## Grafica 2
##   Puntos sin agrupar
##

## clusters iniciales
x = c(0.48, 0.25, 0.06) 
y = c(0.20, 0.51, 0.62)

df$dist1 = sqrt((df$x - x[1])^2 + (df$y - y[1])^2)
df$dist2 = sqrt((df$x - x[2])^2 + (df$y - y[2])^2)
df$dist3 = sqrt((df$x - x[3])^2 + (df$y - y[3])^2)

## computa los puntos pertenecientes a cada cluster
df$z[df$dist1 <= df$dist2 & df$dist1 <= df$dist3] = 1
df$z[df$dist2 <= df$dist1 & df$dist2 <= df$dist3] = 2
df$z[df$dist3 <= df$dist1 & df$dist3 <= df$dist2] = 3


par(pty="s")
jpeg(filename = "agrupamiento-2.jpg",
     width = 500, height = 500, units = "px", pointsize = 12,
     quality = 100,
     bg = "white")
  
plot(s$x, s$y, col = 'white', bg = 'black', 
     xlim=c(0,1), ylim=c(0,1), ylab='',  xlab='', axes=FALSE)
box(col="darkgray")
axis(1, col="black", col.axis="black", cex.axis=0.9)
axis(2, col="black", col.axis="black", cex.axis=0.9)

## grafica los puntos de cada cluster
s = subset(df, z == 1); 
for(index in 1:nrow(s))
	lines(c(x[1], s$x[index]), c(y[1], s$y[index]), col = 'gray')
points(s$x, s$y, col='blue',  bg = 'blue',  lwd = 1, pch = 21, cex = 0.9)

s = subset(df, z == 2); 
for(index in 1:nrow(s))
	lines(c(x[2], s$x[index]), c(y[2], s$y[index]), col = 'gray')

points(s$x, s$y, col='green', bg = 'green', lwd = 1, pch = 21, cex = 0.9)

s = subset(df, z == 3); 
for(index in 1:nrow(s))
	lines(c(x[3], s$x[index]), c(y[3], s$y[index]), col = 'gray')
points(s$x, s$y, col='red',   bg = 'red',   lwd = 1, pch = 21, cex = 0.9)


## centros de los clusters
points(x[1], y[1], col='blue',  bg = 'blue',  lwd=1, pch=22, cex=2.)
points(x[2], y[2], col='green', bg = 'green', lwd=1, pch=22, cex=2.)
points(x[3], y[3], col='red',   bg = 'red',   lwd=1, pch=22, cex=2.)


dev.off()



##
## Grafica 3
##   K-means
##

for(iter in 1:10)
{
	s = subset(df, z == 1);  x[1] = mean(s$x); y[1] = mean(s$y)
	s = subset(df, z == 2);  x[2] = mean(s$x); y[2] = mean(s$y)
	s = subset(df, z == 3);  x[3] = mean(s$x); y[3] = mean(s$y)

	df$dist1 = sqrt((df$x - x[1])^2 + (df$y - y[1])^2)
	df$dist2 = sqrt((df$x - x[2])^2 + (df$y - y[2])^2)
	df$dist3 = sqrt((df$x - x[3])^2 + (df$y - y[3])^2)

	## computa los puntos pertenecientes a cada cluster
	df$z[df$dist1 <= df$dist2 & df$dist1 <= df$dist3] = 1
	df$z[df$dist2 <= df$dist1 & df$dist2 <= df$dist3] = 2
	df$z[df$dist3 <= df$dist1 & df$dist3 <= df$dist2] = 3
	
}


par(pty="s")
jpeg(filename = "agrupamiento-3.jpg",
     width = 500, height = 500, units = "px", pointsize = 12,
     quality = 100,
     bg = "white")
  
plot(s$x, s$y, col = 'white', bg = 'black', 
     xlim=c(0,1), ylim=c(0,1), ylab='',  xlab='', axes=FALSE)
box(col="darkgray")
axis(1, col="black", col.axis="black", cex.axis=0.9)
axis(2, col="black", col.axis="black", cex.axis=0.9)

## grafica los puntos de cada cluster
s = subset(df, z == 1); 
for(index in 1:nrow(s))
	lines(c(x[1], s$x[index]), c(y[1], s$y[index]), col = 'gray')
points(s$x, s$y, col='blue',  bg = 'blue',  lwd = 1, pch = 21, cex = 0.9)

s = subset(df, z == 2); 
for(index in 1:nrow(s))
	lines(c(x[2], s$x[index]), c(y[2], s$y[index]), col = 'gray')

points(s$x, s$y, col='green', bg = 'green', lwd = 1, pch = 21, cex = 0.9)

s = subset(df, z == 3); 
for(index in 1:nrow(s))
	lines(c(x[3], s$x[index]), c(y[3], s$y[index]), col = 'gray')
points(s$x, s$y, col='red',   bg = 'red',   lwd = 1, pch = 21, cex = 0.9)


## centros de los clusters
points(x[1], y[1], col='blue',  bg = 'blue',  lwd=1, pch=22, cex=2.)
points(x[2], y[2], col='green', bg = 'green', lwd=1, pch=22, cex=2.)
points(x[3], y[3], col='red',   bg = 'red',   lwd=1, pch=22, cex=2.)


dev.off()




##
## Grafica 4
##   Canopy
##

par(pty="s")
jpeg(filename = "agrupamiento-4.jpg",
     width = 500, height = 500, units = "px", pointsize = 12,
     quality = 100,
     bg = "white")
  
plot(s$x, s$y, col = 'white', bg = 'black', 
     xlim=c(0,1), ylim=c(0,1), ylab='',  xlab='', axes=FALSE)
box(col="darkgray")
axis(1, col="black", col.axis="black", cex.axis=0.9)
axis(2, col="black", col.axis="black", cex.axis=0.9)

points(df$x, df$y, col='black', bg = 'black', lwd=1, pch=21, cex=0.9)



df$z = 0

L = 0.15
library(plotrix)
while(nrow(subset(df, z == 0)) > 0)
{
	
	## puntos no asignados a un canopy
	s = subset(df, z == 0)
	n = sample(1:nrow(s), 1)
	x = s$x[n]
	y = s$y[n]
	
	df$dist = sqrt((df$x - x)^2 + (df$y - y)^2)
	df$z[df$z == 0 & df$dist <= L] = max(df$z) + 1
	
	draw.circle(x, y, L, nv = 1000, border = NULL, col = NA, lty = 1, lwd = 1)
	
}
cat('termine')


dev.off()




