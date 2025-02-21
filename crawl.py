from bs4 import BeautifulSoup
import test

def crawl_arona_students_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # 원하는 div 클래스를 정확하게 지정합니다.
    student_divs = soup.find_all('div', class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-20 MuiGrid-grid-sm-15 MuiGrid-grid-md-12 MuiGrid-grid-lg-10 MuiGrid-grid-xl-6 css-1wsxtpe")
    
    student_list = []
    for div in student_divs:
        name_tag = div.select_one('span.textkr')
        character_name = name_tag.text.strip() if name_tag else "unknown"
        student_list.append(character_name)
        test.save_character_image(str(div))
    
    return student_list

file_path = 'test.html'  # test.html의 경로
students = crawl_arona_students_from_file(file_path)


