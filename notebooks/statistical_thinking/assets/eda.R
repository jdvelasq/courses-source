df <- read.csv('muestra.csv')

## 
summary(df)


## 
par(mfrow=c(2,3))
z <- subset(df, Clase == 'A'); hist(z$ancho, main ='Clase A', xlab='Ancho')
z <- subset(df, Clase == 'B'); hist(z$ancho, main ='Clase B', xlab='Ancho')
z <- subset(df, Clase == 'C'); hist(z$ancho, main ='Clase C', xlab='Ancho')
z <- subset(df, Clase == 'A'); hist(z$largo, main = '', xlab='Largo')
z <- subset(df, Clase == 'B'); hist(z$largo, main = '', xlab='Largo')
z <- subset(df, Clase == 'C'); hist(z$largo, main = '', xlab='Largo')

##

par(mfrow=c(1,2))
boxplot(ancho ~ Clase, data=df, main = 'Ancho', cex = 0.8, col = 'gray')
boxplot(largo ~ Clase, data=df, main = 'Largo', cex = 0.8, col = 'gray')

##
par(mfrow=c(1,2))

z <- subset(df, Clase == 'A')
hist(z$ancho, xlim=c(8,18), 
     col=rgb(1,0,0,0.5), 
     xlab="Ancho", 
     ylab=" ", main="" )

z <- subset(df, Clase == 'B'); hist(z$ancho, xlim=c(8,18), col=rgb(0,0,1,0.5), add=T)
z <- subset(df, Clase == 'C'); hist(z$ancho, xlim=c(8,18), col=rgb(0,1,0,0.5), add=T)
legend("topright", legend=c("A","B", "C"), col=c(rgb(1,0,0,0.5), 
     rgb(0,0,1,0.5), rgb(0,1,0,0.5)), pt.cex=2, pch=15 )



z <- subset(df, Clase == 'A')
hist(z$largo, xlim=c(5, 20), ylim=c(0,18), 
     col=rgb(1,0,0,0.5), 
     xlab="Largo", 
     ylab=" ", main="" )

z <- subset(df, Clase == 'B'); hist(z$largo, xlim=c(5,20), ylim=c(0,18), col=rgb(0,0,1,0.5), add=T)
z <- subset(df, Clase == 'C'); hist(z$largo, xlim=c(5,20), ylim=c(0,18), col=rgb(0,1,0,0.5), add=T)
legend("topright", legend=c("A","B", "C"), col=c(rgb(1,0,0,0.5), 
     rgb(0,0,1,0.5), rgb(0,1,0,0.5)), pt.cex=2, pch=15 )

##

par(mfrow=c(1,2))

z <- subset(df, Clase == 'A')
plot(density(z$ancho), xlim=c(8,18), 
     col='red', 
     xlab="Ancho", 
     ylab=" ", main="", lwd = 2 )

z <- subset(df, Clase == 'B'); lines(density(z$ancho), col='blue', lwd=2)
z <- subset(df, Clase == 'C'); lines(density(z$ancho), col='green', lwd=2)
legend("topright", legend=c("A","B", "C"), col=c('red', 'blue', 'green'), pt.cex=2, pch=15 )



z <- subset(df, Clase == 'A')
plot(density(z$largo), xlim=c(5, 20),
     col='red', 
     xlab="Largo", 
     ylab=" ", main="", lwd=2 )

z <- subset(df, Clase == 'B'); lines(density(z$largo), col='blue', lwd=2)
z <- subset(df, Clase == 'C'); lines(density(z$largo), col='green',  lwd=2)
legend("topright", legend=c("A","B", "C"), col=c('red', 'blue', 'green'), pt.cex=2, pch=15 )


##

z <- subset(df, Clase == 'A'); summary(z)
z <- subset(df, Clase == 'B'); summary(z)
z <- subset(df, Clase == 'C'); summary(z)

##

panel.hist <- function(x, ...)
{
    usr <- par("usr"); on.exit(par(usr))
    par(usr = c(usr[1:2], 0, 1.5) )
    h <- hist(x, plot = FALSE)
    breaks <- h$breaks; nB <- length(breaks)
    y <- h$counts; y <- y/max(y)
    rect(breaks[-nB], 0, breaks[-1], y, col = "cyan", ...)
}

panel.cor <- function(x, y, digits = 2, prefix = "", cex.cor, ...)
{
    usr <- par("usr"); on.exit(par(usr))
    par(usr = c(0, 1, 0, 1))
    r <- abs(cor(x, y))
    
    txt <- format(c(r, 0.123456789), digits = digits)[1]
    txt <- paste0(prefix, txt)
    if(missing(cex.cor)) cex.cor <- 0.8/strwidth(txt)
    text(0.5, 0.5, txt, cex = cex.cor * r)
}

pairs(df, col=df$Clase)
pairs(df, diag.panel = panel.hist)

##

library(vioplot)
par(mfrow=c(1,2))
A <- subset(df, Clase == 'A'); summary(z)
B <- subset(df, Clase == 'B'); summary(z)
C <- subset(df, Clase == 'C'); summary(z)
vioplot(A$ancho, B$ancho, C$ancho, col='gray')
vioplot(A$largo, B$largo, C$largo, col='gray')

##

library(hexbin)
#par(mfrow=c(1,3))
#plot(hexbin(A$ancho, A$largo))
#plot(hexbin(B$ancho, B$largo))
plot(hexbin(C$ancho, C$largo))



#legend("topright", legend=c("Ixos","Primadur"), col=c(rgb(1,0,0,0.5), 
#     rgb(0,0,1,0.5)), pt.cex=2, pch=15 )