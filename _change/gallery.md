---
title: "Music Collection"
layout: splash
permalink: /gallery/
author_profile: false
---

<style>
  /* 1. 와이드 화면 강제 적용 (불필요한 안쪽 여백 제거) */
  .page__inner-wrap {
    padding-left: 0;
    padding-right: 0;
  }

  /* 2. 반응형 4열 그리드 설정 */
  .custom-gallery-grid {
    display: grid;
    gap: 24px;
    margin-top: 2em;
    grid-template-columns: repeat(1, 1fr); 
  }

  @media (min-width: 768px) {
    .custom-gallery-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (min-width: 1024px) {
    .custom-gallery-grid {
      grid-template-columns: repeat(4, 1fr);
    }
  }

  /* 3. 개별 썸네일 프레임 */
  .custom-gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }
  
  .custom-gallery-item img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
  }
  
  /* 4. 타이틀 오버레이 설정 (처음엔 아래로 숨겨둠) */
  .gallery-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0, 0, 0, 0.7);
    color: #ffffff;
    padding: 15px;
    text-align: center;
    font-weight: bold;
    font-size: 1rem;
    transform: translateY(100%);
    transition: transform 0.3s ease;
    pointer-events: none;
  }

  /* 5. 마우스 오버(Hover) 효과 */
  .custom-gallery-item:hover img {
    transform: scale(1.05); /* 이미지 5% 확대 */
  }
  .custom-gallery-item:hover .gallery-overlay {
    transform: translateY(0); /* 숨겨뒀던 오버레이를 원래 위치로 끌어올림 */
  }

  /* 더보기 페이징용 숨김 클래스 */
  .hidden-item {
    display: none;
  }
</style>

<!-- 갤러리 이미지 반복 출력 -->
<div class="custom-gallery-grid" id="gallery-grid">
  {% for post in site.posts %}
    {% if post.teaser %}
      <div class="custom-gallery-item gallery-item-card">
        <a href="{{ post.url }}">
          <img src="{{ post.teaser }}" alt="{{ post.title }}">
          <div class="gallery-overlay">{{ post.title }}</div>
        </a>
      </div>
    {% endif %}
  {% endfor %}
</div>

<!-- 페이징 대체용 투명 감지 센서 -->
<div id="scroll-sentinel" style="height: 20px; margin-top: 40px; margin-bottom: 40px;"></div>

<!-- 무한 스크롤 자바스크립트 로직 -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll('.gallery-item-card');
    const sentinel = document.getElementById('scroll-sentinel');
    
    let currentVisible = 16; // 처음에 보여줄 이미지 개수
    const loadStep = 16;     // 한 번 스크롤할 때마다 추가할 개수

    // 초기 숨김 처리
    for (let i = 0; i < items.length; i++) {
      if (i >= currentVisible) {
        items[i].classList.add('hidden-item');
      }
    }

    // 처음부터 숨겨진 아이템이 없다면 감지 센서를 아예 숨김
    if (items.length <= currentVisible) {
      sentinel.style.display = 'none';
      return; 
    }

    // 스크롤 감지기(Observer) 설정
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        // 감지 센서가 화면에 나타나면
        if (entry.isIntersecting) {
          let shown = 0;
          for (let i = 0; i < items.length; i++) {
            if (items[i].classList.contains('hidden-item') && shown < loadStep) { 
              items[i].classList.remove('hidden-item');
              shown++;
              currentVisible++;
            }
          }
          
          // 더 이상 보여줄 항목이 없으면 감지 종료 및 센서 숨김
          if (currentVisible >= items.length) {
            observer.unobserve(sentinel);
            sentinel.style.display = 'none';
          }
        }
      });
    }, {
      // 화면 바닥에 닿기 300px 전에 미리 로딩을 시작하도록 설정
      rootMargin: "0px 0px 300px 0px" 
    });

    // 감지 센서 관찰 시작
    observer.observe(sentinel);
  });
</script>