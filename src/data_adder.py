
f = open("C:\\Users\\최진서\\Desktop\\캡스톤 디자인 자료\\경상남도 소비자 물가 총지수.csv",'r')
f_loan = open("C:\\Users\\최진서\\Desktop\\캡스톤 디자인 자료\\경남 가계대출금.csv",'r')
f_building = open("C:\\Users\\최진서\\Desktop\\캡스톤 디자인 자료\\건축허가면적_1.csv",'r')
f_interest = open("C:\\Users\\최진서\\Desktop\\캡스톤 디자인 자료\\cd금리.csv",'r')
f_housingprice = open("C:\\Users\\최진서\\Desktop\\캡스톤 디자인 자료\\uc_housing_price.csv",'r')
f_multi_dataset = open("C:\\Users\\최진서\\Desktop\\캡스톤 디자인 자료\\integrated_data.csv",'w')
count=0
while True:
    consumer_price = f.readline() #소비자 물가지수
    house_loan = f_loan.readline() # 경남 가계대출금 
    building_space = f_building.readline() # 건축허가 면적 
    interest_idx = f_interest.readline() # 금리
    housing_price = f_housingprice.readline() # 주택가격지수 

    if count == 0:
        f_multi_dataset.write('date, consumer_price, house_loan, building_space, interest_idx, housing_price')
    else:
        count = count+1
        date = consumer_price.split(',')[1]
        lone = house_loan.split(',')[1]
        space = bulu