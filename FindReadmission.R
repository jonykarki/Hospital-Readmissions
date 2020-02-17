# Find the readmitted ones

rm(list=ls())
setwd("")
readmission.days.req = 30

# data = read.csv("Data1.csv")
# uniqdata = unique(data)
# write.csv(uniqdata, "uniq_data_one.csv")

data = read.csv("D1_sFNDOB.csv")
data["IsReadmission"] <- 0

previous.date = as.Date(data[2,]["Disch.Date"][[1]],format='%m/%d/%Y')
previous.name = data[2,]["First.Name"][[1]]
data[2,]["First.Name"][[1]]
previous.dob = data[2,]["Date.of.Birth"][[1]]
for(i in 2:nrow(data)) 
{
  print(i)
  current.row = data[i,]
  current.name = current.row["First.Name"][[1]]
  current.dob = current.row["Date.of.Birth"][[1]]
  current.dob == previous.dob
  
  # first check if it's the same person
  if (current.name == previous.name && current.dob == previous.dob){
    # check if the admission was within (30) days
    current.date = as.Date(data[i,]["Admit.Date"][[1]],format='%m/%d/%Y')
    if ((current.date - previous.date) <= readmission.days.req) {
      data[i,]["IsReadmission"] = 1
    }
  }
  
  previous.date = as.Date(current.row["Disch.Date"][[1]],format='%m/%d/%Y')
  previous.name = current.name
  previous.dob = current.dob
}

write.csv(data, "result.csv")
