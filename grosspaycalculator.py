print 'Hello there, my name is Pyt and I will be assisting you with your salary calculations'
name = raw_input('First of all, what is your name?\n')
print 'Hi ' + name + ', lovely to meet you'
hours_week = float(raw_input('How many hours a week do you work?\n'))
print 'Thanks!'
rate = float(raw_input('What is your hourly rate?\n'))
print 'Thanks! I will calculate the results now.'
pay_week = hours_week * rate
print 'Your weekly gross pay is: ' + str(pay_week)

