# print the season according to the day and month
month=input("Enter a month: ")
day=int(input("Enter a day: "))
season=""
if month in "Nov, Dec, Jan, Feb" :
	season="winter"
elif month in  "Mar, Apr":
	season="spring"
elif month in "May, Jun, July":
	season="summer"
elif month in "Aug, Sep, Oct":
	season="autum"
else:
	season="Please enter a month."

if month=="Nov" and day>15:
	season="winter"
elif month=="Mar" and day>5:
	season="spring"
elif month=="May" and day>15:
	season="summer"
elif month=="Aug" and day>20:
	season="autum"
else:
	season="Please enter a month and day."
