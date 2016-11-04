import sys
#print ("year = " + sys.argv[1])
first_year=1973 #the year started from monday
#first_day="mon"
year = int(sys.argv[1])
test = str(sys.argv[2])
#first_day = "sun"
leap = False
day_table = {}
days_in_year = 365
the_week = [ "mon", "tue", "wed", "thu", "fri", "sat", "sun" ]
res = [75,20]
ans = {}
ll=0
ssumm=0
iterat=0
w_ends=0
weighted_average = {}

for y in range(0,80,5):
	weighted_average[y]=0

#=========Main Sequence==========
def CheckYear(year):
	if year < first_year:
		print ("The year myst be above 1970")
	else:
		LeapYear(year)
		FirstWeek(year)
		DaysTable(leap)

#================================

def FirstWeek(year):
	i=0
	global the_week
	global day_table
	global first_year
	years_past=year-first_year
	print("years past " + str(years_past))
	tot_n_of_leaps = divmod(year, 4)[0]
	xx=divmod(years_past,4)[0]
	total_move=((years_past - xx) + (xx*2)) 
	total_move=int(total_move % 7)
	print("total_move is "+str(total_move))
	for i in range(total_move):
		c_day=the_week.pop(0)
		the_week.insert(7, c_day)
	i=0
	for i in range(7):
		print(the_week[i] + " " + str(i))
	print("=======================")



def LeapYear(year):	
	if (year % 4) == 0:
		global leap 
		leap = True
		print("leap year, 366") 
	else:
		print("not leap year, 365")
	print (leap)

def DaysTable(c_leap):
	global test
	i = 0
	global the_week
	global days_in_year
	#print ("DaysTable", c_leap)
	if c_leap == True:
		days_in_year=366
	else:
		days_in_year=365
		#print(c_leap)
	if test == "test": 
		days_in_year=20
	for i in range(days_in_year):
		i = i + 1
		day_table[i]=the_week.pop(0)
		the_week.insert(7, day_table[i])
		#print(day_table[i] + " " + str(i))
			
def Seconds(c_leap):
	hours = 24
	minutes = 60
	seconds = 60
	day_secons = hours * minutes * seconds
	red=75
	green=20
	#lights_sq=75+20
	lights_sq = red + green
	print("========Seconds========")
	left = 0 
	i=0
	wait = {}
	global day_table
	for i in range(days_in_year):
	#for i in range(7):
		i = i +1
		left=(day_secons + left) % lights_sq
		print(day_table[i] + " " + str(i) + " smeschenie " + str(left) )
		#if day_table[i] != "sun" or day_table[i] != "sat":
		CheckFunc(left,day_table[i])	
	print("=======================")

def CheckFunc(c_get,c_day):
	#aaa={'r':75,'g':20}
	aaa={'r':res[0], 'g':res[1]}
	global res
	if c_get<0:
	 	print("error, smeschenie mensche 0")
	i=c_get
	j=0
	k=False
	t=False
	global ll
	global ans
	global ssumm
	global iterat
	global w_ends
	global weighted_average
	for i in range(c_get):
		if aaa['r']==74 and aaa['g']==20 and c_get==75:
			weighted_average[75]+=1
			weighted_average[0]-=1
		if aaa['r']>0:
			aaa['r']=aaa['r']-1
			#if aaa['r']==0:
			k=True
		if k==False and aaa['r']==0 and aaa['g']>0:
			aaa['g']=aaa['g']-1
			#if aaa['g']==0:
			t=True
		#if k==False and t==True and aaa['r']==0 and aaa['g']==0: ?????
		if k==False and t==False and aaa['r']==0 and aaa['g']==0:
			aaa['r']=74
			aaa['g']=20
			k=False
			#j=-1 #Don't remember, why i needed it.
			#j=0
		i+=1
		j+=1
		k=False
		t=False
		print(str(aaa['r']) + " , " + str(aaa['g']) + " , local smesch = " + str(j))
	
	res[0]=aaa['r']
	res[1]=aaa['g']



	if c_day == "sun" or c_day == "sat":
	#test
	#if 0 ==1:
		w_ends+=1
		print ("weekend")
	else:
		if res[0] > 0:
			ans[ll]=res[0]
			ssumm=ssumm+res[0]
			ll+=1
			weighted_average[res[0]]+=1
		if res[0]==0:
			iterat+=1
			weighted_average[0]+=1
	print(res)

CheckYear(year)
Seconds(leap)
print("drift: " + str(ssumm)+", work days with drift: "+ str(ll))
print("average wait with NO zero wait: " + str(ssumm / ll))
print("Total averange wait: "+ str(ssumm / (ll+iterat)))
print("days with zero drift: " + str(iterat) + ", weekends: " + str(w_ends))
#sorted(weighted_average, key=lambda x : int(x[:x.index(' ')]))
#a={}
#sorted(weighted_average, key=lambda x: weighted_average.index(x.split(' ')[0]))
print("=================")
print("Waiting time: numer of times waited")
for y in range(0,80,5):
	#weighted_average[y]=0
	print(str(y)+": "+str(weighted_average[y]))
#FirstWeek(year)


