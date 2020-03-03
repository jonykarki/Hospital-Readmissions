
rm(list=ls())
setwd("")
data = read.csv("finala.csv", stringsAsFactors = FALSE)
disease <- data.frame(Disease=character(), stringsAsFactors = FALSE)

for(i in 1:nrow(data)) 
{
  current.row = data[i,]
  if (current.row["IsReadmission"][[1]] == "1"){
    disease <- rbind(disease, data.frame(Disease = toString(data[i,]$Reason.for.Visit.Call)))
    #print(current.row["Reason.for.Visit.Call"][[1]])
    #disease <- rbind(disease, c(count,))
  }
}

write.csv(disease,"disease and readmission.csv")


#Histogram
rm(list=ls())
setwd("")
data = read.csv("disease and readmission.csv")
freq = rev(sort(table(data$Disease)))[1:7]
freq
barplot(freq,cex.names=0.8,space=0.1)

