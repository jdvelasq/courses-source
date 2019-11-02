## generacion de los datos

set.seed(12345678)

df <- data.frame(x1=rnorm(30),
                 x2=rnorm(30),
                 x3=rnorm(30))
                 
df$y = 1.56 * df$x1 - 0.53 * df$x2 + 0.1 * rnorm(30)

df$y[1]  = 8.96
df$y[29] = 9.52
df$y[30] = 9.36

for(i in 1:30)
{
	cat(sprintf("      %2d   %5.2f   %5.2f   %5.2f   %5.2f\n", i, df$x1[i], df$x2[i], df$x3[i], df$y[i]))	
} 


##
## regresion simple
##
m = lm(y ~ ., data = df)
summary(m)

hist(m$residuals, freq=FALSE, ylim=c(0, 0.3), main='', xlab='', ylab='')
lines(density(m$residuals), col='red', lwd = 2)

str(m)

## ridge regression
library(MASS)
m = lm.ridge(y ~ ., data = df)
print(m)

m = lm.ridge(y ~ ., data = df, lambda = seq(0, 0.5, 0.01))
print(m)
