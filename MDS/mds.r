library(stats)
> library(ggplot2)
> iris=iris
> dis_iris=dist(iris[,1:4],p=2)
> mds_x = cmdscale(dis_iris)
> mds_x = data.frame(mds_x)
> xy = cbind(mds_x,iris[,5])
> ggplot(xy,aes(x=X1,y=X2,colour=iris[,5]))+geom_point()