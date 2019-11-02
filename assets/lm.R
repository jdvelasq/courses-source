set.seed(1234567)

x = 0.2 + 0.6 * runif(10) 
y = 0.9 * x + 0.05 * rnorm(10) - 0.1
test = data.frame(x=c(0, 1.2))

x = c(x, 0.0); y = c(y, 1)

df = data.frame(x=x, y=y)
m = lm(y ~ x, df) 

plot(test$x, predict(m, test), 
     col = 'black', pch = 19, cex = 0.5, type='l',
     xlim=c(0, 1), ylim=c(0,1), lwd = 1,
     ylab='y',  xlab='x', axes=FALSE)
box(col="gray")
axis(1, col="gray", col.axis="black", cex.axis=0.6)
axis(2, col="gray", col.axis="black", cex.axis=0.6)
grid()
points(df$x, df$y, pch=19, col='black', cex = 0.6)







##
##
##


library(MASS)


set.seed(1234567)
x = c(0.2, 0.8)
y = c(0.2, 0.8)

df = data.frame(x=x, y=y)
m = lm(y ~ x, df) 
test = data.frame(x=c(0, 1))


plot(test$x, predict(m, test), 
     col = 'blue', pch = 19, cex = 0.5, type='l',
     xlim=c(0, 1), ylim=c(0,1), lwd = 2,
     ylab='y',  xlab='x', axes=FALSE)
box(col="gray")
axis(1, col="gray", col.axis="black", cex.axis=0.6)
axis(2, col="gray", col.axis="black", cex.axis=0.6)
grid()

points(df$x, df$y, pch=19, col='red')

for(i in 1:8)
{
	this_x = c(df$x + 0.08 * rnorm(2), df$x + 0.08 * rnorm(2))
	z = data.frame(x = this_x, y = c(y, y))
	m = lm.ridge(y ~ x, z)
	lines(test$x, predict(m, test), col = 'gray') 
	## points(z$x, z$y, pch=19, col='gray', cex=0.5)		
}



