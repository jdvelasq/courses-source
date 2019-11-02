##
## 
##

## datos para las clases
x <- c( 1, 2, 3, 4, 1, 2, 3, 4, 1, 2 ,3, 4, 1, 2 ,3, 4)
y <- c( 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4)
z <- c( 1, 1, 3, 3, 1, 2, 2, 3, 1, 2, 2, 3, 1, 1, 1, 2)


jpeg(filename = "tree-exercise.jpg",
     width = 500, height = 500, units = "px", pointsize = 12,
     quality = 100,
     bg = "white")
     
plot(x, y, 
     col = 'white', bg  = 'white', 
     xlim=c(0,5), ylim=c(0,5), 
     ylab='x2',  xlab='x1', 
     asp = 1,
     axes=FALSE)
     
box(col="gray")
axis(1, col="black", col.axis="black", cex.axis=1.0)
axis(2, col="black", col.axis="black", cex.axis=1.0)
grid()

x1 <- x[z == 1]
y1 <- y[z == 1]
x2 <- x[z == 2]
y2 <- y[z == 2]
x3 <- x[z == 3]
y3 <- y[z == 3]

points(x1, y1, col='red',      lwd = 2, pch = 19, cex=1.5)
points(x2, y2, col='blue',     lwd = 2, pch = 19, cex=1.5)
points(x3, y3, col='darkgray', lwd = 2, pch = 19, cex=1.5)


dev.off()

