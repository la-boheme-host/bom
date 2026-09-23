import os
import shutil
import re
import html
from datetime import datetime
from bs4 import BeautifulSoup

# 이미지 비율 확인을 위한 Pillow 임포트
try:
    from PIL import Image
except ImportError:
    print("Pillow 라이브러리가 필요합니다. 실행 전 'pip install Pillow'를 입력해 설치해주세요.")
    Image = None

# 설정 경로
SOURCE_DIR = "./tistory_backup_posts"   # 티스토리 백업 폴더
TARGET_POSTS_DIR = "./_posts"           # Jekyll _posts 폴더
TARGET_IMG_DIR = "./assets/images"       # Jekyll 이미지 폴더

# 감지할 OTT 플랫폼 키워드 목록
OTT_PLATFORMS = [
    "디즈니플러스", "넷플릭스", "쿠팡플레이", 
    "아마존프라임", "티빙", "웨이브", "왓챠", "애플티비"
]


def clean_and_convert_html(body_tag, post_id):
    if not body_tag:
        return ""

    # 1. H2 태그 추출 후 마커로 치환
    for h2 in body_tag.find_all('h2'):
        h2_text = h2.get_text(strip=True)
        h2.replace_with(f"\n\n__H2_MARKER__{h2_text}__H2_END__\n\n")

    # 2. 유튜브 데이터(figure, iframe) 추출 후 마커로 치환
    for fig in body_tag.find_all('figure', attrs={'data-video-host': 'youtube'}):
        url = fig.get('data-video-url', '')
        match = re.search(r'(?:v=|/)([0-9A-Za-z_-]{11})', url)
        if match:
            fig.replace_with(f"\n\n__YOUTUBE_MARKER__{match.group(1)}__YOUTUBE_END__\n\n")
        else:
            fig.decompose()

    for iframe in body_tag.find_all('iframe'):
        src = iframe.get('src', '')
        match = re.search(r'(?:v=|embed/|youtu\.be/)([0-9A-Za-z_-]{11})', src)
        if match:
            iframe.replace_with(f"\n\n__YOUTUBE_MARKER__{match.group(1)}__YOUTUBE_END__\n\n")
        else:
            iframe.decompose()

    # 3. 이미지 태그 경로 수정 후 마커로 치환
    for img in body_tag.find_all('img'):
        src = img.get('src', '')
        filename = os.path.basename(src)
        if filename:
            new_src = f"/assets/images/{post_id}/{filename}"
            alt = img.get('alt', '')
            img.replace_with(f"\n\n__IMG_MARKER__{new_src}||{alt}__IMG_END__\n\n")
        else:
            img.decompose()

    # 4. 외부 링크 추출 후 마커로 치환 (오픈그래프용)
    for a_tag in body_tag.find_all('a'):
        href = a_tag.get('href', '')
        if '__IMG_MARKER__' in str(a_tag):
            a_tag.unwrap()
            continue

        if href.startswith('http'):
            a_tag.replace_with(f"\n\n__LINK_MARKER__{href}__LINK_END__\n\n")
        else:
            a_tag.unwrap()

    # 5. 본문 내 숨겨진 스크립트나 스타일 태그 완전히 제거
    for hidden in body_tag.find_all(['script', 'style', 'head', 'meta', 'link']):
        hidden.decompose()

    for tag in body_tag.find_all(['p', 'div', 'br', 'li', 'tr', 'h1', 'h3', 'h5', 'h6']):
        tag.append("\n")

    while True:
        tag = body_tag.find(True)
        if not tag:
            break
        tag.unwrap()

    raw_text = html.unescape(body_tag.decode_contents())
    lines = raw_text.split('\n')
    processed_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            processed_lines.append("")
            continue

        if '__H2_MARKER__' in line:
            line = re.sub(r'__H2_MARKER__(.*?)__H2_END__', r'# \1', line)
            processed_lines.append(line)
            continue

        if '__YOUTUBE_MARKER__' in line:
            line = re.sub(r'__YOUTUBE_MARKER__(.*?)__YOUTUBE_END__', r'{% include video id="\1" provider="youtube" %}', line)
            processed_lines.append(line)
            continue

        if '__IMG_MARKER__' in line:
            line = re.sub(r'__IMG_MARKER__(.*?)\|\|(.*?)__IMG_END__', r'<img src="\1" alt="\2">', line)
            processed_lines.append(line)
            continue

        if '__LINK_MARKER__' in line:
            line = re.sub(r'__LINK_MARKER__(.*?)__LINK_END__', r'{% include auto-link.html url="\1" %}', line)
            processed_lines.append(line)
            continue

        processed_lines.append(line + "  ")

    final_output = "\n".join(processed_lines)
    final_output = re.sub(r'\n{3,}', '\n\n', final_output)

    # 본문 내 텍스트 치환
    final_output = final_output.replace("라보엠", "**한스**")

    return final_output.strip()


