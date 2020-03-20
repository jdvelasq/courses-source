
set.seed(12345)
N1 = 15
N2 = 20
x  = c(runif(N1) * 0.55, 0.5 + runif(N2) * 0.45)
y = c(rep(0, N1), rep(1, N2))

df = data.frame(x=x, y=y)

m = lm(y ~ x, df)

plot(df$x, df$y, col = 'black', bg = 'black', pch = 19, cex = 0.5,
     xlim=c(-0.1, 1.2), ylim=c(-0.1,1.1), ylab='y',  xlab='x', axes=FALSE)
box(col="gray")
axis(1, col="gray", col.axis="black", cex.axis=0.6)
axis(2, col="gray", col.axis="black", cex.axis=0.6)
grid()

p = predict(m, df)
lines(df$x, p)


###
x = seq(from=-6, to=6, length.out=100)
y = 1 / (1 + exp(-x))

plot(x, y, col = 'black', pch = 19, cex = 0.5, type = 'l',
     xlim=c(-6, 6), ylim=c(-0.1,1.1), ylab='s(u)',  xlab='u', axes=FALSE)
box(col="gray")
axis(1, col="gray", col.axis="black", cex.axis=0.6)
axis(2, col="gray", col.axis="black", cex.axis=0.6)
grid()

###
m = glm(y ~ x, data=df, family=binomial(link='logit'))

z = data.frame(x=seq(from=0, to=1, length.out=80))
p = predict(m, z)
p = 1 / (1 + exp(-p))

plot(df$x, df$y, col = 'black', bg = 'black', pch = 19, cex = 0.6,
     xlim=c(-0.05, 1.05), ylim=c(-0.05,1.05), ylab='y',  xlab='x', axes=FALSE)
box(col="gray")
axis(1, col="gray", col.axis="black", cex.axis=0.6)
axis(2, col="gray", col.axis="black", cex.axis=0.6)
grid()
lines(z$x, p, col='red', lwd=1)

