from pathlib import Path
from urllib.request import urlretrieve

데이터가 저장된 텍스트 파일 서버 주소는 다음과 같다.

base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"

현재 작업 디렉토리의 `data` 하위 디렉토리에 파일을 다운로드해서 저장할 준비를 한다.

# 저장위치 지정과 생성
data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)

def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체

    with open(data_path / shop_file, mode='r', encoding='utf-8') as f:    
      for line in f:
        price_of_goods = line.strip().split() 
        if price_of_goods != []:      
          goods, price = price_of_goods 
        if price != shop_file[4]:
          shop_dict[goods] = int(price.rstrip('원'))

    return shop_dict

def item_price(shop_file, item):
    return shopping(shop_file)[item]
