리스트 = [값1, 값2, ...]
my_list = ['감자', '고구마', '카사바'] #순서 보장
print(my_list[0]) #실행:감자
#리스트는 내부에 칸막이가 있어서 마구잡이가 아닌 집어넣는 순서대로 차곡차곡 관리가 된다.

my_list = ['감자', '고구마', '카사바'] #순서가 보장되기 때문에 슬라이싱이 가능하다.
print(my_list[0:2]) #실행: ['감자', '몽쉘']

my_list = ['감자', '고구마', '카사바'] #리스트에 포함되어 있늕지 확인 가능
print('감자' in my_list) #실행:True

my_list = ['감자', '고구마', '카사바'] #리스트 안에 몇개가 있는지 알 수 있다.(len 함수로 사용 가능)
print(len(my_list)) #실행: 3

my_list = ['감자', '고구마', '카사바'] #자유롭게 사용 가능
my_list[1] = '호박고구마'
print(my_list[1]) #실행:호박고구마

my_list = ['감자', '고구마', '카사바'] #자유롭게 사용 가능
my_list.append('수박') # append를 이용하여 값 추가
print(my_list) #실행:'감자', '고구마', '카사바', '수박'

my_list = ['감자', '고구마', '카사바'] #자유롭게 사용 가능
my_list.remove('감자') # remove를 이용하여 값 삭제
print(my_list) #실행:'고구마', '카사바'

my_list = ['감자', '고구마', '카사바'] #자유롭게 사용 가능
your_list = ['수박', '멜론']
my_list.extend(your_list) # extend를 이용하여 리스트 확장
print(my_list) #실행:'감자', '고구마', '카사바', '수박', '멜론'

#리스트 메소드 insert() 원하는 위치에 값 추가, pop() 원하는 위치(또는 마지막)의 값 삭제, clear(), 모든 값 삭제, sort()값 순서대로 정렬
#reverse() 순서 뒤집기, copy() 리스트 복사, count() 어떤값이 몇 개 있는지, index() 어떤 값이 어디에 있는지
