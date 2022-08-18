#import the library pulp as p 
import pulp as p 


#Create a LP maximisation problem 
Lp_prob = p.LpProblem('Problem' , p.LpMaximize)

#Create problem variables 
x = p.LpVariable("x" , lowBound=0 )
y = p.LpVariable("y" , lowBound=0 )

#objective function 
Lp_prob += 25 * x + 20 * y

#Constraints
Lp_prob += 6 * x + 4 * y <= 3600
Lp_prob += 2 * x + 4 * y <= 2000

#Display the problem 
print(Lp_prob)

 



status = Lp_prob.solve()
print(p.LpStatus[status])

#printing final solution
print("Cordinates are:", "(",p.value(x) ,",", p.value(y),")", "\n" "The maximum value is :", p.value(Lp_prob.objective))
