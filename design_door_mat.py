def theFunc(n, m):
	q = '.|.'
	p = 'WELCOME'
	half_m = int((m - 3)/2)
	for i in range((int(n/2))):
		print((q*i).rjust(half_m, '-')+'.|.'+(q*i).ljust(half_m, '-'))
	t = int((m-6)/2)
	print('-'*t+p+'-'*t)
	for i in range((int(n/2))-1, -1, -1):
		print(
			(q*i).rjust(half_m, '-')+q+(q*i).ljust(half_m, '-')
		)

n, m = map(int, input().split())
theFunc(n, m)