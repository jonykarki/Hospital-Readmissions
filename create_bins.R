rm(list=ls())
setwd("")
data = read.csv("data.csv", stringsAsFactors = FALSE)

## method 1
# breaks <- c(min(data$LOS, na.rm = TRUE), 30, 40, max(data$LOS, na.rm=TRUE))
# names <- c("0-30","30-40","40-69")
# group_tags <- cut(data$LOS, breaks=breaks, labels=names, right = FALSE)

groups <- cut(data$LOS, breaks=3)
summary(groups)

data$LOS_Bins <- cut(data$LOS, breaks=3)

# data$LOS_Bins <- cut(data$LOS, breaks=breaks, labels=names)

