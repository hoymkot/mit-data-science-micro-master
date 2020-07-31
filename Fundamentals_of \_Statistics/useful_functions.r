wald_test_ gaussian <- function(data, hypo) {
  a = mean(data) #  average
  v = sd(data)^2 * (length(data) - 1) /length(data) # variance
  d = matrix(c(a, v) - hypo) # deviation from hypo
  I = matrix(c(1/hypo[2], 0,0,1/(2*hypo[2]^2)),2) # fisher info
  w = t(d) %*% I %*% d * length(data)  
  return(w)
}

WelchSatterthwaite <- function(sx, sy, nx, my) {
  num = (sx/nx + sy/my)^2
  den = (sx/nx)^2/(nx-1) + (sy/my)^2/(my-1); 
  return (num/den);
}

ks.statistic <- function(x){
  x <- sort(x)  # reordered sample 
  n <- length(x)
  i <- 1:n

  max(
    max(abs((i-1)/n - punif(x))), 
    max(abs(i/n - punif(x)))
    ) * sqrt(n)
}
x = c(0.8,0.7,0.4,0.7,0.2)
ks.statistic(x)
