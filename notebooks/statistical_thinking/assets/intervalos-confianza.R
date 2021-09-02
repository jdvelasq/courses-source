ciplot <- function()
{
	normplot <- function(limits=4, sigma = 1)
	{
		x <- seq(from=-limits, to=limits, length.out=100)
		y <- dnorm(x)
		plot(x, y, type = 'l', lwd=1,
		     ylab='',  xlab='', axes=FALSE,)
	    box(col="gray")
    	axis(1, col="darkgray", col.axis="darkgray", cex.axis=1.2)
	    axis(2, col="darkgray", col.axis="darkgray", cex.axis=1.2)
	    lines(c(-limits, limits), c(0,0), col='darkgray')
	    
	    area.x <- seq(from=-sigma, to=sigma, length.out=100)	
		area.y <- dnorm(area.x)
	    polygon(c(-sigma, area.x, sigma), c(0, area.y, 0), col='lightgray', lwd=3)    
	}
	

	par(mfrow=c(1,3))	

	normplot(sigma=3)
	title('', cex=0.5)
#	lines(c(-3, -3), c(-0.1, 0.25), col='red', lwd=2)
#	lines(c( 3,  3), c(-0.1, 0.25), col='red', lwd=2)
 	text(0, 0.1, pos=NULL, '99.70%', cex = 2.4)
	
	normplot(sigma=2)
	title('', cex=0.5)
#	lines(c(-2, -2), c(-0.1, 0.25), col='red', lwd=2)
#	lines(c( 2,  2), c(-0.1, 0.25), col='red', lwd=2)
	text(0, 0.1, pos=NULL, '95.44%', cex = 2.4)
	
	normplot(sigma=1)
	title('', cex=0.5)
#	lines(c(-1, -1), c(-0.1, 0.30), col='red', lwd=2)
#	lines(c(+1, +1), c(-0.1, 0.30), col='red', lwd=2)
	text(0, 0.1, pos=NULL, '68.26%', cex = 2.4)
	
}

jpeg(filename = "intervalos-confianza.jpg",
     width = 1300, height = 400, units = "px", pointsize = 12,
     quality = 100,
     bg = "white")
     
ciplot()

dev.off()
