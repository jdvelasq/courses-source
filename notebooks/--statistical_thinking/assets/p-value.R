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
	
	right_tailed <- function(z.test, limits=4, pvalue=TRUE)
	{
		p <- dnorm(z.test)
		x <- seq(from=z.test, to=limits, length.out=20)	
		y <- dnorm(x)
		polygon(c(z.test, x, limits), c(0, y, 0), col='gray')
		z <- dnorm(z.test) + 0.05
		lines(c(z.test, z.test), c(-0.1, z), lwd = 2)
		if (pvalue)
			text(z.test, z-0.01, pos = 4, sprintf('p-value=%6.4f', 1-pnorm(z.test)), cex = 1.2)
	}

	left_tailed <- function(z.test, limits=4, pvalue=TRUE)
	{
		p <- dnorm(z.test)
		x <- seq(from=-limits, to=z.test, length.out=50)	
		y <- dnorm(x)
		polygon(c(-limits, x, z.test), c(0, y, 0), col='gray')
		z <- dnorm(z.test) + 0.05
		lines(c(z.test, z.test), c(-0.1,z), lwd=2)
		if (pvalue)
			text(z.test, z-0.01, pos=4, sprintf('p-value = %6.4f', pnorm(z.test)), cex = 1.2)
	}
	
	two_tailed <- function(z.test, limits=4)
	{
		left_tailed(  -z.test, limits, pvalue=FALSE)		
		right_tailed( z.test, limits, pvalue=FALSE)		
		pvalue = 2 * pnorm(-abs(z.test))
		text(0, 0.05, pos=NULL, sprintf('p-value = %6.4f', pvalue), cex = 1.2)
	}

	par(mfrow=c(1,3))
	
	normplot()
	title('Cola a la izquierda', cex=0.5)
	lines(c(1.75, 1.75), c(-0.1, 0.25), col='red', lwd=2)
	text(1.75, 0.25, pos=4, '1.75', cex = 1.2)
	left_tailed(z.test=1.75)
	
	normplot()
	title('Dos colas', cex=0.5)
	lines(c(-1.75, -1.75), c(-0.1, 0.25), col='red', lwd=2)
	lines(c( 1.75,  1.75), c(-0.1, 0.25), col='red', lwd=2)
	text(1.75, 0.25, pos=4, '1.75', cex = 1.2)
	text(-1.75, 0.25, pos=2, '-1.75', cex = 1.2)
	two_tailed(z.test=1.75)
	
	normplot()
	title('Cola a la derecha', cex=0.5)
	lines(c(1.75, 1.75), c(-0.1, 0.25), col='red', lwd=2)
	text(1.75, 0.25, pos=4, '1.75', cex = 1.2)
	right_tailed(z.test=1.75)
	
}

colas()