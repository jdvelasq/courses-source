colas <- function()
{
	normplot <- function(limits=4)
	{
		x <- seq(from=-limits, to=limits, length.out=100)
		y <- dnorm(x)
		plot(x, y, type = 'l', lwd=1,
		     ylab='',  xlab='', axes=FALSE,)
	    box(col="gray")
    	axis(1, col="gray", col.axis="gray", cex.axis=0.8)
	    axis(2, col="gray", col.axis="gray", cex.axis=0.8)
	    lines(c(-limits, limits), c(0,0), col='gray')
	}
	
	right_tailed <- function(alpha=0.1, limits=4)
	{
		p <- qnorm(1 - alpha)
		x <- seq(from=p, to=limits, length.out=20)	
		y <- dnorm(x)
		polygon(c(p, x, limits), c(0, y, 0), col='gray')
		z <- dnorm(p) + 0.05
		lines(c(p, p), c(-0.1, z), lwd = 2)
		text(p, z-0.01, pos = 4, sprintf('%6.4f', p), cex = 1.2)
	}

	left_tailed <- function(alpha=0.1, limits=4)
	{
		p <- qnorm(alpha)
		x <- seq(from=-limits, to=p, length.out=20)	
		y <- dnorm(x)
		polygon(c(-limits, x, p), c(0, y, 0), col='gray')
		z <- dnorm(p) + 0.05
		lines(c(p, p), c(-0.1,z), lwd=2)
		text(p, z-0.01, pos=2, sprintf('%6.4f', p), cex = 1.2)
	}
	
	two_tailed <- function(alpha=0.1, limits=4)
	{
		left_tailed(  alpha/2.0, limits)		
		right_tailed( alpha/2.0, limits)		
	}

	par(mfrow=c(1,3))
	
	normplot()
	left_tailed(alpha=0.05)
	title('Cola a la izquierda', cex=0.5)
	lines(c(1.75, 1.75), c(-0.1, 0.25), col='red', lwd=2)
	text(1.75, 0.25, pos=4, '1.75', cex = 1.2)
	
	normplot()
	two_tailed(alpha=0.05)
	title('Dos colas', cex=0.5)
	lines(c(1.75, 1.75), c(-0.1, 0.25), col='red', lwd=2)
	text(1.75, 0.25, pos=4, '1.75', cex = 1.2)
	
	normplot()
	right_tailed(alpha=0.05)
	title('Cola a la derecha', cex=0.5)
	lines(c(1.75, 1.75), c(-0.1, 0.25), col='red', lwd=2)
	text(1.75, 0.25, pos=4, '1.75', cex = 1.2)
	
}

colas()