import requests
from bs4 import BeautifulSoup

def save_character_image(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    # 이미지 URL 추출
    image_tag = soup.select_one('div.css-b3sghu img')
    image_url = image_tag['src'] if image_tag else None

    # 캐릭터 이름 추출
    name_tag = soup.select_one('span.textkr')
    character_name = name_tag.text.strip() if name_tag else "unknown"

    attackTypeDict = {"css-asi5kr":"폭발", "css-g1wr2d":"관통","css-pv4aqq":"신비","css-19lpkib":"진동"}
    # 배경색을 포함하는 div 찾기 (공격 아이콘 앞의 div)
    attack_icon_tag = soup.select_one('img[alt="공격 아이콘"]')
    background_class = "unknown"

    if attack_icon_tag:
        parent_div = attack_icon_tag.find_parent("div")
        if parent_div and parent_div.has_attr("class"):
            background_class = parent_div.get("class")[1] if len(parent_div.get("class")) > 1 else "unknown"

    if image_url:
        file_name = f"./images/{attackTypeDict[background_class]},{character_name}.png"
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"이미지 저장 완료: {file_name}")
        else:
            print("이미지 다운로드 실패")
    else:
        print("이미지를 찾을 수 없음")