def advanced_migrate():
    if not os.path.exists(SOURCE_DIR):
        print(f"오류: {SOURCE_DIR} 폴더를 찾을 수 없습니다.")
        return

    os.makedirs(TARGET_POSTS_DIR, exist_ok=True)

    for post_folder in os.listdir(SOURCE_DIR):
        folder_path = os.path.join(SOURCE_DIR, post_folder)

        if os.path.isdir(folder_path):
            post_id = post_folder
            src_img_folder = os.path.join(folder_path, "img")
            dest_img_folder = os.path.join(TARGET_IMG_DIR, post_id)

            target_image_path = ""
            if os.path.exists(src_img_folder):
                os.makedirs(dest_img_folder, exist_ok=True)
                img_files = sorted(os.listdir(src_img_folder))
                
                # 이미지 폴더 내 파일 복사
                for img_file in img_files:
                    if img_file.startswith('.'):
                        continue
                    shutil.copy(
                        os.path.join(src_img_folder, img_file),
                        os.path.join(dest_img_folder, img_file)
                    )
                
                valid_imgs = [f for f in img_files if not f.startswith('.')]
                if valid_imgs:
                    first_img_name = valid_imgs[0]
                    last_img_name = valid_imgs[-1]
                    
                    selected_img_name = first_img_name # 기본값은 첫번째 이미지
                    
                    # 🌟 첫번째 이미지와 마지막 이미지 비율 검사 (세로가 긴 포스터 이미지 판별)
                    if Image is not None:
                        try:
                            # 첫번째 이미지 검사
                            with Image.open(os.path.join(dest_img_folder, first_img_name)) as img1:
                                is_first_vertical = img1.height > img1.width
                            
                            # 마지막 이미지 검사
                            with Image.open(os.path.join(dest_img_folder, last_img_name)) as img2:
                                is_last_vertical = img2.height > img2.width
                            
                            # 세로가 긴 이미지를 우선 선택
                            if is_first_vertical:
                                selected_img_name = first_img_name
                            elif is_last_vertical:
                                selected_img_name = last_img_name
                            else:
                                selected_img_name = first_img_name # 둘 다 아니면 첫번째
                                
                        except Exception as e:
                            print(f"[{post_id}] 이미지 크기 확인 실패, 기본 이미지 사용: {e}")
                    
                    target_image_path = f"/assets/images/{post_id}/{selected_img_name}"

            for file_name in os.listdir(folder_path):
                if file_name.endswith(".html") or file_name.endswith(".md"):
                    src_file = os.path.join(folder_path, file_name)

                    with open(src_file, "r", encoding="utf-8") as f:
                        raw_html = f.read()

                    soup = BeautifulSoup(raw_html, 'html.parser')

                    title_tag = soup.find('title')
                    post_title = title_tag.text.strip() if title_tag else f"Post {post_id}"

                    # 제목 내 텍스트 치환
                    post_title = post_title.replace("라보엠", "**한스**")

                    # 1. 본문 제목(<h2 class="title-article">) 추출 및 OTT 판별
                    h2_title_tag = soup.find('h2', class_='title-article')
                    matched_ott = ""
                    if h2_title_tag:
                        article_title = h2_title_tag.get_text(strip=True)
                        
                        for ott in OTT_PLATFORMS:
                            pattern = rf'^(?:\[\s*{re.escape(ott)}\s*\]|{re.escape(ott)})'
                            if re.search(pattern, article_title):
                                matched_ott = ott
                                break
                                
                        h2_title_tag.decompose()

                    # 2. 카테고리 추출 및 전처리
                    category_tag = soup.find('p', class_='category')
                    post_category = ""
                    if category_tag:
                        raw_cat = category_tag.text.strip()
                        post_category = raw_cat.replace("Screen./", "").strip()
                        category_tag.decompose()

                    # 카테고리 목록 생성
                    categories = []
                    if post_category:
                        categories.append(post_category)
                    if matched_ott and matched_ott not in categories:
                        categories.append(matched_ott)

                    # 태그 추출
                    tags_tag = soup.find(class_='tags')
                    post_tags = []
                    if tags_tag:
                        tags_text = tags_tag.text.strip()
                        if tags_text:
                            raw_tags = re.findall(r'#([^\s,]+)', tags_text)
                            post_tags = raw_tags[:2]
                        tags_tag.decompose()

                    # 날짜 추출
                    date_tag = soup.find('p', class_='date')
                    extracted_date_str = date_tag.text.strip() if date_tag else ""
                    if date_tag:
                        date_tag.decompose()

                    file_date_prefix = datetime.now().strftime('%Y-%m-%d')
                    formatted_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S +0900')

                    if extracted_date_str:
                        try:
                            parsed_dt = datetime.strptime(extracted_date_str, "%Y-%m-%d %H:%M:%S")
                            file_date_prefix = parsed_dt.strftime('%Y-%m-%d')
                            formatted_date = parsed_dt.strftime('%Y-%m-%d %H:%M:%S +0900')
                        except ValueError:
                            pass

                    # 본문 처리
                    body_tag = soup.find('body')
                    post_excerpt = ""
                    if body_tag:
                        plain_text = body_tag.get_text(separator=' ', strip=True)
                        post_excerpt = plain_text[:150].replace('"', "'").replace('\n', ' ') + "..."
                        # 요약문 내 텍스트 치환
                        post_excerpt = post_excerpt.replace("라보엠", "**한스**")
                        
                        post_content = clean_and_convert_html(body_tag, post_id)
                    else:
                        post_content = raw_html.replace("라보엠", "**한스**")

                    # Front Matter 생성
                    front_matter = f"""---
layout: single
title: "{post_title}"
date: {formatted_date}
permalink: /{post_id}/
"""
                    if post_excerpt:
                        front_matter += f'excerpt: "{post_excerpt}"\n'

                    # Jekyll 계층형 카테고리
                    if categories:
                        front_matter += f"categories: {' '.join(categories)}\n"

                    if post_tags:
                        tags_str = " ".join(post_tags)
                        front_matter += f"tags: {tags_str}\n"

                    # 🌟 이미지 Front Matter 변경 (판별된 대표 이미지를 삽입)
                    if target_image_path:
                        front_matter += f"""header:
  overlay_image: {target_image_path}
teaser: {target_image_path}
"""
                    front_matter += "---\n\n"

                    final_markdown_content = front_matter + post_content

                    new_file_name = f"{file_date_prefix}-{post_id}.md"
                    dest_file = os.path.join(TARGET_POSTS_DIR, new_file_name)

                    with open(dest_file, "w", encoding="utf-8") as f:
                        f.write(final_markdown_content)

                    print(f"정밀 변환 완료: {new_file_name}")


if __name__ == "__main__":
    advanced_migrate()
