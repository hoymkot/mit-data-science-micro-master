wald_test_ gaussian <- function(data, hypo) {
  a = mean(data) #  average
  v = sd(data)^2 * (length(data) - 1) /length(data) # variance
  d = matrix(c(a, v) - hypo) # deviation from hypo
  I = matrix(c(1/hypo[2], 0,0,1/(2*hypo[2]^2)),2) # fisher info
  w = t(d) %*% I %*% d * length(data)  
  return(w)
}
