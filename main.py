# 8X8 체스판에서 나이트의 위치 P 입력받기 (ex: C2)
# 나이트의 이동가능 위치 수 

def main():
	P = input()
	Moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
	x = ord(P[0])-ord('a')+1
	y = int(P[1])
	count=0
	for Move in Moves:
		if x+Move[1]<=8 and x+Move[1]>0 and y+Move[0]>0 and y+Move[1]<=8:
			count+=1
			print(Move)

	print(count)

	
main()