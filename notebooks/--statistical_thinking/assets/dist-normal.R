x <- seq(from=-4, to=4, length.out=101)
plot(x, dnorm(x), col = 'black', lwd = 2, type='l', 
     axes=FALSE,
     ylim=c(0, 1), 
     xlab='', ylab='')
axis(1, col="darkgray", col.axis="darkgray", cex.axis=0.8)
axis(2, col="darkgray", col.axis="darkgray", cex.axis=0.8)

lines(x, dnorm(x, mean=0,  sd=sqrt(0.2)), col='red', lwd=2)
lines(x, dnorm(x, mean=-2, sd=sqrt(0.5)), col='blue', lwd=2)

text( 0.20, 0.9, pos=4, expression(paste(mu, "=0.0, ", sigma^2, "=0.2")), cex = 1)
text( 1.40, 0.2, pos=4, expression(paste(mu, "=0.0, ", sigma^2, "=1.0")), cex = 1)
text(-2.00, 0.63, pos=NULL, expression(paste(mu, "=-2.0, ", sigma^2, "=0.5")), cex = 1)


