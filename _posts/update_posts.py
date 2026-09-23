import os
import re

def process_all_features():
    # 1. 스크립트 파일이 위치한 폴더를 기준으로 경로를 확실하게 고정합니다.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = base_dir
    target_dir = os.path.join(base_dir, '_change')
    
    # 2. _change 폴더가 없으면 새로 만듭니다.
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    # 3. 소스 폴더에 있는 모든 .md 파일 목록을 가져옵니다.
    md_files = [f for f in os.listdir(source_dir) if f.endswith('.md')]
    
    count = 0
    for filename in md_files:
        filepath = os.path.join(source_dir, filename)
        
        # 파일을 읽기 모드로 엽니다.
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 4. 정규표현식을 사용해 --- 기준으로 설정 영역과 본문을 명확하게 3등분 합니다.
        parts = re.split(r'^-{3,}\s*$', content, maxsplit=2, flags=re.MULTILINE)
        
        # 정상적인 포스트 형식이 아니면 건너뜁니다.
        if len(parts) < 3:
            continue
            
        front_matter = parts[1]
        body = parts[2]
        
        # 5. 본문 인사말 변경
        body = body.replace("라보엠", "**한스**")
        
        # 설정 영역 분석을 위한 준비
        lines = front_matter.strip().split('\n')
        new_lines = []
        
        artist_name = ""
        has_tags = False
        categories_idx = -1
        
        for line in lines:
            clean_line = line.rstrip()
            
            # 규칙: excerpt 주석 처리
            if clean_line.startswith('excerpt:'):
                clean_line = '# ' + clean_line
                
            # 태그 존재 여부 확인
            if clean_line.startswith('tags:'):
                has_tags = True
                
            # 규칙: 타이틀에서 가수 이름 추출
            if clean_line.startswith('title:'):
                raw_title = clean_line.replace('title:', '').strip().strip('\'"')
                match = re.search(r'\[(.*?)\]\s*(.*)', raw_title)
                if match:
                    bracket_word = match.group(1).strip()
                    rest_title = match.group(2).strip()
                    
                    if bracket_word == "지금이노래":
                        if rest_title:
                            artist_name = rest_title.split()[0]
                    else:
                        artist_name = bracket_word
                        
            # 규칙: 카테고리 대분류 추가
            if clean_line.startswith('categories:'):
                categories_idx = len(new_lines)
                cat_value = clean_line.replace('categories:', '').strip()
                
                if cat_value:
                    main_cat_raw = cat_value.split('.')[0]
                    main_cat_title = main_cat_raw.capitalize()
                    
                    # 중복 추가 방지
                    if not cat_value.startswith(main_cat_title + ' '):
                        clean_line = f"categories: {main_cat_title} {cat_value}"
                        
            new_lines.append(clean_line)
            
        # 규칙: 태그가 없었고 가수 이름이 추출되었다면 카테고리 바로 아래에 삽입
        if not has_tags and artist_name and categories_idx != -1:
            new_lines.insert(categories_idx + 1, f"tags: {artist_name}")
            
        # 6. 수정한 내용을 다시 하나로 결합합니다.
        new_front_matter = '\n'.join(new_lines)
        new_content = f"---\n{new_front_matter}\n---{body}"
        
        # 7. _change 폴더에 최종 파일을 저장합니다.
        target_filepath = os.path.join(target_dir, filename)
        with open(target_filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        count += 1
        
    print(f"작업 완료! 총 {count}개의 포스팅 파일이 모든 규칙에 맞게 수정되어 '_change' 폴더에 저장되었습니다.")

if __name__ == "__main__":
    process_all_features()